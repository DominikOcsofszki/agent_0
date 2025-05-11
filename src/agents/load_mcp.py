import asyncio
from contextlib import asynccontextmanager
import json
from typing import Any
from icecream import ic
from langchain_core.messages import AIMessage, HumanMessage
from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.graph.graph import CompiledGraph
from langgraph.prebuilt import create_react_agent

from agents.ollama_helper import llm_ollama
from agents.tools.get_all_mcp import get_mcp_config_from_dir


def get_json_mcp(mcp_json_file):
    return get_mcp_config_from_dir(mcp_json_file)


async def get_mcp_client_from_json(mcp_json_file):
    mcp_config = get_json_mcp(mcp_json_file)
    async with MultiServerMCPClient(mcp_config) as client:
        return client


async def create_agent(mcp_json_file) -> CompiledGraph:
    client = await get_mcp_client_from_json(mcp_json_file)
    tools = client.get_tools()
    print("=================", flush=True)
    for x in tools:
        print(x, flush=True)
    print("=================", flush=True)

    agent: CompiledGraph = create_react_agent(llm_ollama, tools)
    return agent


# async def ask_agent(agent: CompiledGraph, content) -> dict[str, Any] | Any:
async def ask_agent(agent: CompiledGraph, content) -> dict[str, Any]:
    # res = await agent.invoke({"messages": [{"role": "user", "content": content}]})
    res = await agent.ainvoke({"messages": [{"role": "user", "content": content}]})
    ic(res)
    return res


async def main():
    MCP_TOOLS_DIR = "/Users/dominik/2025/GPT/mcp/agents/src/agents/tools/Calculate/"
    agent = await create_agent(MCP_TOOLS_DIR)
    # res = await ask_agent(agent, "what's (3 + 5) x 12?")
    content = "what's (3 + 5) x 12?"
    content = "what's (3 + 5)"
    res = await ask_agent(agent, content)
    listMessages: list[AIMessage | HumanMessage] = res.get("messages")
    for x in listMessages:
        ic(x)
        # ic(x.content)
        if isinstance(x, AIMessage):
            ic("=================")
            ic(x.tool_calls)
            ic("=================")


if __name__ == "__main__":
    asyncio.run(main())
