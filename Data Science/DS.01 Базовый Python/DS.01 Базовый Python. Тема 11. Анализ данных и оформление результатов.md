# DS.01 Базовый. Тема 11. Анализ данных и оформление результатов 

Компании по-разному оценивают реакцию пользователя на обновления. Но чаще всего оценивают пять метрик HEART модели:

* **Happiness** — счастье. Например, высокая оценка приложения от пользователя;
* **Engagement** — вовлечённость. Например, количество действий, которые пользователь совершает за единицу времени.
* **Adoption** — принятие сервиса. Например, нового обновления.
* **Retention** — удержание. Например, сколько раз пользователь открывал приложение за единицу времени.
* **Task success** — буквально, «успех задач». Эта метрика показывает, оправдываются ли ожидания пользователя от сервиса.

  

```python

import pandas as pd 
df = pd.read_csv('music_log.csv') 
print(df.head(15))  выведет первые 15 строк таблицы 
 подсчёт пропусков в данных
print(df.isna().sum()) 
 подсчёт дубликатов
print(df.duplicated().sum())
```  

### Тема 11. Урок 3. Лабораторка - Яндекс Музыка: работа с предобработанными данными

  
```python
import pandas as pd
df = pd.read_csv('music_log_upd.csv')
#print(df.columns) # выводим названия столбцов
na_number = 0
#for column in df.columns:
na_number += df[column].isna().sum()
na_number = df.isna().sum()
print(na_number)
```  

### Тема 11. Урок 4. Группировка данных

Стадии группировки выражают **формулой** split-apply-combine_:_

* **разделить**, split — сначала данные разбивают на группы по определённому критерию;
* **применить**, apply — затем к каждой группе применяют методы вычисления, например: считают элементы группы методом `count()` или их суммы методом `sum()`;
* **объединить**, combine — наконец, результаты сводят в новую структуру данных, таблицу или `Series`.

```python

print(exoplanet.groupby('discovered').count())

exo_number = exoplanet.groupby('discovered')['radius'].count()

print(exo_number)

exo_radius_sum = exoplanet.groupby('discovered')['radius'].sum()

print(exo_radius_sum)

exo_radius_mean = exo_radius_sum/exo_number

print(exo_radius_mean)
```

### Тема 11. Урок 5. Лабораторка - Яндекс Музыка: группировка данных


```python

import pandas as pd
df = pd.read_csv('music_log_upd.csv')
track_grouping = df.groupby('user_id')['genre_name']

def user_tracks(group):
	for col in group:
		if len(col[1]) > 50:
			user = col[0]
			return user

search_id = user_tracks(track_grouping)
print(search_id)

#print(df[df['user_id'] == search_id])
```  

### Тема 11. Урок 6. Сортировка данных pandas

```python
print(exoplanet.sort_values(by='radius').head(30)) # отсортируем по радиусу

print(exoplanet[exoplanet['radius'] < 1]) # отфильтруем по радиусу

print(exoplanet[exoplanet['discovered'] == 2014]) # отфильтруем по году
```

Если нужно отсортировать таблицу по какому-либо столбцу, не забудьте указать название столбца при вызове функции. В методе `sort_values()` для этого есть параметр `by`. Но если вы применяете метод к объекту `Series`, то есть к одному столбцу, аргумент указывать не нужно.

```python

#экзопланеты меньше Земли и ещё открытые в 2014 году
exo_small_14 = exoplanet[exoplanet['radius'] < 1]
exo_small_14 = exo_small_14[exo_small_14['discovered'] == 2014]
print(exч, ascending=False)) 
exo_small_14 = exo_small_14.sort_values(by='radius', ascending=False)
```  

### Тема 11. Урок 7. Лабораторка - Яндекс Музыка: сортировка данных

```python

import pandas as pd
df = pd.read_csv('music_log_upd.csv')

genre_grouping = df.groupby('user_id')['genre_name']

def user_genres(group):
    for col in group:
        if len(col[1]) > 50:
            user = col[0]
            return user

search_id = user_genres(genre_grouping)

music_user = df[df['user_id'] == search_id]
music_user = music_user[music_user['total_play_seconds'] != 0]
#print(music_user)

sum_music_user = music_user.groupby('genre_name')['total_play_seconds'].sum() 
#print(sum_music_user)

count_music_user = music_user.groupby('genre_name')['genre_name'].count() 

final_sum = sum_music_user.sort_values(ascending=False) #by='genre_name', 
final_count = count_music_user.sort_values(ascending=False) #by='genre_name', 

print(final_count)
```  

### Тема 11. Урок 8. Описательная статистика

```python
#показать максимальное значение:
print(df['total_play_seconds'].max())

#вывести строку с максимальным значением:
print(df[df['total_play_seconds'] == df['total_play_seconds'].max()])

#отфильтровать нулевые значения и вывести минимум из ненулевых:
df_drop_null = df[df['total_play_seconds'] != 0]

print(df_drop_null['total_play_seconds'].min())

#вывести строку с минимальным значением:
print(df_drop_null[df_drop_null['total_play_seconds'] == df_drop_null['total_play_seconds'].min()])

#вывесли последнюю строку:
df_stat_1 = df.tail()

print(df_stat_1['total_play_seconds'].sort_values())

df_stat = df.tail(4)

print(df_stat['total_play_seconds'].sort_values())

#получим медиану
print(df_stat['total_play_seconds'].median())

df_drop_null = df[df['total_play_seconds'] != 0]

print(df_drop_null['total_play_seconds'].median())

#найдём среднюю
print(df_drop_null['total_play_seconds'].mean())

```

### Тема 11. Урок 9. Лабораторка - Яндекс Музыка: описательная статистика

```python

import pandas as pd
df = pd.read_csv('music_log_upd.csv')

#df.info()
temp_df = df[df['genre_name'] == 'pop'] 
pop_music = temp_df[temp_df['total_play_seconds'] != 0] 
#print(pop_music.tail(2))
#pop_music.info()
#print()
pop_music_max_total_play = pop_music['total_play_seconds'].max()
#print(pop_music_max_total_play)
pop_music_max_info = df[df['total_play_seconds'] == pop_music_max_total_play]
#print(pop_music_max_info)

pop_music_min_total_play = pop_music['total_play_seconds'].min()
#print(pop_music_min_total_play)
pop_music_min_info = pop_music[pop_music['total_play_seconds'] == pop_music_min_total_play]
#print(pop_music_min_info)
pop_music_median = pop_music['total_play_seconds'].median()
#print(pop_music_median)
pop_music_mean = pop_music['total_play_seconds'].mean()
print(pop_music_mean)
```  

### Тема 11. Урок 10. Лабораторка - Яндекс Музыка: решение кейса и оформление результатов
  
 1. взять последние 5 строк
```python
df.tail()
```

 2. Группируете по пользователю:
```python
df.tail().groupby('user_id')
```

 3. Считаете общее время прослушивания музыки:
```python
df.tail().groupby('user_id').sum()
```

 4. Находите медианное значение для суммы прослушиваний по пользователю:
```python
print(df.tail().groupby('user_id').sum().median())
```

Аналитики и специалисты по data science показывают свою работу нетехническим специалистам: проджектам, маркетологам, топ-менеджерам. Они могут не владеть терминологией. Поэтому ваш отчёт, не теряя в содержательности, должен быть доступен широкой аудитории без подробных комментариев.

**!!! есть правила, которые стоит соблюдать.

* Показывая, как меняется какой-нибудь параметр во времени, поместите его значения в строке, а столбцами задавайте временные промежутки.
* Если нужно показать разнородные признаки для конкурирующих категорий (например для жанров), то каждой категории отведите отдельную строку, а значения признаков размещайте по столбцам.

* Не старайтесь обязательно собрать все данные в одну таблицу: лучше несколько таблиц, чтобы каждая отражала одну важную идею.
* Отлично работает детализация от большего к меньшему. К общей сводной таблице прилагайте более подробные. Например, сначала обзорная таблица по всему сервису, затем более детальные: сводки по группам пользователей, по городам и т. п.
* Проявите заботу о коллегах — старайтесь оформлять результаты наглядно и понятно.

  
### Найти медиану вовлечённости по времемени объединяя пользователей

```python

import pandas as pd
df = pd.read_csv('music_log_upd.csv')
#engagement = df.tail()

engagement = df.groupby('user_id').sum()

current_engagement = df.groupby('user_id').sum().median()
print(current_engagement)
```  

### Заменить в списке значения медианы прослушивания до и после эксперимента

```python

import pandas as pd
exp = [['engagement', 0, 0, 0]]
columns = ['metrics','before_test','after_test','absolute_difference']

metrics = pd.DataFrame(data=exp,columns=columns)
#print(metrics)
#metrics.loc[0, 'before_test'] = 57.456
#metrics.loc[0, 'after_test'] = 62.344431
#metrics.loc[0, 'absolute_difference'] = metrics.loc[0, 'after_test'] - metrics.loc[0, 'before_test']
exp[0][1] = 57.456
exp[0][2] = 62.344431
exp[0][3] = exp[0][2] - exp[0][1]
print(exp)

```

### Найти минимум и максимум времени для другого жанра

```python

import pandas as pd
df = pd.read_csv('music_log_upd.csv')

#введите здесь решение для поиска недостающих данных&gt;
genre_rock = df[df['genre_name'] == 'rock'] 
genre_rock = genre_rock[genre_rock['total_play_seconds'] != 0] 

 максимальное время прослушивания в жанре рок
genre_rock_max = genre_rock['total_play_seconds'].max()
print(f'Максимальное время прослушивания в жанре рок равно: {genre_rock_max}')

 минимальное время прослушивания в жанре рок
genre_rock_min = genre_rock['total_play_seconds'].min()
print(f'Минимальное время прослушивания в жанре рок равно: {genre_rock_min}')