#2. Реализовать программу с функционалом калькулятора для операций
# над двумя числами. Числа и операция вводятся пользователем с клавиатуры.
# Использовать обработку исключений.

def calculate(a: float, b: float, op: str) -> float:
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        return a / b
    elif op == '**':
        return a ** b
    elif op == '%':
        return a % b
    else:
        raise ValueError(f"Не поддерживаемая операция: '{op}'")

try:
    a_input = input("Введите первое число: ").strip()
    b_input = input("Введите второе число: ").strip()
    op = input("Введите операцию (+, -, *, /, **, %): ").strip()

    a = float(a_input)
    b = float(b_input)

    if op == '/' and b == 0:
        raise ZeroDivisionError(" Деление на ноль недопустимо.")
    if op == '%' and b == 0:
        raise ZeroDivisionError("Остаток от деления на ноль недопустим.")

    result = calculate(a, b, op)
    print(f"Результат: {a} {op} {b} = {result}")

except ValueError as ve:
        print(f"Ошибка ввода: {ve}")
except ZeroDivisionError as zde:
        print(f"Ошибка вычисления: {zde}")
except Exception as e:
        print(f"Произошла неожиданная ошибка: {e}")

