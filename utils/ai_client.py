"""Gemini client used by the translation route."""

import os

import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()


def translate_text(text: str, source_language: str, target_language: str) -> str:
    """Translate *text* from the supplied source to target language."""
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("GEMINI_API_KEY is not configured.")

    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-3.8-flash")
    prompt = (
        f"Translate the following text from {source_language} to "
        f"{target_language}. Return only the translation.\n\n{text}"
    )
    response = model.generate_content(prompt)
    return response.text.strip()
