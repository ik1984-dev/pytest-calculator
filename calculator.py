"""
Простой калькулятор с базовыми арифметическими операциями.
Поддерживает сложение, вычитание, умножение и деление с обработкой ошибок.
"""


def add(a: float, b: float) -> float:
    """
    Сложение двух чисел.

    Args:
        a (float): Первое слагаемое
        b (float): Второе слагаемое

    Returns:
        float: Сумма a и b
    """
    return a + b


def subtract(a: float, b: float) -> float:
    """
    Вычитание двух чисел.

    Args:
        a (float): Уменьшаемое
        b (float): Вычитаемое

    Returns:
        float: Разность a и b (a - b)
    """
    return a - b


def multiply(a: float, b: float) -> float:
    """
    Умножение двух чисел.

    Args:
        a (float): Первый множитель
        b (float): Второй множитель

    Returns:
        float: Произведение a и b
    """
    return a * b


def divide(a: float, b: float) -> float:
    """
    Деление двух чисел.

    Args:
        a (float): Делимое
        b (float): Делитель

    Returns:
        float: Частное от деления a на b

    Raises:
        ValueError: Если делитель b равен нулю
    """
    if b == 0:
        raise ValueError("Нельзя делить на ноль.")
    return a / b


if __name__ == "__main__":
    # Импорт модуля argparse для обработки аргументов командной строки
    import argparse

    # Создание парсера аргументов с описанием программы
    parser = argparse.ArgumentParser(description="Простой калькулятор.")

    # Добавление аргументов:
    # operation - тип операции (обязательный аргумент)
    parser.add_argument("operation",
                        choices=["add", "subtract", "multiply", "divide"],
                        help="Операция: сложение, вычитание, умножение, деление")

    # a - первый операнд (обязательный аргумент, преобразуется в float)
    parser.add_argument("a",
                        type=float,
                        help="Первый операнд")

    # b - второй операнд (обязательный аргумент, преобразуется в float)
    parser.add_argument("b",
                        type=float,
                        help="Второй операнд")

    # Парсинг аргументов командной строки
    args = parser.parse_args()

    # Словарь для сопоставления строковых операций с функциями
    operations = {
        "add": add,  # Сложение
        "subtract": subtract,  # Вычитание
        "multiply": multiply,  # Умножение
        "divide": divide  # Деление
    }

    # Выполнение выбранной операции с переданными аргументами
    result = operations[args.operation](args.a, args.b)

    # Вывод результата
    print(f"Результат: {result}")