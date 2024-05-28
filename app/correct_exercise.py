import time
import json
import os
from importlib import import_module


PROMP_FILE = "/prompt.txt"
EXERCISE_FILE = "/tmp/exercise"
MODEL=os.getenv("MODEL")

# LLM_PROVIDER can be either "groq" or "g4f"
module_name = f'{os.getenv("LLM_PROVIDER")}_client'
try:
    client = import_module(module_name).client

    def read_file(file_name):
        with open(file_name, 'r') as file:
            data = file.read()
        return data

    prompt = read_file(PROMP_FILE)
    exercise = read_file(EXERCISE_FILE)

    messages=[
        {
            "role": "system",
            "content": prompt,
        },
        {
            "role": "user",
            "content": exercise,
        }
    ]

    chat_completion = client.chat.completions.create(
        model=MODEL,
        messages=messages,
    )

    def call_LLM(max_retries=5, delay=1):
        retries = 0
        while retries < max_retries:
            result = chat_completion.choices[0].message.content
            if result != "":
                return result
            retries += 1
            time.sleep(delay)
        raise Exception("Max retries reached")

    try:
        correction_result = call_LLM()
        response = {
            "success": True,
            "comments": [ correction_result ]
        }
    except Exception as e:
        response = {
            "success": False,
            "error": str(e)
        }

    print(json.dumps(response))

except Exception as e:
    response = {
        "success": False,
        "error": str(e)
    }
    print(json.dumps(response))
    exit(0)
