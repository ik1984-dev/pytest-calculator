import pytest
from calculator import add, subtract, multiply, divide

def test_add(capfd):
    for a, b in [(2, 3), (-1, -1)]:
        result = add(a, b)
        print(f"Тестирование сложения с a={a}, b={b}: {result}")
        assert result == a + b

def test_subtract(capfd):
    for a, b in [(5, 3), (3, 5)]:
        result = subtract(a, b)
        print(f"Тестирование вычитания с a={a}, b={b}: {result}")
        assert result == a - b

def test_multiply(capfd):
    for a, b in [(2, 3), (-1, 1)]:
        result = multiply(a, b)
        print(f"Тестирование умножения с a={a}, b={b}: {result}")
        assert result == a * b

def test_divide(capfd):
    for a, b in [(6, 3)]:
        result = divide(a, b)
        print(f"Тестирование деления с a={a}, b={b}: {result}")
        assert result == a / b

    with pytest.raises(ValueError) as excinfo:
        divide(5, 0)
    print("Тестирование деления на ноль вызвало ValueError, как и ожидалось.")
    assert str(excinfo.value) == "Нельзя делить на ноль."  # Изменение на русский текст

