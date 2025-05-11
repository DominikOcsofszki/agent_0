import asyncio
from contextlib import asynccontextmanager
from typing import Annotated

from typing_extensions import TypedDict

from langgraph.graph import StateGraph, START
from langgraph.graph.message import add_messages

from agents import helper_graph
from agents.helper_graph import run_graph, show_graph
from agents.load_mcp import get_mcp_client_from_json
from agents.ollama_helper import llm_ollama


class State(TypedDict):
    # Messages have the type "list". The `add_messages` function
    # in the annotation defines how this state key should be updated
    # (in this case, it appends messages to the list, rather than overwriting them)
    messages: Annotated[list, add_messages]


async def build_graph():
    graph_builder: StateGraph = StateGraph(State)
    llm = llm_ollama
    mcp_json_file = "/Users/dominik/2025/GPT/mcp/agents/src/agents/tools/Apply/"

    client = await get_mcp_client_from_json(mcp_json_file)
    tools = client.get_tools()

    llm_with_tools = llm.bind_tools(tools)

    def chatbot(state: State):
        return {"messages": [llm.invoke(state["messages"])]}

    def chatbot_rag(state: State):
        return {"messages": [llm_with_tools.invoke(state["messages"])]}

    graph_builder.add_node("chatbot", chatbot)
    graph_builder.add_node("chatbot_rag", chatbot_rag)

    graph_builder.add_edge(START, "chatbot")
    graph = graph_builder.compile()
    # run_graph(graph)
    return graph


async def run():
    graph = await build_graph()
    helper_graph.run_graph(graph)


if __name__ == "__main__":
    asyncio.run(run())
