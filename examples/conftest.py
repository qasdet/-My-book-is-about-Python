import pytest
import logging
from datetime import datetime

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Хук конфигурации pytest
def pytest_configure(config):
    """Конфигурация перед запуском тестов"""
    # Регистрация пользовательских маркеров
    config.addinivalue_line("markers", "slow: mark test as slow running")
    config.addinivalue_line("markers", "integration: mark test as integration test")
    config.addinivalue_line("markers", "api: mark test as API test")
    
    # Добавление пользовательских опций
    config.addinivalue_line(
        "markers",
        "env(name): mark test to run only on named environment"
    )

# Хук модификации собранных тестов
def pytest_collection_modifyitems(session, config, items):
    """Модификация собранных тестов"""
    for item in items:
        # Добавление меток для медленных тестов
        if "slow" in item.keywords:
            item.add_marker(pytest.mark.skip(reason="slow tests are disabled"))
        
        # Добавление дополнительной информации к тестам
        item.user_properties.append(
            ("timestamp", datetime.now().isoformat())
        )

# Хук для настройки перед каждым тестом
def pytest_runtest_setup(item):
    """Выполняется перед каждым тестом"""
    logger.info(f"Setting up test: {item.name}")
    # Проверка окружения для тестов с маркером env
    for marker in item.iter_markers(name="env"):
        env_name = marker.args[0]
        if env_name != "test":  # Пример проверки окружения
            pytest.skip(f"test requires env {env_name}")

# Хук для действий после каждого теста
def pytest_runtest_teardown(item, nextitem):
    """Выполняется после каждого теста"""
    logger.info(f"Tearing down test: {item.name}")

# Глобальная фикстура для всех тестов
@pytest.fixture(scope="session")
def global_config():
    """Глобальная конфигурация для всех тестов"""
    return {
        "environment": "test",
        "log_level": "INFO",
        "timeout": 30
    }

# Фикстура для измерения времени выполнения
@pytest.fixture(autouse=True)
def timer():
    """Автоматически измеряет время выполнения каждого теста"""
    start = datetime.now()
    yield
    duration = datetime.now() - start
    logger.info(f"Test duration: {duration}")

# Фикстура для работы с временными данными
@pytest.fixture()
def temp_data(tmpdir):
    """Создает временную директорию с тестовыми данными"""
    data_file = tmpdir.join("test_data.json")
    data_file.write('{"test": "data"}')
    return data_file

# Фикстура для эмуляции базы данных
@pytest.fixture(scope="session")
def db():
    """Эмулирует подключение к базе данных"""
    class TestDB:
        def __init__(self):
            self.data = {}
        
        def insert(self, key, value):
            self.data[key] = value
        
        def get(self, key):
            return self.data.get(key)
        
        def clear(self):
            self.data.clear()
    
    return TestDB()

# Фикстура для очистки после каждого теста
@pytest.fixture(autouse=True)
def cleanup():
    """Автоматическая очистка после каждого теста"""
    yield
    # Здесь можно добавить код очистки
    logger.info("Cleaning up after test")

# Пользовательская фикстура для параметризации
@pytest.fixture(params=["user1", "user2", "admin"])
def user_type(request):
    """Параметризованная фикстура для разных типов пользователей"""
    return request.param

# Фикстура для мока HTTP-клиента
@pytest.fixture
def mock_http_client(mocker):
    """Создает мок HTTP-клиента"""
    class MockResponse:
        def __init__(self, status_code=200, json_data=None):
            self.status_code = status_code
            self.json_data = json_data or {}
        
        def json(self):
            return self.json_data
    
    mock_get = mocker.patch("requests.get")
    mock_get.return_value = MockResponse()
    return mock_get