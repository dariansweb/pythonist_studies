
from pathlib import Path
from typing import Generator, Iterable, List
import itertools

def read_chunks(path: Path, size: int = 8192) -> Generator[bytes, None, None]:
    with path.open("rb") as f:
        while (chunk := f.read(size)):
            yield chunk

def running_totals(nums: Iterable[int]) -> List[int]:
    return list(itertools.accumulate(nums))

def batched(iterable: Iterable[int], n: int) -> List[List[int]]:
    # Try itertools.batched if available
    if hasattr(itertools, "batched"):
        return [list(batch) for batch in itertools.batched(iterable, n)]  # type: ignore[attr-defined]
    # Fallback
    batch: List[int] = []
    out: List[List[int]] = []
    for x in iterable:
        batch.append(x)
        if len(batch) == n:
            out.append(batch)
            batch = []
    if batch:
        out.append(batch)
    return out
