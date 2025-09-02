
# Pythonian Kata
Exercises to drill Python idioms: snake_case, comprehensions, unpacking, EAFP, context managers,
dataclasses, generators, itertools, pattern matching, typing, and a dash of logging.

## How to use
1) Open each `NN_*` file in the root and implement the TODOs.
2) Run `python run_all_tests.py` to check your work (simple asserts; no external deps).
3) Peek at `solutions/` if you get stuck, then come back and implement it yourself.

## Files
- 01_comprehensions.py
- 02_unpacking_and_enumerate.py
- 03_eafp_and_context.py
- 04_dataclass_and_repr.py
- 05_generators_and_itertools.py
- 06_pattern_matching.py
- run_all_tests.py

Solutions for each live in `solutions/` with the same names.


---

## Badges
![CI](https://img.shields.io/badge/CI-GitHub_Actions-informational)
![Style](https://img.shields.io/badge/style-Black-000000.svg)
![Lint](https://img.shields.io/badge/lint-Ruff-46a2f1)

## Quickstart (GitHub Template)
1. Create a new repo on GitHub and push this content, or click "Use this template" if hosted there.
2. Run the tests locally: `python run_all_tests.py`
3. Optional quality checks: `make fmt && make lint`

## Suggested Branch Protections
- Require CI to pass.
- Require at least one review.
