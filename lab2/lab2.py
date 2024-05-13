import numpy as np
from scipy.stats import f

# Функция для расчёта доверительного интервала
def calculate_CI(n1, n2, S1, S2, alpha):
    lower_bound = (n1 / n2) * (S1 / S2) / f.ppf(1 - alpha / 2, n1 - 1, n2 - 1)
    upper_bound = (n1 / n2) * (S1 / S2) / f.ppf(alpha / 2, n1 - 1, n2 - 1)
    return (lower_bound, upper_bound)

# Заданные параметры
mu1 = 0
mu2 = 0
sigma1_sq = 2
sigma2_sq = 1
alpha = 0.05
n1 = 25
n2 = 25  # Обе выборки имеют одинаковый объём для простоты

# Создание списков для хранения результатов
coverage_count_n25 = 0

# Проведение эксперимента 1000 раз
for _ in range(1000):
    # Генерация выборок
    X1 = np.random.normal(mu1, np.sqrt(sigma1_sq), n1)
    X2 = np.random.normal(mu2, np.sqrt(sigma2_sq), n2)
    
    # Вычисление выборочных смещённых дисперсий
    S1_sq = np.var(X1, ddof=1)
    S2_sq = np.var(X2, ddof=1)
    
    # Расчёт доверительного интервала
    lower, upper = calculate_CI(n1, n2, S1_sq, S2_sq, alpha)
    
    # Проверка попадания истинного значения в интервал
    if lower < sigma1_sq / sigma2_sq < upper:
        coverage_count_n25 += 1

# Вывод результатов
print("95%-ый доверительный интервал для n1 = n2 = 25:", coverage_count_n25 / 1000)

# Повторяем для выборок объёма 10000
n1 = 10000
n2 = 10000
coverage_count_n10000 = 0

for _ in range(1000):
    X1 = np.random.normal(mu1, np.sqrt(sigma1_sq), n1)
    X2 = np.random.normal(mu2, np.sqrt(sigma2_sq), n2)
    S1_sq = np.var(X1, ddof=1)
    S2_sq = np.var(X2, ddof=1)
    lower, upper = calculate_CI(n1, n2, S1_sq, S2_sq, alpha)
    if lower < sigma1_sq / sigma2_sq < upper:
        coverage_count_n10000 += 1

print("95%-ый доверительный интервал для n1 = n2 = 10000:", coverage_count_n10000 / 1000)
