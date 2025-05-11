import logging
from mcp.server.fastmcp import FastMCP

from agents.logger_config import setup_logger

mcp = FastMCP("Calc:Add")
logger = setup_logger(mcp.name)


@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    result = a + b
    logger.info(f"add() called with a={a}, b={b}, result={result}")
    return result


if __name__ == "__main__":
    logger.info(f"Starting: {mcp.name} ")
    mcp.run()  # from mcp.server.fastmcp import FastMCP
