
from typing import Iterable, Dict, List, Set

def squares(nums: Iterable[int]) -> List[int]:
    return [n*n for n in nums]

def even_squares(nums: Iterable[int]) -> List[int]:
    return [n*n for n in nums if n % 2 == 0]

def word_index(words: Iterable[str]) -> Dict[str, int]:
    return {w: i for i, w in enumerate(words) if w not in locals().setdefault("_seen", set()) and not _seen.add(w)}  # playful trick avoided below

# Cleaner version avoiding tricks:
def word_index(words: Iterable[str]) -> Dict[str, int]:  # type: ignore[no-redef]
    seen: Dict[str, int] = {}
    for i, w in enumerate(words):
        if w not in seen:
            seen[w] = i
    return seen

def unique_normalized(items: Iterable[str]) -> Set[str]:
    return {s.strip().lower() for s in items}
