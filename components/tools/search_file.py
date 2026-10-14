
from pathlib import Path

WORKSPACE = (
    Path(__file__).resolve().parents[2] / "safe_workspace"
).resolve()


def search_file(keyword: str) -> list[str]:
    """Search for a keyword in text files inside the safe workspace."""

    if not keyword or not keyword.strip():
        raise ValueError("Search keyword cannot be empty.")

    if not WORKSPACE.is_dir():
        raise RuntimeError("Safe workspace directory does not exist.")

    results = []

    for path in WORKSPACE.iterdir():
        if not path.is_file() or path.is_symlink():
            continue

        try:
            content = path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue

        if keyword.casefold() in content.casefold():
            results.append(path.name)

    return sorted(results)
