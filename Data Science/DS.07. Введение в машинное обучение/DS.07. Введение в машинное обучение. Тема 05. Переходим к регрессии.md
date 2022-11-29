## [Тема 05. Переходим к регрессии](https://practicum.yandex.ru/trainer/data-scientist/lesson/72e256e3-bbab-458d-860b-911da6071308/)
Узнаете, как решать задачи регрессии.
Оцените качество моделей регрессии по MSE.
Обучите в регрессии дерево решений, случайный лес и модель линейной регрессии.

### [Урок 2 Регрессия](https://practicum.yandex.ru/trainer/data-scientist/lesson/60f332c3-8944-486f-a769-0ecb3ccf0aed/)
Целевой признак (ответ) бывает категориальным и количественным. Если он категориальный, то решается задача классификации; если количественный — регрессии.

- Предсказать, какую максимальную сумму готов заплатить пассажир за такси. Целевой признак количественный, значит, это задача регрессии.
- Спрогнозировать, сколько будет продано билетов на утренние и вечерние киносеансы. 
Верно, ведь число билетов — это количественный целевой признак.
- В зависимости от посольства, типа разрешения на въезд и данных заявителя предсказать, сколько дней уйдёт на оформление визы. Да, найти, сколько дней, — это задача регрессии.

Цена квартиры — это количественный целевой признак. Значит, нужно решить задачу регрессии.

### [Урок 3 Средняя квадратичная ошибка](https://practicum.yandex.ru/trainer/data-scientist/lesson/60f332c3-8944-486f-a769-0ecb3ccf0aed/)
Какая метрика подходит для задачи регрессии? Средняя квадратичная ошибка! Полное, вплоть до последнего рубля, совпадение цены квартиры? Если абсолютная точность в задаче не важна, метрика `accuracy` не подходит.
Наиболее распространённая метрика качества в задаче регрессии — **средняя квадратичная ошибка**, _MSE_ (от англ. _Mean Squared Error_).
Ошибка объекта = Предсказания модели - Правильный ответ
![image|480](https://pictures.s3.yandex.net/resources/otklonenie_1574860449.jpg)
_MSE_ рассчитывается по схеме:
MSE = Сумма квадратов объектов ошибок / Количество объектов
Что значат вычисления?
1.  Ошибка объекта показывает, как сильно правильный ответ отличается от предсказания. Если ошибка намного больше нуля, модель квартиру переоценила; меньше — недооценила.
2.  Возведение в квадрат убирает разницу между переоценкой и недооценкой. Без этого шага нет смысла суммировать ошибки: положительные будут компенсировать отрицательные.
3.  Усреднение нужно, чтобы получить данные по всем объектам.
В прошлых уроках вы добивались наибольшего значения `accuracy`. Величина _MSE_, наоборот, должна быть как можно меньше.
Представьте, ваш стартап выходит на рынок Латинской Америки. Вы построили модель регрессии, которая спрогнозирует бюджеты рекламных кампаний. В таблице приведены предсказанные и реальные затраты.
Страна | Предсказание | Реальные затраты
-|-|-
 Бразилия | 623 | 649
 Перу | 253 | 253
Мексика | 150 | 370
Колумбия | 237 | 148
Посчитайте _MSE_ на калькуляторе или в Python. Не забыть возвести в квадрат.
14249.25 - Верно! Вот бы отправиться в командировки и проконтролировать бюджеты рекламных компаний на месте.

### [Урок 4 Расчёт MSE](https://practicum.yandex.ru/trainer/data-scientist/lesson/4130a0e1-73c6-49d7-81e8-646f2637fc90/task/3db3f9af-1943-46c7-a180-d33cb9271741/)
#### Урок 4. Задача 1
Напишите функцию `mse()`. На вход она принимает правильные ответы и предсказания, а возвращает значение средней квадратичной ошибки.
```python
import numpy as np
def mse(answers, predictions):
    mse = ((np.array(answers)-np.array(predictions))**2).sum()/len(answers) 
    return mse
answers = [623, 253, 150, 237]
predictions = [649, 253, 370, 148]
print(mse(answers, predictions))
```
#### Урок 4. Задача 2
Функция расчёта _MSE_ есть и в `sklearn`. [Найдите в документации](https://scikit-learn.org/stable/modules/classes.html) и импортируйте `mean_squared_error`, чтобы решить ту же задачу. Напечатайте на экране значение _MSE_.
```python
# импорт функцию расчёта MSE из библиотеки sklearn >
from sklearn.metrics import mean_squared_error
answers = [623, 253, 150, 237]
predictions = [649, 253, 370, 148]
result = mean_squared_error(answers, predictions)
print(result)
```

### [Урок 5 Интерпретация MSE](https://practicum.yandex.ru/trainer/data-scientist/lesson/87951a4e-a61b-42e6-ac88-33a283d21507/task/8695ac61-2197-4089-8418-819e86a62c78/)
Чтобы оценить адекватность модели в задачах классификации, нужно сравнить её со случайной. Как проверить модель регрессии на вменяемость?
Отвечать на все объекты одним и тем же числом — простой способ регрессионного предсказания. Чтобы оно не сильно расходилось с правдой, примем за такое число среднее значение цены квартиры.

Подготовьте набор данных и найдите среднее значение цены:
-   Создайте переменную `features` со всеми признаками, кроме `last_price`.
-   Создайте переменную `target` с целевым признаком `last_price`. Поделите его значение на 1 миллион.
-   Посчитайте среднее значение по элементам переменной `target`.
```python
import pandas as pd
from sklearn.metrics import mean_squared_error
df = pd.read_csv('/datasets/train_data.csv')

# создание переменных features и target >
features = df.drop(['last_price'], axis = 1)
target =  df['last_price']/1000000
print('Средняя цена:',target.mean())
```
#### Урок 5. Задача 2
Найдите _MSE_ по обучающей выборке, чтобы средней ценой предсказать ответ. Предсказания запишите в переменную `predictions`.
Функция `mean_squared_error` в `sklearn` довольно капризная. Придётся поработать с документацией или _Stack Overflow_.
Функция `mean_squared_error` принимает только последовательности. Создать последовательность из средних значений можно так: `pd.Series(target.mean(), index=target.index) `
```python
import pandas as pd
from sklearn.metrics import mean_squared_error
df = pd.read_csv('/datasets/train_data.csv')

features = df.drop(['last_price'], axis=1)
target = df['last_price'] / 1000000
predictions = pd.Series(target.mean(), target.index)
# < найдите MSE >
mse = mean_squared_error(target,predictions)
print("MSE:", mse)
```
#### Урок 5. Задача 3
«Квадратные рубли» нам ни к чему. Чтобы метрика показывала просто рубли, возьмите корень от _MSE_. Это величина _RMSE_ (англ. _root mean squared error_, «корень из средней квадратичной ошибки»). Напечатайте результат на экране в таком формате:
Корень из числа извлеките операцией возведения в степень `**`. Число возведите в степень `0.5`. Например:
```python
rmse = mse**0.5
print("RMSE:", rmse)
```
`RMSE: 11.757737744151`

### [Урок 6 Дерево решений в регрессии](https://practicum.yandex.ru/trainer/data-scientist/lesson/ff0b4597-a6fb-49df-b52d-b0ff0578c5bf/task/89ccb93a-4889-407e-97e5-7017ddbaf8a4/)
Решающее дерево подходит не только для задач классификации, но и для регрессии.
Дерево в задаче регрессии обучается так же, только предсказывает оно не класс, а число.
К примеру, Ваня всё-таки поехал в отпуск в Иваново. Во сколько ему обойдётся билет в музей ивановского ситца?
![image|320](https://pictures.s3.yandex.net/resources/bilet_1577278582.jpg)
#### Урок 6. Задача 1
-   Выделите 25% данных для валидационной выборки, остальные — для обучающей.
-   Обучите модели дерева решений для задачи регрессии с различными значениями глубины от 1 до 5.
-   Для каждой модели посчитайте значение метрики _RMSE_ на валидационной выборке.
-   Сохраните модель с наилучшим значением _RMSE_ на валидационной выборке в переменной `best_model`.
```python
import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
df = pd.read_csv('/datasets/train_data.csv')

features = df.drop(['last_price'], axis=1)
target = df['last_price'] / 1000000
# отделите 25% данных для валидационной выборки
features_train, features_valid, target_train, target_valid = train_test_split(features, target, test_size=0.25, random_state=12345) 

best_model = None
best_result = 10000
best_depth = 0
for depth in range(1, 6):
	# инициализируйте модель DecisionTreeRegressor с параметром random_state=12345 и max_depth=depth
    model = DecisionTreeRegressor(random_state=12345, max_depth=depth) 
    model.fit(features_train,target_train) # обучите модель на тренировочной выборке
    predictions_valid = model.predict(features_valid) # получите предсказания модели на валидационной выборке
    result = mean_squared_error(target_valid,predictions_valid)**0.5
    # посчитайте значение метрики rmse на валидационной выборке
    if result < best_result:
        best_model = model
        best_result = result
        best_depth = depth

print("RMSE наилучшей модели на валидационной выборке:", best_result, "Глубина дерева:", best_depth)
```

### [Урок 7 Случайный лес в регрессии](https://practicum.yandex.ru/trainer/data-scientist/lesson/36431774-6c48-46d0-91f8-5369b182f57c/task/bdb4a898-3ef3-4646-a2fa-f35385c03dc1/)
Где одно дерево, там и лес. Разберёмся, как обучить модель случайного леса в регрессии.
Случайный лес для регрессии не сильно меняется. Он обучает множество независимых деревьев, а потом принимает решение, усредняя их ответы.
#### Урок 7. Задача 1
-   Извлеките признаки для обучения в `features`, а целевой признак `last_price` поделите на `1000000` и сохраните в переменную `target`.
-   Выделите 25% данных для валидационной (тестовой) выборки, остальные — для обучающей.
-   Обучите модели случайного леса для задачи регрессии:
    - с количеством деревьев: от 10 до 50 с шагом 10,
    -   с максимальной глубиной от 1 до 10.
-   Для каждой модели посчитайте _RMSE_ на валидационной выборке.
-   Сохраните модель с наилучшим значением _RMSE_ на валидационной выборке в переменной `best_model`.
Код может выполняться около минуты. Это нормально, ведь вы обучаете 50 моделей.
С помощью метода `drop` извлеките все признаки, кроме `last_price`: `df.drop(['last_price'])`.
```python
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
df = pd.read_csv('/datasets/train_data.csv')

features = df.loc[:,'total_area':]# извлеките признаки
target = df['last_price']/1000000# извлеките целевой признак

features_train, features_valid, target_train, target_valid = train_test_split(features, target, test_size=0.25, random_state=12345)

best_model = None
best_result = 10000
best_est = 0
best_depth = 0
for est in range(10, 51, 10):
    for depth in range (1, 11):
        model = RandomForestRegressor(random_state=12345, n_estimators=est, max_depth=depth)# инициализируйте модель RandomForestRegressor с параметрами random_state=12345, n_estimators=est и max_depth=depth
        model.fit(features_train,target_train) # обучите модель на тренировочной выборке
        
        predictions_valid = model.predict(features_valid) # получите предсказания модели на валидационной выборке
        result = mean_squared_error(target_valid,predictions_valid)**0.5# посчитайте значение метрики rmse на валидационной выборке
        if result < best_result:
            best_model = model
            best_result = result
            best_est = est
            best_depth = depth
print("RMSE наилучшей модели на валидационной выборке:", best_result, "Количество деревьев:", best_est, "Максимальная глубина:", depth)
```

### [Урок 8 Линейная регрессия](https://practicum.yandex.ru/trainer/data-scientist/lesson/14e29275-7f3d-4fdb-98e7-ab56297762ab/task/a55c242d-5b34-4637-a3ed-13b4dd885a9b/)
Какой алгоритм заменит логистическую регрессию? Линейная!
**Линейная регрессия** похожа на логистическую. Название пришло из линейной алгебры, которой будет посвящён отдельный курс. Стоимость предсказывается, к примеру, по такой формуле: цена = площадь * 150000 р/м2 - (растояние до центра) * 200 р/м
![image](https://pictures.s3.yandex.net/resources/Screenshot_2019-11-03_at_02.01.41_1572736038.png)
Здесь учтены только два параметра: площадь и отдалённость от центра. Стоимость каждого квадратного метра — 150 000 р. По мере удаления от центра каждый метр снижает цену на 200 р.
Из-за малого количества параметров линейная регрессия менее склонна к переобучению, чем, например, деревья решений.
#### Урок 8. Задача 1
Извлеките признаки для обучения в переменную `features` и целевой признак `last_price` в переменную `target`. Поделите значение целевого признака на `1000000`.
Инициализируйте модель линейной регрессии, обучите её. Посчитайте значение метрики _RMSE_ на валидационной выборке и сохраните в переменной `result`.
```python
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
df = pd.read_csv('/datasets/train_data.csv')

features = df.drop('last_price', axis=1) # извлеките признаки 
target = df['last_price']/1000000 # извлеките целевой признак

features_train, features_valid, target_train, target_valid = train_test_split(features,target, test_size=0.25, random_state=12345) # отделите 25% данных для валидационной выборки
# !!!!!!!! 
model = LinearRegression() # инициализируйте модель LinearRegression
model.fit(features_train,target_train) # обучите модель на тренировочной выборке
predictions_valid = model.predict(features_valid) # получите предсказания модели на валидационной выборке

result = mean_squared_error(target_valid,predictions_valid)**0.5 # посчитайте значение метрики RMSE на валидационной выборке
print("RMSE модели линейной регрессии на валидационной выборке:", result)
```
`RMSE модели линейной регрессии на валидационной выборке: 7.726006697008267`

### [Урок 9 Выбираем лучшую модель](https://practicum.yandex.ru/trainer/data-scientist/lesson/14e29275-7f3d-4fdb-98e7-ab56297762ab/task/a55c242d-5b34-4637-a3ed-13b4dd885a9b/)
Вы обучили дерево решений, случайный лес и линейную регрессию. Чтобы найти модель с наименьшей ошибкой:
1.  Рассмотрите наилучшие модели, получившиеся в предыдущих заданиях.
2.  Для каждой модели запишите параметры и значения _RMSE_ на валидационной выборке.
3.  Опираясь на значения _RMSE_, выберите наилучшую модель. Напомним, от вас скрыты данные, которые служат для тестирования качества модели. Поэтому не все модели пройдут: значения метрики на валидационной и тестовой выборке могут сильно отличаться.
4.  На основе выбранной модели замените пропуски в шаблоне кода. Нажмите «Проверить».
#### Урок 9. Задача 1
Найдите модель, у которой на тестовой выборке RMSE не больше 7.3:
1.  Извлеките целевой признак в переменную `target`, а остальные — в `features`.
2.  Отделите 25% данных для валидационной выборки. Для этого передайте `train_test_split` признаки и значение аргумента `test_size`.
3.  Инициируйте ту модель, которая показала лучшее значение RMSE в прошлых уроках.
4.  С помощью метода `.fit()` обучите модель на тренировочной выборке.
5.  Получите предсказания модели на валидационной выборке методом `.predict()`.
6.  Посчитайте значение метрики RMSE на валидационной выборке и сохраните его в переменную `result`.
На валидационной выборке наилучшее значение показала модель дерева решений. Но на тестовой выборке её результат хуже. Поэтому попробуйте наилучшую модель случайного леса.
```python
import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
df = pd.read_csv('/datasets/train_data.csv')

features = df.drop('last_price', axis=1)# извлеките признаки 
target = df['last_price']/1000000# извлеките целевой признак

features_train, features_valid, target_train, target_valid = train_test_split(features,target,test_size=0.25, random_state=12345) # отделите 25% данных для валидационной выборки
model = RandomForestRegressor(random_state=12345,n_estimators=40, max_depth=10)#  инициализируйте модель с наилучшим значением метрики RMSE
model.fit(features_train,target_train) # обучите модель на тренировочной выборке
predictions_valid = model.predict(features_valid) # получите предсказания модели на валидационной выборке

result = mean_squared_error(target_valid,predictions_valid)**0.5# посчитайте значение метрики RMSE на валидационной выборке
print("RMSE наилучшей модели на валидационной выборке:", result)
'''
model = LinearRegression()#  инициализируйте модель с наилучшим значением метрики RMSE
model.fit(features_train,target_train) # обучите модель на тренировочной выборке
predictions_valid = model.predict(features_valid) # получите предсказания модели на валидационной выборке

result = mean_squared_error(target_valid,predictions_valid)**0.5# посчитайте значение метрики RMSE на валидационной выборке
print("RMSE наилучшей модели на валидационной выборке:", result)
'''
```

### [Урок 10 Заключение](https://practicum.yandex.ru/trainer/data-scientist/lesson/6a9074fa-bd37-4203-a8f0-14e72a774366/)
### Чему научились:
-   Обучать в регрессии дерево решений, случайный лес и линейную регрессию;
-   Рассчитывать _MSE_;
-   Сравнивать качество моделей регрессии.
Вы провели первое исследование и подготовили прототип решения задачи. Не переживайте, что не добились нулевой ошибки: в машинном обучении такого практически не бывает. 

### Заберите с собой
Чтобы ничего не забыть, [скачайте шпаргалку](https://code.s3.yandex.net/data-analyst/conspects/praktikum_data_scientist_takeaways_course6_theme5.pdf) и [конспект темы](https://code.s3.yandex.net/data-analyst/conspects/praktikum_data_scientist_abstract_course6_theme5.pdf).
























