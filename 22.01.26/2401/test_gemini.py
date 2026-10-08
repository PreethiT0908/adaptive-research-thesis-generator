import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
print("API Key Found:", bool(api_key))

genai.configure(api_key=api_key)

try:
    model = genai.GenerativeModel("gemini-2.5-flash")
    response = model.generate_content("Write 50 words about climate change.")
    print("\nSUCCESS!")
    print(response.text)
except Exception as e:
    print("\nERROR:")
    print(e)