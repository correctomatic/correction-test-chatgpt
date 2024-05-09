from g4f.client import Client
from g4f import get_model_and_provider
# from g4f.Provider import You

client = Client()

model, provider = get_model_and_provider("gpt-3.5-turbo", None, stream=False)
print(model, provider)
exit()

messages=[
    {
        "role": "system",
        "content": "Contesta al usuario pero al revés",
    },
    {
        "role": "user",
        "content": "Explica cómo llenar un vaso de agua",
    }
]

chat_completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    # model="mixtral-8x7b-32768",
    # model="llama3-70b-8192",
    messages=messages,
)

print(chat_completion.choices[0])
print(chat_completion.choices[0].message.content or "")
