
"""
05 — Generators & itertools
Goal: Stream data with generators, then compose operations.
"""

from pathlib import Path
from typing import Generator, Iterable, List
import itertools

def read_chunks(path: Path, size: int = 8192) -> Generator[bytes, None, None]:
    """Yield chunks of bytes from the file. Use a while loop and := walrus with f.read()."""
    # TODO
    raise NotImplementedError

def running_totals(nums: Iterable[int]) -> List[int]:
    """Return running totals (prefix sums). Use itertools.accumulate."""
    # TODO
    raise NotImplementedError

def batched(iterable: Iterable[int], n: int) -> List[List[int]]:
    """Group items into lists of length n (last may be shorter). Use itertools.batched (py3.12+) or fallback."""
    # TODO
    raise NotImplementedError

if __name__ == "__main__":
    p = Path("tmp_05.bin")
    p.write_bytes(b"abcdefghij")
    try:
        chunks = list(read_chunks(p, size=4))
        assert chunks == [b"abcd", b"efgh", b"ij"]
    finally:
        p.unlink(missing_ok=True)

    assert running_totals([1,2,3,4]) == [1,3,6,10]
    assert batched([1,2,3,4,5], 2) == [[1,2],[3,4],[5]]
    print("05 ok")
