from langchain.agents import create_agent
from langchain_ollama import ChatOllama
from langchain.tools import tool


@tool
def calculate(a, b):
    """this is tool/ function which take two number and return sum/addtion of two numbers"""
    return a + b


model = ChatOllama(model="qwen3:1.7b")

agent = create_agent(
    model,
    tools=[calculate],
    system_prompt="you are a agent, that help to calculate, which provided by user",
)


def runAgent(usrPrompt: str):
    """ this is main agent function where we are putting all steps and logic"""
    result = agent.invoke({"messages": [{"role": "user", "content": usrPrompt}]})

    print(result)


if __name__ == "__main__":
    runAgent("What is sum of 2 and 5")
