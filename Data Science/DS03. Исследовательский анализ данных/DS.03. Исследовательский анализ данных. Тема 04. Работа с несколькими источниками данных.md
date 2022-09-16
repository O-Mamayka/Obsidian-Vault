# [Тема 04. Работа с несколькими источниками данных](https://practicum.yandex.ru/trainer/data-scientist/lesson/2a45a4fa-877e-49f4-a838-8e90fd2df0b8/)


### Урок 3. Срез по данным из внешнего словаря

```python
our_list = [1, 2, 3]
our_dict = {0: 10, 1: 11, 2: 12}
our_series = pd.Series([10,11,12])

df = pd.DataFrame({
    'a': [2, 3, 10, 11, 12],
    'b': [5, 4, 3, 2, 1],
    'c': ['X', 'Y', 'Y', 'Y', 'Z']
})
print(df.query('a in @our_list')) # строим срез, в котором значения столбца a равны элементам списка our_list

print(df.query('a in @our_dict')) # строим срез, в котором значения столбца a равны ключам словаря

print(df.query('a in @our_series')) # строим срез, в котором значения столбца a равны значениям Series, но не их индексам

print(df.query('a in @our_series.index')) # строим срез, в котором значения столбца a равны индексам Series, т. е. 0, 1 или 2

our_df = pd.DataFrame ({ 'a1': [2, 4, 6], 'b1': [3, 2, 2], 'c1': ['A', 'B', 'C'] }) print(df.query('a in @our_df.index')) # строим срез, в котором значения столбца a равны индексам датафрейма our_df, т. е. 0, 1 или 2

print(df.query('b in @our_df.b1')) # строим срез, в котором значения столбца b равны значениям столбца b1 датафрейма our_df

```


#### [Урок 3. Задача 1](https://practicum.yandex.ru/trainer/data-scientist/lesson/7c8dd1bd-912d-47b2-a35d-3ed0e9b4206f/task/cab5b553-f0a8-481e-af34-446cf7a6a75b/)

**Правило**: исключаются из анализа те объекты, на которых длительность половины или более событий очень мала.
