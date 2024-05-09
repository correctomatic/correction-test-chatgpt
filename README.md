
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


docker run --rm \
    -v ./exercise/example_exercise.txt:/tmp/exercise \
    -v ./exercise/prompt.txt:/app/prompt.txt \
    correction-test-chatgpt



GPT4Free es un proyecto que intenta ofrecer la posibilidad de utilizar el modelo de lenguaje GPT-4 de forma gratuita. Lanza el strem a una lista de proveedores.
Aquí tienes la lista: https://github.com/xtekky/gpt4free#-providers-and-models
Los que están en verde funcionan y puedes lanzar directamente el strem a ese proveedor o modelo.
Página principal de G4F:
https://g4f.mintlify.app/get-started/introduction
https://github.com/xtekky/gpt4free

Hay que instalar el módulo de Python:
https://g4f.mintlify.app/get-started/quickstart
pip install -U g4f

Código ejemplo de la página web:
https://g4f.mintlify.app/get-started/usage
