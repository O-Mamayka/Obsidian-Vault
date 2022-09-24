## [DS.02 Предобработка данных. Тема 5. Категоризация данных](https://practicum.yandex.ru/trainer/data-scientist/lesson/695fdcbb-7aaf-446f-a86c-e37172861ca4/)

Если категориальный статус хранится в таблице в виде строк разной длины, такой способ хранения приводит к:

* Усложняется визуальная работа с таблицей.
* Увеличивается размер файла и время обработки данных.
* Чтобы отфильтровать данные по типу обращения, приходится набирать его полное название. А в нём можно ошибиться.
* Создание новых категорий и изменение старых отнимает много времени.

Предупредить появление этих проблем можно. Создать отдельный «словарь», где названию категории будет соответствовать номер. И в будущих таблицах обращаться уже не к длинной строке, а к её числовому обозначению.

!!! В категоризацию данных на этапе предобработки входит: Объединение числовых значений в группы-диапазоны. Когда учились заполнять пропуски в данных, определяли тип значений в столбце: количественный или категориальный. Некоторые количественные значения можно объединить в группы, например значение возраста. Такие группы проще анализировать. Обратите внимание, что количественное значение возраста в этом случае станет категориальным. Поэтому такое объединение данных и называют категоризацией.

Одна таблица хуже справится с большим объёмом информации, поэтому лучше разделять данные на небольшие сегменты. Это значительно упростит работу и позволит избежать ошибок.

  
```Python
print(rest_log.groupby('id').mean().sort_values('rating',ascending=False).head(10))
```
  

### Урок 3. Классификация по типу. Лабораторка:

Уточните, сколько раз встречается каждый тип обращении
```Python
import pandas as pd

support = pd.read_csv('/datasets/support_upd.csv')

#print(support['type_message'].value_counts())

support_log = support[support.columns[[0,2,3]]]

print(support_log.head(10))

support_dict = support[support.columns[[1,2]]]

print(support_dict.head(10))

support_dict = support_dict.drop_duplicates().reset_index(drop=True) #заменит старые индексы

print(support_dict.sort_values(by='type_id', ascending=True))
```
  

### Урок 4. Классификация по группам. Лабораторка:

```Python

import pandas as pd
clients = pd.read_csv('stats_by_age.csv')
print(clients.head()) 
print(clients['age'].value_counts())
```
  

Работать с единичными отрывками и делать из них статистические выводы нельзя. Значит, нужно сгруппировать данные, чтобы численности каждой группы хватало для формулировки выводов. Нужна **категоризация** — объединение данных в категории. Например так: Клиенты **до 18** лет включительно попадают в категорию «**дети**»; Клиенты **от 19 до 64** лет — категория «**взрослые**»;

```Python

def age_group(age):
    """
    Возвращает возрастную группу по значению возраста age, используя правила:
    - 'дети', если age <= 18 лет;
    - 'взрослые', если age от 19 до 64;
    - 'пенсионеры' — от 65 и старше.
    """
    
    if age <= 18:
        return 'дети'
    if age <= 64:
        return 'взрослые'
    return 'пенсионеры' 
print(age_group(14))
```
  

Осталось создать отдельный столбец с возрастными категориями, и в его ячейках записать значения, возвращаемые функцией. Для этого нужен метод `apply()`: он берёт значения столбца датафрейма и применяет к ним функцию из своего аргумента. Здесь `apply()` следует вызвать для столбца `AGE`, так как в нём содержатся данные, которые функция примет на вход. Аргументом метода станет сама функция `age_group`.

```Python

clients['age_group'] = clients['age'].apply(age_group)
print(clients.head(10)) 
print(clients['age_group'].value_counts())
```
  

Также методом `apply()` можно создать столбец на основе данных из нескольких других столбцов.

Допустим, нужно сделать новый столбец с полным именем клиента. Напишем функцию, которая принимает строку датафрейма как аргумент `row`. Строка таблицы — это объект `Series`, поэтому в теле функции можно обратиться к отдельным её ячейкам.

Когда метод `apply()` оперирует данными из нескольких столбцов, его вызывают ко всему датафрейму. В таком случае он принимает не только название функции, но и параметр `axis`: со значением 1, чтобы применить метод ко всем строкам датафрейма, и со значением 0 — ко всем столбцам.

Метод `apply()` позволяет применить функцию к каждой строке датафрейма без цикла. В pandas перебор строк циклами — это неоптимальный путь, «сжирающий» время и память.

```Python

def make_full_name(row):
    """
    Возвращает полное имя (сочетание имени и фамилии)
    """
    full_name = row['first_name'] + ' ' + row['last_name']
    return full_name 
clients['full_name'] = clients.apply(make_full_name, axis=1)
print(clients.head(10))
```
  

### Лабораторка:
```Python
import pandas as pd

support_log = pd.read_csv('/datasets/support_log.csv')

support_log_grouped = support_log.groupby('type_id')['type_id'].count()

print(support_log_grouped)

def alert_group(messages):
    if messages <= 300:
        return 'средний'
    elif ((messages > 300) and (messages <= 500)):
        return 'высокий'
    elif messages > 500:
        return 'критичный'

print(alert_group(10))
print(alert_group(450))
print(alert_group(1000))

#добавим в таблицу новое поле с критерием важности_
support_log_grouped['alert_group'] = support_log_grouped['user_id'].apply(alert_group)

print(support_log_grouped.head(10))

#подсчитаем сколько обращений по каждому приоритету_
alert_count = support_log_grouped.groupby('alert_group')['user_id'].sum()

print(alert_count)
```
  

### Урок 5. Функция для одной строки.

Если критериев для категоризации несколько, то задача немного усложняется. Например, теперь необходимо поделить «взрослых» на занятых и безработных. Разработчики добавили новый столбец `['unemployed']`, где значение 1 означает, что у клиента нет работы, а значение 0 — что работа есть.

Правила распределения клиентов по категориям перестали зависеть только от возраста:

* Клиенты от 19 до 64 лет при наличии работы — категория «занятые»;
* Клиенты от 19 до 64 лет без работы — «безработные»;

принимают во внимание значения двух столбцов: возраста `['age']` и занятости `['unemployed']`. Чтобы функция учитывала несколько столбцов датафрейма, в качестве аргумента ей передают всю строку целиком.

```Python

import pandas as pd
clients = pd.read_csv('/datasets/stats_by_age_employment.csv')
def age_group_unemployed(row):
"""
Возвращает возрастную группу по значению возраста age и занятости unemployed, используя правила:
- 'дети' при значении age <= 18 лет
- 'безработные' при значении age от 19 до 64 лет включительно и значении unemployed = 1
- 'занятые' при значении age от 19 до 64 лет включительно и значении unemployed = 0
- 'пенсионеры' во всех остальных случаях
"""
    age = row['age']
    unemployed = row['unemployed']
    if age <= 18:
        return 'дети'
    if age <= 64:
        if unemployed == 1:
            return 'безработные'
        return 'занятые'
    return 'пенсионеры'
```
  

на входе не только возраст, но и занятость, значит, для проверки нужно передавать целую строку датафрейма с этими значениями

```Python
#Создают два списка. В одном — значения, в другом — названия столбцов датафрейма.
row_values = [24, 1] #значения возраста и занятости 
row_columns = ['age', 'unemployed'] #названия столбцов 
#Формируют строку:
row = pd.Series(data=row_values, index=row_columns)  
#!! Передаём строку в качестве аргумента функции для тестирования:
age_group_unemployed(row)
```
  

Осталось создать новый столбец `clients['age_group']` со значениями-результатами работы функции `age_group_unemployed()`. Вызовем метод `apply()`, однако с двумя важными отличиями от прошлого примера:

1) Метод `apply()` применяем не к столбцу `clients['age']`, а к датафрейму `clients`.

2) По умолчанию Pandas передаёт в функцию `age_group_unemployed()` столбец. Чтобы на вход в функцию отправлялись строки, нужно указать параметр `axis = 1` метода `apply()`.

С учётом этих двух замечаний новый столбец `age_group` формируется так:

```Python
clients['age_group'] = clients.apply(age_group_unemployed, axis=1)
```

```Python
#Проверяем:
clients['age_group'] = clients.apply(age_group_unemployed, axis=1)
print(clients.head(10)) 
#Применим метод value_counts() для подсчёта значений каждой категории.
print(clients['age_group'].value_counts())
```
  
### Лабораторка:
```Python
import pandas as pd
support_log_grouped = pd.read_csv('/datasets/support_log_grouped.csv')

def alert_group_importance(row):

	importance = row['importance']
	
	alert_group = row['alert_group']
	
	if importance == 1:
	
		if alert_group == 'средний':
		
			return 'обратить внимание'
		
		elif alert_group == 'высокий':
		
			return 'высокий риск'
		
		elif alert_group == 'критичный':
		
			return 'блокер'
	
	return 'в порядке очереди'
```
  
```Python
row_values = ['высокий', 1]
row_columns = ['alert_group', 'importance']

#Формируем Series из значений row_values и row_columns
row = pd.Series(data=row_values, index=row_columns)

#print(alert_group_importance(row))

#Формируем новый столбец функцией
support_log_grouped['importance_status'] = support_log_grouped.apply(alert_group_importance, axis=1)

#Выводим новый столбец сгруппированный и упорядоченный value_counts
print(support_log_grouped['importance_status'].value_counts())
```

**Выражение следующего вида применит функцию к каждой строке:
```Python
clients_df['age_category'] = clients_df.apply(categorize_age, axis=1)
```

Таблица в `pandas` — двумерный объект. У него есть две координаты: строка и столбец. Перебирать элементы в цикле не стоит — это неоптимальный путь, который займёт много времени. Выбором строки или столбца управляет параметр `axis`. Чтобы применить метод к строкам, в аргументе указывают `axis` со значением `1`.

Параметр `axis` позволит применить код к нужным элементам: строкам или столбцам

axis=1, если нужно применить функцию к строкам
axis=0, если нужно применить функцию к столбцам


# ШПОРЫ?

  

  

  

  

  

  

  

  

  

  

  

  

Чтобы ничего не забыть, скачайте [шпаргалку](https://code.s3.yandex.net/data-analyst/praktikum_data_analysis_takeaways_course2_theme4.pdf) и [конспект](https://code.s3.yandex.net/data-analyst/praktikum_data_analysis_abstract_course2_theme4.pdf) темы.

### Где ещё почитать про категоризацию данных

[Полезные приёмы библиотеки _Pandas_](https://proglib.io/p/pandas-tricks/)