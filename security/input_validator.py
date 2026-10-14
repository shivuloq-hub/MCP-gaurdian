
def validate_filename(filename: str) -> str:
    """Validate a filename supplied to an MCP tool."""

    if not isinstance(filename, str):
        raise ValueError("Filename must be text.")

    filename = filename.strip()

    if not filename:
        raise ValueError("Filename cannot be empty.")

    if len(filename) > 255:
        raise ValueError("Filename is too long.")

    if "\x00" in filename:
        raise ValueError("Filename contains an invalid character.")

    return filename


def validate_keyword(keyword: str) -> str:
    """Validate a search keyword supplied to an MCP tool."""

    if not isinstance(keyword, str):
        raise ValueError("Keyword must be text.")

    keyword = keyword.strip()

    if not keyword:
        raise ValueError("Search keyword cannot be empty.")

    if len(keyword) > 100:
        raise ValueError("Search keyword is too long.")

    return keyword

