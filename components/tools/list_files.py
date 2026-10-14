
from pathlib import Path

WORKSPACE = (
    Path(__file__).resolve().parents[2] / "safe_workspace"
).resolve()


def list_files() -> list[str]:
    """List files available in the approved safe workspace."""

    if not WORKSPACE.is_dir():
        raise RuntimeError("Safe workspace directory does not exist.")

    return sorted(
        path.name
        for path in WORKSPACE.iterdir()
        if path.is_file() and not path.is_symlink()
    )
