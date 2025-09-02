
"""
01 — Comprehensions
Goal: Build lists, sets, and dicts with comprehension syntax; filter with guards; prefer clarity.
"""

from typing import Iterable, Dict, List, Set

def squares(nums: Iterable[int]) -> List[int]:
    """Return the square of each value in order. Use a list comprehension."""
    # TODO: implement with a list comprehension
    raise NotImplementedError

def even_squares(nums: Iterable[int]) -> List[int]:
    """Return squares of even numbers only. Use a guard inside the comprehension."""
    # TODO
    raise NotImplementedError

def word_index(words: Iterable[str]) -> Dict[str, int]:
    """Return a mapping of word -> first index seen. Use a dict comprehension and enumerate."""
    # TODO
    raise NotImplementedError

def unique_normalized(items: Iterable[str]) -> Set[str]:
    """Return a set of lowercased, stripped items. Use a set comprehension."""
    # TODO
    raise NotImplementedError

if __name__ == "__main__":
    assert squares([1,2,3]) == [1,4,9]
    assert even_squares(range(6)) == [0,4,16]
    assert word_index(["a","b","a","c"]) == {"a":0,"b":1,"c":3}
    assert unique_normalized(["  Hi","hi  ","HI"]) == {"hi"}
    print("01 ok")
