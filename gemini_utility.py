import os
import json
import google.generativeai as genai
from PIL import Image

# Get the working directory
working_directory = os.path.dirname(os.path.abspath(__file__))

# Load configuration
config_file_path = f"{working_directory}/config.json"
config_data = json.load(open(config_file_path))

# Load the API key
GOOGLE_API_KEY = config_data["GOOGLE_API_KEY"]
print(GOOGLE_API_KEY)

# Configure google.generativeai with API key
genai.configure(api_key=GOOGLE_API_KEY)

# Function to load gemini-pro model for chatbot
def load_gemini_pro_model():
    gemini_pro_model = genai.GenerativeModel("gemini-1.5-flash")  # Updated model
    return gemini_pro_model

# Function for image captioning
def gemini_pro_vision_response(prompt, image):
    # Using the updated model `gemini-1.5-flash`
    gemini_pro_vision_model = genai.GenerativeModel("gemini-1.5-flash")
    response = gemini_pro_vision_model.generate_content([prompt, image])
    result = response.text
    return result

# just for TESTING Purpose:
# # Load and process the image
# image = Image.open("test_image.jpg")

# # Define the prompt and get the response
# prompt = "write a short caption for this image"
# output = gemini_pro_vision_response(prompt, image)

# print(output)

# function to get embeddings for text:
import google.generativeai as genai

def embedding_model_response(input_text):
    # Correct model path spelling and ensure proper configuration
    embedding_model = "models/embedding-001"  # Fixing 'modles' to 'models'
    
    try:
        # Generate embedding with proper task type
        embedding = genai.embed_content(
            model=embedding_model,
            content=input_text,
            task_type="retrieval_document"
        )
        
        # Safely extract embedding data
        embedding_list = embedding.get("embedding", [])
        return embedding_list
    
    except Exception as e:
        print(f"An error occurred while generating embeddings: {e}")
        return None

# Example usage
output = embedding_model_response("Who is Thanos?")
print(output)


# function to get a response from gemini-pro LLM

def gemini_pro_response(use_prompt):
     gemini_pro_model = genai.GenerativeModel("gemini-1.5-flash")
     response = gemini_pro_model.generate_content([use_prompt])
     result = response.text
     return result

output=gemini_pro_response("What is Machine Learning")
print(output)