## [Тема 01. Введение в курс](https://practicum.yandex.ru/learn/data-scientist/courses/b4c42b64-08d6-489c-b8da-bdaddb2b7386/sprints/43501/topics/03496afb-5c66-451a-9075-307a4fd82d0b/lessons/29935957-cdfa-47a2-ae34-c83b238354c9/)

В этом курсе вы познакомитесь с новыми метриками и случаями, в которых нужны классификация и регрессии. Научитесь настраивать модели машинного обучения, чтобы повысить значения метрик.
### Структура курса
Три темы курса посвящены задаче классификации, а последняя — регрессии.
В первых темах вы научитесь готовить признаки к анализу: преобразовывать категориальные признаки и улучшать количественные.
Затем построите модель и проверите, подходит ли для решения задачи _accuracy_. Поработаете с новыми метриками и улучшите их, чтобы решить задачу классификации при дисбалансе классов.
В последней теме вы познакомитесь с метриками регрессии. Узнаете их отличия, и в каких ситуациях они нужны.
В конце курса выполните самостоятельный проект: решая задачу классификации, научитесь прогнозировать отток клиентов банка.

### Ваши цели
-   Освоить новые метрики качества для задачи классификации: точность, полноту, _F1_-меру и _AUC-ROC._ Научиться вычислять их значения средствами библиотеки _scikit-learn_.
-   Уметь решать задачу классификации при дисбалансе классов. Например, взвешивать классы и настраивать пороги.
-   Разобраться, как устроены новые метрики качества для регрессии: _MAE_ и _R²_. Научиться их вычислять средствами библиотеки _scikit-learn_.


### [Урок 2 Проектная работа](https://practicum.yandex.ru/learn/data-scientist/courses/b4c42b64-08d6-489c-b8da-bdaddb2b7386/sprints/43501/topics/03496afb-5c66-451a-9075-307a4fd82d0b/lessons/da12fc71-38c8-4898-b672-5d82901b2a1e/)
### Описание проекта
Из «Бета-Банка» стали уходить клиенты. Каждый месяц. Немного, но заметно. Банковские маркетологи посчитали: сохранять текущих клиентов дешевле, чем привлекать новых.
Нужно спрогнозировать, уйдёт клиент из банка в ближайшее время или нет. Вам предоставлены исторические данные о поведении клиентов и расторжении договоров с банком.
Постройте модель с предельно большим значением _F1_-меры. Чтобы сдать проект успешно, нужно довести метрику до 0.59. Проверьте _F1_-меру на тестовой выборке самостоятельно.
Дополнительно измеряйте _AUC-ROC_, сравнивайте её значение с _F1_-мерой.

### Инструкция по выполнению проекта
1.  Загрузите и подготовьте данные. Поясните порядок действий.
2.  Исследуйте баланс классов, обучите модель без учёта дисбаланса. Кратко опишите выводы.
3.  Улучшите качество модели, учитывая дисбаланс классов. Обучите разные модели и найдите лучшую. Кратко опишите выводы.
4.  Проведите финальное тестирование.

### Описание данных
Данные находятся в файле `/datasets/Churn.csv` (англ. «отток клиентов»). [Скачать датасет](https://code.s3.yandex.net/datasets/Churn.csv)
**Признаки**
-   _RowNumber —_ индекс строки в данных
-   _CustomerId_ — уникальный идентификатор клиента
-   _Surname —_ фамилия
-   _CreditScore —_ кредитный рейтинг
-   _Geography —_ страна проживания
-   _Gender —_ пол
-   _Age —_ возраст
-   _Tenure —_ сколько лет человек является клиентом банка
-   _Balance —_ баланс на счёте
-   _NumOfProducts —_ количество продуктов банка, используемых клиентом
-   _HasCrCard —_ наличие кредитной карты
-   _IsActiveMember —_ активность клиента
-   _EstimatedSalary —_ предполагаемая зарплата

**Целевой признак**
-   _Exited_ — факт ухода клиента

На что обращают внимание ревьюер, проверяя проект:
-   Как вы готовите данные к обучению? Все ли типы признаков обрабатываете?
-   Хорошо ли поясняете этапы предобработки?
-   Как исследуете баланс классов?
-   Изучаете ли модель без учёта дисбаланса классов?
-   Какие выводы об исследовании задачи делаете?
-   Корректно ли разбиваете данные на выборки?
-   Как работаете с несбалансированными классами?
-   Правильно ли проводите обучение, валидацию и финальное тестирование модели?
-   Насколько высокое значение _F1_-меры получаете?
-   Изучаете ли значения метрики _AUC-ROC_?
-   Следите за структурой проекта и поддерживаете аккуратность кода?


