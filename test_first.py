import first
import unittest
import pytest

def test_positive_values():
    length = 5
    width = 10
    expected_result = 50
    actual_result = first.get_rectangle(length, width)
    assert actual_result == expected_result


def test_zero_width():
    length = 8
    width = 0
    expected_result = 0
    actual_result = first.get_rectangle(length, width)
    assert actual_result == expected_result


def test_negative_length():
    length = -5
    width = 10
    expected_result = -1
    actual_result = first.get_rectangle(length, width)
    assert actual_result == expected_result

@pytest.mark.parametrize("length, width, expected_result", [[5,10,50],[8,0,0],[-5,10,-1]])
def test_all(length, width, expected_result):
    actual_result = first.get_rectangle(length, width)
    assert actual_result == expected_result

class TestGetRectangle:
    @pytest.mark.parametrize("length, width, expected_result", [[5, 10, 50], [8, 0, 0], [-5, 10, -1]])
    def test_all(self,length, width, expected_result):
        actual_result = first.get_rectangle(length, width)
        assert actual_result == expected_result
