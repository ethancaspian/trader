import pytest
from src.utils.helpers import safe_float, safe_int, calculate_zscore

class TestHelpers:
    def test_safe_float_valid(self):
        assert safe_float("1.23") == 1.23
        assert safe_float(45) == 45.0

    def test_safe_float_invalid(self):
        assert safe_float("invalid") is None
        assert safe_float(None, default=0.0) == 0.0

    def test_safe_int_valid(self):
        assert safe_int("42") == 42
        assert safe_int(3.14) == 3

    def test_safe_int_invalid(self):
        assert safe_int("bad", default=7) == 7
        assert safe_int(None) is None

    def test_calculate_zscore(self):
        series = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        result = calculate_zscore(series, 5)
        assert isinstance(result, float)
