from mcp.server.fastmcp import FastMCP

from agents.logger_config import setup_logger

mcp = FastMCP("Calc:mul")
logger = setup_logger(mcp.name)


@mcp.tool()
def mul(a: int, b: int) -> int:
    """Mul two numbers"""
    result = a * b
    logger.info(f"mul() called with a={a}, b={b}, result={result}")
    return result


if __name__ == "__main__":
    logger.info(f"Starting: {mcp.name} ")
    mcp.run()
