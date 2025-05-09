from src.calc import calculate

def test_calc_addition():
    """Тестирование сложения"""
    assert calculate(10, 2, '+') == 12
    assert calculate(-5, -3, '+') == -8  

def test_calc_subtraction():
    """Тестирование вычитания"""
    assert calculate(10, 2, '-') == 8
    assert calculate(5, 10, '-') == -5  

def test_calc_multiplication():
    """Тестирование умножения"""
    assert calculate(10, 2, '*') == 20
    assert calculate(-5, 3, '*') == -15  

def test_calc_division():
    """Тестирование деления"""
    assert calculate(10, 2, '/') == 5
    assert calculate(1, 2, '/') == 0.5  

def test_division_by_zero():
    """Проверка деления на ноль"""
    assert calculate(10, 0, '/') == "Ошибка: деление на ноль!"

def test_invalid_operation():
    """Проверка неверной операции"""
    assert calculate(10, 2, 'invalid') == "Неверная операция"