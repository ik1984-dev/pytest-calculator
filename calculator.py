def add(a: float, b: float) -> float:
    return a + b

def subtract(a: float, b: float) -> float:
    return a - b

def multiply(a: float, b: float) -> float:
    return a * b

def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Нельзя делить на ноль.")
    return a / b

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Простой калькулятор.")
    parser.add_argument("operation", choices=["add", "subtract", "multiply", "divide"], help="Операция: сложение, вычитание, умножение, деление")
    parser.add_argument("a", type=float, help="Первый операнд")
    parser.add_argument("b", type=float, help="Второй операнд")

    args = parser.parse_args()

    operations = {
        "add": add,
        "subtract": subtract,
        "multiply": multiply,
        "divide": divide
    }

    result = operations[args.operation](args.a, args.b)
    print(f"Результат: {result}")

