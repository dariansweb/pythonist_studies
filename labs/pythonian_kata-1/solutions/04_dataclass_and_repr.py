
from dataclasses import dataclass, field
from typing import List

@dataclass
class Rectangle:
    width: float
    height: float
    tags: List[str] = field(default_factory=list)

    @property
    def area(self) -> float:
        return self.width * self.height

def debug_rectangles(rects: List["Rectangle"]) -> str:
    return "\n".join(repr(r) for r in rects)

if __name__ == "__main__":
    r1 = Rectangle(3, 4)
    r2 = Rectangle(10, 2)
    assert r1.area == 12
    r1.tags.append("wide")
    assert r2.tags == []
    s = debug_rectangles([r1, r2])
    assert isinstance(s, str) and "\n" in s
