## [DS.02 Предобработка данных. Тема 3. Изменение типов данных](https://practicum.yandex.ru/trainer/data-scientist/lesson/3e8cf2c4-d388-43b4-b54f-0ef5ff709318/)

**SEO**-оптимизация (от англ. Search Engine Optimization, «оптимизация поисковых машин») — действия, направленные на повышение позиций сайта в результатах выдачи поисковых систем. Цель SEO-оптимизации — увеличение трафика из поисковиков на сайт и, как следствие, рост числа покупок.

Место сайта в результатах поиска зависит от огромного количества факторов. Их делят на внутренние и внешние. Так, внутренние факторы — скорость загрузки и качество контента сайта. Важный внешний фактор — то, как часто сайт цитируют на других ресурсах, например, в СМИ и соцсетях.

* Переводить строку в форматы даты и времени;
* Превращать строковые значения в числовые методами `to_numeric()` и `astype()`;
* Обрабатывать ошибки связкой `try-except`;
* Соединять таблицы методом `merge()`;
* Создавать сводные таблицы методом `pivot_table()`.


### Урок 2. Как читать файлы из Excel


«Определить, какие товарные категории и подкатегории на сайте представлены в поисковиках хуже всего» — так обозначили свой запрос SEO-оптимизаторы.

* **«какие товарные категории и подкатегории на сайте...»**: нужен список товарных категорий и подкатегорий;
* **«....представлены в поисковиках...»**: нужна таблица посещаемости категорий сайта с источником трафика «Переходы из поисковых систем». Эти переходы ещё называют **органическими**, потому что их обеспечивают пользователи, которые _естественным образом_ нашли сайт в поисковой выдаче, а не попали на сайт через рекламу;

* **«…хуже всего»**: нужно определить, насколько высоко страницы товарных категорий стоят в поисковой выдаче. Ограничимся сравнением количества заходов из поисковиков с трафиком из других источников.

   `read_excel()` нужно два аргумента: строка с именем самого файла или пути к нему, и имя листа `sheet_name`. По умолчанию первый Лист.
```python
category_dict = pd.read_excel('/datasets/seo_data.xlsx', sheet_name='category_ids' )
```
  
### Лабораторка
```python
import pandas as pd

#прочитайте файл seo_data, лист traffic_data

data = pd.read_excel('/datasets/seo_data.xlsx', sheet_name='traffic_data')

print(data.head())

print(data['source'].unique())

subcategory_dict = pd.read_excel('/datasets/seo_data.xlsx', sheet_name='subcategory_ids' )

print(subcategory_dict.head())

category_dict = pd.read_excel('/datasets/seo_data.xlsx', sheet_name='category_ids' )

print(category_dict.head())
```

### Урок 3. Неидеальные данные
```python
print(data.groupby('source').sum())
```

Если Pandas считает данные не числовыми, а строковыми (**object**), необходимо исправлять.

### Урок 4. Перевод строковых значений в числа

Сделать строки числами может стандартный метод Pandas —  **`to_numeric()`**. Он превращает значения столбца в числовой тип `float64` (вещественное число).

У метода _to_numeric()_ есть параметр **errors**. От значений, принимаемых _errors_, зависят действия _to_numeric_ при встрече с некорректным значением:

* `errors='raise' — дефолтное поведение: при встрече с некорректным значением выдаётся ошибка, операция перевода в числа прерывается;
* `errors='coerce' — некорректные значения _принудительно_ заменяются на NaN;
* `errors='ignore' — некорректные значения _игнорируются_, но остаются.

```python
transactions['amount'] = pd.to_numeric(transactions['amount'], errors='coerce')

pd.to_numeric(data['column']) # первый аргумент - колонка из датафрейма # второй аргумент (errors) - метод обработки ошибок

pd.to_numeric(data['column'], errors='raise' ) # если errors='raise' (значение по умолчанию), то при встрече с некорректным # значением выдается ошибка, операция перевода в числа прерывается;

pd.to_numeric(data['column'], errors='coerce') # если errors='coerce', то некорректные значения принудительно заменяются на NaN;

pd.to_numeric(data['column'], errors='ignore') # если errors='ignore', то некорректные значения игнорируются, но остаются.
```

Особенность метода `to_numeric()` в том, что при переводе все числа будут иметь тип данных _float_. Это подходит далеко не всем значениям. Но есть и хорошие новости: в нужный тип значения переводят методом `astype()`. Например, аргумент `('int')` метода `astype()` означает, что значение нужно перевести в целое число

**df['column'] = df['column'].astype('int')**

![astype|640x250](https://pictures.s3.yandex.net/resources/Frame_3.3_1561106592.jpg)

### [Лабораторка](https://practicum.yandex.ru/trainer/data-scientist/lesson/cac735ca-95a3-46f4-ae61-524bd4f90f28/task/ed63606f-d57f-473e-834b-870895498022/)
```python
import pandas as pd

transactions = pd.read_excel('/datasets/ids.xlsx')

#transactions.info()

transactions['amount'] = pd.to_numeric(transactions['amount'])

transactions['id'] = pd.to_numeric(transactions['id'], errors='coerce')

transactions.info()

print(transactions.tail())

transactions['id'] = pd.to_numeric(transactions['id'], errors='coerce')

transactions['amount'] = pd.to_numeric(transactions['amount'], errors='coerce')

summ = transactions['amount'].sum()

transactions_per_category = transactions.groupby('category')['amount'].sum()

print(transactions_per_category)

print(data.loc[964])

l = data['subcategory_id'].count()

#len(data.loc[data['subcategory_id'] == 'total'])

print(f'Количество строк: {l}')

print(data.loc[data['subcategory_id'] == 'total'])

data = data[data['subcategory_id'] != 'total']

print(data[data['subcategory_id'] == 'total'])

data['visits'] = data['visits'].astype('int')

data.info()

# выберем столбец visits после группировки

print(data.groupby('source')['visits'].sum())
```

### Урок 5. Методы Pandas для работы с датой и временем
[Урок 5](https://practicum.yandex.ru/trainer/data-scientist/lesson/d5626819-8847-4cf6-87b3-31fadf405d9b/task/e181eca5-21ad-4838-af44-8502506a98ab/)

Вне зависимости от способа записи, дату и время нужно вводить в арифметические операции. Для этого в Python существует особый тип данных — **datetime**

Методом **to_datetime()** превратим содержимое этого столбца в понятные для Python даты.

Для этого строку форматируют, обращаясь к специальной системе обозначений, где:

* %d — день месяца (от 01 до 31)
* %m — номер месяца (от 01 до 12)
* %Y — четырёхзначный номер года (например, 2019), %y - два знака
* Z — стандартный разделитель даты и времени
* %H — номер часа в 24-часовом формате
* %I — номер часа в 12-часовом формате
* %M — минуты (от 00 до 59)
* %S — секунды (от 00 до 59)

Преобразуем формат даты 01.04.2019Z11:03:00 из первой строчки датафрейма:

* Сначала номер дня месяца. В соответствии с таблицей форматов заменяем его на **%d**: **%d**.04.2019Z11:03:00
* Далее точка (ее оставляем без изменений), потом номер месяца: **%m**: **%d.%m**.2019Z11:03:00
* После четырёхзначный номер года, заменяем 2019 на **%Y**: **%d.%m.%Y**Z11:03:00
* Букву **Z** оставляем без изменений: **%d.%m.%YZ**11:03:00
* Номер часа в 24-часовом формате заменим на **%H: %d.%m.%YZ%H:**03:00
* Количество минут обозначим **%M: %d.%m.%YZ%H:%M:**00
* Завершим форматирование обозначением секунд **%S: %d.%m.%YZ%H:%M:%S**

arrivals['date_datetime'] = pd.to_datetime( arrivals['date'], format='%d.%m.%YZ%H:%M:%S' )

Среди самых разнообразных способов представления даты и времени особое место занимает формат **unix time**. Его идея проста — это количество секунд, прошедших с 00:00:00 1 января 1970 года. Время _unix_ соответствует Всемирному координированному времени, или _UTC_.

1661503588 = Fri Aug 26 2022 08:46:28 GMT+0

В формате _unix time_ дата и время хранятся в виде целого числа. Отсюда преимущества:

* хранение даты и времени в виде целого числа экономит место на диске;
* с датами-числами легко проводить арифметические операции;
* даты, записанные в виде целого числа, удобно принимать за единый формат.

Метод `to_datetime()` работает и с форматом _unix time_. Первый аргумент — это столбец со временем в формате _unix time_, второй аргумент `unit` со значением `'s'` сообщит о том, что нужно перевести время в привычный формат с точностью до секунды.

arrivals['month'] = pd.DatetimeIndex(arrivals['date_datetime']).month

## Получение из столбца с датой и временем...
```python
pd.DatetimeIndex(data['time']).year # года

pd.DatetimeIndex(data['time']).month # месяца

pd.DatetimeIndex(data['time']).day # дня

pd.DatetimeIndex(data['time']).hour # часа

pd.DatetimeIndex(data['time']).minute # минуты

pd.DatetimeIndex(data['time']).second # секунды
```

### Лабораторка
```python
import pandas as pd

position = pd.read_csv('/datasets/position.csv')

position['timestamp'] = pd.to_datetime(position['timestamp'], format='%Y-%m-%dT%H:%M:%S')

print(position.head())

print(position.sort_values(by='level', ascending=False))

position['month'] = pd.DatetimeIndex(position['timestamp']).month

ndf = position.groupby('month')['level'].mean()
```

### Урок 6. Обработка ошибок: try-except

[https://practicum.yandex.ru/trainer/data-scientist/lesson/2001dde5-8429-48c6-b504-b0667782e8a0/task/7924ce5c-6b0a-421b-99cd-c61ad037f99e/](https://practicum.yandex.ru/trainer/data-scientist/lesson/2001dde5-8429-48c6-b504-b0667782e8a0/task/7924ce5c-6b0a-421b-99cd-c61ad037f99e/)

* Некорректный формат приводит к невыполнению кода. Говорят, что _«код падает с ошибкой»_. Здесь вы уже опытны: например, если числа в наборе данных вдруг стали строками, умеете вызвать метод `to_numeric()`;
* Ошибки в данных встречаются ближе к концу файла, и код на строках с неверными значениями не выполняется. Значит, пропадают расчёты для предыдущих, «безошибочных» строк;
* Данные могут поменяться. К примеру, в выгрузку для бухгалтерии с появлением нового контрагента могут проникнуть некорректные данные, из-за которых код упадёт.

Для работы с непредсказуемым поведением данных есть конструкция `**try-except**`. Принцип работы такой: исходный код помещают в блок `try`. Если при выполнении кода из блока `try` возникнет ошибка, воспроизведётся код из блока `except`.  Благодаря `try-except` и цикл `for` не прервётся на ошибке, а продолжит работу.

```python
a = 1; b = 0

try:

	print(a / b)

except:

	print('Проверьте значения параметров a и b')

print('Кстати, хорошего дня')
```

### Лабораторка
```python
position = [['2019-05-01', '6'],

['2019-05-10', '3'],]

count_lines = 0; total_position = 0

for row in position:

count_lines += 1

#total_position = total_position + int(position[count_lines-1][1])

total_position = total_position + int(row[1])

#в этой переменной сохраните позицию в выдаче

level = total_position / count_lines

print(level)

```

**II**
```

count_lines = 0; wrong_lines = 0; total_position = 0

wrong_lines_content = []

for row in position:

try:

	count_lines += 1
	
	level = int(row[1])
	
	total_position +=1

except:

	wrong_lines_content.append(row)
	
	wrong_lines +=1
	
level = total_position / count_lines

print(f'Количество измерений {count_lines}')

#print(f'Количество некорректных строк {wrong_lines}')

print(f'Некорректные строки {wrong_lines_content}')
```

### Урок 7. Метод merge()

Объединим несколько таблиц в одну методом `merge()`. Передавая тот или иной аргумент методу `merge()`, можно по-разному объединять таблицы.

`merge()` применяют к таблице, к которой присоединяют другую. У метода следующие аргументы:

* `right` — имя `DataFrame` или `Series`, присоединяемого к исходной таблице.
* `on` — название общего списка в двух соединяемых таблицах: по нему происходит слияние.
* `how` — чьи `id` включать в итоговую таблицу. Аргумент `how` может принять значение `left`: тогда в итоговую таблицу будут включены id из левой таблицы. Аргумент `right` включает `id` из правой таблицы.

**data.merge(d, on, how)


**d - датасет, с которым сливают

**on - колонка, по значениям которой сливают

**how - тип слияния: data.merge(data2, on='merge_column', how='left')

**left - обязательно присутствуют все значения из таблицы data,

**вместо значений из data2 могут быть NaN data.merge(data2, on='merge_column', how='right')

**right - обязательно присутствуют все значения из таблицы data2,

вместо значений из data могут быть NaN
```python
data_subcategory = data.merge(subcategory_dict, on='subcategory_id', how='left') print(data_subcategory.head(10))
```

### Лабораторка
```python
import pandas as pd

data = pd.read_excel('/datasets/seo_data.xlsx', sheet_name='traffic_data')

subcategory_dict = pd.read_excel('/datasets/seo_data.xlsx', sheet_name='subcategory_ids')

data_subcategory = data.merge(subcategory_dict, on='subcategory_id', how='left')

data_final = data_subcategory.merge(category_dict, on='category_id', how='left')

#print(data.head())

#print(subcategory_dict.head())

print(data_subcategory.head(10))

#data.info()

#subcategory_dict.info()
```

### Урок 8. Сводные таблицы

**Сводная таблица** - инструмент обработки данных для их обобщения

В Pandas для подготовки сводных таблиц вызывают метод **pivot_table()**.

Аргументы метода:

* _`index`_ — столбец или столбцы, по которым группируют данные (название товара)
* _`columns`_ — столбец, по значениям которого происходит группировка (даты)
* _`values`_ — значения, по которым мы хотим увидеть сводную таблицу (количество проданного товара)
* _`aggfunc`_ — функция, применяемая к значениям (сумма товаров). Например:
-   `median` — медианное значение;
-   `count` — количество значений;
-   `sum` — сумма значений;
-   `min` — минимальное значение;
-   `max` — максимальное значение;
-   `first` — первое значение из группы;
-   `last` — последнее значение из группы.

```python
data_pivot = data.pivot_table(index = ['column1', 'column2'], columns = 'source', values = 'column_pivot', aggfunc = 'function')
```

cделаем по ней сводную таблицу методом `pivot_table()`:
```python
data_pivot = data_final.pivot_table(index=['category_name', 'subcategory_name'], columns='source', values='visits', aggfunc='sum')

print(data_pivot.head(10))
```

основная категория включает в себя подкатегорию и это представлено в структуре датафрейма: категория отображена иерархически главной над подкатегорией. Такие датафреймы содержат в себе мультииндекс. Часто при работе с такими датафреймами мультииндекс убирают, чтобы категория была отображена на каждой строчке датафрейма
```python
data_pivot_with_reset_index = data_pivot.reset_index()

print(data_pivot_with_reset_index.head(10))
```

В таблице выше суммы визитов `visits` по каждому из источников `source` (`direct` и `organic`) представлены в отдельных столбцах. Такой вид таблицы называется «**широкий**». Он удобен, когда нужно сравнить значения столбцов. Хорошо заметно, например, что в подкатегории «Автомобильные инверторы» количество визитов из источников `direct` и `organic` практически одинаково, а в подкатегории «Автомагнитолы» из источника `organic` пришло почти в два раза больше посетителей, чем из `direct`.

Для группировки данных также подходит изученная вами ранее комбинация методов `groupby()` и `agg()` , но с ними таблица будет выглядеть иначе. Метод `groupby()` принимает один аргумент — столбец (или список столбцов), по которым группируют данные. В метод `agg()` передают словарь. Его ключ — это названия столбцов, а значение — функции, которые будут к этим столбцам применены (например, `sum` или `count`). Такие функции называются агрегирующие.
```python
data_grouped = data_final.groupby(['category_name','subcategory_name','source']).agg({'visits':'sum'}) 

print(data_grouped.head(10))
```

Сгруппировав данные методами `groupby()` и `agg()` вместо `pivot_table()`, мы получили точно такие же данные, но в несколько другом виде. Он называется «**длинный**». Методы `groupby()` и `agg()` удобны, когда нужно применить функцию к столбцу со сгруппированными визитами `visits` или создать новый столбец на его основе

```python
data_grouped['daily_visits'] = data_grouped['visits'] / 30

print(data_grouped.head(10))
```

### Лабораторка

```python
import pandas as pd

data_final = pd.read_csv('/datasets/data_final.csv')

data_pivot = data_final.pivot_table(index=['category_name', 'subcategory_name'], columns='source', values='visits', aggfunc='sum')

data_pivot_with_reset_index = data_pivot.reset_index()

data_pivot['ratio'] = data_pivot['organic'] / data_pivot['direct']

data_pivot = data_pivot.sort_values(by='ratio', ascending=False) # по убыванию

print(data_pivot.head(10))

print(data_pivot.sort_values(by='ratio', ascending=False).tail(10))

print(data_pivot.loc[(data_pivot['direct'] > 1000) & (data_pivot['organic'] > 1000)].sort_values(by='ratio', ascending=False).tail(10))
```

Чтобы ничего не забыть, скачайте [шпаргалку](https://code.s3.yandex.net/data-analyst/praktikum_data_analysis_takeaways_course2_theme3.pdf) и [конспект](https://code.s3.yandex.net/data-analyst/praktikum_data_analysis_abstract_course2_theme3.pdf) темы.

### Где ещё почитать про изменение типов данных:

[Интересная статья об устройстве типов данных в _Pandas_](https://habr.com/ru/company/ruvds/blog/442516/)