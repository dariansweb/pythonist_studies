
"""
06 — Pattern Matching
Goal: Use 'match' to cleanly dispatch on message shape.
"""

from typing import Any, Dict, Optional

def handle_message(msg: Dict[str, Any]) -> Optional[str]:
    """
    Implement behavior:
    - {"type": "ping"} -> "pong"
    - {"type": "greet", "name": <str>} -> "hello <name>"
    - {"type": "sum", "nums": [ints]} -> "<sum>"
    - default -> None
    Use match/case with a guard for type checks where needed.
    """
    # TODO
    raise NotImplementedError

if __name__ == "__main__":
    assert handle_message({"type": "ping"}) == "pong"
    assert handle_message({"type": "greet", "name": "Dude"}) == "hello Dude"
    assert handle_message({"type": "sum", "nums": [1,2,3]}) == "6"
    assert handle_message({"type": "sum", "nums": []}) == "0"
    assert handle_message({"type": "???","x":42}) is None
    print("06 ok")
