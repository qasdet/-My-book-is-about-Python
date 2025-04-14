# Полное руководство по pytest

## Содержание
1. [Введение](#введение)
2. [Установка и базовая настройка](#установка-и-базовая-настройка)
3. [Конфигурация pytest.ini](#конфигурация-pytestini)
4. [Фикстуры](#фикстуры)
5. [Хуки](#хуки)
6. [Параметризация тестов](#параметризация-тестов)
7. [Маркеры](#маркеры)
8. [Лучшие практики](#лучшие-практики)

## Введение
pytest - это мощный фреймворк для тестирования Python-кода. Он предоставляет простой синтаксис для написания тестов и богатый набор функций для их выполнения.

## Установка и базовая настройка
```bash
pip install pytest
```

## Конфигурация pytest.ini
Файл pytest.ini позволяет настроить поведение pytest:

```ini
[pytest]
# Паттерны для поиска тестовых файлов
python_files = test_*.py *_test.py

# Маркеры тестов
markers =
    slow: marks tests as slow (deselect with '-m "not slow"')
    integration: marks tests as integration tests

# Опции по умолчанию
addopts = -v --tb=short

# Игнорируемые директории
norecursedirs = .* venv dist build

# Настройка вывода
console_output_style = progress

# Максимальное время выполнения теста
timeout = 300
```

## Фикстуры
Фикстуры - это мощный механизм для подготовки тестового окружения:

```python
import pytest

@pytest.fixture(scope="session")
def db_connection():
    # Установка соединения с БД
    connection = create_connection()
    yield connection
    # Закрытие соединения после всех тестов
    connection.close()

@pytest.fixture(scope="function")
def temp_data():
    # Подготовка временных данных
    data = {"test": "value"}
    yield data
    # Очистка после каждого теста
    data.clear()

def test_database(db_connection, temp_data):
    assert db_connection.is_connected()
    assert temp_data["test"] == "value"
```

## Хуки
Хуки позволяют настраивать поведение pytest на разных этапах выполнения тестов:

```python
# conftest.py
def pytest_configure(config):
    """Конфигурация перед запуском тестов"""
    config.addinivalue_line("markers", "slow: mark test as slow running")

def pytest_collection_modifyitems(session, config, items):
    """Модификация собранных тестов"""
    for item in items:
        if "slow" in item.keywords:
            item.add_marker(pytest.mark.skip(reason="slow tests are disabled"))

def pytest_runtest_setup(item):
    """Выполняется перед каждым тестом"""
    print(f"Setting up test: {item.name}")
```

## Параметризация тестов
Параметризация позволяет запускать один тест с разными входными данными:

```python
import pytest

@pytest.mark.parametrize("input,expected", [
    ("hello", 5),
    ("world", 5),
    ("", 0)
])
def test_string_length(input, expected):
    assert len(input) == expected

# Параметризация с несколькими аргументами
@pytest.mark.parametrize("x", [1, 2])
@pytest.mark.parametrize("y", [3, 4])
def test_multiplication(x, y):
    print(f"{x} * {y} = {x * y}")
```

## Маркеры
Маркеры помогают организовывать и фильтровать тесты:

```python
import pytest

@pytest.mark.slow
def test_slow_operation():
    # долгая операция
    pass

@pytest.mark.skip(reason="not implemented yet")
def test_future_feature():
    pass

@pytest.mark.xfail(strict=True)
def test_known_failure():
    assert False

@pytest.mark.dependency(depends=["test_a"])
def test_b():
    pass
```

## Лучшие практики

### 1. Организация тестов
```python
# test_module.py
class TestUserService:
    def test_create_user(self):
        pass

    def test_delete_user(self):
        pass

    @pytest.mark.parametrize("user_data", [
        {"name": "John", "age": 30},
        {"name": "Jane", "age": 25}
    ])
    def test_update_user(self, user_data):
        pass
```

### 2. Эффективное использование фикстур
```python
# conftest.py
import pytest

@pytest.fixture(scope="session")
def app_config():
    return {
        "database_url": "postgresql://localhost/test",
        "api_key": "test_key"
    }

@pytest.fixture(scope="function", autouse=True)
def setup_logging():
    # Настройка логирования перед каждым тестом
    yield
    # Очистка логов после каждого теста
```

### 3. Оптимизация производительности
```python
# pytest.ini
[pytest]
# Параллельное выполнение тестов
addopts = -n auto

# Пропуск медленных тестов
markers =
    slow: marks tests as slow
```

### 4. Обработка исключений
```python
def test_exception_handling():
    with pytest.raises(ValueError) as exc_info:
        raise ValueError("test error")
    assert str(exc_info.value) == "test error"

@pytest.mark.xfail(raises=ZeroDivisionError)
def test_division_by_zero():
    1 / 0
```

### 5. Временные файлы и директории
```python
def test_with_tmpdir(tmpdir):
    # tmpdir - это встроенная фикстура pytest
    file_path = tmpdir.join("test.txt")
    file_path.write("test content")
    assert file_path.read() == "test content"
```

### Tips and Tricks

1. **Использование capsys для проверки вывода:**
```python
def test_output(capsys):
    print("hello")
    captured = capsys.readouterr()
    assert captured.out == "hello\n"
```

2. **Пропуск тестов при определенных условиях:**
```python
import sys

@pytest.mark.skipif(sys.version_info < (3, 7),
                    reason="requires python3.7 or higher")
def test_new_feature():
    pass
```

3. **Кастомные сравнения:**
```python
@pytest.mark.assertrepr_compare(op='==')
def assert_equal_detailed(op, left, right):
    return ["Detailed comparison:",
            f"Left: {left}",
            f"Right: {right}"]
```

4. **Динамическое создание тестов:**
```python
def pytest_generate_tests(metafunc):
    if "param" in metafunc.fixturenames:
        metafunc.parametrize("param",
                           [1, 2, 3])
```

5. **Профилирование тестов:**
```ini
# pytest.ini
[pytest]
addopts = --durations=10 --durations-min=1.0
```

Эта документация охватывает основные аспекты работы с pytest и предоставляет практические примеры для эффективного использования фреймворка. Используйте эти техники и рекомендации для создания надежных и поддерживаемых тестов.