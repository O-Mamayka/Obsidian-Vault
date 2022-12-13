## [Тема 04. Несбалансированная классификация](https://practicum.yandex.ru/trainer/data-scientist/lesson/72cf2552-e9b0-4e7d-885e-aa55cc45843c/)

Значения метрик из прошлой темы были близки к нулю. Поможем модели!
-   Чтобы увеличить качество модели при дисбалансе классов, освоите техники: взвешивание классов, _upsampling_ и _downsampling_.
-   Настраивать метрики классификации, учитывая вероятности классов.
-   Строить _ROC_-кривую и вычислять площадь под ней.

### [Урок 2 Взвешивание классов](https://practicum.yandex.ru/trainer/data-scientist/lesson/eeae1c6a-9784-4436-99c1-36b6e731ca4b/task/15fef92f-2594-4e4a-8076-a538afd4f47c/)

Придадим объектам редкого класса больший вес.
Например, вы готовитесь к экзаменам и проходите тест. За решение одного вида задач вы получите один балл, другого — два. Чтобы получить более высокую оценку, вы сосредоточились только на «двухбалльных» задачах. Так и модели проще запоминать объекты бóльшей значимости.
Алгоритмы машинного обучения считают все объекты обучающей выборки равнозначными по умолчанию. Если важно указать, что какие-то объекты важнее, их классу присваивается **вес** (англ. _class_weight,_ «вес класса»).
В алгоритме логистической регрессии в библиотеке _sklearn_ есть аргумент _class_weight_. По умолчанию он равен `None`, т. е. классы равнозначны:
`вес класса «0» = 1.0`
`вес класса «1» = 1.0`
Если указать `class_weight='balanced'` (англ. «сбалансированный»), алгоритм посчитает, во сколько раз класс «0» встречается чаще класса «1». Обозначим это число _N_ (неизвестное количество раз). Новые веса классов выглядят так:
`вес класса «0» = 1.0`
`вес класса «1» = N`
Бóльший вес будет у редкого класса.
Аргумент _class_weight_ также есть у решающего дерева и случайного леса.

#### Урок 3 Задача
Код обучения логистической регрессии с равнозначными классами из прошлых уроков. Сделайте веса классов сбалансированными. Обратите внимание, как изменится значение _F1_-меры.
Добавьте логистической регрессии аргумент `class_weight='balanced'`
```python
import pandas as pd
from sklearn.metrics import f1_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
data = pd.read_csv('/datasets/travel_insurance_preprocessed.csv')

target = data['Claim']
features = data.drop('Claim', axis=1)
features_train, features_valid, target_train, target_valid = train_test_split(
    features, target, test_size=0.25, random_state=12345)

model = LogisticRegression(random_state=12345, 
						   solver='liblinear', class_weight='balanced')
model.fit(features_train, target_train)
predicted_valid = model.predict(features_valid)
print("F1:", f1_score(target_valid, predicted_valid))
```
`F1: 0.08698830409356724`

### [Урок 3 Увеличение выборки](https://practicum.yandex.ru/trainer/data-scientist/lesson/b990f044-59b7-42b7-9c82-79b7e9ac3be6/task/851cc0be-4bd3-4669-ab9c-0fe548696a95/)

Как сделать объекты редкого класса не такими редкими в данных?
Теперь в тесте за решение любой задачи вы получаете 1 балл. Самые важные задачи повторяются по несколько раз, чтобы их легче запомнить.
Когда обучают модели, такая техника называется **upsampling** (от англ. _up_, «вверх»; _sampling_, «выборка»).
Преобразование проходит в несколько этапов:
-   Разделить обучающую выборку на отрицательные и положительные объекты;
-   Скопировать несколько раз положительные объекты;
-   С учётом полученных данных создать новую обучающую выборку;
-   Перемешать данные: идущие друг за другом одинаковые вопросы не помогут обучению.
Скопировать объекты несколько раз поможет синтаксис умножения списков в Python. Чтобы повторить элементы списка, он умножается на число (нужное количество раз):
```PYTHON
answers = [0, 1, 0]
print(answers)
answers_x3 = answers * 3
print(answers_x3) 
```
`[0, 1, 0, 0, 1, 0, 0, 1, 0]`

#### Урок 3 Задача 1
Мы разделили обучающую выборку на отрицательные и положительные объекты.
Объявите четыре переменные и запишите в них:
-   _features_zeros_ — признаки объектов с ответом «0»;
-   _features_ones_ — признаки объектов с ответом «1»;
-   _target_zeros_ — целевой признак объектов, у которых ответы только «0»;
-   _target_ones_ — целевой признак объектов, у которых ответы только «1».
Напечатайте на экране размеры таблиц, которые хранятся в четырёх переменных.
```python
import pandas as pd
from sklearn.model_selection import train_test_split
data = pd.read_csv('/datasets/travel_insurance_preprocessed.csv')

target = data['Claim']
features = data.drop('Claim', axis=1)
features_train, features_valid, target_train, target_valid = train_test_split(
    features, target, test_size=0.25, random_state=12345)

features_zeros = features_train[target_train==0]
features_ones = features_train[target_train==1]
target_zeros = target_train[target_train == 0]
target_ones = target_train[target_train == 1]

print(features_zeros.shape) #(37411, 196)
print(features_ones.shape) #(584, 196)
print(target_zeros.shape) #(37411,)
print(target_ones.shape) #(584,)
```

#### Урок 3 Задача 2
Продублируйте объекты положительного класса и объедините их с объектами отрицательного класса. Чтобы соединить таблицы, воспользуйтесь функцией **pd.concat()** (от англ. _concatenate_, «сцепить»). Поработайте с документацией.
Мы объединили таблицы с признаками и сохранили результат в переменной _features_upsampled_ (признаки, преобразованные техникой _upsampling_). Сделайте то же самое для целевого признака и объявите переменную _target_upsampled_ (целевой признак, преобразованный техникой _upsampling_).
Количество повторений уже сохранено в переменной _repeat_ (англ. «повторять»).
Напечатайте на экране размеры новых переменных.
Функция _concat()_ на вход получает список таблиц, которые нужно соединить.
Если применить умножение списков, получится таблица с продублированными положительными объектами.
```python
import pandas as pd
from sklearn.model_selection import train_test_split
data = pd.read_csv('/datasets/travel_insurance_preprocessed.csv')

target = data['Claim']
features = data.drop('Claim', axis=1)
features_train, features_valid, target_train, target_valid = train_test_split(
    features, target, test_size=0.25, random_state=12345)

features_zeros = features_train[target_train == 0]
features_ones = features_train[target_train == 1]
target_zeros = target_train[target_train == 0]
target_ones = target_train[target_train == 1]

repeat = 10
features_upsampled = pd.concat([features_zeros] + [features_ones] * repeat)
target_upsampled = pd.concat([target_zeros]+[target_ones]*repeat)
print(features_upsampled.shape) #(43251, 196)
print(target_upsampled.shape) #(43251,)
```

#### Урок 3 Задача 3
Перемешайте данные. Импортируйте функцию `shuffle()` (англ. «перетасовать») из модуля `sklearn.utils` (от англ. «утилиты»).
Создайте функцию `upsample()` с тремя параметрами:
-   `features` — признаки,
-   `target` — целевой признак,
-   `repeat` — количество повторений.
Функция вернёт признаки и целевой признак после операции `upsampling`.
Вызовите функцию для обучающих данных. Если всё будет верно, размеры преобразованных выборок появятся на экране.
```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.utils import shuffle

data = pd.read_csv('/datasets/travel_insurance_preprocessed.csv')

target = data['Claim']
features = data.drop('Claim', axis=1)
features_train, features_valid, target_train, target_valid = train_test_split(
    features, target, test_size=0.25, random_state=12345)

def upsample(features_train,target_train,repeat):
    features_zeros = features_train[target_train == 0]
    features_ones = features_train[target_train == 1]
    target_zeros = target_train[target_train == 0]
    target_ones = target_train[target_train == 1]
    repeat = 10
    features_upsampled = pd.concat([features_zeros] + [features_ones] * repeat)
    target_upsampled = pd.concat([target_zeros] + [target_ones] * repeat)
    features_upsampled,target_upsampled = shuffle(features_upsampled, target_upsampled,random_state=12345)
    return features_upsampled, target_upsampled

features_upsampled, target_upsampled = upsample(features_train, target_train, 10)
print(features_upsampled.shape) #(43251, 196)
print(target_upsampled.shape) #(43251,)
```

#### Урок 3 Задача 4
Обучите на новых данных модель `LogisticRegression`. Найдите для неё значение F1-меры, и выведете её на экран.
Вызовите `fit()` с аргументами `features_upsampled`, `target_upsampled`. Затем вызовите _predict()_ с аргументом `features_valid`.
Добавьте к логистической регрессии аргумент `solver='liblinear'`.
```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.utils import shuffle
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import f1_score
data = pd.read_csv('/datasets/travel_insurance_preprocessed.csv')

target = data['Claim']
features = data.drop('Claim', axis=1)
features_train, features_valid, target_train, target_valid = train_test_split(
    features, target, test_size=0.25, random_state=12345)

def upsample(features, target, repeat):
    features_zeros = features[target == 0]
    features_ones = features[target == 1]
    target_zeros = target[target == 0]
    target_ones = target[target == 1]
    features_upsampled = pd.concat([features_zeros] + [features_ones] * repeat)
    target_upsampled = pd.concat([target_zeros] + [target_ones] * repeat)
    
    features_upsampled, target_upsampled = shuffle(
        features_upsampled, target_upsampled, random_state=12345)
    
    return features_upsampled, target_upsampled

features_upsampled, target_upsampled = upsample(features_train, target_train, 10)
model = LogisticRegression(random_state=12345, solver = 'liblinear')
model.fit(features_upsampled,target_upsampled)
predicted_valid = model.predict(features_valid)

print("F1:", f1_score(target_valid, predicted_valid)) #F1: 0.13714285714285715
```

### [Урок 4 Уменьшение выборки](https://practicum.yandex.ru/trainer/data-scientist/lesson/6c3729c5-d296-4777-8c85-ffcdf84e23ff/task/d1c49d29-7ede-4b72-bb47-6d144e01e33f/)
Как сделать объекты частого класса не такими частыми? Вместо повторения важных вопросов убрать часть неважных. Это можно сделать техникой downsampling (от англ. _down_ — «вниз»; _sampling_ — «выборка»).

Преобразование проходит в несколько этапов:
-   Разделить обучающую выборку на отрицательные и положительные объекты;
-   Случайным образом отбросить часть из отрицательных объектов;
-   С учётом полученных данных создать новую обучающую выборку;
-   Перемешать данные. Положительные не должны идти следом за отрицательными: алгоритмам будет сложнее обучаться.
Чтобы выбросить из таблицы случайные элементы, примените функцию `sample()`. На вход она принимает аргумент `frac` (от англ. _fraction_, «доля»). Возвращает случайные элементы в таком количестве, чтобы их доля от исходной таблицы была равна `frac`.
```PYTHON
print(features_train.shape)
features_sample = features_train.sample(frac=0.1, random_state=12345)
print(features_sample.shape) 
```
`(3800, 196)` Чтобы ваши результаты сошлись с нашими, указывайте `random_state=12345`.

#### Урок 4 Задача
Чтобы выполнить downsampling, напишите функцию `downsample()` с тремя аргументами:
-   `features` — признаки;
-   `target` — целевой признак;
-   `fraction` — доля отрицательных объектов, которые нужно сохранить.
Функция вернёт признаки и целевой признак после операции `downsampling`. Вызовите функцию для обучающих данных с аргументом `fraction`, равным 0.1. Код выведет на экран размеры выборок.
Переменная `features_downsampled` создаётся так:  `features_downsampled = pd.concat( [features_zeros.sample(frac=fraction, random_state=12345)] + [features_ones])`. Не забывайте перемешивать данные.
```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.utils import shuffle
data = pd.read_csv('/datasets/travel_insurance_preprocessed.csv')

target = data['Claim']
features = data.drop('Claim', axis=1)
features_train, features_valid, target_train, target_valid = train_test_split(
    features, target, test_size=0.25, random_state=12345)

def downsample(features, target, fraction):
    features_zeros = features[target == 0]
    features_ones = features[target == 1]
    target_zeros = target[target == 0]
    target_ones = target[target == 1]
    features_downsampled = pd.concat([features_zeros.sample(frac=fraction, random_state=12345)] + [features_ones])
    target_downsampled = pd.concat([target_zeros.sample(frac=fraction, random_state=12345)]+[target_ones])
    features_downsampled,target_downsampled = shuffle(features_downsampled, target_downsampled, random_state=12345)
    return features_downsampled, target_downsampled

features_downsampled, target_downsampled = downsample(features_train, target_train, 0.1)
print(features_downsampled.shape) #(4325, 196)
print(target_downsampled.shape) #(4325,)
```
#### Урок 4 Задача 2
Обучите на новых данных модель LogisticRegression. Найдите для неё значение _F1_-меры, и код выведет его на экран.
```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.utils import shuffle
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import f1_score
data = pd.read_csv('/datasets/travel_insurance_preprocessed.csv')

target = data['Claim']
features = data.drop('Claim', axis=1)
features_train, features_valid, target_train, target_valid = train_test_split(
    features, target, test_size=0.25, random_state=12345)

def downsample(features, target, fraction):
    features_zeros = features[target == 0]
    features_ones = features[target == 1]
    target_zeros = target[target == 0]
    target_ones = target[target == 1]
    features_downsampled = pd.concat(
        [features_zeros.sample(frac=fraction, random_state=12345)] + [features_ones])
    target_downsampled = pd.concat(
        [target_zeros.sample(frac=fraction, random_state=12345)] + [target_ones])
    features_downsampled, target_downsampled = shuffle(
        features_downsampled, target_downsampled, random_state=12345)
    return features_downsampled, target_downsampled

features_downsampled, target_downsampled = downsample(features_train, target_train, 0.1)

model = LogisticRegression(random_state=12345, solver = 'liblinear')
model.fit(features_downsampled, target_downsampled)
predicted_valid = model.predict(features_valid)
print("F1:", f1_score(target_valid, predicted_valid)) #F1: 0.13333333333333333
```

### [Урок 5 Порог классификации](https://practicum.yandex.ru/trainer/data-scientist/lesson/f9340f80-654e-4c5a-a1f4-2bd119c1f974/)

Как лучше обучать логистическую регрессию? Посмотрим, что у неё внутри.
Чтобы определить ответ, логистическая регрессия вычисляет, к какому классу близок объект, затем сравнивает результат с нулём. Для удобства близость к классам переведём в **вероятность классов**: модель пытается оценить, насколько вероятен тот или иной класс. У нас всего два класса (ноль и единица). Нам достаточно вероятности класса «1». Число будет от нуля до единицы: если больше 0.5 — объект положительный, меньше — отрицательный.
Граница, где заканчивается отрицательный класс и начинается положительный, называется **порогом** (англ. _threshold_). По умолчанию он равен 0.5, но что если его поменять?
![image|480](https://pictures.s3.yandex.net/resources/Ordinal-baa29295-dc33-41c8-ab76-db4513959184_1573942093.jpg)
Как поменяется точность и полнота, если уменьшить порог?
Точность уменьшится, а полнота увеличится
Наоборот, увеличивая пороговую вероятность, мы увеличиваем точность, но снижаем полноту.

### [Урок 6 Изменение порога](https://practicum.yandex.ru/trainer/data-scientist/lesson/fa8cd087-0ba9-4586-900a-30f5ca020aee/task/29728a37-e47d-4981-b8eb-f0ccfac56354/)
Изменим значение порога и посмотрим, какими станут метрики.
В библиотеке _sklearn_ вероятность классов вычисляет функция **predict_proba()** (от англ. _predict probabilities_, «предсказать вероятности»). На вход она получает признаки объектов, а возвращает вероятности:
```python
probabilities = model.predict_proba(features) 
```
Строки соответствуют объектам. В первом столбце указана вероятность отрицательного класса, а во втором — положительного (сумма вероятностей равна единице). Выведем их на экран.
```
[[0.5795 0.4205]
 [0.6629 0.3371]
 [0.7313 0.2687]
 [0.6728 0.3272]
 [0.5086 0.4914]] 
```
Для решающего дерева и случайного леса в _sklearn_ тоже есть функция _predict_proba()_.

#### Урок 6 Задача 1
Найдите значения вероятностей классов для валидационной выборки. Значения вероятностей класса «1» сохраните в переменной _probabilities_one_valid_. Напечатайте на экране первые пять элементов этой переменной.
```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

data = pd.read_csv('/datasets/travel_insurance_preprocessed.csv')
target = data['Claim']
features = data.drop('Claim', axis=1)
features_train, features_valid, target_train, target_valid = train_test_split(
    features, target, test_size=0.25, random_state=12345)
model = LogisticRegression(random_state=12345, solver='liblinear')
model.fit(features_train, target_train)
#prid = model.predict(features_valid)
probabilities_valid = model.predict_proba(features_valid)
probabilities_one_valid = probabilities_valid[:,-1] 

print(probabilities_one_valid[:5])
```
`[0.01854999 0.00952462 0.00419866 0.00157633 0.00956128]`

#### Урок 6 Задача 2
Переберите значения порогов от 0 до 0.3 с шагом 0.02. Найдите для каждого значения точность и полноту. Напечатайте результаты на экране.
Чтобы создать цикл с нужным диапазоном, мы применили функцию _arange()_ (от англ. «упорядочивать») библиотеки _numpy_. Как и _range()_, функция перебирает указанные элементы диапазона, но работает не только с целыми, но и дробными числами.
Средства библиотеки _numpy_ вы ещё изучите.
Предсказания модели `predicted_valid` — это булев массив, состоящий из _True_ (класс «1») и _False_ (класс «0»).
Чтобы найти нужный класс, оператором `>` сравните значения вероятностей класса «1» с порогом:
`predicted_valid = probabilities_one_valid > threshold`
```python
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import precision_score, recall_score
data = pd.read_csv('/datasets/travel_insurance_preprocessed.csv')

target = data['Claim']
features = data.drop('Claim', axis=1)
features_train, features_valid, target_train, target_valid = train_test_split(
    features, target, test_size=0.25, random_state=12345)
model = LogisticRegression(random_state=12345, solver='liblinear')
model.fit(features_train, target_train)
probabilities_valid = model.predict_proba(features_valid)
probabilities_one_valid = probabilities_valid[:, 1]

for threshold in np.arange(0, 0.3, 0.02):
    predicted_valid = probabilities_one_valid>threshold
    precision = precision_score(target_valid,predicted_valid) 
    recall = recall_score(target_valid,predicted_valid)
    print("Порог = {:.2f} | Точность = {:.3f}, Полнота = {:.3f}".format(
        threshold, precision, recall))
```
Порог = 0.00 | Точность = 0.013, Полнота = 1.000
Порог = 0.02 | Точность = 0.052, Полнота = 0.645
...
Порог = 0.28 | Точность = 0.000, Полнота = 0.000

### [Урок 7 PR-кривая](https://practicum.yandex.ru/trainer/data-scientist/lesson/86f9012b-afa7-41b2-b7ac-439222b6697b/)

Изобразим на графике, как выглядят значения метрик при изменении порога.
На графике по вертикали наносится значение точности, по горизонтали — полноты. Кривая, показывающая их значения, называется **PR-кривой** (от англ. _**P**recision_ и _**R**ecall_). Чем выше кривая, тем лучше модель.
![image|360](https://pictures.s3.yandex.net/resources/Untitled-4811aecf-fbc3-4549-9aa9-24c82b4f4c5e_1573942584.png)
Интересно посмотреть, как получили график? Вот код:
```PYTHON
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import precision_recall_curve
from sklearn.linear_model import LogisticRegression
data = pd.read_csv('/datasets/travel_insurance_preprocessed.csv')

target = data['Claim']
features = data.drop('Claim', axis=1)
features_train, features_valid, target_train, target_valid = train_test_split(
    features, target, test_size=0.25, random_state=12345)
model = LogisticRegression(random_state=12345, solver='liblinear')
model.fit(features_train, target_train)
probabilities_valid = model.predict_proba(features_valid)
precision, recall, thresholds = precision_recall_curve(target_valid, probabilities_valid[:, 1])

plt.figure(figsize=(6, 6))
plt.step(recall, precision, where='post')
plt.xlabel('Recall')
plt.ylabel('Precision')
plt.ylim([0.0, 1.05])
plt.xlim([0.0, 1.0])
plt.title('Кривая Precision-Recall')
plt.show() 
```
Смысл этого кода подробно разбирается в уроке 9.

### [Урок 8 TPR и FPR](https://practicum.yandex.ru/trainer/data-scientist/lesson/de2e4433-6a26-43e9-8b90-d8870a8c377f/)

Когда положительных объектов нет, точность не вычислить. Выберем другие характеристики, в которых нет деления на ноль.
Прежде чем перейти к новой кривой, дадим несколько важных определений.
Как измерить, насколько правильно классификатор находит объекты? Долей верно предсказанных объектов к общему числу объектов класса. Это отношение называется `TPR` (англ. _True Positive Rate_) или «полнота», а на английском используют термин _recall_. Формула выглядит так, где `P = TP + FN`.
`TPR = TP / P`
Доля ложных срабатываний к общему числу объектов за пределами класса (англ. False Positive Rate, FPR) вычисляется аналогично. Это отношение FP-ответов (англ. _False Positives_ — отрицательные, классифицированные как положительные) к сумме отрицательных ответов: `FP и TN` (англ. _True Negatives_ — верно классифицированные отрицательные ответы). Ниже дана формула, где `N=FP+TN`:
`FPR = FP / N`
Деления на ноль не будет: в знаменателях значения, которые постоянны и не зависят от изменения модели.
Как изменится величина _TPR_, если уменьшить порог в логистической регрессии?
- Увеличится
Положительных ответов станет больше, значит, истинно положительных — тоже.

Как изменится величина _FPR_, если уменьшить порог в логистической регрессии?
Не поменяется
Тоже правильный ответ
Увеличится
Положительных ответов станет больше, значит, ложноположительных — тоже.

### [Урок 9 ROC-кривая](https://practicum.yandex.ru/trainer/data-scientist/lesson/62fbf7ea-ef66-49a9-915c-37cfec100822/task/964953a1-a4ad-4a7d-b6f3-86b296b5a6c3/)



#### Урок 3 Задача











