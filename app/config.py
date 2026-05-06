import os
from dotenv import load_dotenv

load_dotenv()  # loads from project root

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY is not set")

print("KEY LOADED:", OPENAI_API_KEY)