from langchain.agents import create_agent
from langchain_ollama import ChatOllama
from langchain.tools import tool


@tool
def find_all_arguments(text: str) -> list[int]:
    """Extract all numbers from the user's mathematical question."""
    return [int(number) for number in re.findall(r"\d+", text)]

@tool
def find_opration(text: str) -> str:
    """Extract all numbers from the user's mathematical question."""
    return text


@tool
def calculate(arr: list[int], method: str) -> int:
    """Calculate numbers using the requested mathematical operation."""

    if method == "add":
        return sum(arr)

    if method == "multiply":
        result = 1
        for number in arr:
            result *= number
        return result

    return 0


model = ChatOllama(model="qwen3:1.7b")

agent = create_agent(
    model,
    tools=[find_all_arguments, find_opration, calculate],
    system_prompt="you are a agent, that help to calculate, which provided by user. As final result you need to send only result in number full message is not needed. final message should result: result",
)


def runAgent(usrPrompt: str):
    """this is main agent function where we are putting all steps and logic"""
    result = agent.invoke({"messages": [{"role": "user", "content": usrPrompt}]})

    print(result["messages"][-1].content)


if __name__ == "__main__":
    runAgent("calculate multiplication of 2 3 4 and 8")
