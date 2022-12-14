## [Тема 04. Улучшение модели](https://practicum.yandex.ru/trainer/data-scientist/lesson/eff1009c-c9a6-4f1a-81a9-c00349d96447/)

**Валидационная выборка** - набор данных, извлекаемый из исходного датасета, на которой проверяется качество работы алгоритма во время обучения модели 
**Параметры** - настройки модели, определяющие её работу и получаемые из обучающих данных
**Гиперпараметры** - настройки алгоритмов обучения

-   Контролировать переобучение делением данных на обучающую и валидационную выборки.
-   Менять гиперпараметры модели.
-   Обучать модели случайного леса и логистической регрессии.
-   Сравнивать качество других моделей и выбирать лучшую.

### [Урок 2 Валидационная выборка](https://practicum.yandex.ru/trainer/data-scientist/lesson/60f332c3-8944-486f-a769-0ecb3ccf0aed/)
Проверять модель на правильность предсказаний нужно, а тестовую выборку спрятали. Что делать?
Представьте: вы готовитесь к экзамену по тестам прошлых лет. Не торопитесь решить всё за раз. Отложите часть заданий, чтобы потом проверить, насколько хорошо вы разобрались в теме. Так и в машинном обучении. Чтобы оценка качества была более надёжной, нужно подготовить новую выборку — **валидационную** (англ. _validation_, «проверка»), или **проверочную**.
Валидационная выборка отбирается из исходного датасета ещё до обучения модели. Иначе, обучившись на тренировочном наборе, модель будет знать все ответы. Именно валидация подсказывает, как ведёт себя модель в полевых условиях и нет ли переобучения.
Какую часть данных отвести под валидационную выборку, решают в зависимости от количества объектов, признаков и вариативности данных. Вот два самых распространённых сценария:
1) Доступен исходный датасет, а тестовая выборка спрятана. Тогда рекомендуется 75% данных отвести под обучающую, а 25% — под валидационную. Соотношение 3:1. Этот сценарий используется в задачах нашего тренажёра.
![image|320]()
2) Спрятанной тестовой выборки нет. Значит, данные нужно разбить на три части: обучающую, валидационную и тестовую. Размеры тестового и валидационного наборов обычно равны. Исходные данные разбивают в соотношении 3:1:1.

Валидация помогает выявить переобучение модели.
Валидация показывает, как поведёт себя модель с незнакомыми данными. Если правильность предсказаний резко падает, модель переобучена.
Тестовая выборка нужна, чтобы правильно оценить готовую модель.
Всё так. Пока модель совершенствуется, тестовая выборка всё ждёт и ждёт, и всё ещё ждёт... И наконец-то дожидается звёздной минуты — итоговой оценки!

### [Урок 3 Деление на две выборки](https://practicum.yandex.ru/trainer/data-scientist/lesson/3c44cb0e-c394-4a84-82e5-64a142bc1f6b/task/93fcc532-a4a8-4075-a55b-ce181471a1e9/)

Валидационная выборка — это 25% исходных данных. Как её извлечь?
В `sklearn` для этого предусмотрена функция `train_test_split` (от англ. «разделить на обучающую и тестовую»). Она разбивает любой датасет на обучающую и тестовую выборки. Но мы применим эту функцию, чтобы получить валидационный и обучающий наборы.
Импортируем `train_test_split` из модуля `sklearn.model_selection` (от англ. «выбор модели»):
```python
from sklearn.model_selection import train_test_split
```
Прежде чем разделить набор данных, нужно указать два параметра:
-   **Название набора**, данные которого делим;
-   **Размер валидационной выборки** (`test_size`). Выражается в долях — от 0 до 1. В нашем примере `test_size=0.25`, поскольку работаем с 25% исходных данных.
Функция `train_test_split()` возвращает два новых набора данных — обучающий и валидационный.

```python
# test_size - доля валидационной выборки от общего числа объектов, число от 0 до 1
df_train, df_valid = train_test_split(df, test_size=0.25, random_state=12345)
```
#### Урок 3. Задача 1
Разделите набор данных на обучающую (`df_train`) и валидационную (`df_valid`) выборки. В валидационной выборке — 25% исходных данных. В `random_state` положите значение `12345`.
В коде мы объявили переменные с признаками для обучения: `target_train` (англ. цель для обучения) и  `features_train` (англ. признаки для обучения). Создайте аналогичные переменные для проверки:
-   с целевым признаком — `target_valid`;
-   с остальными признаками — `features_valid`.
Выведите на экран размеры таблиц, которые хранятся в четырёх переменных
Переменные для валидационной выборки:
```python
features_valid = df_valid.drop(['last_price', 'price_class'], axis=1)
target_valid = df_valid['price_class'] 
```

```python
import pandas as pd
# < импортируйте функцию train_test_split из библиотеки sklearn >
from sklearn.model_selection import train_test_split 

df = pd.read_csv('/datasets/train_data.csv')
df.loc[df['last_price'] > 5650000, 'price_class'] = 1
df.loc[df['last_price'] <= 5650000, 'price_class'] = 0

# < разделите данные на обучающую и валидационную выборки >
df_train, df_valid = train_test_split(df, test_size=0.25, random_state=12345)
# < создайте переменные для признаков и целевого признака >
features_train = df_train.drop(['last_price', 'price_class'], axis=1)
target_train = df_train['price_class']
features_valid = df_valid.drop(['last_price','price_class'], axis=1)#
target_valid = df_valid['price_class'] # 

print(features_train.shape)
print(target_train.shape)
print(features_valid.shape)
print(target_valid.shape)
```

### [Урок 4 Гиперпараметры](https://practicum.yandex.ru/trainer/data-scientist/lesson/f65932b9-4915-465b-954e-f415cca5a8a6/)
Что определяет правильность предсказания решающего дерева? Количество узлов и их взаимное расположение (структура), вопрос в вершине и ответы в нижних узлах. Всё это **параметры**, которые модель узнаёт из обучающих данных (только не путайте параметры в Python и машинном обучении).
Помимо обычных параметров, есть ещё **гиперпараметры,** настройки алгоритмов обучения. В решающем дереве, например, это максимальная глубина или выбор критерия — Джини либо энтропийного (о нём расскажем позже). Гиперпараметры помогают улучшить модель. Изменить их можно до начала обучения.
- Параметры определяют, как предсказывает модель.
Параметры — это настройки, которые помогают модели в работе.
- На значение параметров влияют обучающие данные.
Параметры связаны с данными, поскольку формируются при обучении.
ещё раз:
```python
DecisionTreeClassifier(class_weight=None, criterion='gini', max_depth=None,
            max_features=None, max_leaf_nodes=None,
            min_impurity_decrease=0.0, min_impurity_split=None,
            min_samples_leaf=1, min_samples_split=2,
            min_weight_fraction_leaf=0.0, presort=False, random_state=None,
            splitter='best')
```
Наш «чёрный ящик» теперь не такой уж «чёрный». В скобках — все гиперпараметры алгоритма. С максимальной глубиной вы уже знакомы.
— **criterion='gini'** — критерий Джини - критерий разделения, который показывает меру сходства двух наборов данных. Обучаясь, дерево в каждом узле (на каждой развилке) из возможных вопросов задаёт наилучший. Сейчас оно выбирает тот вопрос, для которого критерий Джини показывает, что отнесённые к левой ветке данные меньше всего похожи на те, что в правой.
— **min_samples_split** (от англ. «минимальное количество примеров для разделения»). Этот гиперпараметр запрещает создавать узлы, в которые попадает слишком мало объектов обучающей выборки.
— **min_samples_leaf** (от англ. «минимальное количество объектов в листе»). Листья — это нижние узлы с ответами. А гиперпараметр не разрешает создавать лист, в котором слишком мало объектов обучающей выборки.
Значения гиперпараметров установлены по умолчанию, вы можете их не прописывать или, наоборот, поменять все. Например, вы готовите борщ по бабушкиному рецепту. В нём прописаны все исходные ингредиенты и пропорции. Но очень хочется бабушку удивить и сделать суп острее, поэтому добавляете больше перца. Пока не понятно, ваши близкие будут рады или нет, но «гиперпараметры борща» вы точно поменяли.
Для каждого алгоритма есть отдельный набор настроек, которые можно указать до обучения.

Что значит «менять гиперпараметры»?
- Вручную задавать характеристики модели перед обучением.
Вас не запутать, как ни крути. Настройки.
Что относится к параметрам?
- Глубина обученного дерева.
Ваши познания в природе решающего дерева достаточно глубоки. Это часть структуры обученного дерева.
- Признак, который используется в вопросе первого узла.
Это часть вопроса в обученном дереве.

### [Урок 5 Смена гиперпараметров](https://practicum.yandex.ru/trainer/data-scientist/lesson/3a7016cd-008f-4f84-94ec-3006d3407434/task/feacc18d-50c7-4aa9-aca7-9aec21252ca8/)
Самый важный гиперпараметр решающего дерева — `max_depth` - максимальная глубина дерева. Именно он определяет, что в итоге получим — пень с одним вопросом или клён с ветвистой кроной.
Каким должен быть гиперпараметр `maх_depth`, чтобы улучшить нашу модель? Неизвестно. Поэтому в цикле нужно перебрать разные значения и сравнить качество моделей в разных вариантах. Сейчас мы будем проверять автоматически, не дожидаясь проверки на тестовой выборке.

#### Урок 5. Задача 1
Поменяйте гиперпараметр `max_depth` от 1 до 5 в цикле. Для каждого значения напечатайте на экране качество на валидационной выборке.
Проверять на тестовой выборке пока не нужно, сначала найдите наилучшую модель.
Допишите код цикла:
```python
for depth in range(1, 6):
    # < создайте модель, указав max_depth=depth >
	model = 
    # < обучите модель >
	# < найдите предсказания на валидационной выборке >
	predictions_valid = 
	
    print("max_depth =", depth, ": ", end='')
    print(accuracy_score(target_valid, predictions_valid)) 
```

```python
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

df = pd.read_csv('/datasets/train_data.csv')
df.loc[df['last_price'] > 5650000, 'price_class'] = 1
df.loc[df['last_price'] <= 5650000, 'price_class'] = 0

df_train, df_valid = train_test_split(df, test_size=0.25, random_state=12345)

features_train = df_train.drop(['last_price', 'price_class'], axis=1)
target_train = df_train['price_class']
features_valid = df_valid.drop(['last_price', 'price_class'], axis=1)
target_valid = df_valid['price_class']

# < сделайте цикл для max_depth от 1 до 5 >
for i in range(1,6):
    
    model = DecisionTreeClassifier(random_state=12345, max_depth=i)
    model.fit(features_train,target_train)
    predictoins = model.predict(features_valid)
    accuracy = accuracy_score(target_valid,predictoins)
    print('max_depth = {} : {}'.format(i,accuracy))
```

## [Урок 6 Новые модели: случайный лес](https://practicum.yandex.ru/trainer/data-scientist/lesson/5b9d654e-4bc9-4447-a202-cac54e8432af/task/e512e62b-1bac-478b-8b64-832ab9f75033/)
Вы поменяли гиперпараметры модели. Но результат всё ещё не устраивает. Одного дерева явно недостаточно, нужен целый лес!
Попробуем новый алгоритм классификации — **случайный лес** (англ. _random forest_). Алгоритм обучает большое количество независимых друг от друга деревьев, а потом принимает решение на основе голосования. Случайный лес помогает улучшить результат предсказания и избежать переобучения.
Чтобы управлять количеством деревьев в лесу, пропишем гиперпараметр `n_estimators` (от англ. _number of estimators_, «количество оценщиков»). Чем больше деревьев, тем дольше модель будет учиться, но результат станет лучше (и наоборот). Возьмём пока значение `n_estimators`, равное `3`.
```python
model = RandomForestClassifier(random_state=12345, n_estimators=3) 
```
Как и в прошлых уроках, обучим модель методом `fit()`.
```python
model.fit(features, target) 
```
Модель обучена и готова предсказывать. Вызовем метод `predict()`.
```python
model.predict(new_item) 
```
Правильность модели мы проверяли функцией `accuracy_score()`. Но можно — и методом `score()`. Он считает _accuracy_ для всех алгоритмов классификации.
```python
model.score(features, target) 
```

#### Урок 5. Задача 1
Обучите модели случайного леса с числом деревьев от 1 до 10. Для этого:
1.  разделите тренировочную и валидационную выборки,
2.  при инициализации модели укажите число деревьев равное состоянию счётчика циклов — `est`;
3.  обучите модель на тренировочной выборке,
4.  сохраните модель с лучшим значением `accuracy` на валидационной выборке.
Качество на тестовой выборке должно получиться не меньше 0.88.
1.  Выделите 25% исходных данных в валидационную выборку,
2.  передайте в качестве параметра `n_estimators=est`,
3.  обучите модель на тренировочной выборке: `features_train, target_train`,
4.  посчитайте качество модели на валидационной выборке `features_valid`, `target_valid` и сохраните лучший результат в `best_model`.
```python
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
df = pd.read_csv('/datasets/train_data.csv')
df.loc[df['last_price'] > 5650000, 'price_class'] = 1
df.loc[df['last_price'] <= 5650000, 'price_class'] = 0
# отделите 25% данных для валидационной выборки
df_train, df_valid = train_test_split(df, test_size=0.25, random_state=12345) 

features_train = df_train.drop(['last_price', 'price_class'], axis=1)
target_train = df_train['price_class']
features_valid = df_valid.drop(['last_price', 'price_class'], axis=1)
target_valid = df_valid['price_class']

best_model = None
best_result = 0
for est in range(1, 11):
	# обучите модель с заданным количеством деревьев
    model = RandomForestClassifier(random_state=12345, n_estimators=est) 
    # обучите модель на тренировочной выборке
    model.fit(features_train,target_train) 
    # посчитайте качество модели на валидационной выборке
    result = model.score(features_valid,target_valid) 
    if result > best_result:
        # сохраните наилучшую модель
        best_model = model
        #  сохраните наилучшее значение метрики accuracy на валидационных данных
        best_result = result

print("Accuracy наилучшей модели на валидационной выборке:", best_result)
```

## [Урок 7 Логистическая регрессия](https://practicum.yandex.ru/trainer/data-scientist/lesson/7230fee0-2be9-4304-96d7-5730f171cdf3/task/47911c54-a8d2-4f65-a893-ef70b479ca26/)

Алгоритмы не ограничиваются деревьями. Есть и другие способы классификации.
Если сделать гиперпараметр `n_estimators` больше, модель начнёт разрастаться и медленно обучаться. Это плохо. Мало деревьев и результаты не лучше — тоже неудачно. Сколько можно быть зависимым от деревьев? Попробуем ещё один алгоритм — логистическую регрессию.
Слово «логистическая» не значит, что кривая связана с поставками товаров. Оно происходит от греческого _λογιστικός_, «искусный в расчётах». Логистическое уравнение придумал бельгийский математик Франсуа Ферхюльст, который на основе пяти переписей населения построил кривую изменения численности, предсказавшую значение на 100 лет вперёд с точностью до 1%.
Если название и «мимикрирует» под задачу регрессии, всё-таки это алгоритм классификации.
Чтобы предсказать класс жилья, логистическая регрессия:
-   Сначала считает, к какому классу близок объект. Например, по такой формуле:  
    близость к классу = 10 * площадь / м^2 - (расстояние  до центра) / м
    Площадь увеличивает стоимость, а расстояние до центра — уменьшает. Причём каждый квадратный метр площади в 10 раз важнее одного метра до центра. (Мы рассмотрели лишь площадь и расстояние. Но чтобы получить близость к классу, в чёрный ящик помещаются все признаки. В последующих уроках расскажем подробнее, как работает чёрный ящик.)
-   В зависимости от ответа выбирает нужный класс: если результат вычисления положительный, то — `1` (высокие цены); отрицательный — `0` (низкие цены).
В логистической регрессии параметров мало. Что-либо вызубрить по признакам в формуле не выйдет, поэтому и вероятность переобучения невелика.
Модель `LogisticRegression` (англ. «логистическая регрессия») лежит в модуле `sklearn.linear_model` (от англ. «линейная модель») библиотеки `sklearn`. Импортируйте его:
```python
from sklearn.linear_model import LogisticRegression 
```
Запишите модель в переменной, указав гиперпараметры. Для постоянства результата задайте `random_state`, равный `12345`. Добавьте дополнительные гиперпараметры: `solver='lbfgs'` и `max_iter=1000`. Первый гиперпараметр позволяет выбрать алгоритм, который будет строить модель. Алгоритм `'lbfgs'` — один из самых распространённых. Он подходит для большинства задач. Гиперпараметром `max_iter` задаётся максимальное количество итераций обучения. Значение этого параметра по умолчанию равно 100, но в некоторых случаях понадобится больше итераций.
Обучите модель вызовом метода `fit()`.
```python
model = LogisticRegression(random_state=12345, solver='lbfgs', max_iter=1000) 
```
Обученная модель готова предсказывать. Вызовите метод `predict()`.
```python
model.predict(new_item) 
```
Чтобы посмотреть _accuracy_ модели, нужно вызвать функцию `.score()`:
```python
model.score(features, target) 
```

#### Урок 7. Задача 1
Обучите модель логистической регрессии и загрузите её в тренажёр.
Подсказка
Гиперпараметры логистической регрессии настраивать не нужно. Просто обучите и загрузите её.

```python
import pandas as pd
from joblib import dump
from sklearn.linear_model import LogisticRegression 
df = pd.read_csv('/datasets/train_data.csv')
df['price_class']=df['last_price'].apply(lambda x: 1 if x > 5650000 else 0)
features=df.drop(['last_price','price_class'],axis=1)
target=df['price_class']
model = LogisticRegression(random_state=12345, solver='lbfgs', max_iter=1000) 
model.fit(features, target) 
dump(model, 'model_9_1.joblib')
```

## [Урок 8 Сравнение моделей](https://practicum.yandex.ru/trainer/data-scientist/lesson/22381a83-5c9a-4f51-ac51-e43f149563dc/)

Специалист по Data Science не только обучает модели, но и объясняет заказчику их плюсы и минусы. Сравним наши модели.
-   дерево решений,
-   случайный лес,
-   логистическую регрессию.
Одновременно работать с тремя моделями не нужно. У каждой — свои достоинства и недостатки. Оценим модели по качеству (_accuracy)_ и скорости работы.
**1. Качество _(accuracy)._** Это самый важный критерий для бизнеса: чем выше качество, тем больше прибыли приносит продукт.
Самое высокое качество у случайного леса: вместо одного решающего дерева используется целый ансамбль.
На втором месте — логистическая регрессия. Модель несложная, а значит, переобучение ей не грозит.
Самое низкое качество предсказания у дерева решений. Если глубина меньше четырёх, оно недообучается, когда больше — переобучается.

**2. Скорость работы.** Не менее значимый критерий: если сервис работает медленно, оттока пользователей не избежать.
Высокая скорость работы у логистической регрессии: у неё меньше всего параметров.
Скорость решающего дерева тоже высокая и зависит от глубины. Помните, в экспериментах наилучшее качество модели получилось при глубине, равной 4. Ответ на вопрос модель получила всего-то за четыре проверки значений признаков — а это очень быстро!
Случайный лес медленнее всех: чем больше деревьев, тем неторопливее работает модель.
Name | Качество | Скорость
-|-|-
Решающее дерево | Низкое | Высокая
Случайный лес | Высокое | Низкая
Логистическая регрессия | Среднее | Высокая

## [Урок 9 Заключение](https://practicum.yandex.ru/trainer/data-scientist/lesson/f4ad84c0-0313-49c3-bcf8-cb3f7ea85c31/)
-   Как проверять качество модели;
-   Что такое гиперпараметры и как они влияют на правильность предсказания;
-   Как «вырастить» случайный лес и обучить логистическую регрессию.
Чтобы ничего не забыть, [скачайте шпаргалку](https://code.s3.yandex.net/data-analyst/conspects/praktikum_data_scientist_takeaways_course6_theme4.pdf) и [конспект темы](https://code.s3.yandex.net/data-analyst/conspects/praktikum_data_scientist_abstract_course6_theme4.pdf).








x