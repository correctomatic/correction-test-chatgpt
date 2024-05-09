import time
from g4f.client import Client

MODEL = "gpt-3.5-turbo"
PROMP_FILE = "prompt.txt"
EXERCISE_FILE = "/tmp/exercise"

def read_file(file_name):
    with open(file_name, 'r') as file:
        data = file.read()
    return data

prompt = read_file(PROMP_FILE)
exercise = read_file(EXERCISE_FILE)

client = Client()

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

result = call_LLM()
print(result)
