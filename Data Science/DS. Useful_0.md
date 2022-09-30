## DS. Useful 

```python
lucky_number = random.randint(10, 100)
```

### Строки

```python
introduction = 'Hello, {0}, {1}'.format(name, age)

print('Конверсия рассылок: {:.0%}'.format(conversion))
print(f'Доля {russian_web_part:.2f}')

```

`replace()` — заменит часть строки;

`find()` — ищет подстроку в строке;

`upper()` — заменяет все буквы в строке на прописные;

`lower()` — заменяет все буквы на строчные.

`replace`(ЧТО, НаЧто)

`find()`

```python
print(f'Доля русского языка в интернете составляет {russian_web_part:.1%}')

print(f'Доля русского языка в интернете составляет {russian_web_part:.2%}')

print(f'Доля русского языка в интернете составляет {russian_web_part:.2f}')

introduction = 'Hello, this is {0}, he is {1}, his height is {2}'.format(name, age, height)
```

### Списки

`append()` - дабавить один в конец, first_row.append('Фрэнк')

`extend()` - добавить несколько в конец, second_row.extend(['Фрэнсис', 'Нино'])

`insert()` - дабавить один куда надо, first_row.insert(КУДА, 'Чего')

`pop()` - удаляет в конце, row.pop()

`sort()` - сортирует в существующем списке, years.sort(reverse=True)

`sorted()` - сортирует в новый список, years = sorted(years, reverse=True)

`index()` - даёт индекс по имени, ind = beatles.index('Пол Маккартни')

`split()` - разбивает строку на список, res = phrase.split('-')

`join()` - объединяет список в строку, info = '>'.join(stations)


**Обработка ошибок**

```python
try:
	print(777 / 0)

except:
	print('Нельзя делить на ноль!')
```

**!!!** rule - 'Строки в Python помещают в одинарные кавычки, вот так: 'текст''

`len(x)` - Длинна строки или списка


```python
for i in range(1, number):
	fact *= i

print(math.factorial(8)) - факториал
```

### Вложенные списки

```python
print(movies_table[9][1])

for row in movies_table: # перебирается каждый внутренний список

r = row # строка - список! row[0] ячейка

for elem in row: #  в очередном внутреннем списке перебирается каждый элемент_

	print(elem, end='   ') # печатается очередной элемент, в конец добавляются три пробела, без перевода на новую строку
```

```python
    for elem in movie: # перебираем элементы очередного списка
		print(f'{elem:<45}', end='') # выравнивание каждого элемента по левому краю с фиксированной шириной строки 45
```



movies_table_sorted = sorted(movies_table, key=**lambda** row: row[5], reverse=True)

* `islower()` — возвращает `True`, если в строке нет прописных букв;
* `isdigit()` — возвращает `True`, если строка состоит только из числовых знаков;
* `ilpha()` — возвращает `True`, если в строке только буквы, без пробелов и знаков препинания.

```python
if Условие 1:

	elif Условие 2:
		print()
	
	else:
		print()
```


**Можно так: print(1) if Условие else print(2)

`%` - остаток от деления

`//` - целочисленное деление

`while` Условие:

### Создание функции

```python
def f(x, y=2, z=5):
	result = x * x
	return result

f(random.randint(10, 10)) ИЛИ f(z=1, y=2, x=3):
```

```Python
def find_square_and_perim(side1, side2):
    square = side1 * side2
    perimeter = 2 * (side1 + side2)
    return square, perimeter
square, perimeter = find_square_and_perim(7, 3)
```
  

**Словарь** — структура данных в Python, в которой каждый элемент представляет собой пару из ключа и значения.

```python
value = dictionary_name.get('key')
value = dictionary_name.get('key', 'Ключ не найден!')

dictionary['new_key'] = 'новое значение'
```

**!!!!!**
print(dumps(filtered_order, indent=1, ensure_ascii=False)) # печатаем список с помощью_ dumps(), **indent**=4 — настроит отступ; **ensure_ascii**=False — обработает кириллические символы.

## PANDAS

```python
import pandas as pd

pd.DataFrame(data=data, columns=columns)
```

аргумент **data** — список с данными, аргумент **columns** — список с названиями столбцов

```python
print(df.dtypes) # выводит информацию о типах данных в таблице

print(df.columns) # выводит названия столбцов

print(df.shape) # выводит размер таблицы

df.info() # метод выводит сводную информацию о таблице

print(realty_df[realty_df['price'] <= 190000]['price'].count())
```

### Фильтры:

```python
result = df.loc[4, 'genre']

result = df.loc[2:4]

df.loc[:, ['genre', 'Artist']]

df.loc[5, 'total play': 'genre']

df.loc[:, 'total_play': 'genre']

df[['genre', 'Artist']]

df[2:5]

print(board_df.loc[5:6, ['C','D','E','F']])

df[~df['number'].isin([4,5])] # фильтр выберет строки КРОМЕ 4,5

df.query('a in @our_series') # Срез по данным из внешнего словаря

```

### Логическая индексация

```python
df.loc[df.loc[:,'В'] == 'X']

print(df.loc[df.loc[:,'В'] == 'X']['В'].count())

**data.loc[data['Эксперимент'] == '+', 'Роль'] = 'экспериментатор'
```

--------------------------------------------------------------------------------

```python
print(df[df['В'] == 'X']['В'].count())

print(df[df['H'] == 1]['H'])

df[df['genre'] == 'jazz']

df[df['genre'] == 'pop']['genre'].count()
```

### Обработка данных

`NaN` замещает отсутствующее в ячейке число и принадлежит к типу `float`, с ним можно проводить математические операции. 

`None` относят к нечисловому типу `NoneType`, и математические операции с ним неосуществимы.

`isna()` посчитает количество NaN и None в каждой колонке:

```python
print(df.isna().sum())
```

`fillna()` В столбце imported_cases заменим все NaN и None на 0

```python
df['imported_cases'] = df['imported_cases'].fillna('unknown')
```

`dropna()` - удалит строки, в столбцах total_cases, deaths где встречается NaN и None

df = df.dropna(subset=['total_cases', 'deaths'])

`dropna() + axis` - удалит столбцы из списка если встречается NaN и None

```python
df = df.dropna(subset=['total_cases', 'deaths', 'case_fatality_rate'], axis='columns')
```

**удалит любой столбец с пропуском.

```python
df = df.dropna(axis='columns')
```


**посчитать строки, результат метода передают функции sum():

```python
print(df.duplicated().sum())
```

**результат — датафрейм с дубликатами

```python
df = df[df.duplicated()].head() # первые n строк
df = df[df.duplicated()].tail() # последние n строк
df = df[df.duplicated()].sample() # случайные n строк
```

**Удаление явных дубликатов**

```python
df = df.drop_duplicates()

df = df.drop_duplicates().reset_index() # создаст новые инжексы, а старые перенесёт в новую колонку

df = df.drop_duplicates().reset_index(drop=True) #заменит старые индексы
```


**возвращает перечень уникальных значений в столбце:**

```python
print(tennis['name'].unique())
```


**Неявные дубликаты ищут методом `unique()`**
```
print(tennis['name'].unique()) #
```

**количество всех уникальных значений в столбце**
```
n = df['column'].nunique()
```

**написания значений исправляют методом `replace()`**

```python
df['name'] = df['name'].replace('Roger Federer', 'Роджер Федерер')
```

```python
ong_valueduplicateslues: # перебираем неправильные имена
        tennis['name'] = tennis['name'].replong_value, correct_value) # и для каждого неправильного имени вызываем метод replace()
duplicates = ['Roger Fderer', 'Roger Fdrer', 'Roger Federer'] # список неправильных имён
name = 'Роджер Федерер' # правильное имя
```
  
### Переименование столбцов

```python
df = df.rename(columns={' user_id': 'user_id', 'total play': 'total_play', 'Artist': 'artist'})
```

### Группировка данных

```python
ndf= df.groupby('discovered')['radius'].count()
```

### Сортировка данных pandas

```python
print(exoplanet.sort_values(by='radius', ascending=False).head(30)) # отсортируем по радиусу
```

### Описательная статистика

**показать максимальное значение:

```python
print(df['total_play_seconds'].max())
```

**вывести строку с максимальным значением:

```python
print(df[df['total_play_seconds'] == df['total_play_seconds'].max()])
```

**отфильтровать нулевые значения и вывести минимум из ненулевых:**

```python
df_drop_null = df[df['total_play_seconds'] != 0]

print(df_drop_null['total_play_seconds'].min())
```

**получим медиану**

```python
print(df_stat['total_play_seconds'].median())

df_drop_null = df[df['total_play_seconds'] != 0]

print(df_drop_null['total_play_seconds'].median())
```

**средняя**

```python
print(df_drop_null['total_play_seconds'].mean())
```

**вовлеченность**

```python
current_engagement = df.groupby('user_id').sum().median()
```

В тетрадке Jupyter по-разному выводите на экран разные типы данных:

* датафреймы и `Series` — функцией `display()`;
* любые другие данные — функцией `print()`.

`idxmax()`, чтобы получить индекс элемента — с наибольшим численным значением.

```python
m = df.groupby('column1')['column2'].sum().idxmax()

ss= df.groupby('column1')['column2'].sum().sum()
```
  
```python
rows = [False, True, False, False, False, False, False, False] # ИЛИ

rows = data['Статья'] == '+'

print(data.loc[rows])

print(data.loc[(data['Новая функция'] == '+') & (data['Роль'] == 'разработчик')])
```

```python
df['family'] = df['family'].fillna(value='') # пустая строка
```

**метод `agg()`**, указывающий, какие именно функции применить к столбцу _'purchase'._

```python
logs_grouped = logs.groupby('source').agg({'purchase': ['count', 'sum']})
```
Применение нескольких операций к столбцу при группировке
```python
data.groupby('column1').agg({'column2': ['count', 'sum'], 'column3': ['min', 'max']})
```

**!!!!!!!!!!**

```python
df = pd.read_excel( '/datasets/file.xlsx', sheet_name='sheet' )
```

# https://code.s3.yandex.net/data-analyst/praktikum_data_analysis_abstract_course2_theme1.pdf

## Перевод строковых значений в числа (float)
```python
transactions['amount'] = pd.to_numeric(transactions['amount'], errors='coerce')

pd.to_numeric(data['column']) # первый аргумент - колонка из датафрейма # второй аргумент (errors) - метод обработки ошибок

pd.to_numeric(data['column'], errors='raise' ) # если errors='raise' (значение по умолчанию), то при встрече с некорректным # значением выдается ошибка, операция перевода в числа прерывается;

pd.to_numeric(data['column'], errors='coerce') # если errors='coerce', то некорректные значения принудительно заменяются на NaN;

pd.to_numeric(data['column'], errors='ignore') # если errors='ignore', то некорректные значения игнорируются, но остаются.
```

**Перевезти в INT можно командой `astype()`
```
df['column'] = df['column'].astype('int')
```

## Получение из столбца с датой и временем...
```python
pd.DatetimeIndex(data['time']).year # года

pd.DatetimeIndex(data['time']).month # месяца

pd.DatetimeIndex(data['time']).day # дня

pd.DatetimeIndex(data['time']).hour # часа

pd.DatetimeIndex(data['time']).minute # минуты

pd.DatetimeIndex(data['time']).second # секунды
```

**Объединим несколько таблиц в одну методом
```
data.merge(data2, on='merge_column', how='left')
```


```python
data_pivot = data.pivot_table(index = ['column1', 'column2'], columns = 'source', values = 'column_pivot', aggfunc = ['count', 'first', 'last', 'max', 'mean', 'median', 'min', 'sum'])
```

```
df = df.drop_duplicates().reset_index(drop=True) # удалить дубликаты с обновлением индексов
```

Чтобы ничего не забыть, скачайте [шпаргалку](https://code.s3.yandex.net/data-analyst/praktikum_data_analysis_takeaways_course2_theme3.pdf) и [конспект](https://code.s3.yandex.net/data-analyst/praktikum_data_analysis_abstract_course2_theme3.pdf) темы.

**Метод анализирует столбец, выбирает каждое уникальное значение и подсчитывает частоту его встречаемости в списке. Выводит список пар отсортированные по убыванию.
```python
models_counts = stock['item'].value_counts()
```

# Чтобы ничего не забыть, скачайте [шпаргалку](https://code.s3.yandex.net/data-analyst/praktikum_data_analysis_takeaways_course2_theme4.pdf) и [конспект](https://code.s3.yandex.net/data-analyst/praktikum_data_analysis_abstract_course2_theme4.pdf) темы.

### Функции
```Python

def name(var):
 comand
 return var2
```

```Python
# применение функции age_group ко всему столбцу 'age'
clients['age_group'] = clients['age'].apply(age_group, axis=1) # 0 - столбцыб; 1 - строки
```

### DS.03. Исследовательский анализ данных

Гистограмма — это график, который показывает, как часто данные встречается в наборе 
```Python
# отображение гистограммы с числом корзин n_bins и диапазоном
data.hist('time_spent', bins=100, range=(0, 1500))
````
**Диаграмма размаха
```python
plt.ylim(0, 100)
data.boxplot(column='column')
plt.show()
```

**входим в числовое описание данных
```python
print(data.describe())
```

Query - это гибкий инструмент получения срезов
```python
print(df.query('To == "Barcelona"'))
print(df.query('From == "Moscow" and (Is_Direct == True or Has_luggage == True)'))
print(df.query('Has_luggage == False and Airline not in ["S7", "Rossiya"]'))
max_time = 300
print(df.query('Travel_time_from < @max_time and Airline in ["Belavia", "S7", "Rossiya"]'))
# Поддерживают разные операции: `!=`, `>`, `>=`, `<`, `<=`, in, not in, `or`, `and`, `not`. 
```

**Работа с датой и временем

```python
df['time'] = pd.to_datetime(df['time'], format='%Y-%m-%d %H:%M')
df['time_rounded'] = df['time'].dt.round('1H') # округляем до ближайшего значения с шагом в один (1y, 1m, 1d, 1H, 1T, 1S)
df['ceil'] = df['time'].dt.ceil('1H') # округляем к потолку
df['floor'] = df['time'].dt.floor('1H') # округляем к полу
df['ny'] = df['msk'] + pd.Timedelta(hours=-7)
```

**Графики
```python
df.plot(x='b', y='a', style='o-', xlim=(0, 30), grid=True, figsize=(10, 3))
```



Срезы с query
print(len(data.query('time_spent < 60')) / len(data))

**Объединение данных
data1.merge(data2, on='author', how='left') # название столбца, по которому объединять, передают в параметре `on`

first_pupil_df.merge(second_pupil_df, on='author', how='left')

station_stat_full = id_name.join(good_stations_stat, on='id')

**Диаграмма рассеяния

data.plot(x='count', y='time_spent', kind='scatter', grid=True)

**Корреляция

hw.plot(x='height', y='weight', kind='scatter', alpha=0.015)
hw.plot(x='height', y='weight', kind='hexbin', gridsize=20, figsize=(8, 6), sharex=False, grid=True)
data.plot(y='column', kind='pie');
data.sort_values(by='median_time', ascending=True).plot(y='median_time', kind='bar', figsize=(10,5))

print(data['column_1'].corr(data['column_2']))

** Матрица рассеяния

pd.plotting.scatter_matrix(data, figsize=(9, 9))

** Замена данных

print(shopping.where(shopping != 'хамон', 'обойдусь')

# если name нет в big_nets_stat то заменить имя на другие
station_stat_full['group_name'] = station_stat_full['name'].where(
    station_stat_full['name'].isin(big_nets_stat.index), 'Другие')

# Построить гистограму в цикле
for name, group_data in good_data.groupby('group_name'):
    group_data.hist('time_spent', bins=50)








## ПРОПУСКИ 
................






### DS.03. Исследовательский анализ данных. Тема 06. Валидация результатов
Построение столбчатой диаграммы 
```python
data.plot(y='column', kind='bar')
```
Построение круговой диаграммы 
```python
data.plot(y='column', kind='pie')
```
Выборочное изменение значения 
```python
data['column'].where(s > control_value, default_value) # если не выполняется условие - первый параметр, то значение заменяется на второй параметр
```
Срезы по значениям столбца 
```python
# column_value - значение столбца, 
# column_slice - срез данных, в котором значение столбца - column_value 
for column_value, column_slice in data.groupby('column'):
	# do something
```


## Взаимосвязь данных

**Построение точечной диаграммы (диаграммы рассеяния)**
`data.plot(x='column_x', y='column_y', kind='scatter') `
**Построение попарных точечных диаграмм для столбцов датафрейма**
`pd.plotting.scatter_matrix(data) `
**Построение ячеечной диаграммы**
`data.plot(x='column_x', y='column_y', kind='hexbin', gridsize=20, sharex=False)` # gridsize – число ячеек по горизонтальной оси 
**Вычисление коэффициента корреляции Пирсона**
`print(data['column_1'].corr(data['column_2']))`
**Коэффициент корреляции Пирсона между всеми парами столбцов**
`data.corr()`


