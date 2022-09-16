# [DS.01 Базовый Python. Тема 13. Проект: музыка больших городов](https://practicum.yandex.ru/trainer/data-scientist/lesson/5071c53b-4b04-485d-9240-ce3f435e69da/)

Данные хранятся в файле `yandex_music_project.csv`. На платформе он находится по пути `/datasets/yandex_music_project.csv`. Скачать датасет для работы с ним вне проекта можно [здесь](https://code.s3.yandex.net/datasets/yandex_music_project.csv): [https://code.s3.yandex.net/datasets/yandex_music_project.csv](https://code.s3.yandex.net/datasets/yandex_music_project.csv).

**Правило** - Считайте значения по колонкам
```python

# хорошо
df.groupby('city')['genre'].count()
df[df['city'] == 'Moscow']['user_id'].count()

# хуже
df.groupby('сity').count()
df[df['city'] == 'Moscow'].count() 
```
  
```python

# подсчёт в датафрейме после очистки от пропусков и группировки
df.groupby('сity').count()
```
  
```python

# выберем столбец genre после группировки 
df.groupby('city')['genre'].count() 
```

В тетрадке Jupyter по-разному выводите на экран разные типы данных:

* датафреймы и `Series` — функцией `display()`;
* любые другие данные — функцией `print()`.
 
**Правило** - Изменяйте переменные
Когда меняете данные из переменной, уточняйте: понадобятся ли исходные данные в будущем.
* Если больше не понадобятся, измените их и запишите в ту же переменную.
* Если понадобятся — сохраните изменения в новую переменную.
```python
# хорошо
filtered_df = df[df['city'] == 'Moscow']
filtered_df = filtered_df[filtered_df['genre'] == 'pop']
filtered_df = filtered_df[filtered_df['total_play'] > 10.0]

# хуже
filtered_df = df[df['city'] == 'Moscow']
temp = filtered_df[filtered_df['genre'] == 'pop']
one_more_temp = temp[temp['total_play'] > 10.0]
one_more_temp 
```

```python
# хорошо
first_genres = df['genres'][:10]

# хуже
first_genres = df['genres'][0:10] 
```

* Постановка задачи
* Получение данных
* Предобработка данных
* Анализ данных
* Оформление результатов
  

### Тема 13. Урок 4. Лабораторка - Тетрадь исследователя.

**исследование пройдёт в три этапа:
* Обзор данных.
* Предобработка данных.
* Проверка гипотез.