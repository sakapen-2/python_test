import pytest
from app import get_full_name


def test_get_full_name_success():
    assert get_full_name("Ali", "Ahmadi") == "Hello Ali Ahmadi 👋"


def test_get_full_name_empty_first_name():
    with pytest.raises(ValueError):
        get_full_name("", "Ahmadi")


def test_get_full_name_empty_last_name():
    with pytest.raises(ValueError):
        get_full_name("Ali", "")

