import google.generativeai as genai
from dotenv import load_dotenv
import os

#Load variables from .env file
load_dotenv()
# Replace with your actual API Key from Google AI Studio

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def get_atomic_tasks(syllabus_text):
    model = genai.GenerativeModel('gemini-2.5-flash')
    
    # This 'Prompt' is the most important part!
    prompt = f"""
    You are an expert academic coordinator. 
    Take the following syllabus and break it into 'Atomic Tasks'.
    Rules:
    1. Each task must take exactly 45 minutes.
    2. Format the output as a simple list.
    3. Focus on logical flow (e.g., basics before advanced).

    Syllabus:
    {syllabus_text}
    """
    
    response = model.generate_content(prompt)
    return response.text

# Test it locally
if __name__ == "__main__":
    sample_text = "Unit 1: Java Basics, Variables, and Data Types"
    print("Testing AI Connection...")
    print(get_atomic_tasks(sample_text))