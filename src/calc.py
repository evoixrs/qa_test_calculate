def calculate(x, y, operation):
    if operation == '+':
        return x + y
    elif operation == '-':
        return x - y
    elif operation == '*':
        return x * y
    elif operation == '/':
        if y == 0:
            return "Ошибка: деление на ноль!"
        return x / y
    else:
        return "Неверная операция"