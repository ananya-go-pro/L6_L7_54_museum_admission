import pytest
from museum_admission import ticket_price, group_discount, gallery_entry


def test_adult_weekday():
    assert ticket_price("adult", 30, "tuesday", False) == 300


def test_small_group():
    assert group_discount(4, False) == 0


def test_unknown_category_raises():
    with pytest.raises(ValueError, match="unknown category"):
        ticket_price("tourist", 30, "tuesday", False)


def test_negative_age_raises():
    with pytest.raises(ValueError, match="invalid age"):
        ticket_price("adult", -1, "tuesday", False)


def test_under_five_is_free():
    assert ticket_price("child", 4, "tuesday", False) == 0


def test_monday_half_price():
    assert ticket_price("adult", 30, "monday", False) == 150


def test_weekend_surcharge():
    assert ticket_price("adult", 30, "saturday", False) == 350


def test_guided_tour_student():
    assert ticket_price("student", 20, "tuesday", True) == 200


def test_guided_tour_adult():
    assert ticket_price("adult", 30, "tuesday", True) == 400


def test_group_size_zero_raises():
    with pytest.raises(ValueError, match="invalid group size"):
        group_discount(0, False)


def test_large_school_group():
    assert group_discount(20, True) == 40


def test_small_school_group():
    assert group_discount(10, True) == 25


def test_large_regular_group():
    assert group_discount(15, False) == 20


def test_medium_regular_group():
    assert group_discount(8, False) == 10


def test_gallery_full_wait():
    assert gallery_entry(100, 100, False) == "wait"


def test_gallery_nearly_full_queue():
    assert gallery_entry(95, 100, False) == "queue"


def test_gallery_enter():
    assert gallery_entry(50, 100, False) == "enter"
