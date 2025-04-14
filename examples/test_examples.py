import pytest
from datetime import datetime

# Фикстуры различных уровней
@pytest.fixture(scope="session")
def app_config():
    """Фикстура уровня сессии для конфигурации приложения"""
    config = {
        "api_url": "http://api.example.com",
        "timeout": 30,
        "max_retries": 3
    }
    return config

@pytest.fixture(scope="module")
def database_connection():
    """Фикстура уровня модуля для подключения к базе данных"""
    # Здесь был бы код подключения к БД
    connection = {"status": "connected"}
    yield connection
    # Очистка после использования
    connection.clear()

@pytest.fixture(scope="function")
def temp_user():
    """Фикстура уровня функции для создания временного пользователя"""
    user = {"id": 1, "name": "Test User", "created_at": datetime.now()}
    yield user
    # Очистка после каждого теста
    user.clear()

# Примеры параметризованных тестов
@pytest.mark.parametrize("input_data,expected", [
    ({"name": "John", "age": 30}, True),
    ({"name": "Jane"}, False),
    ({}, False)
])
def test_user_data_validation(input_data, expected):
    """Тест валидации данных пользователя"""
    def is_valid_user(data):
        return all(key in data for key in ["name", "age"])
    
    assert is_valid_user(input_data) == expected

# Пример использования маркеров
@pytest.mark.slow
@pytest.mark.integration
def test_slow_integration(app_config):
    """Медленный интеграционный тест"""
    assert "api_url" in app_config
    assert app_config["timeout"] > 0

# Пример теста с ожидаемым исключением
def test_exception_handling():
    """Тест обработки исключений"""
    with pytest.raises(ValueError) as exc_info:
        raise ValueError("Некорректное значение")
    assert str(exc_info.value) == "Некорректное значение"

# Пример класса тестов
class TestUserService:
    @pytest.fixture(autouse=True)
    def setup(self):
        """Автоматически используемая фикстура для настройки"""
        self.users = []

    def test_add_user(self, temp_user):
        """Тест добавления пользователя"""
        self.users.append(temp_user)
        assert len(self.users) == 1
        assert self.users[0]["name"] == "Test User"

    @pytest.mark.parametrize("user_id,expected_found", [
        (1, True),
        (999, False)
    ])
    def test_find_user(self, temp_user, user_id, expected_found):
        """Тест поиска пользователя"""
        self.users.append(temp_user)
        found = any(user["id"] == user_id for user in self.users)
        assert found == expected_found

# Пример использования временных файлов
def test_file_operations(tmpdir):
    """Тест операций с файлами"""
    file_path = tmpdir.join("test.txt")
    content = "Тестовое содержимое"
    
    # Запись в файл
    file_path.write(content)
    
    # Чтение из файла
    assert file_path.read() == content

# Пример проверки вывода
def test_output_capture(capsys):
    """Тест захвата вывода"""
    print("Тестовый вывод")
    captured = capsys.readouterr()
    assert captured.out == "Тестовый вывод\n"

# Пример использования моков
def test_mock_example(mocker):
    """Тест с использованием моков"""
    mock_function = mocker.patch("time.time")
    mock_function.return_value = 12345
    
    import time
    assert time.time() == 12345

# Пример асинхронного теста
@pytest.mark.asyncio
async def test_async_operation():
    """Тест асинхронной операции"""
    async def async_func():
        return "результат"
    
    result = await async_func()
    assert result == "результат"

# Пример использования параметров командной строки
def test_command_line_option(pytestconfig):
    """Тест использования параметров командной строки"""
    verbose = pytestconfig.getoption("verbose")
    assert isinstance(verbose, int)

# Пример пропуска теста при определенном условии
@pytest.mark.skipif(condition=True, reason="Тест пропущен по условию")
def test_conditional():
    """Тест, который будет пропущен"""
    assert False

# Пример теста с зависимостями
@pytest.mark.dependency()
def test_a():
    """Тест A"""
    assert True

@pytest.mark.dependency(depends=["test_a"])
def test_b():
    """Тест B, зависящий от теста A"""
    assert True