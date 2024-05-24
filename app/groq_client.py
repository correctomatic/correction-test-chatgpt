import os
from groq import Groq

API_KEY_FILE = "groq_api_key.txt"

def read_api_key():
    if not os.path.exists(API_KEY_FILE):
        raise FileNotFoundError(f"API key file '{API_KEY_FILE}' not found.")

    with open(API_KEY_FILE, "r") as f:
        return f.read().strip()

client = Groq(
    api_key=read_api_key(),
)
