# Create a small datetime kata with exercises, solutions, and tests.
import os, textwrap, json, datetime
base = "./datetime_kata"   # creates a folder in the same directory as the script

os.makedirs(base, exist_ok=True)

exercises = r'''"""
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
'''

solutions = r'''"""
Datetime + relativedelta KATA (Solutions)
----------------------------------------
Peek only if you must. Each function mirrors one in the exercises.
"""

from datetime import datetime, date, timedelta
from typing import Iterable, Iterator, Optional, Tuple
from dateutil.relativedelta import relativedelta, MO, TU, WE, TH, FR, SA, SU, weekday as WD


def _is_eom(d: date) -> bool:
    return (d + relativedelta(day=31)).day == d.day


def add_months_eom_aware(dt: date, months: int) -> date:
    if _is_eom(dt):
        return (dt + relativedelta(months=months, day=31))
    # Normal month add with clipping
    return dt + relativedelta(months=months)


def next_business_day(d: date, holidays: Optional[Iterable[date]] = None) -> date:
    holidays = set(holidays or ())
    cur = d + timedelta(days=1)
    while cur.weekday() >= 5 or cur in holidays:
        cur += timedelta(days=1)
    return cur


def nth_weekday_of_month(year: int, month: int, nth: int, weekday: int) -> date:
    # weekday int: 0..6, map to dateutil weekday constant via WD
    if nth == -1:
        return date(year, month, 1) + relativedelta(day=31, weekday=WD(weekday)(-1))
    return date(year, month, 1) + relativedelta(weekday=WD(weekday)(nth))


def fiscal_quarter_bounds(d: date, fiscal_year_start_month: int = 1) -> Tuple[date, date]:
    # Normalize month index so fiscal month 1 == fiscal_year_start_month
    offset = (d.month - fiscal_year_start_month) % 12  # 0..11
    q_index = offset // 3  # 0..3
    q_start_month = ((q_index * 3) + fiscal_year_start_month - 1) % 12 + 1
    q_start_year = d.year
    # If quarter is in the "previous" calendar year due to wrap
    if q_start_month > d.month and fiscal_year_start_month != 1:
        q_start_year -= 1
    start = date(q_start_year, q_start_month, 1)
    end = start + relativedelta(months=3, days=-1)
    return start, end


def age_ymd(born: date, on: date) -> Tuple[int, int, int]:
    if on < born:
        raise ValueError("on-date precedes birth-date")
    delta = relativedelta(on, born)
    return delta.years, delta.months, delta.days


def overlap_days(a_start: date, a_end: date, b_start: date, b_end: date) -> int:
    if a_end < a_start or b_end < b_start:
        return 0
    start = max(a_start, b_start)
    end = min(a_end, b_end)
    if end < start:
        return 0
    return (end - start).days + 1


def first_business_day_after_nth_weekday(year: int, month: int, nth: int, weekday: int,
                                         holidays: Optional[Iterable[date]] = None) -> date:
    from dateutil.relativedelta import weekday as WD
    anchor = nth_weekday_of_month(year, month, nth, weekday)
    return next_business_day(anchor, holidays=holidays)


def recur_every_k_months_on_last_weekday(start: date, k: int, weekday: int, count: int) -> Iterator[date]:
    from dateutil.relativedelta import weekday as WD
    cur = date(start.year, start.month, 1)
    for _ in range(count):
        yield cur + relativedelta(day=31, weekday=WD(weekday)(-1))
        cur = cur + relativedelta(months=k)


def classify_day(d: date) -> str:
    def is_eom(x: date) -> bool:
        return (x + relativedelta(day=31)).day == x.day

    def is_business_day(x: date) -> bool:
        return x.weekday() < 5

    # 1) Feb 29
    if d.month == 2 and d.day == 29:
        return "rare_bird"
    # 2) Friday the 13th
    if d.day == 13 and d.weekday() == 4:
        return "spooky"
    # 3) EOM and weekend
    if is_eom(d) and not is_business_day(d):
        return "party"
    # 4) First business day of the month
    # Find first of month, then advance to first business day
    first_of_month = d.replace(day=1)
    first_biz = first_of_month
    while first_biz.weekday() >= 5:
        first_biz += timedelta(days=1)
    if d == first_biz:
        return "fresh_start"
    # 5) else
    return "meh"


def round_to_billing_anchor(d: date, anchor_day: int) -> Tuple[date, date]:
    if not (1 <= anchor_day <= 28 or anchor_day in (30, 31)):
        raise ValueError("anchor_day must be between 1..28 or 30/31")
    # Down: same month (clamped), on/before d; if after d, go one month back
    def clamp(y: int, m: int) -> date:
        # clamp to end-of-month if anchor overflow
        base = date(y, m, 1) + relativedelta(day=31)  # last day of month
        day = min(anchor_day, base.day)
        return date(y, m, day)

    down = clamp(d.year, d.month)
    if down > d:
        prev = d + relativedelta(months=-1)
        down = clamp(prev.year, prev.month)

    # Up: strictly after d
    nxt = d + relativedelta(months=0)  # same month baseline
    up = clamp(nxt.year, nxt.month)
    if up <= d:
        nxt = d + relativedelta(months=1)
        up = clamp(nxt.year, nxt.month)
    return down, up
'''

tests = r'''"""
Tests for the datetime kata.
Run:
    python -m pytest -q
or:
    python tests_datetime_kata.py
"""
from datetime import date, timedelta
from dateutil.relativedelta import MO, TU, WE, TH, FR, SA, SU
import pytest

import exercises_datetime_kata as ex


def test_add_months_eom_aware():
    assert ex.add_months_eom_aware(date(2024,1,31), 1) == date(2024,2,29)
    assert ex.add_months_eom_aware(date(2024,2,29), 12) == date(2025,2,28)
    assert ex.add_months_eom_aware(date(2024,4,30), 1) == date(2024,5,31)
    assert ex.add_months_eom_aware(date(2024,3,30), 1) == date(2024,4,30)
    assert ex.add_months_eom_aware(date(2024,3,15), 1) == date(2024,4,15)


def test_next_business_day():
    h = {date(2025, 1, 6)}
    assert ex.next_business_day(date(2025,1,3)) == date(2025,1,6)  # Fri -> Mon
    assert ex.next_business_day(date(2025,1,4)) == date(2025,1,6)  # Sat -> Mon
    assert ex.next_business_day(date(2025,1,5), holidays=h) == date(2025,1,7)  # Sun -> Mon (holiday) -> Tue


def test_nth_weekday_of_month():
    assert ex.nth_weekday_of_month(2025, 1, 3, 4) == date(2025,1,17)  # 3rd Friday
    assert ex.nth_weekday_of_month(2025, 5, -1, 2) == date(2025,5,28)  # last Wednesday


def test_fiscal_quarter_bounds():
    # Fiscal year starts in April
    assert ex.fiscal_quarter_bounds(date(2025,4,2), 4) == (date(2025,4,1), date(2025,6,30))
    assert ex.fiscal_quarter_bounds(date(2025,12,15), 4) == (date(2025,10,1), date(2025,12,31))
    assert ex.fiscal_quarter_bounds(date(2026,1,2), 4) == (date(2026,1,1), date(2026,3,31))


def test_age_ymd():
    assert ex.age_ymd(date(1980, 6, 15), date(2025, 8, 19)) == (45, 2, 4)
    assert ex.age_ymd(date(2000, 2, 29), date(2001, 2, 28)) == (0, 11, 30)
    with pytest.raises(ValueError):
        ex.age_ymd(date(2000,1,1), date(1999,1,1))


def test_overlap_days():
    assert ex.overlap_days(date(2025,1,1), date(2025,1,10), date(2025,1,5), date(2025,1,15)) == 6
    assert ex.overlap_days(date(2025,1,1), date(2025,1,10), date(2025,1,11), date(2025,1,20)) == 0
    assert ex.overlap_days(date(2025,1,5), date(2025,1,5), date(2025,1,5), date(2025,1,5)) == 1


def test_first_business_day_after_nth_weekday():
    holidays = {date(2025,11,24)}  # suppose Monday after 3rd Fri is a holiday
    assert ex.first_business_day_after_nth_weekday(2025, 11, 3, 4, holidays) == date(2025,11,25)


def test_recur_every_k_months_on_last_weekday():
    got = list(ex.recur_every_k_months_on_last_weekday(date(2025,1,2), 2, 4, 3))
    assert got == [date(2025,1,31), date(2025,3,28), date(2025,5,30)]  # last Fridays


def test_classify_day():
    assert ex.classify_day(date(2024,2,29)) == "rare_bird"
    assert ex.classify_day(date(2026,2,13)) == "spooky"          # Friday the 13th
    assert ex.classify_day(date(2025,8,31)) == "party"           # assume 2025-08-31 is Sunday
    assert ex.classify_day(date(2025,9,1)) == "fresh_start"      # 1st is Monday
    assert ex.classify_day(date(2025,9,2)) == "meh"


def test_round_to_billing_anchor():
    down, up = ex.round_to_billing_anchor(date(2025,2,28), 31)
    assert down == date(2025,1,31)
    assert up == date(2025,3,31)
    down, up = ex.round_to_billing_anchor(date(2025,2,1), 30)
    assert down == date(2025,1,30)
    assert up == date(2025,2,28)
'''

with open(os.path.join(base, "exercises_datetime_kata.py"), "w") as f:
    f.write(exercises)

with open(os.path.join(base, "solutions_datetime_kata.py"), "w") as f:
    f.write(solutions)

with open(os.path.join(base, "tests_datetime_kata.py"), "w") as f:
    f.write(tests)

base
