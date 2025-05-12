import numpy as np
from scipy.stats import multivariate_normal
from itertools import groupby

def task1():
    text = """3,4,17,-3
              5,11,-1,6
              0,2,-5,8"""
    with open('matrix.txt', 'w') as f:
        f.write(text)
    matrix = np.loadtxt('matrix.txt', delimiter=',')
    total_sum = np.sum(matrix)
    max_element = np.max(matrix)
    min_element = np.min(matrix)
    print("Матрица:")
    print(matrix)
    print(f"Сумма: {total_sum}")
    print(f"Максимум: {max_element}")
    print(f"Минимум: {min_element}")


def task2(x):
    values = []
    counts = []

    for val, group in groupby(x):
        values += [val]
        counts += [len(list(group))]

    ans = (np.array(values), np.array(counts))
    print(ans)


def task3():
    np.random.seed(42)
    data = np.random.normal(size=(10, 4))
    min_val = np.min(data)
    max_val = np.max(data)
    mean_val = np.mean(data)
    std_val = np.std(data)
    first_five_rows = data[:5].copy()
    print("Минимальное значение:", min_val)
    print("Максимальное значение:", max_val)
    print("Среднее значение:", mean_val)
    print("Стандартное отклонение:", std_val)
    print("Первые 5 строк:")
    print(first_five_rows)


def task4(x):
    zero_indices = np.where(x[:-1] == 0)[0]
    if len(zero_indices) == 0:
        return None
    elements_after_zero = x[zero_indices + 1]
    result = np.max(elements_after_zero)
    print("Максимальный элемент после нуля:", result)


def task5(X, m, C):
    D = len(m)
    N = X.shape[0]
    inv_C = np.linalg.inv(C)
    det_C = np.linalg.det(C)
    log_norm = -0.5 * D * np.log(2 * np.pi) - 0.5 * np.log(det_C)
    X_centered = X - m
    quadratic_form = np.sum(X_centered @ inv_C * X_centered, axis=1)
    log_pdf = log_norm - 0.5 * quadratic_form

    scipy_logpdf = multivariate_normal(m, C).logpdf(X)
    diff = np.max(np.abs(log_pdf - scipy_logpdf))
    print("Максимальная разница с scipy:", diff)


def task6():
    a = np.arange(16).reshape(4, 4)
    print("Исходная матрица:")
    print(a)
    a[[0, 2]] = a[[2, 0]]
    print("Матрица после замены строк 1 и 3:")
    print(a)


def task7():
    url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
    iris = np.genfromtxt(url, delimiter=',', dtype='object')
    species = iris[:, -1]
    unique_species, counts = np.unique(species, return_counts=True)
    print("Уникальные виды и их количество:")
    for spec, count in zip(unique_species, counts):
        print(f"{spec.decode('utf-8')}: {count}")


def task8(arr):
    nonzero_indices = np.nonzero(arr)[0]
    print("Индексы ненулевых элементов:", nonzero_indices)

print("\n=== Задание 1 ===")
task1()

print("\n=== Задание 2 ===")
task2(np.array([2, 2, 2, 3, 3, 3, 5]))

print("\n=== Задание 3 ===")
task3()

print("\n=== Задание 4 ===")
task4(np.array([6, 2, 0, 3, 0, 0, 5, 7, 0]))

print("\n=== Задание 5 ===")
D = 5
N = 1000
m = np.random.randn(D)
C = np.random.randn(D, D)
C = C @ C.T
X = np.random.randn(N, D)
task5(X, m, C)

print("\n=== Задание 6 ===")
task6()

print("\n=== Задание 7 ===")
task7()

print("\n=== Задание 8 ===")
task8(np.array([0, 1, 2, 0, 0, 4, 0, 6, 9]))