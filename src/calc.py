from src.calc import calculate

def test_addition():
    assert calculate(2, 3, '+') == 5
    assert calculate(-1, 1, '+') == 0
    assert calculate(0, 0, '+') == 0

def test_subtraction():
    assert calculate(5, 3, '-') == 2
    assert calculate(10, -5, '-') == 15
    assert calculate(0, 0, '-') == 0

def test_multiplication():
    assert calculate(2, 3, '*') == 6
    assert calculate(-1, 1, '*') == -1
    assert calculate(0, 5, '*') == 0

def test_division():
    assert calculate(6, 3, '/') == 2
    assert calculate(1, 2, '/') == 0.5
    assert calculate(5, 0, '/') == "Ошибка: деление на ноль!"

def test_invalid_operation():
    assert calculate(2, 3, 'invalid') == "Неверная операция"