# Correctomatic tester with LLM

The purpose of this project is to generate a container that will correct exercises using a LLM model,
integrated in the Correctomatic system.

## How to use it


## Testing the corrections

To test the corrections, you must first build the container with the following command:
```bash
docker build -t correction-test-chatgpt .
```

Then you should run the container with the following command:

```bash
# Must be absolute paths
PROMPT_FILE=$(pwd)/exercise/prompt.txt
EXERCISE_FILE=$(pwd)/exercise/example_exercise.txt

# Run the container
docker run --rm \
    -v "$EXERCISE_FILE":/tmp/exercise \
    -v "$PROMPT_FILE":/app/prompt.txt \
    correction-test-chatgpt
```

Once you're happy with the results, you can build the container and it will be ready to be used in the Correctomatic system.

## Development

Prepare the virtual env:

```bash
pip -m venv .venv
```

TO-DO

### Build the container

TO-DO



### Run the container to develop the code

TO-DO


```bash
# Must be absolute paths
PROMPT_FILE=$(pwd)/exercise/prompt.txt
EXERCISE_FILE=$(pwd)/exercise/example_exercise.txt
LLM_PROVIDER=groq # or g4f

docker run --rm \
    -v "$EXERCISE_FILE":/tmp/exercise \
    -v "$PROMPT_FILE":/prompt.txt \
    -v "$(pwd)/app":/app \
    -e "LLM_PROVIDER=$LLM_PROVIDER" \
    correction-test-chatgpt
```
If you change the requirements.txt file you will need to rebuild the container.


##### Notes


pip install virtualenv
python -m virtualenv .venv

pip install -r requirements.txt

pip install groq

Parece que usa el API de OpenAI:
https://platform.openai.com/docs/api-reference/introduction


API Key:
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


export GROQ_API_KEY=<your-api-key-here>
https://console.groq.com/playground




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



## Huggingchat

HuggingChat
https://github.com/Soulter/hugging-chat-api
