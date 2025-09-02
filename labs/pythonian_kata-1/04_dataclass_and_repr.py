
"""
04 — Dataclass, __repr__, properties
Goal: Model clean data with dataclasses, default factories, and a computed property.
"""

from dataclasses import dataclass, field
from typing import List

# TODO: Create a @dataclass named Rectangle with fields width: float, height: float
# - Provide a default_factory for a tags: List[str] field
# - Add a read-only @property 'area' (width * height)
# - Let Python generate a nice __repr__ via dataclass

# TODO: write a helper that returns a friendly string using __repr__
def debug_rectangles(rects: List["Rectangle"]) -> str:
    """Return a single string with one rectangle per line using repr()."""
    raise NotImplementedError

if __name__ == "__main__":
    # basic behavior
    from typing import Any
    # Construct a couple rectangles
    # TODO: r1 = Rectangle(...); r2 = Rectangle(...)
    # Check property
    # TODO: assert r1.area == ...
    # Ensure tags is an independent list per instance
    # TODO: r1.tags.append("wide"); assert r2.tags == []
    # Debug string
    # TODO: s = debug_rectangles([r1, r2]); assert isinstance(s, str) and "\n" in s
    print("04 ok")
