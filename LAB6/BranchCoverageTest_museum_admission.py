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


def test_age_zero_is_free():
    assert ticket_price("child", 0, "tuesday", False) == 0


def test_age_four_is_free():
    assert ticket_price("child", 4, "tuesday", False) == 0


def test_age_five_is_charged():
    assert ticket_price("child", 5, "tuesday", False) == 100


def test_monday_half_price():
    assert ticket_price("adult", 30, "monday", False) == 150


def test_saturday_surcharge():
    assert ticket_price("adult", 30, "saturday", False) == 350


def test_sunday_surcharge():
    assert ticket_price("adult", 30, "sunday", False) == 350


def test_friday_no_adjustment():
    assert ticket_price("senior", 70, "friday", False) == 200


def test_no_tour_student():
    assert ticket_price("student", 20, "tuesday", False) == 150


def test_tour_student_extra_50():
    assert ticket_price("student", 20, "tuesday", True) == 200


def test_tour_adult_extra_100():
    assert ticket_price("adult", 30, "tuesday", True) == 400


def test_tour_senior_extra_100():
    assert ticket_price("senior", 70, "tuesday", True) == 300


def test_monday_student_with_tour():
    assert ticket_price("student", 20, "monday", True) == 125


def test_sunday_senior_with_tour():
    assert ticket_price("senior", 70, "sunday", True) == 350


def test_group_size_zero_raises():
    with pytest.raises(ValueError, match="invalid group size"):
        group_discount(0, False)


def test_group_size_one_is_valid():
    assert group_discount(1, False) == 0


def test_school_group_of_twenty():
    assert group_discount(20, True) == 40


def test_school_group_of_nineteen():
    assert group_discount(19, True) == 25


def test_small_school_group():
    assert group_discount(1, True) == 25


def test_regular_group_of_fifteen():
    assert group_discount(15, False) == 20


def test_regular_group_of_fourteen():
    assert group_discount(14, False) == 10


def test_regular_group_of_eight():
    assert group_discount(8, False) == 10


def test_regular_group_of_seven():
    assert group_discount(7, False) == 0


def test_gallery_full_wait():
    assert gallery_entry(100, 100, False) == "wait"


def test_gallery_over_capacity_wait():
    assert gallery_entry(120, 100, True) == "wait"


def test_gallery_nearly_full_no_slot_queue():
    assert gallery_entry(99, 100, False) == "queue"


def test_gallery_at_90_percent_queue():
    assert gallery_entry(90, 100, False) == "queue"


def test_gallery_just_below_90_percent_enter():
    assert gallery_entry(89, 100, False) == "enter"


def test_gallery_nearly_full_with_slot_enter():
    assert gallery_entry(99, 100, True) == "enter"


def test_gallery_empty_enter():
    assert gallery_entry(0, 100, False) == "enter"