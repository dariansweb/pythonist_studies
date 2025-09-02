
from pathlib import Path
from typing import Any, Mapping

def safe_get(mapping: Mapping[str, Any], key: str, default: Any = None) -> Any:
    try:
        return mapping[key]
    except KeyError:
        return default

def count_lines(path: Path) -> int:
    count = 0
    with path.open("r", encoding="utf-8") as f:
        for _ in f:
            count += 1
    return count
