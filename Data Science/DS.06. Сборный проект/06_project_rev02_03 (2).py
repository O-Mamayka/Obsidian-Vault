
Ячейка 31

#games.loc[600, 'eu_sales':'other_sales'] = games.loc[[600,15969], 'eu_sales':'other_sales'].sum(axis=0)
#games.iloc[[600]]

rows = games.duplicated(subset=['name','platform','year_of_release', 'genre'], keep=False)

games.loc[rows, 'na_sales'] = games.loc[rows, 'na_sales'].sum()
games.loc[rows, 'eu_sales'] = games.loc[rows, 'eu_sales'].sum()
games.loc[rows, 'jp_sales'] = games.loc[rows, 'jp_sales'].sum()
games.loc[rows, 'other_sales'] = games.loc[rows, 'other_sales'].sum()

games[games.duplicated(subset=['name','platform','year_of_release', 'genre'], keep=False)]



Ячейка 40
sales_group = games.groupby('platform')['total_sales'].sum().sort_values(ascending=False)[:10]
sales_group.plot(kind='bar',figsize=(16,4))

plt.xlabel("Наименование платформы", fontsize=10)
plt.ylabel('Суммарные продажи', fontsize=10)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.figtext(0.35, -0.1, "Рисунок 3. - Изменение продажи по платформам", fontsize=14)
plt.show()

sales_group = sales_group.reset_index(drop=False)
sales_group
favor_platform = sales_group['platform'].head(6)
favor_platform







91

# на примере патформ с наибольшими суммарными продажами выявим время жизни платформ

#favor_platform = ['PS2', 'X360', 'PS3', 'Wii', 'DS', 'PS']
year_life=[]
for platforms in favor_platform:
    platforms_diff = games.query('platform==@platforms')['year_of_release'].max()-\
    games.query('platform==@platforms')['year_of_release'].min()
    year_life.append(platforms_diff)
    print(platforms, platforms_diff)
    
mean = int(round((sum(year_life) / len(year_life)),0))
print('Среднее время жизни платформы: ',mean, 'лет.')



После 52
Посмотрим выбросы с помощью Диаграмма рассеяния и Диаграммы размаха




games.sample(3)


54

plt.figure(figsize=(10, 5))
sns.scatterplot(data = games, x='total_sales', y='year_of_release', alpha=0.4, s=30)
plt.title('продажи по годам')
plt.xlabel('Количество продаж')
plt.ylabel('Год');



55

# выявим выбросы:
games.boxplot(column=['total_sales'], figsize=(16,5), grid=True)
plt.figtext(0.33, 0.03, "Рис.8 - Диаграмма размаха суммарных продаж ", fontsize=14)
plt.show()

56

# и диаграмму размаха без выбросов:
plt.ylim(0.05, 0.5)
games.boxplot(column=['total_sales'], figsize=(16,5), grid=True)
plt.figtext(0.33, 0.03, "Рис.9 - Диаграмма размаха суммарных продаж ", fontsize=14)
plt.show()



выводы:
Из данных графиков видно, что основное количество продаж по платформам от 50 до 500 тысяч экземпляров. Другие значения можно считать выбросами.







57

# за выбросы примем значения продаж выше 40, отбрасываем выбросы 
games_filter = games[games['total_sales'] < 40]
# по гистограмме (рис.2) выбираем актуальный период с 2001 по 2015 
games_filter = games[(games['year_of_release'] > 2000) & (games['year_of_release'] <= 2016)]













