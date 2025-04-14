# Бинарные типы данных в Python

## Описание
Python предоставляет три основных бинарных типа данных:
- `bytes`: неизменяемая последовательность байтов
- `bytearray`: изменяемая последовательность байтов
- `memoryview`: представление памяти для работы с бинарными данными

## Тип bytes

### Создание bytes
```python
# Пустые байты
bytes1 = bytes()
bytes2 = b''

# Из строки
text = "Hello"
bytes3 = text.encode('utf-8')
bytes4 = b'Hello'

# Из списка чисел
bytes5 = bytes([65, 66, 67])  # b'ABC'

# Из шестнадцатеричной строки
bytes6 = bytes.fromhex('68 65 6c 6c 6f')  # b'hello'
```

### Операции с bytes
```python
# Индексация и срезы
bytes1 = b'Python'
bytes1[0]     # 80 (код символа 'P')
bytes1[1:3]   # b'yt'

# Конкатенация
b'Hello' + b' World'  # b'Hello World'

# Повторение
b'Hi' * 3  # b'HiHiHi'

# Поиск
b'Python'.find(b'th')  # 2

# Преобразование в другие типы
list(b'ABC')   # [65, 66, 67]
```

## Тип bytearray

### Создание bytearray
```python
# Пустой bytearray
barr1 = bytearray()

# Из строки
barr2 = bytearray('Hello', 'utf-8')

# Из списка чисел
barr3 = bytearray([65, 66, 67])

# Из bytes
barr4 = bytearray(b'Hello')
```

### Операции с bytearray
```python
# Изменение элементов
barr = bytearray(b'Python')
barr[0] = 74   # bytearray(b'Jython')

# Методы изменения
barr.append(33)      # Добавление байта
barr.extend(b'ing')  # Добавление последовательности
barr.remove(33)      # Удаление байта
barr.pop()          # Удаление и возврат последнего байта

# Преобразование
bytes(barr)    # Преобразование в bytes
list(barr)     # Преобразование в список
```

## Тип memoryview

### Создание memoryview
```python
# Из bytes
data = b'Python'
view = memoryview(data)

# Из bytearray
barr = bytearray(b'Hello')
view = memoryview(barr)
```

### Операции с memoryview
```python
# Получение элементов
view[0]      # Первый байт
view[1:3]    # Срез

# Преобразование
bytes(view)   # Преобразование в bytes
list(view)    # Преобразование в список

# Изменение через view (только для изменяемых объектов)
barr = bytearray(b'Python')
view = memoryview(barr)
view[0] = 74  # Изменяет barr на bytearray(b'Jython')
```

## Работа с кодировками

```python
# Кодирование строк в байты
text = "Привет"
utf8_bytes = text.encode('utf-8')
cp1251_bytes = text.encode('cp1251')

# Декодирование байтов в строки
utf8_text = utf8_bytes.decode('utf-8')
cp1251_text = cp1251_bytes.decode('cp1251')

# Обработка ошибок кодирования
try:
    text = bytes.decode('invalid')
except UnicodeDecodeError:
    print("Ошибка декодирования")
```

## Работа с файлами в бинарном режиме

```python
# Запись бинарных данных
with open('file.bin', 'wb') as f:
    f.write(b'Binary data')

# Чтение бинарных данных
with open('file.bin', 'rb') as f:
    data = f.read()
```

## Распространенные ошибки и их решения

1. Смешивание строк и байтов:
```python
# Неправильно
b'Hello' + ' World'  # TypeError

# Правильно
b'Hello' + b' World'
# или
'Hello'.encode() + ' World'.encode()
```

2. Неправильная кодировка:
```python
# Безопасное декодирование
try:
    text = bytes.decode('utf-8')
except UnicodeDecodeError:
    text = bytes.decode('utf-8', errors='replace')
```

3. Изменение bytes:
```python
# Неправильно
bytes_data = b'Python'
bytes_data[0] = 74  # TypeError

# Правильно
bytearray_data = bytearray(b'Python')
bytearray_data[0] = 74
```

## Советы по эффективному использованию

1. Используйте bytes для неизменяемых бинарных данных

2. Используйте bytearray когда нужно изменять данные

3. Используйте memoryview для эффективной работы с большими бинарными объектами

4. При работе с текстом всегда указывайте кодировку явно

5. Используйте контекстные менеджеры (with) при работе с бинарными файлами

6. Для больших наборов данных используйте чтение/запись порциями