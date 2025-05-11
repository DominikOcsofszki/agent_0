from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.memory import InMemorySaver

from agents.ollama_helper import llm_ollama

checkpointer = InMemorySaver()

agent = create_react_agent(
    model=llm_ollama,
    tools=[get_weather],
    checkpointer=checkpointer,
)

# Run the agent
config = {"configurable": {"thread_id": "1"}}
sf_response = agent.invoke(
    {"messages": [{"role": "user", "content": "what is the weather in sf"}]}, config
)
ny_response = agent.invoke(
    {"messages": [{"role": "user", "content": "what about new york?"}]}, config
)
