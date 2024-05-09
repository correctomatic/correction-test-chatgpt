from g4f.client import Client

# It seems it needs authentication

client = Client()
response = client.images.generate(
  # model="gemini",
  model="dall-e-3",
  prompt="a white siamese cat",
)
print(response)
image_url = response.data[0].url
print(image_url)
