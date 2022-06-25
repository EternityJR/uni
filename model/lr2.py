import random
import numpy as np
import math


def generate_own(n, l):
    """
    Генерация последовательности методом серединных произведений
    :return: список последовательности
    """
    for i in range(n):
        sum = 0
        elem = -1
        while sum < 30:
            elem += 1
            sum -= math.log(random.random())
        l.append(elem)
    return l


def count_parameter(l):
    """
    Определяет следующие характеристики: математическое ожидание, дисперсию и среднеквадратичное отклонение
    """
    print(f"Математическое ожидание: {np.mean(l)}")
    print(f"Дисперсия: {np.var(l)}")
    print(f"Среднеквадратичное отклонение: {np.std(l)}\n")


if __name__ == '__main__':
    sequences = []
    generate_own(100, sequences)
    for i in range(0, 100, 10):
        print(sequences[i:i+10])
    count_parameter(sequences)
