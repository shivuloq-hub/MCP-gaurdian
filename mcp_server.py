
from fastmcp import FastMCP

mcp = FastMCP("Guarding-the-Agent")


@mcp.tool
def hello() -> str:
    """Check that the MCP server is working."""
    return "Guarding the Agent MCP server is running!"


if __name__ == "__main__":
    mcp.run()
