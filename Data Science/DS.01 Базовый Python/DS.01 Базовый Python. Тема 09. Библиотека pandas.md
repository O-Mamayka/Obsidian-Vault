 # [DS.01 Базовый Python. Тема 09. Библиотека pandas](https://practicum.yandex.ru/trainer/data-scientist/lesson/bb6f02a1-ef4c-4601-8b58-5cc851bbc52b/)

**Библиотека** — набор готовых методов для решения распространённых задач.

.**csv** — формат файла (от англ. Comma-Separated Values, «значения, разделённые запятой»). **Датафрейм** — двумерная структура данных pandas, где у каждого элемента есть два индекса: по строке и по столбцу. Каждая строка — это одно наблюдение, запись об объекте исследования. А столбцы — признаки объекта.

Объект **Series** — одномерная структура данных pandas, её элементы можно получить по индексу.

**Конструктор** — это метод, который создаёт новые объекты. Например, конструктор DataFrame() в pandas создаёт датафреймы.

## Данные исследуют в четыре шага:

* **Получение данных и ознакомление.**
* **Предподготовка.**
* **Анализ.**
* **Оформление результатов исследования.**

```python
import pandas as pd
music = [
['Bob Dylan', 'Like A Rolling Stone'],
['John Lennon', 'Imagine'],
['The Beatles', 'Hey Jude'],
['Nirvana', 'Smells Like Teen Spirit'],
]
entries = ['artist', 'track']
```

### Конструктор DataFrame() для создания таблицы
Конструктор — это метод, который создаёт новые объекты. Например, конструктор DataFrame

```python
pd.DataFrame(data=data, columns=columns) 
# аргумент data — список с данными, 
# аргумент columns — список с названиями столбцов
```

### создаём таблицу и сохраняем её в переменную playlist
```python
playlist = pd.DataFrame(data=music, columns=entries)
```

## Атрибуты датафрейма

Датафрейм хранит не только сами данные, но и общую информацию об этих данных. Примеры таких атрибутов:
-   `dtypes` — тип значений в колонках;
-   `columns` — названия колонок;
-   `shape` — размер таблицы.
Обращаясь к атрибутам, можно составить представление обо всей таблице. В следующих темах вы увидите, как атрибуты помогают быстро найти и восполнить недостатки в датафрейме.
Синтаксис атрибутов напоминает методы датафрейма: после названия переменной ставится точка, за ней — имя атрибута. Но есть и отличие: после имени метода всегда ставят скобки, а при вызове атрибута — нет.  
  
```python
import pandas as pd
df = pd.read_csv('/datasets/music.csv') 
# аргумент — путь к файлу
```

datasets/music.csv - относительный путь
/datasets/music.csv - абсолютрый путь в linux  
c:\\datasets\\music.csv - абсолютрый путь в windows  


```python
print(data_df.head()) # - Чтение заголовка
print(data_df.head(10) # - Чтение первых десяти
print(data_df.tail(10) # - Чтение последних десяти
```
  
```
print(df.dtypes) # выводит информацию о типах данных в таблице
print(df.columns) # выводит названия столбцов
print(df.shape) # выводит размер таблицы
df.info() # метод выводит сводную информацию о таблице
```

![df.info|640x480](https://pictures.s3.yandex.net/resources/5_5_20_1614744901.jpg)
### Запрос размера таблицы
```python
import pandas as pd
df = pd.read_csv('music_log.csv') # аргумент — путь к файлу
shape_table = df.shape
print(f'Размер таблицы: {shape_table}')
```
**Размер таблицы.** О размерах таблицы с данными сообщает атрибут `shape`. В нём содержится кортеж, особый тип списков. Первое значение в кортеже — это количество строк, второе — столбцов: `print(df.shape)`
Кортежи похожи на списки, но
-   списки пишут в квадратных скобках, а кортежи — в круглых;
-   элементы списка можно менять, добавлять новые или удалять. Кортеж — неизменяемая структура.
Получить отдельное значение из кортежа так же просто, как и из списка:
```python
# получаем количество столбцов из кортежа 
columns_number = df.shape[1]` 
```


### Подсчёт методами pandas 
```python

import pandas
realty_df = pandas.read_csv('/datasets/yandex_realty_data.csv')
print(realty_df[realty_df['price'] <= 190000]['price'].count())
```

### Фильтр методами pandas
```python
import pandas as pd
df = pd.read_csv('music_log.csv')
result = df.loc[4, 'genre']
print(result)
```


### Срез по индексам методами pandas
```python

import pandas as pd
df = pd.read_csv('music_log.csv')
result = df.loc[2:4]
print(result)
```


### Другие способы индексации

| **Данные** | **Индексация** |
| --- | --- |
| Одна ячейка | .loc[7, 'genre'] |
| Один столбец | .loc[:, 'genre'] |
| Несколько столбцов | .loc[:, ['genre', 'Artist']] |
| Несколько столбцов подряд (срез) | .loc[:, 'total play': 'genre'] |
| Одна строка | .loc[1] |
| Все строки, начиная с заданной | .loc[1:] |
| Все строки до заданной | .loc[:3] |
| Несколько строк подряд (срез) | .loc[2:5] |

### Срезы по номерам строк и списки колонок можно сочетать:
| Данные | Индексация |
| --- | --- |
| Срез строк в заданном диапазоне и выбор определённого столбца | .loc[2:10, 'genre'] |
| Срез нескольких столбцов подряд и выбор определённой строки | .loc[5, 'total play': 'genre'] |
| Выбор заданных столбцов и определённой строки | .loc[10, ['total play', 'Artist']] |
| Выбор заданных столбцов и срез нескольких строк подряд | .loc[7:10, ['total play', 'genre']] |

### Сокращённая запись при индексации

| **-** | **Полная запись** | **Сокращённая запись** |
| --- | --- | --- |
| Один столбец | .loc[:, 'genre'] | df['genre'] |
| Несколько столбцов | .loc[:, ['genre', 'Artist']] | df[['genre', 'Artist']] |
| Все строки, начиная с заданной | .loc[1:] | df[1:] |
| Все строки до заданной | .loc[:3] (включая 3) | df[:3] (не включая 3) |
| Несколько строк подряд (срез) | .loc[2:5] (включая 5 | df[2:5] (не включая 5) |
| Одна ячейка | .loc[7, 'genre'] | -   |
| Одна строка | .loc[1] | -   |
| Несколько столбцов подряд (срез) | .loc[:, 'total_play': 'genre'] | -   |


**Индексация объектов в Series (Объект строка)**

|    -   | **Полная запись** | **Сокращённая запись** |
| --- | --- | --- | --- | --- |
| Один элемент | total_play.loc[7] | total_play[7]
| Несколько элементов | total_play.loc[[5, 7, 10]] | total_play[[5, 7, 10]]
| Несколько элементов подряд (срез) | total_play.loc[5:10] (включая 10) | total_play[5:10] (не включая 10)
| Все элементы, начиная с заданного | total_play.loc[1:] | total_play[1:]
| Все элементы до заданного | total_play.loc[:3] (включая 3) | total_play[:3] (не включая 3)

```python

import pandas as pd

df = pd.read_csv('music_log.csv')
# получение одной ячейки
index_res = df.loc[7, 'genre']
# срез столбца
index_res = df.loc[:, 'genre']
# срез нескольких столбцов по их названиям
index_res = df.loc[: , ['genre', 'Artist']]
# срез нескольких столбцов от одного до другого
index_res = df.loc[:, 'total play': 'genre']
# одна строка
index_res = df.loc[1]
# срез всех строк, начиная с заданной
index_res = df.loc[1:]
# срез всех строк до заданной
index_res = df.loc[:3]
# срез нескольких строк подряд
index_res = df.loc[2:5]
print(index_res)
```

```python

import pandas as pd
df = pd.read_csv('music_log.csv')
# срез строк в заданном диапазоне и выбор определённого столбца
index_res = df.loc[2:10, 'genre']
# срез нескольких столбцов подряд и выбор определённой строки
index_res = df.loc[5, 'total play': 'genre']
# выбор заданных столбцов и определённой строки
index_res = df.loc[10, ['total play', 'Artist']]
# выбор заданных столбцов и срез нескольких строк подряд 
index_res = df.loc[7:10, ['total play', 'genre']]
print(index_res)
```


### Сокращённая запись
```python

import pandas as pd

df = pd.read_csv('music_log.csv')
# срез столбца
index_res = df['genre']
# срез нескольких столбцов по их названиям
index_res = df[['genre', 'Artist']]
# срез всех строк, начиная с заданной
index_res = df[1:]
# срез всех строк до заданной
index_res = df[:3]
# срез нескольких строк подряд
index_res = df[2:5]
print(index_res)
```

### Логическая индексация
```python

battle.loc[battle.loc[:,'В'] == 'X']   
print(battle.loc[battle.loc[:,'В'] == 'X']['В'].count())  
print(battle[battle['В'] == 'X']['В'].count())
```
  

```python

total_play.loc[total_play<10]  #??????

```

## Боевая подготовка
```python
import pandas as pd  
data = [[0,0,0,0,0,0,0,0,0,0],       
...
[0,0,0,0,0,0,0,0,0,0]]  
columns = ['А','Б','В','Г','Д','Е','Ж','З','И','К']  
battle = pd.DataFrame(data = data, columns = columns)  
print(battle)
```

```python

print(battle.loc[:,'В']) 
print(battle.loc[6]) 
print(battle.loc[5:7])
```
  
```python

# срез столбца
index_res = df['genre']
# срез нескольких столбцов по их названиям
index_res = df[['genre', 'Artist']]
# срез нескольких строк подряд
index_res = df[2:5]
```

```python
import pandas as pd
df = pd.read_csv('music_log.csv')
# строки датафрейма, в которых жанр — джаз (jazz)
jazz_df = df[df['genre'] == 'jazz']
print(jazz_df)
```
  
```python
# строки датафрейма, в которых время прослушивания total_play больше 90
high_total_play_df = df[df['total play'] > 90]]
#print(high_total_play_df)
```
  

```python
# строки датафрейма, в которых время прослушивания total_play меньше или равно 10
low_total_play_df = df[df['total play'] <= 10]
#print(low_total_play_df)
```
  

```python
import pandas as pd
df = pd.read_csv('music_log.csv')
# выбираем строки, в которых жанр — джаз и время воспроизведения находится в диапазоне от 80 до 130
df = df[df['total play'] >= 80]
df = df[df['total play'] <= 130]
df = df[df['genre'] == 'jazz']
print(df)
```

```python

import pandas as pd
df = pd.read_csv('music_log.csv')
gf= df[['genre', 'Artist']]
genre_pop = gf[gf['genre'] == 'pop']['genre'].count()
```  

Каждая колонка таблицы — отдельный объект типа Series. Из таблицы можно извлечь отдельные Series, а из Series — собрать новую таблицу.  
  

**Индексация в Series**  
```python

import pandas as pd
df = pd.read_csv('music_log.csv')
# Получаем Series из датафрейма
artist = df['Artist']
# Получаем ячейку из Series по единственной координате
print(artist[0])
```  


## Laboratory. Series

```python
import pandas as pd 
df = pd.read_csv('music_log.csv')  

# сохраняем Series в отдельную переменную 
total_play = df['total play']  
# через логическую индексацию получаем недослушанные треки, 
# и считаем их методом count() 
print(total_play[total_play <= 10].count())
```

```python

import pandas as pd
df = pd.read_csv('music_log.csv')
rock = df[df['genre'] == 'rock']
rock_time = rock['total play']
rock_haters = rock_time.loc[rock_time <=5].count()
print(f'Количество пропущенных треков жанра рок равно {rock_haters}')
```

```python

import pandas as pd
df = pd.read_csv('music_log.csv')

rock = df[df['genre'] == 'rock']
rock_time = rock['total play']
rock_haters = rock_time[rock_time <= 5].count()
print("Количество пропущенных треков жанра рок равно", rock_haters)

pop = df[df['genre'] == 'pop']
pop_time = pop['total play']
pop_haters = pop_time[pop_time <= 5].count()
print("Количество пропущенных треков жанра поп равно", pop_haters)

rock_skip = rock_haters / rock.shape[0]
pop_skip = pop_haters / pop.shape[0]

print(f'Доля пропущенных композиций жанра рок равна: {rock_skip}')
print(f'Доля пропущенных композиций жанра поп равна: {pop_skip}')
```  

### Вывод нескольких ячеек методами полной индексации:
```python

import pandas as pd
board_df = pd.read_csv('game_board.csv')
print(board_df.loc[5:6, ['C','D','E','F']])
```  

### Вывод нескольких ячеек методами сокращенной индексации с логической индексацией:
```python

import pandas as pd
board_df = pd.read_csv('game_board.csv')
print(board_df[board_df['H'] == 1]['H'])
```  

Чтобы ничего не забыть, [скачайте шпаргалку](https://code.s3.yandex.net/data-analyst/praktikum_data_analysis_takeaways_basicPython_theme9.pdf).