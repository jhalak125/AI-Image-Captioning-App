import os
import google.generativeai as genai
from dotenv import load_dotenv
from PIL import Image

# Load environment variables
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

# Configure Gemini API
genai.configure(api_key=API_KEY)

# Load multimodal model
model = genai.GenerativeModel('gemini-1.5-flash')

def generate_caption(image_file):
    try:
        image = Image.open(image_file)
        response = model.generate_content([
            "Describe this image in one engaging caption for social media.",
            image
        ])
        return response.text
    except Exception as e:
        return f"Error generating caption: {e}"
