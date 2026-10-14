
from pathlib import Path

WORKSPACE = (
    Path(__file__).resolve().parents[2] / "safe_workspace"
).resolve()


def read_file(filename: str) -> str:
    """Read a text file from the approved safe workspace only."""

    requested_path = (WORKSPACE / filename).resolve()

    # Block paths that point outside the safe workspace.
    if not requested_path.is_relative_to(WORKSPACE):
        raise ValueError("Access denied: path outside safe workspace.")

    # Allow regular files only.
    if not requested_path.is_file() or requested_path.is_symlink():
        raise ValueError("File does not exist or is not allowed.")

    try:
        return requested_path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        raise ValueError("File is not a valid UTF-8 text file.")
