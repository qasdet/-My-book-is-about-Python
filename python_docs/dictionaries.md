# Словари (dict) в Python

## Описание
Словари - это изменяемые коллекции, хранящие пары ключ-значение. Ключи должны быть неизменяемыми и уникальными.

## Создание словарей

```python
# Пустой словарь
dict1 = {}
dict2 = dict()

# Словарь с элементами
user = {
    'name': 'Alice',
    'age': 25,
    'email': 'alice@example.com'
}

# Создание с помощью dict()
person = dict(name='Bob', age=30)

# Создание из последовательности пар
items = dict([('a', 1), ('b', 2)])

# Создание с помощью генератора словаря
squares = {x: x**2 for x in range(5)}
```

## Доступ к элементам

```python
# Получение значений
name = user['name']      # Может вызвать KeyError
age = user.get('age')    # Возвращает None если ключ не найден
email = user.get('phone', 'не указан')  # Значение по умолчанию

# Проверка наличия ключа
'name' in user           # True
'phone' not in user      # True

# Получение всех ключей и значений
keys = user.keys()       # dict_keys(['name', 'age', 'email'])
values = user.values()   # dict_values(['Alice', 25, 'alice@example.com'])
items = user.items()     # dict_items([('name', 'Alice'), ('age', 25), ...])
```

## Изменение словарей

```python
# Добавление или изменение элементов
user['phone'] = '123-456'
user.update({'city': 'New York', 'age': 26})

# Удаление элементов
del user['phone']        # Удаление по ключу
phone = user.pop('phone', None)  # Удаление с возвратом значения
last = user.popitem()    # Удаление и возврат последней пары
user.clear()            # Очистка словаря
```

## Методы словарей

```python
# Копирование
shallow_copy = user.copy()      # Поверхностная копия
deep_copy = copy.deepcopy(user) # Глубокая копия (import copy)

# Объединение словарей
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
merged = {**dict1, **dict2}     # {'a': 1, 'b': 3, 'c': 4}

# Получение значения с автоматическим созданием
counts = {}.setdefault('key', 0)

# Словарь с значением по умолчанию
from collections import defaultdict
counts = defaultdict(int)  # Значение по умолчанию 0
```

## Вложенные словари

```python
# Создание вложенного словаря
users = {
    'alice': {
        'name': 'Alice',
        'age': 25,
        'contacts': {
            'email': 'alice@example.com',
            'phone': '123-456'
        }
    },
    'bob': {
        'name': 'Bob',
        'age': 30,
        'contacts': {
            'email': 'bob@example.com'
        }
    }
}

# Доступ к вложенным данным
alice_email = users['alice']['contacts']['email']

# Безопасный доступ к вложенным данным
bob_phone = users.get('bob', {}).get('contacts', {}).get('phone', 'не указан')
```

## Сортировка словарей

```python
# Сортировка по ключам
sorted_keys = sorted(user.keys())

# Сортировка по значениям
sorted_values = sorted(user.items(), key=lambda x: x[1])

# Создание упорядоченного словаря
from collections import OrderedDict
ordered = OrderedDict(sorted(user.items()))
```

## Распространенные ошибки и их решения

1. Ошибка KeyError:
```python
# Неправильно
value = dict1['несуществующий_ключ']  # KeyError

# Правильно
value = dict1.get('несуществующий_ключ')  # None
value = dict1.get('несуществующий_ключ', 'значение по умолчанию')
```

2. Изменение словаря при итерации:
```python
# Неправильно
for key in dict1:
    if condition:
        del dict1[key]  # RuntimeError

# Правильно
keys_to_delete = [k for k in dict1 if condition]
for key in keys_to_delete:
    del dict1[key]
```

3. Копирование вложенных словарей:
```python
# Неправильно (shallow copy)
dict2 = dict1.copy()

# Правильно (deep copy)
import copy
dict2 = copy.deepcopy(dict1)
```

## Советы по эффективному использованию

1. Используйте dict.get() для безопасного доступа к значениям
2. Применяйте dict comprehension вместо циклов for
3. Используйте collections.defaultdict для автоматического создания значений
4. При частом доступе к вложенным данным создавайте промежуточные переменные
5. Для сохранения порядка элементов используйте OrderedDict
6. При работе с большими наборами данных используйте generator expressions
7. Используйте update() для обновления нескольких значений одновременно