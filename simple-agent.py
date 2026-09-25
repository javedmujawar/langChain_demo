from langchain_ollama import OllamaLLM, ChatOllama


# model = OllamaLLM(model="qwen3:1.7b")

# resonse = model.invoke("who are you?")

# print(resonse)


model = ChatOllama(model="qwen3:1.7b")

resonse = model.invoke(
    [("system", "you are a helpful teacher"), ("human", "who are you?")]
)

print(resonse)
