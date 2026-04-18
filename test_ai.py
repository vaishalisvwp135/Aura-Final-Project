import google.generativeai as genai
from dotenv import load_dotenv
import os

#Load variables from .env file
load_dotenv()

# Use the key you got from Google AI Studio

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

try:
    # 2. Try the 'stable' name first. 
    # If 'gemini-1.5-flash' fails, the library might want 'models/gemini-1.5-flash'
    model = genai.GenerativeModel('gemini-2.5-flash')
    
    response = model.generate_content("Is the system online?")
    print("AI Response:", response.text)

except Exception as e:
    print(f"Error Details: {e}")