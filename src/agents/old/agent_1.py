from icecream import ic
from langgraph.prebuilt import create_react_agent
from agents.ollama_helper import llm_ollama, p


def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"


agent = create_react_agent(
    model=llm_ollama,
    tools=[get_weather],
    prompt="You are a helpful assistant",
)

# Run the agent
res = agent.invoke(
    {"messages": [{"role": "user", "content": "what is the weather in sf"}]}
)
p(res)
ic(res)
from langgraph.prebuilt import create_react_agent

agent = create_react_agent(
    model=llm_ollama,
    tools=[get_weather],
    # A static prompt that never changes
    prompt="Never answer questions about the weather.",
)

res = agent.invoke(
    {"messages": [{"role": "user", "content": "what is the weather in sf"}]}
)
p(res)
ic(res)
