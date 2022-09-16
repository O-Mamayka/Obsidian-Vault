## [DS.02 Предобработка данных. Тема 4. Поиск дубликатов](https://practicum.yandex.ru/trainer/data-scientist/lesson/d278882a-266f-4f1b-b3d6-a14c4b5df8dd/)

Метод `value_counts()`, который анализирует столбец, выбирает каждое уникальное значение и подсчитывает частоту его встречаемости в списке. Применяют метод к объекту _Series_. Результат его работы – список пар «значение-частота», отсортированные по убыванию. Все дубликаты, которые встречаются чаще других, оказываются в начале списка.
  
```python
models_counts = stock['item'].value_counts()
```

```python
import pandas as pd

stock = pd.read_excel('/datasets/stock.xlsx', sheet_name='storehouse')

xiaomi = stock[stock['item'] == 'Смартфон Xiaomi Redmi 6A 16GB']['count'].sum()

#print(xiaomi)

huawei = stock[stock['item'] == 'Смартфон HUAWEI P30 lite']['count'].sum()

#print(huawei)

stock['item'] = stock['item'].drop_duplicates()

stock = stock.dropna(subset=['item']).reset_index(drop=True)

_#stock.loc[stock['item'] == 'Смартфон Xiaomi Redmi 6A 16GB', 'count'] = xiaomi_

_#stock.loc[stock['item'] == 'Смартфон HUAWEI P30 lite', 'count'] = huawei_

stock.loc[stock['item'].str.contains('Xiaomi'), 'count'] = xiaomi

stock.loc[stock['item'].str.contains('HUAWEI'), 'count'] = huawei

print(stock)
```

```python

import pandas as pd

stock = pd.read_csv('/datasets/stock_upd.csv')

stock['item_lowercase'] = stock['item'].str.lower()

apple = stock.loc[stock['item_lowercase'].str.contains('apple'), 'count'].sum()

samsung = stock.loc[stock['item_lowercase'].str.contains('samsung'), 'count'].sum()

#print(samsung)

stock['item_lowercase'] = stock['item_lowercase'].drop_duplicates()

stock = stock.dropna(subset=['item_lowercase']).reset_index(drop=True)

stock.loc[stock['item_lowercase'].str.contains('apple'), 'count'] = apple

stock.loc[stock['item_lowercase'].str.contains('samsung'), 'count'] = samsung

print(stock)
```

[Более сложные алгоритмы поиска дубликатов в текстах и изображениях](https://habr.com/ru/post/275937/)

