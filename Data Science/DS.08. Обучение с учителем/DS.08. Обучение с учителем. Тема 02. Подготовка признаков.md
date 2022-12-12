## [Тема 02. Подготовка признаков](https://practicum.yandex.ru/trainer/data-scientist/lesson/8f9b117d-f605-49f5-a750-e7192503e8ba/)
В задачах машинного обучения к анализу готовят не только данные, но ещё и признаки.
-   Преобразовывать категориальные признаки прямым кодированием, чтобы обучить логистическую регрессию.
-   Выполнять порядковое кодирование категориальных признаков для обучения решающего дерева.
-   Улучшать метрики качества, масштабируя признаки.
#### Постановка задачи
Подготовим данные для обучения модели, которая предскажет: обратится клиент за страховой выплатой или нет.

**Признаки, с которыми будем работать:**
-   _Agency_ — название страхового агентства
-   _Agency Type_ — тип страхового агентства
-   _Distribution Channel —_ канал продвижения страхового агентства
-   _Product Name_ — название страхового продукта
-   _Duration_ — длительность поездки (количество дней)
-   _Destination_ — направление поездки
-   _Net Sales_ — сумма продаж ($)
-   _Commission_ — комиссия страхового агентства ($)
-   _Gender_ — пол застрахованного
-   _Age_ — возраст застрахованного

**Целевой признак:**
-   _Claim_ (англ. «претензия») — потребовалась ли страховая выплата: «да» — 1, «нет» — 0

### [Урок 2 Загрузка данных](https://practicum.yandex.ru/trainer/data-scientist/lesson/4e7b78f4-5104-4785-905f-830091b9c50d/task/3a2bca8e-1d2a-4f8d-b9d1-13f688906230/)

Доходы от взносов клиентов значительно превышают расходы на страховые выплаты. Компании рассчитывают, что за компенсацией по страховому полису обратится малая доля клиентов. А большей части — страховка, например, в путешествии и вовсе не пригодится. Историческая статистика показывает: только 1% клиентов запрашивает страховую выплату. Как спрогнозировать, потребуется она застрахованному или нет?
#### Урок 2. Задача 1
Загрузите данные из файла `/datasets/travel_insurance.csv` в переменную `data`. Распечатайте первые десять элементов на экране. Изучите данные.
#### Урок 2. Задача 2
Разбейте исходные данные на две выборки:
-   обучающую _(train);_
-   валидационную _(valid)_. Это 25% исходных данных. Установите параметр _(random_state)_ равным 12345. Объявите четыре переменные и запишите в них:
	-   признаки: _features_train, features_valid;_
	-   целевой признак: _target_train, target_valid._
Выведите на экран размеры таблиц, которые хранятся в переменных: _features_train_ и _features_valid._

```python
import pandas as pd
from sklearn.model_selection import train_test_split
data = pd.read_csv('/datasets/travel_insurance.csv')

features = data.drop('Claim',axis=1)
target = data['Claim']

features_train,features_valid, target_train, target_valid = train_test_split(features,target,test_size=0.25, random_state=12345)
print(features_train.shape)
print(features_valid.shape)
```
`(37995, 10)` `(12665, 10)`

### [Урок 3 Пробное обучение](https://practicum.yandex.ru/trainer/data-scientist/lesson/98263cf7-b939-4e6b-b9bb-b8474c4a7336/task/0fa5fc6e-a9e5-44ee-afa5-530a650b03b3/)

Чтобы предсказать класс, обратимся к знакомой логистической регрессии.
Логистическая регрессия подходит для задачи классификации. Например, как у нас, когда выбор между двумя категориями — потребуется страховая выплата или нет.
Попробуем обучить нашу модель. 
```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
data = pd.read_csv('travel_insurance.csv')

train, valid = train_test_split(data, test_size=0.25, random_state=12345)

features_train = train.drop('Claim', axis=1)
target_train = train['Claim']
features_valid = valid.drop('Claim', axis=1)
target_valid = valid['Claim']

model = LogisticRegression()
model.fit(features_train, target_train) 
```
`ValueError: could not convert string to float: 'M'`
Теперь можете сказать: «А я говорил!» Действительно, ошибка.
Принадлежность к категории логистическая регрессия вычисляет по формуле, состоящей из признаков. Они могут быть только численные. Наши данные содержали и категориальные признаки тоже — в этом и была ошибка.
#### Урок 3. Задача 1
Проверьте, признаки какого типа хранятся в таблице. Выведите их на экран. Затем напечатайте первые пять значений столбца _Gender_.
Чтобы получить информацию о типах данных в таблице, используйте атрибут _dtypes._
Выведите первые пять значений столбца _Gender_ методом _head()._
```python
import pandas as pd
data = pd.read_csv('/datasets/travel_insurance.csv')
print(data.dtypes)
print(data.Gender.head(5))
```

### [Урок 4 Прямое кодирование](https://practicum.yandex.ru/trainer/data-scientist/lesson/c29ff40a-c7ea-4b7e-8ade-f146ab148f64/task/ed8771f3-3cfc-4d99-9fec-ec71517f01ef/)
Преобразовать категориальные признаки в численные поможет техника **прямого кодирования**, или **отображения** (англ. _One-Hot Encoding_, _OHE_).
Принцип работы _One-Hot Encoding_ объясним на значениях признака _Gender._

#### Урок 4. Задача 1
Преобразуйте колонку _Gender_ техникой _OHE_. Вызовите функцию _pd.get_dummies()_ и напечатайте на экране первые пять записей изменённой таблицы.
```python
import pandas as pd
data = pd.read_csv('/datasets/travel_insurance.csv')
print(pd.get_dummies(data.Gender)[:5])
```

### [Урок 5 Дамми-ловушка](https://practicum.yandex.ru/trainer/data-scientist/lesson/1a12f545-1027-495f-90d4-8e9a6666e99e/task/90c4320d-c35a-4064-986a-82ad39bb41a6/)
С прямым кодированием не всё так просто. Когда данных в избытке, можно угодить в ловушку фиктивных признаков. Расскажем, как в неё не попасть.
Чтобы подать документы на шенгенскую визу, нужно доказать, что деньги у вас есть. Вы решили перестраховаться, поэтому взяли и выписку с банковского счёта, и справку с работы, и 2-НДФЛ. Хотя визовому центру достаточно двух документов. Вашей модели лишняя информация тоже не очень-то нужна. Если оставить всё как есть, обучаться она будет сложнее.
В таблицу добавились три новых столбца. Поскольку они сильно связаны между собой, один удалим без сожаления. Восстановить столбец можно по оставшимся двум. Так мы не попадём в **дамми-ловушку** (англ. _dummy trap_, «ловушка фиктивных признаков»).
Столбец уберём вызовом функции _pd.get_dummies()_ с аргументом **drop_first** (от англ. «сбросьте первый»). Он удаляет первую колонку и передаётся как `drop_first=True` или `drop_first=False` (_True_ — первый столбец сбрасывается, _False_ — не сбрасывается).
Обучая логистическую регрессию, вы можете столкнуться с предупреждением библиотеки _sklearn._ Чтобы его отключить, укажите аргумент `solver='liblinear'` (англ. _solver_ «алгоритм решения»; _library linear_, «библиотека линейных алгоритмов»):
```python
model = LogisticRegression(solver='liblinear') 
```
#### Урок 5. Задача 1
Преобразуйте колонку _Gender_ техникой _OHE._ Чтобы не попасть в дамми-ловушку, примените аргумент _drop_first_ функции _pd.get_dummies()._ Напечатайте первые пять записей изменённой таблицы.
Чтобы избежать дамми-ловушки, укажите значение аргумента `drop_first=True`.
```python
import pandas as pd
data = pd.read_csv('/datasets/travel_insurance.csv')
#print(pd.get_dummies(data. Gender,drop_first=True)[:5])
# drop_first = True - удаление первого столбца (избегая дамми-ловушки)
print(pd.get_dummies(data. Gender,drop_first=True).head())
```
#### Урок 5. Задача 2
Примените прямое кодирование ко всему датафрейму. Вызовите функцию _pd.get_dummies()_ c аргументом _drop_first._ Сохраните таблицу в переменной _data_ohe._
Выведите на экран первые три строки преобразованной таблицы.
```python
import pandas as pd
data = pd.read_csv('/datasets/travel_insurance.csv')
data_ohe = pd.get_dummies(data, drop_first=True)
print(data_ohe.head(3))
```
#### Урок 5. Задача 3
Разбейте исходные данные на две выборки в соотношении 75:25 (%):
-   обучающую (`train`);
-   валидационную (`valid`).
Объявите четыре переменные и запишите в них:
-   признаки: `features_train`, `features_valid`;
-   целевой признак: `target_train`, `target_valid`.
Вам предстоит освоить альтернативный способ работы с функцией `train_test_split()`: когда на вход подаются две переменные (признаки и целевой признак). Поработайте с документацией.
Обучите логистическую регрессию. Напечатайте на экране текст `"Обучено!"` (уже в прекоде). Так вы убедитесь, что код выполнился без ошибок.
Вложите и в `train_test_split()`, и в `LogisticRegression()` параметр `random_state`, равный `12345`
```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
data = pd.read_csv('/datasets/travel_insurance.csv')

data_ohe = pd.get_dummies(data, drop_first=True)
target = data_ohe['Claim']
features = data_ohe.drop('Claim', axis=1)

features_train, features_valid,target_train, target_valid = train_test_split(features,target, test_size=0.25, random_state=12345)
model = LogisticRegression(random_state=12345, solver='liblinear')
model.fit(features_train,target_train)
print("Обучено!")
```

### [Урок 6 Порядковое кодирование](https://practicum.yandex.ru/trainer/data-scientist/lesson/19d5dccc-3ac7-4df6-8431-7d07f3fab34f/task/80b6fb0b-cf59-4eda-abdc-50fe32f98ce7/)

Расскажем о другой технике кодирования признаков в решающем дереве и случайном лесе.
Если решающее дерево задаёт вопросы в узлах, значит, может работать и с категориальными признаками?
![image|480](https://pictures.s3.yandex.net/resources/otel_1574013602.jpg)
```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
data = pd.read_csv('travel_insurance.csv')
target = data['Claim']
features = data.drop('Claim', axis=1)
features_train, features_valid, target_train, target_valid = train_test_split(
features, target, test_size=0.25, random_state=12345)

tree = DecisionTreeClassifier(random_state=12345)
tree.fit(features_train, target_train) 
```
`ValueError: could not convert string to float: 'EPX' `
Опять ошибка. Вызвана тем, как решающее дерево обучается в библиотеке _sklearn_.
Нужна новая техника, чтобы закодировать цифрами выраженные в тексте категории — **Ordinal Encoding** (от англ. «кодирование по номеру категории»). Она работает так:
1.  Фиксируется, какой цифрой кодируется класс;
2.  Цифры размещаются в столбце.
Техника подходит для преобразования признаков в решающем дереве и случайном лесе (он состоит из деревьев).
![image|480](https://pictures.s3.yandex.net/resources/Ordinal_1574013624.jpg)
Чтобы выполнить кодирование, в _sklearn_ есть структура данных **OrdinalEncoder** (англ. «порядковый кодировщик»). Она находится в модуле **sklearn.preprocessing** (от англ. «предобработка»).
Импортируем _OrdinalEncoder_ из библиотеки:
```python
from sklearn.preprocessing import OrdinalEncoder 
```
Преобразование выполняется в три этапа:
1.  Создаём объект этой структуры данных. `encoder = OrdinalEncoder() `
2.  Чтобы получить список категориальных признаков, вызываем метод _fit()_ — как и в обучении модели. Передаём ему данные как аргумент.  `encoder.fit(data) `
3.  Преобразуем данные функцией **transform()** (англ. «преобразовать»). Изменённые данные будут храниться в переменной _data_ordinal (англ. «порядковые данные»)._ `data_ordinal = encoder.transform(data) `
Чтобы код добавил названия столбцов, оформим данные в структуру _DataFrame():_
`data_ordinal = pd.DataFrame(encoder.transform(data), columns=data.columns) 
Если преобразование признаков требуется лишь один раз, как в нашей задаче, код можно упростить вызовом функции **fit_transform()** (от англ. «подогнать и преобразовать»). Она объединяет функции: _fit()_ и _transform()._
`data_ordinal = pd.DataFrame(encoder.fit_transform(data), columns=data.columns) `

#### Урок 6. Задача 1
Преобразуйте признаки техникой _Ordinal Encoding._ Импортируйте _OrdinalEncoder_ из модуля _sklearn.preprocessing._
Сохраните результат в переменной _data_ordinal_. Оформите данные в структуру _DataFrame()_.
Напечатайте на экране первые пять строк таблицы (уже в прекоде).
```python
import pandas as pd
from sklearn.preprocessing import OrdinalEncoder
data = pd.read_csv('/datasets/travel_insurance.csv')

Encoder = OrdinalEncoder()
data_ordinal = pd.DataFrame(Encoder.fit_transform(data), columns = data.columns)
print(data_ordinal.head())
```

#### Урок 6. Задача 2
Обучите решающее дерево на преобразованных данных. Напечатайте на экране текст `"Обучено!"`. Так вы убедитесь, что код выполнился без ошибок.
Создайте модель _DecisionTreeClassifier_, задайте аргумент `random_state=12345`_._
Обучите модель вызовом функции _fit()_.
```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import OrdinalEncoder
data = pd.read_csv('/datasets/travel_insurance.csv')

encoder = OrdinalEncoder()
data_ordinal = pd.DataFrame(encoder.fit_transform(data),
                            columns=data.columns)
# целевой признак - claim=претензия, потребовалась ли страховая выплата
target = data_ordinal['Claim']
features = data_ordinal.drop('Claim', axis=1) 
features_train, features_valid, target_train, target_valid = train_test_split(features, target, test_size=0.25, random_state=12345)

model = DecisionTreeClassifier(random_state=12345)
model.fit(features_train,target_train)
print("Обучено!")
```

### [Урок 7 Итоги кодирования](https://practicum.yandex.ru/trainer/data-scientist/lesson/72abcb98-fc2a-4e8a-8599-d171fd668511/)

Разберёмся, какую кодировку выбрать и почему _Ordinal Encoding_ не подходит для логистической регрессии.
1.  Если все признаки должны стать количественными, подходит техника _OHE;_
2.  Когда все признаки категориальные, и их нужно преобразовать в числа — _Ordinal Encoding._
![image|640](https://pictures.s3.yandex.net/resources/Ordinal-2_1574013691.jpg)

Почему _Ordinal Encoding_ не подходит для логистической регрессии? Она всё норовит посчитать по формуле. Если речь идёт о признаке _Age_, то это разумно, а вот с _Gender_ есть трудности. Например, сложив значения «1» и «0» («женщина» и «мужчина») и разделив на «2», «средний пол» не получить.
С двумя кодировками мы работать дальше не будем. Это неудобно. Остановимся на технике _One-Hot Encoding_. Она подходит для решения нашей задачи: работает со всеми моделями.

### [Урок 8 Масштабирование признаков](https://practicum.yandex.ru/trainer/data-scientist/lesson/f6db1f34-37e7-47e4-aba0-62e9104135e3/task/bbf7b740-0acc-4fb6-b50c-591d054a654f/)

Что делать, если у признаков разный масштаб? Стандартизировать!
В данных есть столбцы: _Age_ и _Commission_. Допустим, возможен возраст от 0 до 100 лет, а страховая комиссия — от 100 долларов до 1000. Значения и их разбросы в столбце _Commission_ больше, поэтому алгоритм автоматически решит, что этот признак важнее возраста. А это не так: все признаки значимы.
Чтобы избежать этой ловушки, признаки масштабируют — приводят к одному масштабу.
Один из методов масштабирования — **стандартизация данных**.
Предположим, что все признаки распределены нормально, среднее (англ. _mean, M_) и дисперсия (лат. _dispersio, D_) определяются по выборке. Значения признака преобразуются по формуле:

![image](https://pictures.s3.yandex.net/resources/novoe_znachenie-2d6ec950-e595-4850-9358-9280a1866a3f_1573570142.jpg)
У нового признака устанавливается среднее, равное 0, и дисперсия, равная 1.
В `sklearn` есть отдельная структура для стандартизации данных — _StandardScaler_ (от англ. «преобразователь масштаба методом стандартизации»). Он находится в модуле `sklearn.preprocessing`.
Импортируем `StandardScaler` из библиотеки:
```python
from sklearn.preprocessing import StandardScaler 
```
Создадим объект этой структуры и настроим его на обучающих данных. Настройка — это вычисление среднего и дисперсии:
```python
scaler = StandardScaler()
scaler.fit(features_train) 
```
Преобразуем обучающую и валидационную выборки функцией `transform()`. Изменённые наборы сохраним в переменных: `features_train_scaled` (англ. «масштабированные признаки для обучения») и `features_valid_scaled` (англ. «масштабированные признаки для проверки»):
```python
features_train_scaled = scaler.transform(features_train)
features_valid_scaled = scaler.transform(features_valid) 
```
При записи изменённых признаков в исходный датафрейм код может вызывать предупреждение `SettingWithCopy`. Причина в особенности поведения `sklearn` и `pandas`. Специалисты уже привыкли игнорировать такое сообщение.
Чтобы предупреждение не появлялось, в код добавляют строчку: `pd.options.mode.chained_assignment = None`

#### Урок 8. Задача 1
Стандартизируйте численные признаки. Импортируйте `StandardScaler` из модуля `sklearn.preprocessing`.
Создайте объект структуры `StandardScaler()` и настройте его на обучающих данных. В переменной `numeric` уже есть список всех численных признаков.
Сохраните преобразованные обучающую и валидационную выборки в переменных: `features_train` и `features_valid`.
```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler 
data = pd.read_csv('/datasets/travel_insurance.csv')

target = data['Claim']
features = data.drop('Claim', axis=1)
features_train, features_valid, target_train, target_valid = train_test_split(
    features, target, test_size=0.25, random_state=12345)

numeric = ['Duration', 'Net Sales', 'Commission (in value)', 'Age']
scaler = StandardScaler()
scaler.fit(features_train[numeric])
features_train[numeric] = scaler.transform(features_train[numeric])
features_valid[numeric] = scaler.transform(features_valid[numeric])
print(features_train.head())
```

### [Урок 9 Подводим итоги](https://practicum.yandex.ru/trainer/data-scientist/lesson/84e25bbb-46d1-42ec-8c27-258e663ee5e4/)

Вы специалист по Data Science уже на 80%! Ровно столько времени тратится на подготовку к обучению модели.
Совместим кодирование категориальных и масштабирование численных признаков. Посмотрим на финальный код:

```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

data = pd.read_csv('travel_insurance.csv')

data_ohe = pd.get_dummies(data, drop_first=True)
target = data_ohe['Claim']
features = data_ohe.drop('Claim', axis=1)
features_train, features_valid, target_train, target_valid = train_test_split(
    features, target, test_size=0.25, random_state=12345)

numeric = ['Duration', 'Net Sales', 'Commission (in value)', 'Age']

scaler = StandardScaler()
scaler.fit(features_train[numeric])
features_train[numeric] = scaler.transform(features_train[numeric])
features_valid[numeric] = scaler.transform(features_valid[numeric])

print(features_train.shape) 
```
`(37995, 188) `

Укажите, что происходит в этом коде:
```python
data_ohe = pd.get_dummies(data, drop_first=True) 
```
- Обработка категориальных признаков техникой _One-Hot Encoding_. Верно! OHE поможет любому алгоритму.

Укажите, что происходит в этом коде:
```python
features_train, features_valid, target_train, target_valid = train_test_split(features, target, test_size=0.25, random_state=12345) 
```
- Разделение данных на обучающую и валидационную выборки. Верно! Она нужна для проверки модели и настройки гиперпараметров.

Укажите, что происходит в этом коде:
```python
scaler = StandardScaler()
scaler.fit(features_train[numeric])
features_train[numeric] = scaler.transform(features_train[numeric])
features_valid[numeric] = scaler.transform(features_valid[numeric]) 
```
Масштабирование данных. Верно! Чтобы алгоритмам было легче обучать модели, признаки приводятся к одному масштабу.

### [Урок 10 Заключение](https://practicum.yandex.ru/trainer/data-scientist/lesson/f4c737cb-cda2-498c-a9b9-429a4ebd6e0d/)
### Теперь вы умеете:
-   Преобразовывать категориальные признаки техникой _OHE_;
-   Кодировать категориальные признаки техникой _Ordinal Encoding_;
-   Масштабировать признаки.
В следующей теме вы узнаете, почему для решения этой задачи не подходит метрика _accuracy_, и выберете другую.

### Заберите с собой
Чтобы ничего не забыть, [скачайте шпаргалку](https://code.s3.yandex.net/data-scientist/praktikum_data_scientist_takeaways_course7_theme2.pdf) и [конспект темы](https://code.s3.yandex.net/data-scientist/praktikum_data_scientist_abstract_course7_theme2.pdf).






