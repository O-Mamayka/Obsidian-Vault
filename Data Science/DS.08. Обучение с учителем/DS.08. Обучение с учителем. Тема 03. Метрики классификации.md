## [Тема 03. Метрики классификации](https://practicum.yandex.ru/trainer/data-scientist/lesson/6c4ed6a2-5ae3-4a5f-8d3f-6695a0cca354/)

**Полнота** - это метрика качества классификации, показывающая, какова доля TruePositive-ответов среди всех, у которых
истинная метка 1. 
**Точность** - это метрика качества классификации, которая показывает какую долю объектов, распознанных как объекты положительного класса, мы предсказали верно.
**F1-мера** - это метрика качества классификации, являющаяся средним гармоническим полноты и точности.

-   Выясните, когда метрика _accuracy_ не подходит.
-   Узнаете, как строить матрицу ошибок.
-   Поработаете с новыми метриками: точностью, полнотой и _F1_-мерой.

### [Урок 2 Accuracy для решающего дерева](https://practicum.yandex.ru/trainer/data-scientist/lesson/dbcadf14-8389-449e-8297-84aec13efdb3/task/5051528a-c1e9-4856-b72d-5ae5f78632f1/)

Подходит ли нам метрика _accuracy_? Обучим модель и проверим.
Вычислим правильность модели функцией _accuracy_score()_. Она принимает на вход верные ответы и предсказания, а возвращает долю правильных ответов.

#### Урок 3 Задача
Обучите модель решающего дерева. Посчитайте значение _accuracy_ на валидационной выборке. Сохраните результат в переменной _accuracy_valid_. Напечатайте его на экране.

```python
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
data = pd.read_csv('/datasets/travel_insurance_preprocessed.csv')

target = data['Claim']
features = data.drop('Claim', axis=1)
features_train, features_valid, target_train, target_valid = train_test_split(
    features, target, test_size=0.25, random_state=12345)

model = DecisionTreeClassifier(random_state=12345)
model.fit(features_train,target_train)
predicted_valid = model.predict(features_valid)
accuracy_valid = accuracy_score(predicted_valid,target_valid)
print(accuracy_valid)
```
`0.974496644295302`

### [Урок 3 Проверка адекватности модели](https://practicum.yandex.ru/trainer/data-scientist/lesson/435da28e-e8fc-43b6-844a-1c2e32b57592/task/604eaaf4-9940-47b6-b73e-fe5eb58a4cbb/)

Доля правильных ответов — 97%. Это много или мало? Исследуем целевой признак.
Чтобы оценить адекватность модели, проверим, как часто в целевом признаке встречается класс «1» или «0». Количество уникальных значений подсчитывается методом _value_counts()._ Он группирует строго одинаковые величины.

#### Урок 3 Задача 1
Для подсчёта классов в целевом признаке примените метод _value_counts()_. Сделайте частоты относительными (от 0 до 1): в этом поможет документация Pandas.
Значения сохраните в переменной _class_frequency_. Напечатайте их на экране.
Методом _plot()_ c аргументом `kind='bar'` постройте диаграмму.
Чтобы получить относительные частоты (англ. _relative frequencies)_, поделите количества классов на размер выборки.
```python
import pandas as pd
data = pd.read_csv('/datasets/travel_insurance_preprocessed.csv')
class_frequency = data['Claim'].value_counts(normalize=True)
print(class_frequency)
class_frequency.plot(kind='bar')
```
`0 0.985136; 1 0.014864`

#### Урок 3 Задача 2
Проанализируйте частоты классов в результатах предсказаний решающего дерева (переменная _predicted_valid_).
-   Примените метод _value_counts()_. Сделайте частоты относительными.
-   Значения сохраните в переменной _class_frequency_. Напечатайте их на экране.
-   Методом _plot()_ c аргументом `kind='bar'` постройте диаграмму.
```python
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
data = pd.read_csv('/datasets/travel_insurance_preprocessed.csv')

target = data['Claim']
features = data.drop('Claim', axis=1)
features_train, features_valid, target_train, target_valid = train_test_split(
    features, target, test_size=0.25, random_state=12345)

model = DecisionTreeClassifier(random_state=12345)
model.fit(features_train, target_train)

# чтобы работала функция value_counts(), преобразовали результат к pd.Series 
predicted_valid = pd.Series(model.predict(features_valid))
class_frequency = predicted_valid.value_counts(normalize=True)
print(class_frequency)
class_frequency.plot(kind='bar')
```

#### Урок 3 Задача 3
Создайте константную модель: любому объекту она прогнозирует класс «0». Сохраните её предсказания в переменной _target_pred_constant_.
Напечатайте на экране значение _accuracy._
```python
import pandas as pd
from sklearn.metrics import accuracy_score
import numpy as np
data = pd.read_csv('/datasets/travel_insurance_preprocessed.csv')

target = data['Claim']
features = data.drop('Claim', axis=1)
target_pred_constant = pd.Series(data=0, index=range(len(target)))

accuracy = accuracy_score(target,target_pred_constant)
print(accuracy)
```
`0.9851362021318595`

### [Урок 4 Баланс и дисбаланс классов](https://practicum.yandex.ru/trainer/data-scientist/lesson/a210c5b6-ca87-4e7a-a581-a644683535f1/)

Почему _accuracy_ решающего дерева и константной модели почти одинаковы и что с этим делать?
Долю _правильных ответов_, близкую к 100%, мы получили. А вот понимания, воспользуется ли клиент страховкой, — нет. В нашей задаче наблюдается сильный **дисбаланс классов** (англ. _class imbalance_), что плохо сказывается на обучении модели.
Классы несбалансированны, когда их соотношение далеко от 1:1. **Баланс классов** (англ. _class balance_) наблюдается, если их количество примерно равно.
_Accuracy_ не подходит. Нужна новая метрика! Но прежде — несколько важных определений.
Вы уже знаете, что класс с меткой «1» называется **положительным**, с меткой «0» — **отрицательным**.
Если сравнить эти ответы с предсказаниями, получается такое деление:
-   **истинно положительные** (англ. _True Positive, TP_) и **истинно отрицательные ответы** (англ. _True Negative, TN_);
-   **ложноположительные** (англ. _False Positive, FP_) и **ложноотрицательные ответы** (англ. _False Negative, FN_).
Резюмируем. Характеристики «положительный» и «отрицательный» относятся к предсказанию, а «истинный» и «ложный» — к его правильности.

### [Урок 5 Истинно положительные ответы](https://practicum.yandex.ru/trainer/data-scientist/lesson/d8dcb43a-c992-45fa-b4bc-c7aee782bba1/task/cf032762-4521-438f-b961-0f9b20dbeb66/)

Справиться с дисбалансом и более точно классифицировать ответы помогут новые метрики.
Что значит истинно положительный ответ _(TP)_? Модель пометила объект единицей, и его настоящее значение тоже — 1.
В нашей задаче истинно положительный ответ — это количество застрахованных, которые:
-   по прогнозу модели обратились за компенсацией;
-   фактически запросили страховую выплату.
#### Урок 5 Задача
Мы сделали пример предсказаний и правильных ответов. Посчитайте количество _TP_-ответов и напечатайте результат на экране.
Вам нужно составить условия на последовательности: объединить их логическим оператором и найти сумму значений. Как вы знаете, оператор `and` в Pandas записывается символом `&`:

### [Урок 6 Истинно отрицательные ответы]()
Если предсказанное и фактическое значение класса отрицательные, ответ истинно отрицательный.
В нашей задаче истинно отрицательный ответ _(TN)_ — это количество застрахованных, которые:
-   по прогнозу модели не запросили выплату;
-   фактически не обратились за компенсацией по страховке.
#### Урок 6 Задача
Посчитайте количество _TN_-ответов, как и в прошлой задаче. Напечатайте результат на экране.
```python
import pandas as pd
target = pd.Series([1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1])
predictions = pd.Series([1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1])
TP = ((target == 1) & (predictions == 1)).sum() 
print(TP)
TN = ((target == 0) & (predictions == 0)).sum()
print(TN)
```
`5`
`4`

### [Урок 7 Ложноположительные ответы](https://practicum.yandex.ru/trainer/data-scientist/lesson/851689c8-6681-4462-8e45-94f0dca62409/task/4b0ed887-26e7-4975-82b5-62cf0c0956d1/)
Алгоритмы имеют право на ошибки. Только двух видов.
Ошибка первого рода — это ложноположительные ответы (_FP_). Они возникают, когда модель предсказала «1», а вот действительное значение класса — «0».
В нашей задаче ложноположительный ответ — это количество застрахованных, которые:
-   по прогнозу модели запросили выплату;
-   фактически не обратились за компенсацией.

#### Урок 7 Задача
Посчитайте количество _FP_-ответов, как и в прошлой задаче. Напечатайте результат на экране.
Подставьте подходящие значения вместо вопросительных знаков:
Если ответ ложно_положительный_, значит предсказание — «1».

### [Урок 8 Ложноотрицательные ответы](https://practicum.yandex.ru/trainer/data-scientist/lesson/005eb947-ccc8-44d3-9701-03192f8ae693/task/9e34730e-00a2-4ec5-a4ed-07750d96e4d3/)
Ошибка второго рода — ложноотрицательные ответы _(FN)._
Ложноотрицательные ответы появляются, когда модель предсказала «0», а действительное значение класса — «1».
В нашей задаче ложноотрицательный ответ — это количество застрахованных, которые:
-   по прогнозу модели не запросили выплату;
-   фактически обратились за компенсацией.
#### Урок 8 Задача
Посчитайте количество _FN_-ответов. Напечатайте результат на экране.
Подставьте подходящие значения вместо вопросительных знаков:
Если ответ ложно_отрицательный_, значит предсказание — «0».
```python
import pandas as pd

target = pd.Series([1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1])
predictions = pd.Series([1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1])
FP = ((predictions == 1)&(target == 0)).sum()
print(FP)
FN =((target == 1)&(predictions == 0)).sum()
print(FN)
```
`3`; `2`

### [Урок 9 Матрица ошибок](https://practicum.yandex.ru/trainer/data-scientist/lesson/6178662d-4ab1-4510-ae0f-9eddff59e106/task/f84b0d8e-5cb2-4b7c-83d1-1443a65908b2/)
_TP_, _FP_, _TN_, _FN_ собираются в одну таблицу — **матрицу ошибок**, или **матрицу неточностей** (англ. _сonfusion matrix_).
Матрица формируется так:
-   по горизонтали («Предсказания») располагаются метки алгоритма от 0 до 1;
-   по вертикали («Ответы») — истинные метки класса от 0 до 1.
1.  По главной диагонали (от верхнего левого угла) выстроены правильные прогнозы:
    -   _TN_ в левом верхнем углу;
    -   _TP_ в правом нижнем углу.
2.  Вне главной диагонали — ошибочные варианты:
    -   _FP_ в правом верхнем углу;
    -   _FN_ в левом нижнем углу.
 | |0 | True Negative | False Positive
-|-|-|-
Ответы |1 | False Negative | True Positive
 | | | 0 | 1 
 | | | предсказания |  
Наглядно представить результаты вычислений метрик точности и полноты позволяет матрица ошибок.
Матрица неточностей находится в знакомом модуле _sklearn.metrics._ Функция _confusion_matrix()_ принимает на вход верные ответы и предсказания, а возвращает матрицу ошибок.

#### Урок 9 Задача 1
Рассчитайте матрицу ошибок функцией _confusion_matrix()._ Импортируйте её из модуля _sklearn.metrics._ Напечатайте результат на экране.
```python
import pandas as pd
from sklearn.metrics import confusion_matrix
target = pd.Series([1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1])
predictions = pd.Series([1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1])

matrix = confusion_matrix(target,predictions)
print(matrix)
```

#### Урок 9 Задача 2
Постройте матрицу ошибок для решающего дерева. Как и в прошлом задании, вызовите функцию _confusion_matrix()._ Напечатайте результат на экране.
```python
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
data = pd.read_csv('/datasets/travel_insurance_preprocessed.csv')
target = data['Claim']
features = data.drop('Claim', axis=1)
features_train, features_valid, target_train, target_valid = train_test_split(
    features, target, test_size=0.25, random_state=12345)
model = DecisionTreeClassifier(random_state=12345)
model.fit(features_train, target_train)
predicted_valid = model.predict(features_valid)
matrix = confusion_matrix(target_valid,predicted_valid)
print(matrix)
```

### [Урок 10 Полнота](https://practicum.yandex.ru/trainer/data-scientist/lesson/3a08365f-5ac2-4a08-9532-89cdcb70db37/task/3c19652c-ea39-482c-9c65-302da3ec60ed/)
Матрица ошибок поможет построить новые метрики. Начнём с **полноты** (англ. _recall_).
Полнота выявляет, какую долю положительных среди всех ответов выделила модель. Обычно они на вес золота, и важно понимать, как хорошо модель их находит.
_Recall_ рассчитывается по такой формуле:
`Recall = TP / (TP + FN)`
Разберём на примере нашей задачи:
-   за компенсацией обратились 100 застрахованных. Это количество всех положительных объектов, или _TP + FN_;
-   модель определила из них правильно только 20;
-   _recall_ равна 0.2.
Полнота — это доля _TP_-ответов среди всех, у которых истинная метка 1. Хорошо, когда значение _recall_ близко к единице: модель хорошо ищет положительные объекты. Если ближе к нулю — модель надо перепроверить и починить.

#### Урок 10 Задача
Найдите в модуле _sklearn.metrics_ функцию, которая отвечает за вычисление полноты. 
Функция принимает на вход верные ответы и предсказания, а возвращает долю правильных ответов, найденных моделью. Напечатайте результат на экране.
```python
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import recall_score
data = pd.read_csv('/datasets/travel_insurance_preprocessed.csv')

target = data['Claim']
features = data.drop('Claim', axis=1)
features_train, features_valid, target_train, target_valid = train_test_split(
    features, target, test_size=0.25, random_state=12345)
model = DecisionTreeClassifier(random_state=12345)
model.fit(features_train, target_train)
predicted_valid = model.predict(features_valid)

print(recall_score(target_valid,predicted_valid))
```
`0.07100591715976332`

### [Урок 11 Точность](https://practicum.yandex.ru/trainer/data-scientist/lesson/0061503e-edca-4bbd-beca-40f03fb1ac0c/task/da873d00-310f-47ad-bc8d-ba5eb6c3ac77/)

Ещё одна метрика для оценки качества прогноза целевого класса — **точность** (англ. _precision_).
Точность определяет, как много отрицательных ответов нашла модель, пока искала положительные. Чем больше отрицательных, тем ниже точность.
_Precision_ рассчитывается по такой формуле:
`Precision = TP / (TP + FP)`
Разберём на примере нашей задачи:
-   по прогнозу модели за компенсацией обратится 100 застрахованных. Это количество всех объектов с положительным прогнозом, или _TP + FP_;
-   20 из них действительно запросили страховую выплату (предсказание совпало с ответом, и ответ положительный — _TP_).
-   _precision_ равна 0.2.
Напомним, _TP_ — это истинно положительные ответы. _FP_ — отмеченные моделью положительные ответы. Нам нужна точность, близкая к единице.

#### Урок 11 Задача
Найдите в модуле _sklearn.metrics_ функцию, которая отвечает за вычисление точности. Импортируйте её.
Функция принимает на вход верные ответы и предсказания. Возвращает, какая доля объектов, отмеченных моделью как положительные, на самом деле такие. 
Функция называется _precision_score()._
```python
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import precision_score
data = pd.read_csv('/datasets/travel_insurance_preprocessed.csv')

target = data['Claim']
features = data.drop('Claim', axis=1)
features_train, features_valid, target_train, target_valid = train_test_split(
    features, target, test_size=0.25, random_state=12345)

model = DecisionTreeClassifier(random_state=12345)
model.fit(features_train, target_train)
predicted_valid = model.predict(features_valid)
print(precision_score(target_valid, predicted_valid))
	```
`0.06741573033707865`

### [Урок 12 Точность против полноты ](https://practicum.yandex.ru/trainer/data-scientist/lesson/126ce022-6fba-4980-8b32-cb9d496acaaa/)
Когда модель плохо предсказывает положительные классы, то мала как точность, так и полнота. Можно ли повысить их значения?
Ещё раз посмотрим на формулы расчёта полноты и точности:
`Recall = TP / (TP + FN)`
`Precision = TP / (TP + FP)`
Если в задаче ключевая метрика — полнота, как сделать её максимально высокой?
- Обучите модель, которая отвечает «1» на все объекты. Полнота будет равна 1.0.
Достаточно отвечать всегда «1» — и высокая полнота обеспечена.
Полноту мы разобрали, а как же достичь высокой точности? В формуле учитываются только ошибки для положительного класса, а не отрицательного. Нужно обучить модель, которая, наоборот, отвечает «1» как можно реже. Но отвечать на всё «0» не стоит, так метрику не «взломать»: в формуле ноль будет делиться на ноль.

### [Урок 13 F1-мера](https://practicum.yandex.ru/trainer/data-scientist/lesson/0fac5c53-466a-48f5-8d71-db0306cb910b/task/10bff975-9e64-4d08-97bc-39393266bb9f/)
По отдельности полнота и точность не слишком информативны. Нужно одновременно повышать показатели обеих. Или обратиться к новой метрике, которая их объединит.
Полнота и точность оценивают качество прогноза положительного класса с разных позиций. _Recall_ описывает, как хорошо модель разобралась в особенностях этого класса и распознала его. _Precision_ выявляет, не переусердствует ли модель, присваивая положительные метки.
Важны обе метрики. Контролировать их параллельно помогают агрегирующие метрики, одна из которых — **F1-мера** (англ. _F1-score_). Это среднее гармоническое полноты и точности. Единица в _F1_ означает, что соотношение полноты и точности равно 1:1.
`F1 = 2 × Precision × Recall / (Precision + Recall)`
Важно: когда полнота или точность близки к нулю, то к 0 приближается и само среднее гармоническое.
На графике отображены значения _F1_-меры при разных значениях точности и полноты. Синий цвет соответствует нулю, а жёлтый — единице.
![image](https://pictures.s3.yandex.net/resources/Untitled-7704c3eb-db79-42eb-a8a9-d609745ea768_1573819303.png)
Если положительный класс плохо прогнозируется по одной из шкал (_Recall_ или _Precision)_, то близкая к нулю _F1_-мера покажет, что прогноз класса 1 не удался.
#### Урок 13 Задача 1
Посчитайте:
-   точность, применив функцию _precision_score();_
-   полноту функцией _recall_score();_
-   _F1_-меру по формуле из теории.
```python
import pandas as pd
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
target = pd.Series([1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1])
predictions = pd.Series([1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1])

precision = precision_score(target,predictions)
recall =recall_score(target,predictions) # < напишите код здесь >
f1 = 2*precision*recall/(recall+precision)
print("Полнота:", recall)
print("Точность:", precision)
print("F1-мера:", f1)
```
`Полнота: 0.7142857142857143; Точность: 0.625; F1-мера: 0.6666666666666666`
#### Урок 13 Задача 2
Найдите в модуле _sklearn.metrics_ функцию, которая отвечает за вычисление _F1_-меры. Импортируйте её.
Функция принимает на вход верные ответы и предсказания, а возвращает среднее гармоническое точности и полноты. Напечатайте результат на экране.
```python
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score
data = pd.read_csv('/datasets/travel_insurance_preprocessed.csv')

target = data['Claim']
features = data.drop('Claim', axis=1)
features_train, features_valid, target_train, target_valid = train_test_split(
    features, target, test_size=0.25, random_state=12345)

model = DecisionTreeClassifier(random_state=12345)
model.fit(features_train, target_train)
predicted_valid = model.predict(features_valid)

print(f1_score(target_valid, predicted_valid))
```
`0.069164265129683`

### [Урок 14 Заключение](https://practicum.yandex.ru/trainer/data-scientist/lesson/81772321-326a-4ddf-a67f-9ae48865f895/)

Вы научились измерять качество метрик и замечать ошибки в задачах.
В этой теме вы узнали:
-   Что такое дисбаланс классов;
-   Как строить матрицу ошибок предсказаний;
-   Зачем нужны точность, полнота и _F1_-мера.
В следующей теме вы научитесь избавляться от несбалансированных классов и получать более высокие значения _F1_-меры.
*Заберите с собой*

Чтобы ничего не забыть, [скачайте шпаргалку](https://code.s3.yandex.net/data-scientist/praktikum_data_scientist_takeaways_course7_theme3.pdf) и [конспект темы](https://code.s3.yandex.net/data-scientist/praktikum_data_scientist_abstract_course7_theme3.pdf).






