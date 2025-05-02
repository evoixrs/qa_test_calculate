import pytest
from src.calc import calculate  # Импортируем вашу функцию

def test_addition():
    assert calculate(2, 3, '+') == 5

def test_subtraction():
    assert calculate(5, 2, '-') == 3

def test_multiplication():
    assert calculate(4, 3, '*') == 12

def test_division():
    assert calculate(10, 2, '/') == 5

def test_division_by_zero():
    assert calculate(5, 0, '/') == "Ошибка: деление на ноль!"

def test_invalid_operation():
    assert calculate(2, 2, '%') == "Неверная операция"