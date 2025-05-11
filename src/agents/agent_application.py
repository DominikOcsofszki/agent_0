import os
import asyncio
from contextlib import asynccontextmanager
from typing import Annotated, Sequence, TypedDict

from langchain_core.messages import AIMessage, BaseMessage, HumanMessage
from langchain_core.messages.tool import ToolMessage
from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import END, START, StateGraph
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode, tools_condition

from agents.ollama_helper import llm_ollama
from agents.tools.get_all_mcp import get_mcp_config_from_dir
from icecream import ic


class State(TypedDict):
    messages: Annotated[Sequence[BaseMessage], add_messages]


MCP_DIR = "/Users/dominik/2025/GPT/mcp/agents/src/agents/tools"
MCP_DIR_TOOLS = f"{MCP_DIR}/Apply/"
model = llm_ollama


@asynccontextmanager
async def make_graph():
    mcp_client = MultiServerMCPClient(get_mcp_config_from_dir(MCP_DIR_TOOLS))

    def agent(state: State):
        messages = state["messages"]
        response = llm_with_tool.invoke(messages)
        return {"messages": [response]}

    async with mcp_client:
        mcp_tools = mcp_client.get_tools()
        print(f"Available tools:", flush=True)
        for x in [tool.name for tool in mcp_tools]:
            print(x, flush=True)
        llm_with_tool = model.bind_tools(mcp_tools)

        # Compile application and test
        graph_builder = StateGraph(State)
        graph_builder.add_node(agent)
        graph_builder.add_node("tool", ToolNode(mcp_tools))

        graph_builder.add_edge(START, "agent")

        # Decide whether to retrieve
        graph_builder.add_conditional_edges(
            "agent",
            # Assess agent decision
            tools_condition,
            {
                # Translate the condition outputs to nodes in our graph
                "tools": "tool",
                END: END,
            },
        )
        graph_builder.add_edge("tool", "agent")

        graph = graph_builder.compile()
        graph.name = "Tool Agent"

        yield graph


def print_all_ai_messages(listMessages):
    for x in listMessages:
        if isinstance(x, AIMessage):
            print(f"Ai: {x.content}")


def print_all_human_messages(listMessages):
    for x in listMessages:
        if isinstance(x, HumanMessage):
            print(f"Human: {x.content}")


def print_all_tool(listMessages):
    for x in listMessages:
        if isinstance(x, ToolMessage):
            print(f"Tool: {x.content}")


# Run the graph with question
async def main():
    async with make_graph() as graph:
        question = "dominik.ocsofszki@mail.com, "
        # Educational Background – B.S. in Computer Science from University of Washington (2018); Certified AWS Solutions Architect (2023)
        question = """Interview Date – May 9, 2025  
Candidate Full Name – Priya Desai  
Technical Skills Assessment – Strong proficiency in Python, JavaScript, and SQL. Demonstrated solid understanding of React and Node.js during technical questions. Familiar with Docker and CI/CD pipelines. Lacks deep experience in cloud-native development but showed fast learning potential.  
Problem-Solving & Algorithmic Thinking – Approached problems methodically. Solved two out of three algorithm questions accurately. Explained thought process clearly and optimized code after initial draft.  
Communication Skills – Articulate and concise. Able to explain technical decisions in simple terms. Good at active listening and clarified requirements before answering.  
Consulting Mindset / Client Interaction Potential – Demonstrated maturity in discussing ambiguous client requirements. Gave examples of past client interactions and showed ability to frame technical work in business terms. Asked insightful questions.  
Cultural Fit & Team Collaboration – Collaborative mindset. Expressed interest in pair programming and agile environments. Values diversity and mentorship. Seemed a good fit for a team-oriented culture.  
Overall Interview Performance – Strong overall. Technically competent, thoughtful, and personable. Some areas for growth in advanced cloud infrastructure.  
Recommendation / Next Steps – Recommend moving to final round. Assess deeper system design and cloud architecture knowledge.  
"""
        # question = "What info is needed for applicant"
        result = await graph.ainvoke({"messages": question})
        listMessages: list[ToolMessage | AIMessage | HumanMessage] = result.get(
            "messages"
        )
        print_all_tool(listMessages)
        print_all_human_messages(listMessages)
        print_all_ai_messages(listMessages)


asyncio.run(main())
