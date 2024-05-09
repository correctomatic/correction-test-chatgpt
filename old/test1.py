import os

from groq import Groq

api_key=os.environ.get("GROQ_API_KEY")
api_key = "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"

client = Groq(
    api_key=api_key,
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "Contesta al usuario pero al revés",
        },
        {
            "role": "user",
            "content": "Explica cómo llenar un vaso de agua",
        }
    ],
    # model="mixtral-8x7b-32768",
    model="llama3-70b-8192"
)

foo = chat_completion.choices
print(foo)
print(chat_completion.choices[0].message.content)
