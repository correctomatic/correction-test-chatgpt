
pip install virtualenv
python -m virtualenv .venv

pip install -r requirements.txt

pip install groq

Parece que usa el API de OpenAI:
https://platform.openai.com/docs/api-reference/introduction


API Key:
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


export GROQ_API_KEY=<your-api-key-here>



docker build -t correction-test-chatgpt .
docker run --rm correction-test-chatgpt
