# Калькулятор
### Описание проекта

Простой калькулятор с базовыми арифметическими операциями и тестами для проверки функциональности.

### Функциональность:

Сложение (add) - сложение двух чисел

Вычитание (subtract) - вычитание второго числа из первого

Умножение (multiply) - умножение двух чисел

Деление (divide) - деление первого числа на второе (с проверкой деления на ноль)

### Установка

Требования

Python 3.6+

pytest (для запуска тестов)

Установка зависимостей
```bash
pip install pytest
```

## Структура проекта

project/
├── calculator.py      # Основной модуль калькулятора
└── test_calculator.py # Тесты для калькулятора


## Использование
1. Запуск калькулятора из командной строки:
```bash
python calculator.py <операция> <число1> <число2>
```

### Доступные операции:

add - сложение

subtract - вычитание

multiply - умножение

divide - деление

Примеры использования:

```bash
# Сложение
python calculator.py add 5 3
# Результат: 8.0

# Вычитание
python calculator.py subtract 10 4
# Результат: 6.0

# Умножение
python calculator.py multiply 7 2
# Результат: 14.0

# Деление
python calculator.py divide 15 3
# Результат: 5.0
```


2. Использование как модуль
```python
from calculator import add, subtract, multiply, divide

result = add(10, 5)  # 15.0
result = divide(20, 4)  # 5.0
```

### Запуск тестов
Запуск всех тестов
```bash
pytest test_calculator.py -v Запуск с подробным выводом
```

```bash
pytest test_calculator.py -v -s
```

### Запуск конкретного теста
``` bash
# Запуск только тестов сложения
pytest test_calculator.py::test_add -v

# Запуск только тестов деления
pytest test_calculator.py::test_divide -v
```

### Описание тестов
Тесты проверяют:

test_add - корректность сложения положительных и отрицательных чисел

test_subtract - корректность вычитания в разных порядках

test_multiply - корректность умножения положительных и отрицательных чисел

test_divide - корректность деления и обработку деления на ноль

### Обработка ошибок
При делении на ноль возникает исключение ValueError с сообщением "Нельзя делить на ноль."

Все функции принимают и возвращают значения типа float

## Пример вывода тестов
При успешном выполнении тестов вы увидите:

```text
test_calculator.py::test_add PASSED
test_calculator.py::test_subtract PASSED
test_calculator.py::test_multiply PASSED
test_calculator.py::test_divide PASSED
```
