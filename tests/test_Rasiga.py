from src.calc import add, subtract, multiply

def test_addition():
    assert add(2, 3) == 5 

def test_subtraction():
    assert subtract(5, 3) == 2 

def test_multiplication():
    assert multiply(2, 3) == 6 