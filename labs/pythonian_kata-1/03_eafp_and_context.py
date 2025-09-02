
"""
03 — EAFP & Context Managers
Goal: Prefer EAFP over LBYL and use 'with' for file handling.
"""

from pathlib import Path
from typing import Any, Mapping

def safe_get(mapping: Mapping[str, Any], key: str, default: Any = None) -> Any:
    """Return mapping[key] if present, else default (use try/except KeyError)."""
    # TODO
    raise NotImplementedError

def count_lines(path: Path) -> int:
    """Open the file and count lines using a context manager (no manual close)."""
    # TODO
    raise NotImplementedError

if __name__ == "__main__":
    d = {"a": 1}
    assert safe_get(d, "a", 0) == 1
    assert safe_get(d, "b", 0) == 0

    tmp = Path("tmp_03.txt")
    tmp.write_text("one\nTwo\nthree\n")
    try:
        assert count_lines(tmp) == 3
    finally:
        tmp.unlink(missing_ok=True)
    print("03 ok")
