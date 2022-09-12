# DS.01 Базовый Python. Тема 10. Предобработка данных. Принцип GIGO 

**Самые частые проблемы в данных:**
• некорректное именование столбцов,
• дублирование значений,
• отсутствующие значения.


```python
# вывод информации о таблице
import pandas as pd
df = pd.read_csv('music_log.csv')
df.info()
```

**Типичные проблемы в названии столбцов:**
* Пробелы в названиях. Их легко не заметить и неправильно обратиться к столбцу. Как и в именах переменных, названия столбцов лучше писать без пробелов, в «змеином_регистре».
* Названия должны быть на одном языке. Иначе буквы из разных алфавитов легко спутать.
* Из названия непонятно, что за данные хранятся в столбце.
* Заглавных и строчных букв лучше избегать

**Вывод названий столбцов
```python
print(celestial.columns)
```

**Переименование столбцов
```python
celestial = celestial.rename(columns={'Небесные тела ': 'celestial_bodies', 'MIN': 'min_distance', 'MAX': 'max_distance'})
```

**вывод первых строк таблицы
```python
print(df.head(10))
```

**посчитать количество NaN в каждой колонке:
```python
print(cholera.isna().sum())
```

```python
#В столбце imported_cases заменим все NaN на 0
cholera['imported_cases'] = cholera['imported_cases'].fillna(0)
```

```python
#удаление строк, в которых в столбцах total_cases, deaths или case_fatality_rate встречается NaN
cholera = cholera.dropna(subset=['total_cases', 'deaths', 'case_fatality_rate'])
```

```python
#удаление столбцов, в которых в столбцах total_cases, deaths или case_fatality_rate встречается NaN
cholera = cholera.dropna(subset=['total_cases', 'deaths', 'case_fatality_rate'], axis='columns')
```

```python
#удалит любой столбец с пропуском.
cholera = cholera.dropna(axis='columns')
```


Методы `isna()` и `isnull()` найдут пропуски, а `duplicated()` отыщет дубликаты. Что у них общего: в случае пропуска или дубликата возвращается `True`, иначе — `False`. Количество пропусков или дубликатов можно посчитать. Для этого результаты передают методу `sum()`.


### Тема 10. Урок 5. Лабораторка - Яндекс Музыка: пропущенные значения

```python
import pandas as pd
df = pd.read_csv('music_log_upd_col.csv')

# В столбце track_name заменим все NaN на unknown
df['track_name'] = df['track_name'].fillna('unknown')

# В столбце artist_name заменим все NaN на unknown
df['artist_name'] = df['artist_name'].fillna('unknown')

# удаление строк, в которых в столбце genre_name встречается NaN
df = df.dropna(subset=['genre_name'])

# Получим общую информацию о наборе данных
df.info()
#print()
#посчитать количество NaN в каждой колонке:
#print(df.isna().sum())
```  

### Тема 10\. Урок 6. Обработка дубликатов

Дубликаты могут быть явные и не явные.

`duplicated()`\- по умолчанию он признаёт дубликатами те строки, которые полностью повторяют уже встречавшиеся в датасете. Метод возвращает `Series` со значением `True` для таких строк.

```python
print(df.duplicated())
```

```python
#посчитать строки, результат метода передают функции sum():

import pandas as pd

df = pd.read_csv('music_log_upd_col.csv')

print(df.duplicated().sum())

#Выведем на экран несколько строк с результатами

#результат — датафрейм с дубликатами

duplicated_df = df[df.duplicated()].head()

print(duplicated_df)

#Удаление явных дубликатов

df = df.drop_duplicates()
```

**!!! Когда из них удаляют строки, нарушается порядок индексов?**
индексы в датафрейме устроены не так же, как в списках

```python
df = df.drop_duplicates().reset_index() #- создаст новые инжексы, а старые перенесёт в новую колонку

df = df.drop_duplicates().reset_index(drop=True) #заменит старые индексы
```

```python
#возвращает перечень уникальных значений в столбце:
print(tennis['name'].unique())

#удаление всех строк, где есть хотя бы одно пропущенное значение
df = df.dropna()

#удаление строк с пропусками в столбцах, перечисленных в списке subset
df = df.dropna(subset=['a','b','c'])

#удаление всех столбцов, где есть хотя бы одно пропущенное значение
df = df.dropna(axis='columns')
```

## Поиск неявных дубликатов

```python
#Неявные дубликаты ищут методом unique()
print(tennis['name'].unique()) #

#количество всех уникальных значений в столбце
n = df['column'].nunique()

#написания значений исправляют методом replace()
tennis['name'] = tennis['name'].replace('Roger Federer', 'Роджер Федерер')
```

## Функция замены неправильных значений

```python
def replace_wrong_values(wrong_values, correct_value): # на вход функции подаются список неправильных значений и строка с правильным значением

	for wrong_value in wrong_values: # перебираем неправильные имена
	
	tennis['name'] = tennis['name'].replace(wrong_value, correct_value) # и для каждого неправильного имени вызываем метод replace()
	
	duplicates = ['Roger Fderer', 'Roger Fdrer', 'Roger Federer'] # список неправильных имён
	
	name = 'Роджер Федерер' # правильное имя
	
	replace_wrong_values(duplicates, name) # вызов функции, replace() внутри будет вызван 3 раза
	
	print(tennis) # датафрейм изменился, неявные дубликаты устранены
```

### Тема 10. Урок 7. Лабораторка - Яндекс Музыка: дубликаты

Получить таблицу со всеми дубликатами датафрейма `df` c помощью логической индексации и метода `duplicated()` можно так:
```python
duplicated_df = df[df.duplicated()]
```

```python
import pandas as pd

df = pd.read_csv('music_log_upd_nan.csv')

#df.info()

shape_table = df.shape

#print(shape_table)

print(df.duplicated().sum())

#print(df['name'].unique()) #

df = df.drop_duplicates().reset_index(drop=True)

shape_table_update = df.shape

#print(f'Размер таблицы не изменился, текущий размер: {shape_table}') if shape_table_update == shape_table else print(f'Таблица уменьшилась, текущий размер: {shape_table_update}')

if shape_table_update == shape_table:

	print(f'Размер таблицы не изменился, текущий размер: {shape_table}')

else:

	print(f'Таблица уменьшилась, текущий размер: {shape_table_update}')
```

```python
import pandas as pd

df = pd.read_csv('music_log_upd_nan.csv')

#df.info()

shape_table = df.shape

#print(shape_table)

print(df.duplicated().sum())

#print(df['name'].unique()) #

df = df.drop_duplicates().reset_index(drop=True)

shape_table_update = df.shape

#print(f'Размер таблицы не изменился, текущий размер: {shape_table}') if shape_table_update == shape_table else print(f'Таблица уменьшилась, текущий размер: {shape_table_update}')

if shape_table_update == shape_table:

print(f'Размер таблицы не изменился, текущий размер: {shape_table}')

else:

print(f'Таблица уменьшилась, текущий размер: {shape_table_update}')
duplicated_df = df[df.duplicated()]
```

```python
import pandas as pd

df = pd.read_csv('music_log_upd_nan.csv')

#df.info()

shape_table = df.shape

#print(shape_table)

print(df.duplicated().sum())

#print(df['name'].unique()) #

df = df.drop_duplicates().reset_index(drop=True)

shape_table_update = df.shape

#print(f'Размер таблицы не изменился, текущий размер: {shape_table}') if shape_table_update == shape_table else print(f'Таблица уменьшилась, текущий размер: {shape_table_update}')

if shape_table_update == shape_table:

print(f'Размер таблицы не изменился, текущий размер: {shape_table}')

else:

print(f'Таблица уменьшилась, текущий размер: {shape_table_update}')
```

```python

import pandas as pd
df = pd.read_csv('music_log_upd_nan.csv')

# Неявные дубликаты ищут методом unique()
print(df['genre_name'].unique()) #

# написания значений исправляют методом replace()
df['genre_name'] = df['genre_name'].replace('электроника', 'electronic')

# посмотрим сколько осталось в электроника
genre_final_count = df[df['genre_name'] == 'электроника']['genre_name'].count()
print(genre_final_count)
```  

### Тема 10\. Урок 8 - Лаборатория алгоритма предобработки

```python

#импортируйте библиотеку pandas
import pandas as pd

#считайте csv-файл 'music_log.csv' в переменную df
df = pd.read_csv('music_log.csv')

#переименуйте названия столбцов df
#Переименование столбцов

df = df.rename(columns={' user_id': 'user_id', 'total play': 'total_play', 'Artist': 'artist'})

#объявите список columns_to_replace с названиями столбцов track, artist, genre

columns_to_replace = ['track', 'artist', 'genre']

#заполните отсутствующие значения столбцов из списка columns_to_replace значением 'unknown' в цикле

before_fillna = df.isna().sum()

#print(before_fillna)

for column in columns_to_replace:

df[column] = df[column].fillna('unknown')

after_fillna = df.isna().sum()

#print(after_fillna)

#удалите строки-дубликаты из датафрейма df
df = df.drop_duplicates().reset_index(drop=True)

#выведите на экран первые 20 строчек обновлённого набора данных df
print(df.head(20))
```