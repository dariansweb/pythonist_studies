"""
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
