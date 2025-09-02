
from typing import Iterable, List, Tuple

def number_lines(lines: Iterable[str], start: int = 1) -> List[Tuple[int, str]]:
    return [(i, line) for i, line in enumerate(lines, start=start)]

def pairwise_sums(a: Iterable[int], b: Iterable[int]) -> List[int]:
    return [x + y for x, y in zip(a, b)]

def swap_xy(point: Tuple[int, int]) -> Tuple[int, int]:
    x, y = point
    return (y, x)
