import os
from dotenv import load_dotenv

# --------------------------------------------------
# Load Environment Variables from .env
# --------------------------------------------------
load_dotenv()

# --------------------------------------------------
# GROQ API CONFIGURATION
# --------------------------------------------------

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY not found in .env file.")

GROQ_BASE_URL = "https://api.groq.com/openai/v1"

# --------------------------------------------------
# LLM MODEL CONFIGURATION
# --------------------------------------------------

MODEL_NAME = "llama-3.1-8b-instant"   # Free Groq model
TEMPERATURE = 0.7
MAX_TOKENS = 300