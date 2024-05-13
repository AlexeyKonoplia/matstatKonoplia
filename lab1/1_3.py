import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


# Чтение файла CSV
df = pd.read_csv('cars93.csv')

# Уникальные типы автомобилей
types = df['Type'].unique()

# Вывод уникальных типов автомобилей
print("Типы автомобилей в датасете:")
for car_type in types:
    print(car_type)
# Подсчет количества автомобилей каждого типа
type_counts = df['Type'].value_counts()

# Наиболее распространенный тип
most_common_type = type_counts.idxmax()
most_common_count = type_counts.max()

# Наименее распространенный тип
least_common_type = type_counts.idxmin()
least_common_count = type_counts.min()

print(f"Наиболее распространенный тип: {most_common_type} ({most_common_count} автомобилей)")
print(f"Наименее распространенный тип: {least_common_type} ({least_common_count} автомобилей)")
# Рассчеты для всех автомобилей
mean_all = df['Horsepower'].mean()
var_all = df['Horsepower'].var()
median_all = df['Horsepower'].median()
iqr_all = df['Horsepower'].quantile(0.75) - df['Horsepower'].quantile(0.25)

# Рассчеты для американских автомобилей
mean_usa = df[df['Origin'] == 'USA']['Horsepower'].mean()
var_usa = df[df['Origin'] == 'USA']['Horsepower'].var()
median_usa = df[df['Origin'] == 'USA']['Horsepower'].median()
iqr_usa = df[df['Origin'] == 'USA']['Horsepower'].quantile(0.75) - df[df['Origin'] == 'USA']['Horsepower'].quantile(0.25)

# Рассчеты для неамериканских автомобилей
mean_non_usa = df[df['Origin'] == 'non-USA']['Horsepower'].mean()
var_non_usa = df[df['Origin'] == 'non-USA']['Horsepower'].var()
median_non_usa = df[df['Origin'] == 'non-USA']['Horsepower'].median()
iqr_non_usa = df[df['Origin'] == 'non-USA']['Horsepower'].quantile(0.75) - df[df['Origin'] == 'non-USA']['Horsepower'].quantile(0.25)

# Вывод результатов
print("Для всех автомобилей:")
print("Выборочное среднее мощности:", mean_all)
print("Выборочная дисперсия мощности:", var_all)
print("Выборочная медиана мощности:", median_all)
print("Межквартальный размах мощности:", iqr_all)
print("\nДля американских автомобилей:")
print("Выборочное среднее мощности:", mean_usa)
print("Выборочная дисперсия мощности:", var_usa)
print("Выборочная медиана мощности:", median_usa)
print("Межквартальный размах мощности:", iqr_usa)
print("\nДля неамериканских автомобилей:")
print("Выборочное среднее мощности:", mean_non_usa)
print("Выборочная дисперсия мощности:", var_non_usa)
print("Выборочная медиана мощности:", median_non_usa)
print("Межквартальный размах мощности:", iqr_non_usa)


# Сортировка мощности для построения эмпирической функции распределения
horsepower_all = np.sort(df['Horsepower'])
horsepower_usa = np.sort(df[df['Origin'] == 'USA']['Horsepower'])
horsepower_non_usa = np.sort(df[df['Origin'] == 'non-USA']['Horsepower'])

# Рассчитываем эмпирическую функцию распределения
ecdf_all = np.arange(1, len(horsepower_all) + 1) / len(horsepower_all)
ecdf_usa = np.arange(1, len(horsepower_usa) + 1) / len(horsepower_usa)
ecdf_non_usa = np.arange(1, len(horsepower_non_usa) + 1) / len(horsepower_non_usa)

# Строим график
plt.figure(figsize=(10, 6))
plt.step(horsepower_all, ecdf_all, label='Все автомобили')
plt.step(horsepower_usa, ecdf_usa, label='Американские автомобили')
plt.step(horsepower_non_usa, ecdf_non_usa, label='Неамериканские автомобили')
plt.xlabel('Мощность (л.с.)')
plt.ylabel('Эмпирическая функция распределения')
plt.title('Эмпирическая функция распределения мощности')
plt.legend()
plt.grid(True)
plt.show()

# Гистограмма мощности для всех автомобилей
plt.figure(figsize=(12, 6))
sns.histplot(df['Horsepower'], bins=20, kde=True, color='skyblue')
plt.title('Гистограмма мощности для всех автомобилей')
plt.xlabel('Мощность (л.с.)')
plt.ylabel('Частота')
plt.grid(True)
plt.show()

# Box-plot мощности для всех автомобилей
plt.figure(figsize=(8, 6))
sns.boxplot(x=df['Horsepower'], color='lightgreen')
plt.title('Box-plot мощности для всех автомобилей')
plt.xlabel('Мощность (л.с.)')
plt.grid(True)
plt.show()

# Box-plot мощности для американских и неамериканских автомобилей
plt.figure(figsize=(10, 6))
sns.boxplot(x='Origin', y='Horsepower', data=df, palette='pastel')  
plt.title('Box-plot мощности для американских и неамериканских автомобилей')
plt.xlabel('Происхождение')
plt.ylabel('Мощность (л.с.)')
plt.grid(True)
plt.show()