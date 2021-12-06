from my_funcs.utils import division
import pytest


@pytest.mark.parametrize("a, b, expected", [(10, 2, 5),
                                            (20, 10, 2),
                                            (10, 5, 2)])
def test_division_g(a, b, expected):
    assert division(a, b) == expected


@pytest.mark.parametrize("expected_exception, divider, divisionable",
                         [(ZeroDivisionError, 0, 10),
                          (TypeError, "2", 20)])
def test_division_with_error(expected_exception, divider, divisionable):
    with pytest.raises(expected_exception):
        division(divisionable, divider)
