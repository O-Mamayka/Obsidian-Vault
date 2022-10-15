# [Тема 06. Валидация результатов](https://practicum.yandex.ru/trainer/data-scientist/lesson/c99fbf8e-c5f9-46b0-b3a8-58584f3fd733/)
-   строить столбчатые графики и круговые диаграммы;
-   выборочно изменять значения в списке методом `where()`;
-   писать цикл, который строит сразу много гистограмм.
-   объединить мелкие сети в группу «Другие»;
-   построить гистограммы продолжительности заправки в каждой сети;
-   получить финальный список крупных сетей АЗС.

### [Урок 2. Укрупняем группы](https://practicum.yandex.ru/trainer/data-scientist/lesson/017e5915-4323-4015-97ff-77e5b6b89a03/task/d26e0853-4109-4c43-b803-4eeb77195a46/)
Данные бывают разной природы, и для всяких наблюдений есть подходящие графики. Например, если нужно продемонстрировать доли от 100%, строят круговую диаграмму. В методе `plot()` задают тип: `kind='pie'` (от англ. pie chart — «диаграмма-пирог», похожа на круглый пирог, поделённый на дольки). Столбец с данными для диаграммы указывают в параметре `y` метода `plot()`.
На графике же нужно отразить факт, что каждая сеть АЗС — это отдельный объект, никак не связанный с ближайшими соседями в рейтинге. Если объект исследования является обособленным, никак не связанным с ближайшими соседями, то для анализа таких наблюдений лучше подходит столбчатый график, он подчёркивает изолированность данных.
Столбчатый график строят методом `plot()`, параметром передают тип графика: `kind='bar'` (от англ. bar chart — «столбчатая диаграмма»). Однако график может быть не наглядным, ведь сетей много и лишь несколько из них — крупные. Лучше объединить все мелкие сети и отрисовать как один столбец.
Данные по малым сетям можно просто отбросить, но полезнее сгруппировать их в «сеть» под названием «Другие», то есть сделать выборочное переименование. Так вы и данные не потеряете, и покажете отличие малых сетей от старших братьев.
Выборочно изменяют значения методом `where()` (пер. «где»). Ему передают два параметра: условие для булева массива и новые значения. Если условие равно `True`, соответствующее ему значение не изменится, а если `False` — поменяется на второй параметр метода.
```python
print(shopping.where(shopping != 'хамон', 'обойдусь')
```
При объединении данных случается отбрасывать пустые значения. Вы знакомы с методом `dropna()` из вводного курса. Напомним, что он удаляет пропущенные значения из датафрейма. Когда нужно удалить строки с пропусками в конкретном столбце, его название передают параметру `subset` метода `dropna()`:
```python
dataframe.dropna(subset=['column_name'])
```
В некоторых случаях, для визуализации данных уместно использовать круговую диаграмму, т.к. она хороша для показа доли каждого значения от 100% всех. Чтобы получить круговую диаграмму достаточно в .plot задать kind='pie' . При этом нужно задать столбец с данными параметром y : ```
```python
data.plot(y='column', kind='pie');
```

**Разбитые по группам данные**
Перебирать отдельные данные в столбце не всегда бывает удобно. Для работы с данными по группам существует метод groupby() , который автоматически перебирает уникальные значения. Мы передадим ему столбец, а он вернёт последовательность пар: значение столбца — срез данных с этим значением. И в дальнейшем мы сможем обрабатывать эти срезы в соответствии с нашими нуждами. 
```python
for column_value, column_slice in data.groupby('column'): 
	# do something
```

#### Урок 2. Задача 1
Визуализируйте распределение лучших показателей заездов с типичной продолжительностью по сетям
1.  Упорядочьте таблицу `final_stat` по возрастанию лучших показателей из столбца `median_time`. `median_time`— это медиана для распределения медианной продолжительности заправки по АЗС в каждой сети.
2.  Постройте столбчатый график по значениям `median_time`

```python
import pandas as pd

data = pd.read_csv('/datasets/visits.csv', sep='\t')

# фильтруем слишком быстрые и медленные заезды и АЗС
data['too_fast'] = data['time_spent'] < 60
data['too_slow'] = data['time_spent'] > 1000
too_fast_stat = data.pivot_table(index='id', values='too_fast')
good_ids = too_fast_stat.query('too_fast < 0.5')
good_data = data.query('id in @good_ids.index')
good_data = good_data.query('60 <= time_spent <= 1000')

# считаем данные по отдельным АЗС и по сетям
station_stat = data.pivot_table(index='id', values='time_spent', aggfunc='median')
good_stations_stat = good_data.pivot_table(index='id', values='time_spent', aggfunc='median')
stat = data.pivot_table(index='name', values='time_spent')
good_stat = good_data.pivot_table(index='name', values='time_spent', aggfunc='median')
stat['good_time_spent'] = good_stat['time_spent']

id_name = good_data.pivot_table(index='id', values='name', aggfunc=['first', 'count'])
id_name.columns = ['name', 'count']
station_stat_full = id_name.join(good_stations_stat)

# считаем показатели сетей из показателей АЗС,
# а не усреднённые заезды на все АЗС сети
good_stat2 = (
    station_stat_full
    .query('count > 30')
    .pivot_table(index='name', values='time_spent', aggfunc=['median', 'count'])
)
good_stat2.columns = ['median_time', 'stations']
final_stat = stat.join(good_stat2)

final_stat.sort_values(by='median_time', ascending=True).plot(y='median_time', kind='bar', figsize=(10,5))
```

#### Урок 2. Задача 2
Так как в `join()` по умолчанию левое соединение, индексы из `final_stat` будут идентичны индексам из `stat`. Поэтому любой индекс из таблицы `stat`, которого нет в таблице `good_stat2`, после объединения получит значение `NaN`.
1.  Отбросьте значения `NaN` в столбце `median_time` таблицы `final_stat`.
2.  Упорядочьте таблицу `final_stat` по возрастанию значений в столбце `median_time`.
3.  Постройте столбчатый график `median_time`. Задайте размер графика 10х5 дюймов. Добавьте линии сетки.
```python
good_stat2.columns = ['median_time', 'stations']
final_stat = stat.join(good_stat2)

final_stat.dropna(subset=['median_time']).sort_values(
				  by='median_time', ascending=True).plot(
				  y='median_time', kind='bar', figsize=(10,5), grid=True)
```

#### Урок 2. Задача 3
Стоит учесть ещё одну переменную: число АЗС внутри сетей. С точки зрения маркетинга интересны и сети с большей продолжительностью заправки, и сети, в которых много АЗС. Значит, нужно исключить те сети, в которых заправочных станций мало. А для начала посмотрите, как число заправочных станций распределяется по сетям.
Используя данные из таблицы `final_stat`, постройте гистограмму, отображающую число АЗС внутри сетей. Поделите значения на 100 корзин.
```python

stat['good_time_spent'] = good_stat['time_spent']

id_name = good_data.pivot_table(index='id', values='name', aggfunc=['first', 'count'])
id_name.columns = ['name', 'count']
station_stat_full = id_name.join(good_stations_stat)

# считаем показатели сетей из показателей АЗС,
# а не усреднённые заезды на все АЗС сети
good_stat2 = (
    station_stat_full
    .query('count > 30')
    .pivot_table(index='name', values='time_spent', aggfunc=['median', 'count'])
)
good_stat2.columns = ['median_time', 'stations']
final_stat = stat.join(good_stat2)
#print(final_stat)
final_stat.hist('stations', bins=100)

```

#### Урок 2. Задача 4
Так как с точки зрения маркетинга небольшие сети неважны, создайте новую переменную с данными только крупных сетей.
Создайте переменную `big_nets_stat` и поместите в неё строки из таблицы `final_stat`, в которых значение переменной `stations` больше 10.

**Подсказка**
Методом _query()_ получите выборку сетей АЗС с количеством станций больше 10.
```python
big_nets_stat = final_stat.query('stations > 10')
print(big_nets_stat)

```

#### Урок 2. Задача 5
Теперь можно разделить все сети на две группы: «Большая восьмёрка» и «Другие». Вторая группа будет восприниматься как одна большая сеть.
Лучшие показатели средней продолжительности заправки содержатся в таблице `good_stat2` и рассчитываются по данным `station_stat_full`. Повторите вычисления, но вместо того, чтобы группировать данные по столбцу `name`, сгруппируйте данные по новому столбцу, содержащему категорию `Другие`. Чтобы создать этот столбец в таблице `station_stat_full`, примените метод `where()` для сравнения столбца `name` в `station_stat_full` с индексами `big_nets_stat`.
1.  Добавьте в таблицу `station_stat_full` новый столбец `group_name`.
2.  Поместите в столбец `group_name` значения столбца `name`, если сеть присутствует в `big_nets_stat`. Если столбец `name` отсутствует, поместите в `group_name` значения из `Другие`.
**Подсказка**
Примените метод `where()` к столбцу `'name'` из _station_stat_full_. Первым параметром передайте условие булева массива, где _True_ соответствует именам крупных сетей, которые должны остаться без изменений. Список таких сетей — это `big_nets_stat.index`. Для проверки вхождения имени в список примените метод `isin()`. Вторым параметром `where()` передайте новое название `'Другие'`.
```python
final_stat = stat.join(good_stat2)

big_nets_stat = final_stat.query('stations > 10')

# !!!!!!!!!!!!!!!
station_stat_full['group_name'] = station_stat_full['name'].where(
    station_stat_full['name'].isin(big_nets_stat.index), 'Другие')

print(station_stat_full.head())
```

#### Урок 2. Задача 6
Повторите анализ, в процессе которого создали `good_stat2`, но в этот раз сгруппируйте данные по `group_name`.
1.  Создайте переменную `stat_grouped`, которая повторяет вычисления `good_stat2`, но группирует по `group_name`.
2.  Переименуйте столбцы в `stat_grouped` на `time_spent` и `count`.
3.  Упорядочьте `stat_grouped` по возрастанию значений столбца `time_spent`. 
**Подсказка**
Повторите действия, чтобы создать `stat_grouped`, но в `pivot_table()` укажите `index=group_name`. Когда будете сортировать данные методом `sort_values()`, используйте параметр `inplace` или перепишите переменную вручную. После сортировки выведите `stat_grouped` на экран.
```python
stat_grouped = (
    station_stat_full
    .query('count > 30')
    .pivot_table(index='group_name', values='time_spent', aggfunc=['median', 'count'])
)
stat_grouped.columns = ['time_spent', 'count']
stat_grouped = stat_grouped.sort_values(by='time_spent', ascending=True)

print(stat_grouped)
```


#### Урок 2. Задача 7
Визуализируйте относительную величину этих сетей с точки зрения количества заправочных станций.
 По данным `stat_grouped` постройте круговую диаграмму с числом АЗС в каждой сети. Задайте её размер 8x8 дюймов.
**Подсказка**
Примените метод `plot()` к `stat_grouped`. Передайте параметру `y` столбец с числом АЗС: `count`. В параметре `kind` задайте круговой тип диаграммы: `pie`. Укажите размер 8x8 дюймов в параметре `figsize`.
```python
stat_grouped.columns = ['time_spent', 'count']

stat_grouped.plot(y='count', kind='pie', figsize=(8, 8))
```

### [Урок 3. Разбитые по группам данные](https://practicum.yandex.ru/trainer/data-scientist/lesson/2bb23da4-07b6-4774-b6c5-356837ba8c93/)
друг на среднюю продолжительность заправки у ваших избранников повлияли аномально короткие заезды? Нужно посмотреть на гистограммы отдельно для каждой сети.
Можно автоматизировать в цикле. Сначала создать столбец `group_name` и перебрать названия групп так: `good_data['group_name'].unique()`. Затем получить срез из `good_data` методом `query()` и построить гистограмму по отфильтрованным данным. Однако в pandas есть метод `groupby()`, автоматически перебирающий уникальные значения. Если передать ему столбец, то он вернёт последовательность пар: значение столбца — срез данных с этим значением.

```python
for developer_name, developer_data in IT_names.groupby('name'):
    print(
        'Имя {} встречается {} раза'.format(
            developer_name, len(developer_data)
        )
    )
```
Метод `groupby()` позволяет сразу производить простые вычисления над элементами группы. Например, применив метод `count()`, можно добиться аналогичного результата. Получим список имён с их частотой.
```python
print(IT_names.groupby('name').count())
```
Результат работы функции, применённой к `groupby()`, становится аналогом `pivot_table()`. Однако нас интересует перебор значений в цикле. Постройте гистограммы для каждой из сетей.

#### Урок 3. Задача 1
Посмотрите, как продолжительность заездов распределяется по девяти сетям
Если продолжительность сильно различается, то сравнивать показатели разных сетей будет неправильно. Например, если в одной сети больше АЗС с продолжительностью заездов по 60–70 секунд, чем в других, это может понижать медианное значение. Чтобы проверить, не происходит ли такое, сгруппируйте данные из `good_data` по `group_name` и постройте гистограммы. Первым делом создайте столбец для группировки.
- Создайте столбец `group_name` в таблице `good_data` так же, как делали раньше в `station_stat_full`.
**Подсказка**
Скопируйте метод `where()`, который вы применяли к `station_stat_full`, и просто замените `station_stat_full` на `good_data`.
```python
import pandas as pd
data = pd.read_csv('/datasets/visits.csv', sep='\t')

# фильтруем слишком быстрые и медленные заезды и АЗС
data['too_fast'] = data['time_spent'] < 60
data['too_slow'] = data['time_spent'] > 1000
too_fast_stat = data.pivot_table(index='id', values='too_fast')
good_ids = too_fast_stat.query('too_fast < 0.5')
good_data = data.query('id in @good_ids.index')
good_data = good_data.query('60 <= time_spent <= 1000')

# считаем данные по отдельным АЗС и по сетям
station_stat = data.pivot_table(index='id', values='time_spent', aggfunc='median')
good_stations_stat = good_data.pivot_table(index='id', values='time_spent', aggfunc='median')
stat = data.pivot_table(index='name', values='time_spent')
good_stat = good_data.pivot_table(index='name', values='time_spent', aggfunc='median')
stat['good_time_spent'] = good_stat['time_spent']

id_name = good_data.pivot_table(index='id', values='name', aggfunc=['first', 'count'])
id_name.columns = ['name', 'count']
station_stat_full = id_name.join(good_stations_stat)

# считаем показатели сетей из показателей АЗС,
# а не усреднённые заезды на все АЗС сети
good_stat2 = (
    station_stat_full
    .query('count > 30')
    .pivot_table(index='name', values='time_spent', aggfunc=['median', 'count'])
)
good_stat2.columns = ['median_time', 'stations']
final_stat = stat.join(good_stat2)

big_nets_stat = final_stat.query('stations > 10')
station_stat_full['group_name'] = (
    station_stat_full['name']
    .where(station_stat_full['name'].isin(big_nets_stat.index), 'Другие')
)

stat_grouped = (
    station_stat_full
    .query('count > 30')
    .pivot_table(index='group_name', values='time_spent', aggfunc=['median', 'count'])
)
stat_grouped.columns = ['time_spent', 'count']

good_data['group_name'] = (
    good_data['name']
    .where(good_data['name'].isin(big_nets_stat.index), 'Другие')
)
print(good_data.head())
```
#### Урок 3. Задача 2
Сгруппируйте `good_data` и постройте гистограмму, чтобы увидеть, как распределяется продолжительность заездов в каждой сети.
- Сгруппируйте `good_data` по `group_name`, используя цикл `for`. Используйте в цикле переменные `name` и `group_data`.
**Подсказка**
Создайте цикл, перебирающий сгруппированные по _'group_name'_ данные из _good_data_.
Названию и срезу данных, которые возвращает _groupby()_ на каждом шаге цикла, дайте имена _name_ и _group_data_. Внутри цикла вызовите метод _hist()_ к данным _group_data_.
Параметрами метода _hist()_ передайте столбец `'time_spent'`, по которому нужно построить гистограмму, и _bins=50_.
график в цикле:
```python
for name, group_data in good_data.groupby('group_name'):
    group_data.hist('time_spent', bins=50)
```

#### Урок 3. Задача 3
Повторите предыдущее задание, но теперь сделайте название сети заголовком гистограмм. Как вы помните, метод `plot()` даёт больше вариантов для форматирования, чем метод `hist()`.
1.  Напишите ещё один цикл `for`, как в предыдущем задании. Используйте в качестве переменных цикла `name` и `group_data`.
2.  В каждой итерации `group_data` вызовите метод `plot()`, чтобы построить гистограмму по значениям `time_spent`.
**Подсказка**
Создайте цикл, перебирающий сгруппированные по _'group_name'_ данные из _good_data_.
Названию и срезу данных, которые возвращает _groupby()_ на каждом шаге цикла, дайте имена _name_ и _group_data_. Внутри цикла вызовите метод _plot()_ к данным _group_data_. Параметру `y` передайте столбец `'time_spent'`, в параметре `title` укажите `name` (без кавычек, это переменная!) В _kind_ укажите тип графика _'hist'_, а в _bins_ = 50.
```python
for name, group_data in good_data.groupby('group_name'):
    group_data.plot(y='time_spent', kind='hist', title=name, bins=50, grid=True)
```


Чтобы ничего не забыть, [скачайте шпаргалку](https://code.s3.yandex.net/data-analyst/conspects/praktikum_data_analysis_takeaways_course3_theme5.pdf) и [конспект темы](https://code.s3.yandex.net/data-analyst/conspects/praktikum_data_analysis_abstract_course3_theme5.pdf).

### Где ещё почитать про группировку данных
[«Первичный анализ данных с Pandas», раздел «Группировка данных»](https://habr.com/ru/company/ods/blog/322626/) — группировка с `groupby`.

[«Аналитикам: большая шпаргалка по Pandas», раздел «Считаем производные метрики»](https://smysl.io/blog/pandas/#%D0%A1%D1%87%D0%B8%D1%82%D0%B0%D0%B5%D0%BC-%D0%BF%D1%80%D0%BE%D0%B8%D0%B7%D0%B2%D0%BE%D0%B4%D0%BD%D1%8B%D0%B5-%D0%BC%D0%B5%D1%82%D1%80%D0%B8%D0%BA%D0%B8) — примеры `groupby`.



