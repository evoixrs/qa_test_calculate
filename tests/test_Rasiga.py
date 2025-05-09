from src.calc import calculate

def test_addition():
    assert add(1, 2) == 3
    assert add(-1, -1) == -2
    assert add(0, 0) == 0

def test_subtraction():
    assert subtract(5, 3) == 2
    assert subtract(0, 4) == -4
    assert subtract(-3, -2) == -1

def test_multiplication():
    assert multiply(2, 3) == 6
    assert multiply(-1, 5) == -5
    assert multiply(0, 100) == 0
