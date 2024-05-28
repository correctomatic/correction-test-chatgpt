import os
from groq import Groq

API_KEY = os.getenv("API_KEY")
client = Groq(
    api_key=API_KEY
)
