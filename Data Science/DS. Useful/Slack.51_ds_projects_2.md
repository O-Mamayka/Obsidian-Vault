
Флотация 
Мы тут находили такое видео которое описывает процесс: https://www.youtube.com/watch?v=BY9d1MC6qLs


неплохо может смотреться heatmap, он еще на значение смотрит: [https://seaborn.pydata.org/generated/seaborn.heatmap.html](https://seaborn.pydata.org/generated/seaborn.heatmap.html)


при использовании нескольких метрик, нужно указать метрику, относительно которой будет искаться лучшая модель. Это делается в параметре refit, т.е. вместо `refit=False` стоит указать метрику, например refit=‘f1’.
> Refit an estimator using the best found parameters on the whole dataset.  
> For multiple metric evaluation, this needs to be a `str` denoting the scorer that would be used to find the best parameters for refitting the estimator at the end.
Подробнее можно глянуть в документации по ссылкам:[https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.RandomizedSearchCV.html](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.RandomizedSearchCV.html)  
[https://scikit-learn.org/stable/modules/grid_search.html#randomized-parameter-search](https://scikit-learn.org/stable/modules/grid_search.html#randomized-parameter-search)  
[https://scikit-learn.org/stable/auto_examples/model_selection/plot_multi_metric_evaluation.html#sphx-glr-auto-examples-m[…]ulti-metric-evaluation-py](https://scikit-learn.org/stable/auto_examples/model_selection/plot_multi_metric_evaluation.html#sphx-glr-auto-examples-model-selection-plot-multi-metric-evaluation-py)


А в качестве бонуса - можно сделать совсем без цикла сугубо инструментами pandas, как предложено тут во втором ответе: [https://stackoverflow.com/questions/19966018/pandas-filling-missing-values-by-mean-in-each-group](https://stackoverflow.com/questions/19966018/pandas-filling-missing-values-by-mean-in-each-group) Когда можно уложиться в рекордные 9мс.

нашел такую штуку, там есть несколько способов как провернуть операцию: [https://stackoverflow.com/questions/21022865/pandas-elementwise-multiplication-of-two-dataframes](https://stackoverflow.com/questions/21022865/pandas-elementwise-multiplication-of-two-dataframes)

Как поменять dpi
1.  никогда не приходилось этого делать, из того, что удалось найти, можно подсмотреть для sns [тут](https://stackoverflow.com/questions/62537825/how-to-save-a-figure-with-high-dpi-resolution-using-seaborn). Можно выставить dpi при сохранении графика, для df.plot - [тут](https://stackoverflow.com/questions/48227792/how-to-change-dpi-of-my-pandas-dataframe-plot). Не совсем понял вопрос про разницу.
2.  По поводу медианы должно сработать `estimator=np.median` - [https://stackoverflow.com/questions/38799080/seaborne-bar-plot-median-estimator-error](https://stackoverflow.com/questions/38799080/seaborne-bar-plot-median-estimator-error)


попробуй такое решение, должно помочь:[https://stackoverflow.com/questions/23690284/pandas-apply-function-that-returns-multiple-values-to-rows-in-pandas-dataframe](https://stackoverflow.com/questions/23690284/pandas-apply-function-that-returns-multiple-values-to-rows-in-pandas-dataframe)

как сделать все короче и в одну строчку: [https://stackoverflow.com/questions/19966018/pandas-filling-missing-values-by-mean-in-each-group](https://stackoverflow.com/questions/19966018/pandas-filling-missing-values-by-mean-in-each-group) - обрати внимание на ответ, у которого 95 баллов - второй.


[https://www.geeksforgeeks.org/how-to-calculate-confidence-intervals-in-python/](https://www.geeksforgeeks.org/how-to-calculate-confidence-intervals-in-python/)
GeeksforGeeks
[How to Calculate Confidence Intervals in Python? - GeeksforGeeks](https://www.geeksforgeeks.org/how-to-calculate-confidence-intervals-in-python/)