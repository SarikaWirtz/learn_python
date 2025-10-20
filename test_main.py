import pytest
from main import add, subtract, multiply, divide


class TestAdd:
    def test_add_positive_numbers(self):
        assert add(2, 3) == 4

    def test_add_negative_numbers(self):
        assert add(-2, -3) == -5

    def test_add_mixed_numbers(self):
        assert add(-2, 3) == 1

    def test_add_zero(self):
        assert add(0, 5) == 5


class TestSubtract:
    def test_subtract_positive_numbers(self):
        assert subtract(5, 3) == 2

    def test_subtract_negative_numbers(self):
        assert subtract(-5, -3) == -2

    def test_subtract_mixed_numbers(self):
        assert subtract(5, -3) == 8

    def test_subtract_zero(self):
        assert subtract(5, 0) == 5


class TestMultiply:
    def test_multiply_positive_numbers(self):
        assert multiply(2, 3) == 6

    def test_multiply_negative_numbers(self):
        assert multiply(-2, -3) == 6

    def test_multiply_mixed_numbers(self):
        assert multiply(-2, 3) == -6

    def test_multiply_by_zero(self):
        assert multiply(5, 0) == 0


class TestDivide:
    def test_divide_positive_numbers(self):
        assert divide(6, 3) == 2

    def test_divide_negative_numbers(self):
        assert divide(-6, -3) == 2

    def test_divide_mixed_numbers(self):
        assert divide(-6, 3) == -2

    def test_divide_by_zero_raises_error(self):
        with pytest.raises(ValueError, match="Cannot divide by zero."):
            divide(5, 0)

    def test_divide_result_float(self):
        assert divide(7, 2) == 3.5
