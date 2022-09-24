  
5.

Теперь можно разделить все сети на две группы: «Большая восьмёрка» и «Другие». Вторая группа будет восприниматься как одна большая сеть.

Лучшие показатели средней продолжительности заправки содержатся в таблице `good_stat2` и рассчитываются по данным `station_stat_full` (просмотрите код, чтобы вспомнить эти вычисления). Повторите вычисления, но вместо того, чтобы группировать данные по столбцу `name`, сгруппируйте данные по новому столбцу, содержащему категорию `Другие`. Чтобы создать этот столбец в таблице `station_stat_full`, примените метод `where()` для сравнения столбца `name` в `station_stat_full` с индексами `big_nets_stat`.

Выполните следующие шаги:

1.  Добавьте в таблицу `station_stat_full` новый столбец `group_name`.
2.  Поместите в столбец `group_name` значения столбца `name`, если сеть присутствует в `big_nets_stat`. Если столбец `name` отсутствует, поместите в `group_name` значения из `Другие`.
3.  Выведите на экран первые пять строк таблицы `station_stat_full`.

Подсказка

Примените метод `where()` к столбцу `'name'` из _station_stat_full_. Первым параметром передайте условие булева массива, где _True_ соответствует именам крупных сетей, которые должны остаться без изменений. Список таких сетей — это `big_nets_stat.index`. Для проверки вхождения имени в список примените метод `isin()`. Вторым параметром `where()` передайте новое название `'Другие'`.

Выведите на экран первые значения _station_stat_full_ методом _head()_.

code:
```
import pandas as pd

data = pd.read_csv('/datasets/visits.csv', sep='\t')

# фильтруем слишком быстрые и медленные заезды и АЗС
data['too_fast'] = data['time_spent'] < 60
data['too_slow'] = data['time_spent'] > 1000
too_fast_stat = data.pivot_table(index='id', values='too_fast')
good_ids = too_fast_stat.query('too_fast < 0.5')
good_data = data.query('id in @good_ids.index')
good_data = good_data.query('60 <= time_spent <= 1000')

# считаем данные по отдельным АЗС и по сетям
station_stat = data.pivot_table(index='id', values='time_spent', aggfunc='median')
good_stations_stat = good_data.pivot_table(index='id', values='time_spent', aggfunc='median')
stat = data.pivot_table(index='name', values='time_spent')
good_stat = good_data.pivot_table(index='name', values='time_spent', aggfunc='median')
stat['good_time_spent'] = good_stat['time_spent']

id_name = good_data.pivot_table(index='id', values='name', aggfunc=['first', 'count'])
id_name.columns = ['name', 'count']
station_stat_full = id_name.join(good_stations_stat)

# считаем показатели сетей из показателей АЗС,
# а не усреднённые заезды на все АЗС сети
good_stat2 = (
    station_stat_full
    .query('count > 30')
    .pivot_table(index='name', values='time_spent', aggfunc=['median', 'count'])
)
good_stat2.columns = ['median_time', 'stations']
final_stat = stat.join(good_stat2)
big_nets_stat = final_stat.query('stations > 10')
#station_stat_full['group_name'] = 

#print(station_stat_full['name'].unique())
#print(station_stat_full)
print(station_stat_full.where('name' in big_nets_stat, 'Другие'))
```


<div class="Markdown base-markdown base-markdown_with-gallery base-markdown markdown markdown_size_small markdown_type_theory theory-viewer__markdown"><div class="paragraph">У вас есть категория <code class="code-inline code-inline_theme_light">Другие</code> с небольшими сетями. Теперь повторите анализ, в процессе которого создали <code class="code-inline code-inline_theme_light">good_stat2</code>, но в этот раз сгруппируйте данные по <code class="code-inline code-inline_theme_light">group_name</code>.</div><div class="paragraph">Выполните следующие шаги:</div><ol start="1"><li>Создайте переменную <code class="code-inline code-inline_theme_light">stat_grouped</code>, которая повторяет вычисления <code class="code-inline code-inline_theme_light">good_stat2</code>, но группирует по <code class="code-inline code-inline_theme_light">group_name</code>.</li><li>Переименуйте столбцы в <code class="code-inline code-inline_theme_light">stat_grouped</code> на <code class="code-inline code-inline_theme_light">time_spent</code> и <code class="code-inline code-inline_theme_light">count</code>.</li><li>Упорядочьте <code class="code-inline code-inline_theme_light">stat_grouped</code> по возрастанию значений столбца <code class="code-inline code-inline_theme_light">time_spent</code>. Убедитесь, что изменение постоянное, а не временное.</li><li>Выведите на экран <code class="code-inline code-inline_theme_light">stat_grouped</code>.</li></ol></div>
```
stat_grouped = (
    station_stat_full
    .query('count > 30')
    .pivot_table(index='group_name', values='time_spent', aggfunc=['median', 'count'])
    
stat_grouped = stat_grouped.sort_values(by='time_spent', ascending=True)

```

