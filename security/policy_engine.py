
ALLOWED_TOOLS = {
    "list_files",
    "read_file",
    "search_file",
}


def is_tool_allowed(tool_name: str) -> bool:
    """Check whether a tool is approved by the security policy."""

    if not isinstance(tool_name, str):
        return False

    return tool_name in ALLOWED_TOOLS
