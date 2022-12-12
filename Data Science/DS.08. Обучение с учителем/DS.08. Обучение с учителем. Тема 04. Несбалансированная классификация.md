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

### [Урок 3 Несбалансированная классификация](https://practicum.yandex.ru/trainer/data-scientist/lesson/b990f044-59b7-42b7-9c82-79b7e9ac3be6/task/851cc0be-4bd3-4669-ab9c-0fe548696a95/)





#### Урок 3 Задача




