"""
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
