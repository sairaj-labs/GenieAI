import streamlit as st
from streamlit_option_menu import option_menu
import os
from PIL import Image
from gemini_utility import load_gemini_pro_model, gemini_pro_vision_response,embedding_model_response,gemini_pro_response

# Get the working directory
working_directory = os.path.dirname(os.path.abspath(__file__))
print(working_directory)

# Setting page configuration
st.set_page_config(
    page_title="GEMINI_AI",
    page_icon="🧠",
    layout="centered"
)

# Sidebar menu
with st.sidebar:
    selected = option_menu(
        menu_title="Gemini AI",
        options=[
            "ChatBot",
            "Image Captioning",
            "Embed text",
            "Ask me anything"
        ],
        menu_icon='robot',
        icons=['chat-dots-fill', 'image-fill', 'textarea-t', 'patch-question-fill'],
        default_index=0
    )

# Function to translate role between gemini-pro and Streamlit terminology
def translate_role_for_streamlit(use_role):
    return "assistant" if use_role == "model" else use_role

# Chatbot functionality
if selected == "ChatBot":
    # Load the model
    model = load_gemini_pro_model()

    # Initialize chat session in Streamlit if not already present
    if "chat_session" not in st.session_state:
        st.session_state.chat_session = model.start_chat(history=[])

    # Streamlit page title
    st.title("🤖 ChatBot")

    # Display chat history
    for message in st.session_state.chat_session.history:
        with st.chat_message(translate_role_for_streamlit(message.role)):
            st.markdown(message.parts[0].text)

    # Input field for user's message
    user_prompt = st.chat_input("Ask Gemini-Pro...")

    if user_prompt:
        # Display user's input
        st.chat_message("user").markdown(user_prompt)

        # Get Gemini-Pro's response
        gemini_response = st.session_state.chat_session.send_message(user_prompt)

        # Display Gemini-Pro's response
        with st.chat_message("assistant"):
            st.markdown(gemini_response.text)

# Image captioning page
if selected == "Image Captioning":
    # Streamlit page title
    st.title("📸 Snap Narrate")

    uploaded_image = st.file_uploader("Upload an image...", type=["jpg", "jpeg", "png"])

    if uploaded_image and st.button("Generate Caption"):
        image = Image.open(uploaded_image)

        col1, col2 = st.columns(2)

        with col1:
            resized_image = image.resize((800, 500))
            st.image(resized_image)

        default_prompt = "Write a short caption for this image."

        # Getting the response from gemini-pro-vision model
        caption = gemini_pro_vision_response(default_prompt, image)

        with col2:
            st.info(caption)

# text embedding page:

if selected=="Embed text":

    st.title("🔡Embed text")

    # unput text box
    input_text=st.text_area(label="",placeholder="Enter the text to get the embeddings")

    if st.button("get Embeddings"):
        repsonse=embedding_model_response(input_text)
        st.markdown(repsonse)


# question answering page:
if selected=="Ask me anything":
    st.title("? Ask me a question")

    # text box to enter prompt
    user_prompt=st.text_area(label="",placeholder="Ask Gemini-Pro...")

    if st.button("Get an answer"):
        repsonse=gemini_pro_response(user_prompt)
        st.markdown(repsonse)