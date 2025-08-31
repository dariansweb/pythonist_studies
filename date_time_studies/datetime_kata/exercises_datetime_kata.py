"""
Datetime + relativedelta KATA (Exercises)
----------------------------------------
Dude, fill in the functions below. Each one is a compact brain teaser
using `datetime` and `dateutil.relativedelta`. Avoid over-nesting; prefer
guard clauses and small helpers. Run `tests_datetime_kata.py` locally to
check yourself.

Dependencies:
    pip install python-dateutil

Conventions:
- Use timezone-naive datetimes unless explicitly asked to handle TZs.
- Prefer `relativedelta` over naive month math (months are weird).
- Keep conditionals readable (early returns > pyramids of doom).
"""

from datetime import datetime, date, timedelta
from typing import Iterable, Iterator, Optional, Tuple
from dateutil.relativedelta import relativedelta, MO, TU, WE, TH, FR, SA, SU


# 1) End-of-month preserving add
def add_months_eom_aware(dt: date, months: int) -> date:
    """
    Add `months` to `dt`. If `dt` is the last day of its month,
    return the last day of the target month (EOM-preserving behavior).
    Otherwise, behave like normal month addition (clip as needed).

    Examples (not exhaustive):
    - 2024-01-31 + 1 month -> 2024-02-29
    - 2024-02-29 + 12 months -> 2025-02-28
    - 2024-04-30 + 1 month -> 2024-05-31
    - 2024-03-30 + 1 month -> 2024-04-30

    TODO: implement
    """
    raise NotImplementedError


# 2) Next business day, skipping optional holidays set
def next_business_day(d: date, holidays: Optional[Iterable[date]] = None) -> date:
    """
    Return the next business day (Mon-Fri) strictly AFTER `d`.
    If the next day is a holiday (in the provided iterable), skip it too.

    TODO: implement
    """
    raise NotImplementedError


# 3) Nth weekday of a month
def nth_weekday_of_month(year: int, month: int, nth: int, weekday: int) -> date:
    """
    Return the date of the nth weekday (1..5 or -1 for last) within the given month.
    Weekday: Monday=0 ... Sunday=6 (match datetime.weekday())

    Hints:
    - Use dateutil.relativedelta with weekday constants (MO, TU, ...).
    - For last weekday, `weekday(-1)` gets you there.

    TODO: implement
    """
    raise NotImplementedError


# 4) Rolling quarter boundaries (fiscal year start configurable)
def fiscal_quarter_bounds(d: date, fiscal_year_start_month: int = 1) -> Tuple[date, date]:
    """
    Given a date `d`, return (start_date, end_date) for the fiscal quarter
    containing `d`, where the fiscal year starts at `fiscal_year_start_month`.

    Example: if fiscal year starts in April (4), then:
        Q1: Apr-Jun, Q2: Jul-Sep, Q3: Oct-Dec, Q4: Jan-Mar.

    The end_date should be inclusive (the last day of the quarter).

    TODO: implement
    """
    raise NotImplementedError


# 5) Age components (y, m, d) using relativedelta
def age_ymd(born: date, on: date) -> Tuple[int, int, int]:
    """
    Return age as (years, months, days) as of `on`.
    Use relativedelta so calendar weirdness (leap years) is handled.

    TODO: implement
    """
    raise NotImplementedError


# 6) Window overlap in whole days (>=0), else 0
def overlap_days(a_start: date, a_end: date, b_start: date, b_end: date) -> int:
    """
    Given two inclusive windows [a_start, a_end] and [b_start, b_end],
    return the number of whole days they overlap. If no overlap, return 0.

    Hints:
    - Normalize by ensuring starts <= ends (or guard early).
    - Intersection start is max(starts), intersection end is min(ends).
    - Days are inclusive: delta = (end - start).days + 1 when end >= start.

    TODO: implement
    """
    raise NotImplementedError


# 7) First business day after the nth weekday
def first_business_day_after_nth_weekday(year: int, month: int, nth: int, weekday: int,
                                         holidays: Optional[Iterable[date]] = None) -> date:
    """
    Example: “first business day after the 3rd Friday of Nov 2025”.
    Compute the nth weekday and then advance to the next business day
    (skipping weekends and provided holidays).

    TODO: implement
    """
    raise NotImplementedError


# 8) Recurrence generator: every k months on the last weekday of the month
def recur_every_k_months_on_last_weekday(start: date, k: int, weekday: int, count: int) -> Iterator[date]:
    """
    Yield `count` occurrences starting from the month of `start` (inclusive),
    each occurrence being the last specified weekday (Mon=0..Sun=6) of the month,
    jumping by `k` months each time.

    Example: start=2025-01-02, k=2, weekday=4 (Friday), count=3
      -> yields last Friday of Jan 2025, Mar 2025, May 2025.

    TODO: implement
    """
    raise NotImplementedError


# 9) “Weird” rule-set (practice your if/elif readability):
def classify_day(d: date) -> str:
    """
    Classify a date using the following rules (first match wins):
      1) If it's Feb 29 -> "rare_bird"
      2) Else if it's Friday the 13th -> "spooky"
      3) Else if it's the last day of the month AND a weekend -> "party"
      4) Else if it's the first business day of the month -> "fresh_start"
      5) Else -> "meh"

    Use small helpers and early returns to avoid nesting.

    TODO: implement
    """
    raise NotImplementedError


# 10) Relative rounding: round a date up/down to the nearest "billing anchor"
def round_to_billing_anchor(d: date, anchor_day: int) -> Tuple[date, date]:
    """
    Given a date `d` and an `anchor_day` (1..28), return a tuple
    (down, up) where:
      - `down` is the most recent date on or before `d` whose day == anchor_day
      - `up`   is the next date strictly after `d` whose day == anchor_day

    If the month doesn't have `anchor_day` (e.g., 30/31), clamp to the last
    day of that month.

    Example: d=2025-02-28, anchor_day=31 -> down=2025-01-31, up=2025-03-31

    TODO: implement
    """
    raise NotImplementedError
