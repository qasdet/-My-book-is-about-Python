# Строки (str) в Python

## Описание
Строки в Python - это неизменяемые последовательности символов Unicode. Они используются для хранения и обработки текстовых данных.

## Создание строк

```python
# Одинарные или двойные кавычки
s1 = 'Hello'
s2 = "World"

# Многострочные строки
s3 = '''Многострочная
строка'''
s4 = """Другая
многострочная строка"""

# Экранирование символов
s5 = 'Строка с \'кавычками\' внутри'
s6 = "Строка с \"кавычками\" внутри"

# Raw-строки (игнорируют экранирование)
r1 = r'C:\Users\Documents'
```

## Операции со строками

### Конкатенация и повторение
```python
# Сложение строк
'Hello' + ' ' + 'World'  # 'Hello World'

# Повторение строки
'Ha' * 3  # 'HaHaHa'
```

### Индексация и срезы
```python
text = 'Python'

# Индексация (начинается с 0)
text[0]    # 'P'
text[-1]   # 'n' (последний символ)

# Срезы [начало:конец:шаг]
text[1:4]    # 'yth'
text[:3]     # 'Pyt'
text[3:]     # 'hon'
text[::2]    # 'Pto'
text[::-1]   # 'nohtyP' (обратный порядок)
```

## Методы строк

### Поиск и проверка
```python
# Поиск подстроки
'Python'.find('th')      # 2 (индекс первого вхождения)
'Python'.index('th')     # 2 (как find, но вызывает ValueError если не найдено)
'Python'.count('t')      # 1 (количество вхождений)

# Проверка содержимого
'123'.isdigit()         # True
'abc'.isalpha()         # True
'Abc123'.isalnum()      # True
'  '.isspace()          # True
'Title'.istitle()       # True
'UPPER'.isupper()       # True
'lower'.islower()       # True
```

### Преобразование регистра
```python
'python'.upper()        # 'PYTHON'
'PYTHON'.lower()        # 'python'
'python'.capitalize()   # 'Python'
'python'.title()        # 'Python'
'Python'.swapcase()     # 'pYTHON'
```

### Удаление пробельных символов
```python
'  text  '.strip()      # 'text'
'  text  '.lstrip()     # 'text  '
'  text  '.rstrip()     # '  text'
```

### Разделение и объединение
```python
# Разделение строки
'a,b,c'.split(',')      # ['a', 'b', 'c']
'a b c'.split()         # ['a', 'b', 'c']
'a\nb\nc'.splitlines()   # ['a', 'b', 'c']

# Объединение строк
','.join(['a', 'b', 'c'])  # 'a,b,c'
```

### Замена и форматирование
```python
# Замена подстрок
'hello world'.replace('world', 'python')  # 'hello python'

# Форматирование строк
# 1. format()
name = 'Alice'
age = 25
'Name: {}, Age: {}'.format(name, age)
'Name: {n}, Age: {a}'.format(n=name, a=age)

# 2. f-строки (Python 3.6+)
f'Name: {name}, Age: {age}'

# 3. %-форматирование (устаревший способ)
'Name: %s, Age: %d' % (name, age)
```

## Кодировка и декодировка

```python
# Преобразование строки в байты
text = 'Привет'
bytes_data = text.encode('utf-8')

# Преобразование байт обратно в строку
text_again = bytes_data.decode('utf-8')
```

## Распространенные ошибки и их решения

1. Изменение строки (строки неизменяемы):
```python
# Неправильно
text = 'Python'
text[0] = 'p'  # TypeError

# Правильно
text = 'p' + text[1:]  # 'python'
```

2. Конкатенация в цикле:
```python
# Неэффективно
result = ''
for item in items:
    result += str(item)

# Эффективно
result = ''.join(str(item) for item in items)
```

3. Сравнение строк с учетом регистра:
```python
# Учитывает регистр
'Python' == 'python'  # False

# Игнорирует регистр
'Python'.lower() == 'python'.lower()  # True
```

## Советы по эффективному использованию

1. Используйте f-строки для форматирования (Python 3.6+)
2. Применяйте методы строк вместо ручной обработки
3. Используйте ''.join() вместо += для конкатенации множества строк
4. При работе с большими текстами используйте построчную обработку
5. Для сложных шаблонов используйте модуль re (регулярные выражения)