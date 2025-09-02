
from typing import Any, Dict, Optional

def handle_message(msg: Dict[str, Any]) -> Optional[str]:
    match msg:
        case {"type": "ping"}:
            return "pong"
        case {"type": "greet", "name": str(name)}:
            return f"hello {name}"
        case {"type": "sum", "nums": list(nums)}:
            try:
                return str(sum(int(n) for n in nums))
            except (ValueError, TypeError):
                return None
        case _:
            return None
