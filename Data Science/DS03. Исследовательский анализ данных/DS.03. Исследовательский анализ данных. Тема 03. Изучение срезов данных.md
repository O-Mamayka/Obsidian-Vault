[**Тема 03. Изучение срезов данных](https://practicum.yandex.ru/trainer/data-scientist/lesson/63c9f85c-0953-4338-a864-b1249e65bed3/)

В условиях допустимы арифметические операции. Найдём билеты, у которых дорога обратно `Travel_time_to` более чем в 1.5 раза быстрее, чем дорога туда `Travel_time_from`.

```python
df[1.5 * df['Travel_time_to'] < df['Travel_time_from']]
```

Чтобы проверить наличие конкретных значений в столбце, вызовем метод `isin()`. Посмотрим, какие рейсы вылетают после 3 июля 2019:
```python

`df[df['Date_From'].isin(['04.07.2019', '05.07.2019'])] # находим элементы столбца Date_From, равные 4 или 5 июля`
```
Name|Описание|Синтаксис|Оператор 
   ---|---|---|---
**И**|Результат выполнения логической операции True, только если оба условия — True|(df['Is_Direct']) & (df['Price'] < 21000)|`&`
**ИЛИ**|Результат выполнения — True, если хотя бы одно из условий — True|(df['Has_luggage']) \| (df['Price'] < 20000)|\|
**НЕ**|Результат выполнения — True, если условие — False|~((df['Is_Direct']) \| (df['Has_luggage']))|`~`
Оператор `~` можно использовать и для проверки одного условия, например, чтобы отобрать билеты без багажа: `~(df['Has_luggage'])`. Обратите внимание, что здесь условия указывают в скобках — в отличие от синтаксиса логических операций Python с `or`, `and` или `not`.

```python
import pandas as pd

df = pd.DataFrame(
    {
        'From': [
            'Moscow',
            'Moscow',
            'St. Petersburg',
            'St. Petersburg',
            'St. Petersburg',
        ],
        'To': ['Rome', 'Rome', 'Rome', 'Barcelona', 'Barcelona'],
        'Is_Direct': [False, True, False, False, True],
        'Has_luggage': [True, False, False, True, False],
        'Price': [21032, 19250, 19301, 20168, 31425],
        'Date_From': [
            '01.07.19',
            '01.07.19',
            '04.07.2019',
            '03.07.2019',
            '05.07.2019',
        ],
        'Date_To': [
            '07.07.19',
            '07.07.19',
            '10.07.2019',
            '09.07.2019',
            '11.07.2019',
        ],
        'Airline': ['Belavia', 'S7', 'Finnair', 'Swiss', 'Rossiya'],
        'Travel_time_from': [995, 230, 605, 365, 255],
        'Travel_time_to': [350, 225, 720, 355, 250],
    }
)

print(df[df['Price'] < df['Price'].max() / 1.5]) # впишите нужное условие

print(df[(df['Travel_time_from'] >= 365) | (df['Travel_time_to'] < 250)]) 

rows = (df['Is_Direct'] != True) & (df['Date_To'] < '08.07.2019')

#print(rows)
print(df[rows]) # впишите нужное условие
```


### Урок 3. Срезы данных методом query()


