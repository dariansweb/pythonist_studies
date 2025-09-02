
"""
02 — Unpacking, enumerate, zip
Goal: Iterate without range(len(...)), unpack tuples, and stitch sequences with zip.
"""

from typing import Iterable, List, Tuple

def number_lines(lines: Iterable[str], start: int = 1) -> List[Tuple[int, str]]:
    """Return [(n, line)] pairs using enumerate with the given start."""
    # TODO
    raise NotImplementedError

def pairwise_sums(a: Iterable[int], b: Iterable[int]) -> List[int]:
    """Return element-wise sums for pairs from a and b using zip (stop at the shortest)."""
    # TODO
    raise NotImplementedError

def swap_xy(point: Tuple[int, int]) -> Tuple[int, int]:
    """Return (y, x) using tuple unpacking (no indexing)."""
    # TODO
    raise NotImplementedError

if __name__ == "__main__":
    assert number_lines(["a","b"], start=10) == [(10,"a"),(11,"b")]
    assert pairwise_sums([1,2,3], [10,20]) == [11,22]
    assert swap_xy((5,9)) == (9,5)
    print("02 ok")
