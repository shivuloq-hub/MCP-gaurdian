
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
WORKSPACE = (PROJECT_ROOT / "safe_workspace").resolve()


def get_safe_path(filename: str) -> Path:
    """Return a safe file path inside safe_workspace."""

    if not filename or not filename.strip():
        raise ValueError("Filename cannot be empty.")

    requested_path = (WORKSPACE / filename).resolve()

    if not requested_path.is_relative_to(WORKSPACE):
        raise ValueError("Access denied: path outside safe workspace.")

    if requested_path.is_symlink():
        raise ValueError("Access denied: symbolic links are not allowed.")

    return requested_path
