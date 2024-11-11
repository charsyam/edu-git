import pytest
from calculator import add, subtract, multiply, divide

class TestCalculator:
    def test_add(self):
        assert add(1, 2) == 3
        assert add(-1, 1) == 0
        assert add(0, 0) == 0
        assert add(100, 200) == 300

    def test_subtract(self):
        assert subtract(5, 3) == 2
        assert subtract(1, 1) == 0
        assert subtract(0, 5) == -5
        assert subtract(10, -5) == 15

    def test_multiply(self):
        assert multiply(2, 3) == 6
        assert multiply(-2, 3) == -6
        assert multiply(-2, -3) == 6
        assert multiply(0, 5) == 0

    def test_divide(self):
        assert divide(6, 2) == 3
        assert divide(5, 2) == 2.5
        assert divide(-6, 2) == -3
        assert divide(0, 5) == 0

    def test_divide_by_zero(self):
        with pytest.raises(ValueError, match="0으로 나눌 수 없습니다"):
            divide(5, 0)

    def test_edge_cases(self):
        # 큰 숫자 테스트
        assert add(999999, 1) == 1000000
        assert multiply(99999, 0) == 0
        
        # 음수 테스트
        assert add(-5, -7) == -12
        assert multiply(-3, -4) == 12