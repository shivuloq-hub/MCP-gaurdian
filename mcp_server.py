
from fastmcp import FastMCP

from components.tools.list_files import list_files
from components.tools.read_file import read_file
from components.tools.search_file import search_file

mcp = FastMCP("Guarding-the-Agent")

# Register the approved tools with the MCP server.
mcp.tool(list_files)
mcp.tool(read_file)
mcp.tool(search_file)


if __name__ == "__main__":
    mcp.run()
