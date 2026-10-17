import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise RuntimeError("Set GOOGLE_API_KEY in .env")

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.5-flash")

def translate_text(text, target_language):
    response = model.generate_content(
        f"Translate this text to {target_language}: {text}"
    )
    return response.text