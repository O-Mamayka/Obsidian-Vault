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

our_df = pd.DataFrame ({ 'a1': [2, 4, 6], 'b1': [3, 2, 2], 'c1': ['A', 'B', 'C'] }) 
print(df.query('a in @our_df.index')) # строим срез, в котором значения столбца a равны индексам датафрейма our_df, т. е. 0, 1 или 2

print(df.query('a in @our_df.a1')) # Проверяет, есть ли значение среди значений колонки датафрейма

print(df.query('b in @our_df.b1')) # строим срез, в котором значения столбца b равны значениям столбца b1 датафрейма our_df

```


#### [Урок 3. Задача 1](https://practicum.yandex.ru/trainer/data-scientist/lesson/7c8dd1bd-912d-47b2-a35d-3ed0e9b4206f/task/cab5b553-f0a8-481e-af34-446cf7a6a75b/)

**Правило**: исключаются из анализа те объекты, на которых длительность половины или более событий очень мала.
**Правило**: эксперименты, результаты которых меньше или больше обычных , исключаются из анализа

```python
good_ids = too_fast_stat.query('too_fast < 0.5')
good_data = data.query('id in @good_ids.index')
good_data = good_data.query('time_spent >=  60 and time_spent <= 1000')

print(data.shape[0]) # число записей в таблице data
print(good_data.shape[0]) # число записей в таблице good_data

# сводная таблица с медианными значениями time_spent после фильтрации
good_stations_stat = good_data.pivot_table(index='id', values='time_spent', aggfunc='median') 
good_stations_stat.hist(bins=50)

good_stat = good_data.pivot_table(index='name', values='time_spent', aggfunc='median').sort_values(by='time_spent', ascending=True)
print(good_stat)

```


### [Урок 4. Добавляем столбец](https://practicum.yandex.ru/trainer/data-scientist/lesson/12ce13d5-48bd-43ad-9a8f-32e0055b6070/)

```python

median_station_stat = data.pivot_table(
    index='id', values='time_spent', aggfunc='median'
)
good_stations_stat = good_data.pivot_table(
    index='id', values='time_spent', aggfunc='median'
)

ax = median_station_stat.plot(
    kind='hist',
    y='time_spent',
    histtype='step',
    range=(0, 500),
    bins=25,
    linewidth=5,
    alpha=0.7,
    label='raw',
)
good_stations_stat.plot(
    kind='hist',
    y='time_spent',
    histtype='step',
    range=(0, 500),
    bins=25,
    linewidth=5,
    alpha=0.7,
    label='filtered',
    ax=ax,
    grid=True,
    legend=True,
)```

Мы вызвали не метод `plot()` с параметром `kind` (пер. «вид»), которому установили значение `kind='hist'`. Та же гистограмма, только её построил другой метод. Метод `plot()` умеет задействовать не поддерживаемые `hist()` параметры
![Plot|320x240](https://pictures.s3.yandex.net/resources/_6_1562613425.png)

-   `histtype` (от англ. the type of histogram _—_ «тип гистограммы»). В параметре указывают тип гистограммы, по умолчанию — это столбчатая (закрашенная). Значение `step` (пер. «шаг») чертит только линию.
-   `linewidth` (от англ. width of line _—_ «толщина линии»). Задаёт толщину линии графика в пикселях.
-   `alpha` (от термина «альфа-канал»). Назначает густоту закраски линии. 1 — это 100%-я закраска; 0 — прозрачная линия. С параметром 0.7 линии чуть прозрачны, так виднее их пересечения.
-   `label` (пер. «ярлык», «этикетка»). Название линии.
-   `ax` (от англ. axis _—_ «ось»). Метод `plot()` возвращает оси, на которых был построен график. Чтобы обе гистограммы расположились на одном графике, сохраним оси первого графика в переменной `ax`, а затем передадим её значение параметру `ax` второго `plot()`. Так, сохранив оси одной гистограммы и построив вторую на осях первой, мы объединили два графика.
-   `legend` (пер. «легенда»). Выводит легенду — список условных обозначений на графике. На графике вы можете найти её в верхнем правом углу.
-  `grid`  - «сетка, решётка»


### Урок 5. Добавляем столбец (продолжение)

df1['new'] = df2['d'] - объединение по индексам

Кажется просто: Pandas копирует столбец из data2 и вставляет его в data1 , однако всё сложнее. Для каждой строки первого датафрейма Pandas ищет «пару» — строку с таким же индексом во втором датафрейме. Находит и берёт значение из этой строки. В нашем случае индексы в data1 и data2 совпадали, и всё казалось простым копированием строк по порядку. Если же индексы не будут совпадать, например, в data2 не будет некоторых значений индекса data1 , то при копировании столбца на их месте будет значение NaN
Число строк в data2 не обязательно должно совпадать с числом строк data1 . Если в data2 не хватит значений, то будет None. А будут лишние — просто не попадут в обновлённый датафрейм. А вот повторяющиеся значения в индексе data2 приведут к ошибке. Pandas не поймёт, какое из значений следует подставить в data1 .

Если передавать столбцу список значений, сохранённых не как `Series`, а, например, как `list`, присвоение будет идти по порядку строк.
В случае со списком присвоение происходит по порядку строк, а в случае с `Series` — по совпадению индексов.
Поменяем индексы в `df2`. Вызовем метод `set_index()`, передадим ему название столбца, который заменит собой индекс: при этом пропадёт и сам столбец, и старый индекс. Метод `set_index()` не меняет исходный датафрейм, а возвращает обновлённый. Если же оригинальную таблицу нужно заменить, добавляют параметр `inplace=True`.

```python
df1 = pd.DataFrame({'a': [1, 2, 3, 3, 3], 
                    'b': ['Q', 'R', 'S', 'T', 'U']})
df2 = pd.DataFrame({'c': [3, 4, 5, 6, 7], 
                    'd': ['V', 'W', 'X', 'Y', 'Z'], 
                    'e': [3, 3, 3, 3, 3]})
df2.set_index('c', inplace=True)
print(df1)
print()
print(df2)
df1['new'] = df2['d']
print()
print(df1)
```

#### Урок 5. Задачи

Создайте в таблице `stat` новый столбец `good_time_spent` с медианной
```python
import pandas as pd

data = pd.read_csv('/datasets/visits.csv', sep='\t')

# фильтруем слишком быстрые и медленные заезды и АЗС
data['too_fast'] = data['time_spent'] < 60
data['too_slow'] = data['time_spent'] > 1000
too_fast_stat = data.pivot_table(index='id', values='too_fast')
good_ids = too_fast_stat.query('too_fast < 0.5')
good_data = data.query('id in @good_ids.index and 60 <= time_spent <= 1000')

# считаем данные по отдельным АЗС и по сетям
station_stat = data.pivot_table(index='id', values='time_spent', aggfunc='median')
good_stations_stat = good_data.pivot_table(index='id', values='time_spent', aggfunc='median')

stat = data.pivot_table(index='name', values='time_spent')
good_stat = good_data.pivot_table(index='name', values='time_spent', aggfunc='median')

stat['good_time_spent'] = good_stat['time_spent']

print(stat)
```


### Урок 6. Объединяем данные из двух таблиц
Когда нужно к существующему датафрейму добавить несколько новых столбцов, существует более лаконичный способ сделать это, по сравнению добавлением каждого столбца по очереди. Такая процедура называется объединение (`join`) или слияние (merge). Для слияния используем метод `merge()` , параметр `how` - метод объединения:
Если совпадут имена столбцов в data1 и data2 , то pandas переименует их, чтобы мы могли разобраться, где какое значение. К названию столбца из data1 в таком случае припишется _x , а к столбцу из data1 - _y . Вы можете самостоятельно задать, что приписать к названию столбцов, используя параметр suffixes=('_x','_y') (заменив '_x', '_y' на нужные вам окончания имён столбцов).
Отметим так же, что если столбец индекса именованный, то можно передать его имя в параметр on . Объединять можно не только по одному столбцу, но и по совпадению значений в нескольких столбцах — достаточно только передать список в on .

Cреднее по всем заездам или сначала по АЗС, а потом уже среднее из средних. Во втором случае среднее подскочило с 71 до 168 секунд, а медиана — с 60 до 180. Это утрированный пример, но в реальных задачах выбор метода усреднения может радикально поменять ваши выводы. Поэтому аналитику важно понимать как природу изучаемых данных, так и постановку задачи.

#### Урок 6. Задачи

Создайте переменную `id_name`, которая для каждой АЗС хранит информацию о названии сети и общем числе заездов. Из одинаковых названий сети выбирайте первое.
```python
import pandas as pd

data = pd.read_csv('/datasets/visits.csv', sep='\t')

# фильтруем слишком быстрые и медленные заезды и АЗС
data['too_fast'] = data['time_spent'] < 60
data['too_slow'] = data['time_spent'] > 1000
too_fast_stat = data.pivot_table(index='id', values='too_fast')
good_ids = too_fast_stat.query('too_fast < 0.5')
good_data = data.query('id in @good_ids.index and 60 <= time_spent <= 1000')

# считаем данные по отдельным АЗС и по сетям
station_stat = data.pivot_table(index='id', values='time_spent', aggfunc='median')
good_stations_stat = good_data.pivot_table(index='id', values='time_spent', aggfunc='median')

stat = data.pivot_table(index='name', values='time_spent')
good_stat = good_data.pivot_table(index='name', values='time_spent', aggfunc='median')
stat['good_time_spent'] = good_stat['time_spent']

id_name = good_data.pivot_table(index='id', values='name', aggfunc=['first', 'count'])

print(id_name.head())

```

### Урок 7. Переименование столбцов
В курсе «Базовый Python» для переименования столбцов вы использовали метод `rename()`. Мы рекомендуем использовать его в большинстве случаев. Однако если нужно переименовать все столбцы датафрейма, то можно воспользоваться атрибутом `columns`. Особенно в случае с мультииндексом.
Список, который передаётся в `columns`, должен иметь столько же элементов, сколько столбцов в датафрейме, и содержать как новые названия столбцов, так и старые в той последовательности, в которой столбцы расположены в таблице. Поэтому составлять такой список нужно осторожно — легко перепутать порядок или количество названий.
```python
# превращаем двухэтажные названия в одноэтажные в датафрейме df
# при этом переименовываем только второй столбец в 'column_2', 
# а первый оставляем со старым названием 'no_name'
df.columns = ['no_name', 'column_2']
```



#### Урок 7. Задачи
```python
import pandas as pd

data = pd.read_csv('/datasets/visits.csv', sep='\t')

# фильтруем слишком быстрые и медленные заезды и АЗС
data['too_fast'] = data['time_spent'] < 60
data['too_slow'] = data['time_spent'] > 1000
too_fast_stat = data.pivot_table(index='id', values='too_fast')
good_ids = too_fast_stat.query('too_fast < 0.5')
good_data = data.query('id in @good_ids.index and 60 <= time_spent <= 1000')

# считаем данные по отдельным АЗС и по сетям
station_stat = data.pivot_table(index='id', values='time_spent', aggfunc='median')
good_stations_stat = good_data.pivot_table(index='id', values='time_spent', aggfunc='median')

stat = data.pivot_table(index='name', values='time_spent')
good_stat = good_data.pivot_table(index='name', values='time_spent', aggfunc='median')
stat['good_time_spent'] = good_stat['time_spent']

id_name = good_data.pivot_table(index='id', values='name', aggfunc=['first', 'count']) #

id_name.columns = ['name', 'count']
print(id_name.head())
```

### Урок 8. Объединение столбцов методами merge() и join()
Методом `merge()` объединим строки датафреймов учеников по совпадающим значениям столбца `author`:

```PYTHON
`first_pupil_df.merge(second_pupil_df, on='author') # название столбца, по которому объединять, передают в параметре on`
```
Финальная таблица сложилась из совпадений по авторам записей первого и второго массива. Такой тип объединения называется `inner` (от англ. «внутренний», здесь значит «пересечение данных»). Он собирает данные из внутренней области (которые есть в обоих датафреймах). В `merge()` тип `inner` работает по умолчанию.
Ему противоположен тип слияния `outer` (от англ. «внешний», здесь значит «объединение данных»). Он объединяет данные из внешней общей области — такие, которые есть хотя бы в одном из датафреймов. Режим объединения задаётся параметром `how` (от англ. «как, каким образом»).
```python
first_pupil_df.merge(second_pupil_df, on='author', how='outer')
```
Режим объединения `'left'` указывает, что в результат слияния обязательно должны войти все строки из левого датафрейма:
```python
first_pupil_df.merge(second_pupil_df, on='author', how='left')
```
В аналогичном режиме `'right'` сохранятся все совпадающие строки и правый датафрейм.
Обратите внимание, что в таблице-результате работы метода `merge()` к названиям столбцов добавились `_x` и `_y`. Окончания названий столбцов задают в параметре `suffixes` (от англ. _suffix_ — «суффикс, окончание»):


```PYTHON
`first_pupil_df.merge(second_pupil_df, on='author', how='left', suffixes=('_записал первый', '_записал второй'))`
```
author | literary_work_записал первый | literary_work_записал второй
--- | --- | ---
Фонвизин | Недоросль | NaN
Если столбец индекса именованный, его имя также можно передать параметру `on`. Объединять можно и по нескольким столбцам сразу — достаточно передать список параметру `on`.
Метод `join()` похож на `merge()`. Без параметра `on` этот `join()` будет искать совпадения по индексам в первом и втором датафреймах. Если же передать параметру `on` столбец, то `join()` найдёт его в первом датафрейме и начнёт сравнивать с индексом второго. В отличие от `merge()`, по умолчанию в `join()` установлен тип слияния `how='left'`, в `merge()` по умолчанию `how='inner'`. А параметр `suffixes` разделён на два независимых: `lsuffix` (от англ. left suffix, «левый суффикс») и `rsuffix` (от англ. right suffix, «правый суффикс»). Ещё методом `join()` можно объединять больше двух таблиц: их набор передают списком вместо второго датафрейма.

```PYTHON
print (df1.join(df2, on='a', rsuffix='_y')['c'])
```

Каждому значению в столбце `'a'` первого датафрейма метод ищет соответствие в индексах второго датафрейма. И находит. В индексах второго датафрейма есть 1, 2 и 3. На экран выводят соответствующие им значения столбца `'c'`: F, G и H. В индексах второго датафрейма нет 4: `join()` не находит её и возвращает в итоговый столбец `NaN`.

#### Урок 8. Задачи
Нужно рассчитать медиану этих медиан по каждой сети. Это даст ещё один показатель «типичной» медианной длительности заездов в каждой сети: медиану распределения медианной длительности заездов на АЗС.
Создайте переменную `station_stat_full`, которая для каждой АЗС хранит название сети, число заездов и лучший показатель медианной длительности заправки. Подсказка: название сети и число заездов есть в `id_name`, а лучший показатель медианной длительности заправки — в `good_stations_stat`. Объедините эти две таблицы.
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

# name, counts, m_time
station_stat_full = id_name.join(good_stations_stat, on='id')

print(station_stat_full.head())

# постройте гистограмму числа заездов на 30 корзин. И гистограмму по тем же данным, с диапазоном от 0 до 300 заездов.
station_stat_full = id_name.join(good_stations_stat)
station_stat_full.hist('count', bins=30)
station_stat_full.hist('count', bins=30, range=(0, 300))

```

Не прибегая к вспомогательной переменной, сделайте срез данных из таблицы `station_stat_full` — так вы найдёте все строки, где число заездов больше 30. Для каждой сети рассчитайте медиану медианного времени заезда на АЗС, а также число АЗС, из которых складывается эта новая медиана. Сохраните результат в переменной `good_stat2`.
```
good_stat2 = station_stat_full.query('count > 30').pivot_table(index='name', values='time_spent', aggfunc=['median', 'count'])
good_stat2.columns = ['median_time', 'stations']
print(good_stat2.head())
```

### Заберите с собой

Чтобы ничего не забыть, [скачайте шпаргалку](https://code.s3.yandex.net/data-analyst/conspects/praktikum_data_analysis_takeaways_course3_theme3.pdf) и [конспект темы](https://code.s3.yandex.net/data-analyst/conspects/praktikum_data_analysis_abstract_course3_theme3.pdf).
### Где ещё почитать про объединение данных
[Аналитикам: большая шпаргалка по Pandas. Объединение датафреймов.](https://smysl.io/blog/pandas/#%D0%9E%D0%B1%D1%8A%D0%B5%D0%B4%D0%B8%D0%BD%D1%8F%D0%B5%D0%BC-%D0%BD%D0%B5%D1%81%D0%BA%D0%BE%D0%BB%D1%8C%D0%BA%D0%BE-%D0%B4%D0%B0%D1%82%D0%B0%D1%84%D1%80%D0%B5%D0%B9%D0%BC%D0%BE%D0%B2)

### [ТЕСТ](https://practicum.yandex.ru/trainer/data-scientist/lesson/2370febb-2b04-461e-a6b8-5987b6db179a/task/c958443d-49f7-44de-b594-7d0700027e6c/)
С помощью конструкции `'a in @our_series'` можно вывести три строки датафрейма. Такой код проверяет, равны ли значения столбца `a` значениям объекта `Series`: `2`, `11`, `12`. Вывести одну строку можно, проверив, совпадают ли значения `a` с индексами `our_series`: `0`, `1`, `2`. Совпадает только строка, в которой значение `a` равно `2`.

Добавляя новый столбец, вы не просто копируете и вставляете его в датафрейм. В `pandas` для каждой строки первого датафрейма будет подобрана строка с таким же индексом во втором датафрейме. Присвоение значений происходит только в случае, если индексы совпадают. У датафреймов `df_old` и `df_new` общих индексов нет, поэтому в столбец `new` войдут только `NaN`.