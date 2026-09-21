from langchain_ollama import ChatOllama


def run_model():
    model = ChatOllama(
        model="qwen3:1.7b"
    )

    response = model.invoke("What is LangChain?")

    print(response.content)


if __name__ == "__main__":
    run_model()