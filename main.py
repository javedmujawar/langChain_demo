from langchain.agents import create_agent

def calculator(expression: str) -> str:
    """Calculate a basic mathematical expression."""
    try:
        return str(eval(expression))
    except Exception:
        return "Invalid mathematical expression"

def runAgent():
    print("----- create agent -----")
    agent = create_agent(
        model="ollama:qwen3:1.7b", system_prompt="You are a helpful assistant"
    )
    result = agent.invoke({"messages": [{"role": "user", "content": "2+5"}]})
    print(result["messages"])
    print("----- end agent -----")


if __name__ == "__main__":
    runAgent()
