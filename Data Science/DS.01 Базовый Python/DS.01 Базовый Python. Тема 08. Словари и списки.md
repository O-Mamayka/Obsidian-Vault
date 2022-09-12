 # [DS.01 Базовый Python. Тема 08. Словари и списки](https://practicum.yandex.ru/learn/data-scientist/courses/f332f1ff-8036-4f31-ad9c-866410873a45/sprints/43469/topics/0ee25cfd-af3f-4ba8-bb9a-fea1f013f7a0/lessons/fa5a7c5b-1155-49bc-bbf3-b8601b229132/)


**Словарь** — структура данных в Python, в которой каждый элемент представляет собой пару из ключа и значения. Ключами могут быть строки ( str ) и числа ( int и float ), а значениями — любые типы данных. Словарь это набор пар «**ключ:значение**»:

ключами могут быть строки (str) и числа (int и float);

значениями — любые типы данных.

**Длина словаря** — число его элементов, то есть пар из ключа и значения.

### Как получить **значение** из словаря

```python
value = dictionary_name['key']  
```

**Безопасный способ****.** Чтобы избежать ошибки, небезопасный способ иногда сочетают с конструкцией try...except:
```python
try:
	value = dictionary_name['key'] # ищем ключ key в словаре_
	print(value) # если ключ найден — выводим значение_
except:
	print('Ключ не найден!') # иначе выводим сообщение_
```

Ещё проще — вызвать метод словаря `get()` и передать ключ в его скобках. Если метод не найдёт ключ в словаре, он вернёт значение по умолчанию, None:

```python
value = dictionary_name.get('key')
value = dictionary_name.get('key', 'Ключ не найден!')  
```

**Добавить:**
```python
dictionary['new_key'] = 'новое значение'  
```

К значениям в списке словаря обращаются по двум «координатам»:

* индексу списка,
* имени ключа.  


## пример списка словарей

movies_table = [ {'movie_name':'Побег из Шоушенка', 'country':'США', 'genre':'драма', 'year':1994, 'duration':142, 'rating':9.111}, {'movie_name':'Крёстный отец', 'country':'США', 'genre':'драма, криминал', 'year':1972, 'duration':175, 'rating':8.730}, {'movie_name':'Тёмный рыцарь', 'country':'США', 'genre':'фантастика, боевик, триллер', 'year':2008, 'duration':152, 'rating':8.499} ]  
  

**Примеры:**
```python
game_scores = {
    'Иванов': [23, 35, 70, 45],
    'Петров': [38, 72, 65, 80],
    'Сидоров': [30, 35, 90, 73],
    'Антонов': [45, 20, 95, 80]
}

# Цикл переберёт пары в словаре —
# в person попадает ключ (строка с фамилией игрока),
# в points — значение (список с набранными очками):
for person, points in game_scores.items(): 
    total_points = sum(points) # функция sum() вернёт сумму элементов списка points
    print(f'{person} - {total_points}') # выводим сумму игрока person

```

```python
movies_table = [
    {'movie_name':'Побег из Шоушенка', 'country':'США', 'genre':'драма', 'year':1994, 'duration':142, 'rating':9.111},
    {'movie_name':'Крёстный отец', 'country':'США', 'genre':'драма, криминал', 'year':1972, 'duration':175, 'rating':8.730},
    {'movie_name':'Тёмный рыцарь', 'country':'США', 'genre':'фантастика, боевик, триллер', 'year':2008, 'duration':152, 'rating':8.499}
]

# теперь мы обращаемся к колонке по имени:
print(movies_table[2]['movie_name'])
```

**DRUMPS**
```python
from json import dumps # подключение dumps() для красивого вывода списка словарей

order = [
    {
        'item': 'Пицца Маргарита',
        'category': 'пицца',
        'quantity': 2,
        'price': 320
    },
    {
        'item': 'Pepsi 1 л',
        'category': 'напитки',
        'quantity': 3,
        'price': 75
    }
]

filtered_order = [] # переменная для хранения результата_

for item in order: # перебираем каждый словарь в списке

if item['category'] == 'пицца': # если категория - пицца..._

        filtered_order.append(item) # ...то добавим в словарь в список filtered_order

print('Результат:')

print(dumps(filtered_order, indent=1, ensure_ascii=False)) # печатаем список с помощью dumps()

```  

![два измерения|640x480](https://pictures.s3.yandex.net/resources/Untitled_-_2020-11-23T145701.973_1606132631.png)
### Задание 2
```python

summ = 0 # переменная для общей суммы заказа

for item in order: # перебираете каждый словарь в списке

    if item['category'] == 'пицца':

        summ = summ + item['quantity'] * item['price'] # считаем сумму

print(summ)
```


## пример списка словарей

```python
movies_table = [ {'movie_name':'Побег из Шоушенка', 'country':'США', 'genre':'драма', 'year':1994, 'duration':142, 'rating':9.111}, {'movie_name':'Крёстный отец', 'country':'США', 'genre':'драма, криминал', 'year':1972, 'duration':175, 'rating':8.730}, {'movie_name':'Тёмный рыцарь', 'country':'США', 'genre':'фантастика, боевик, триллер', 'year':2008, 'duration':152, 'rating':8.499} ]

total_duration = 0 # присваиваем переменной с общей длительностью стартовое значение_ 

for movie in movies_table: # перебираем каждый словарь в списке_ 

	total_duration += movie['duration'] # добавляем к переменной длительность фильма_
print(total_duration)
```

  

**Вывод словаря на экран**

```python
from **json** import dumps # подключение dumps() для красивого вывода словаря_

print(dumps(movies_table, indent=4, ensure_ascii=False))
```

Функцией dumps() управляют два параметра:

**indent**=4 — настроит отступ;
**ensure_ascii**=False — обработает кириллические символы.


Не забудьте [шпаргалку по словарям](https://code.s3.yandex.net/data-analyst/praktikum_data_analysis_takeaways_basicPython_theme8.pdf),


[https://pictures.s3.yandex.net/resources/concept\_karta\_changes_1640089673.png](https://pictures.s3.yandex.net/resources/concept_karta_changes_1640089673.png)

![КатраАнализа|640x480](https://pictures.s3.yandex.net/resources/concept_karta_changes_1640089673.png)
