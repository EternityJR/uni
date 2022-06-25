import random
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt


def draw_g(l):
    """
    Отрисовка графика
    """
    plt.hist(l[2], bins=100, facecolor='yellow')
    plt.title(len(l[2]))
    plt.show()


def generate(n, k, l):
    """
    Генерация последовательности с помощью стандартного генератора
    """
    for i in range(n):
        l[k].append(random.random())
    return l


def generate_own(n, k, l):
    """
    Генерация последовательности методом серединных произведений
    """
    while len(l[k]) != n:
        l[k].clear()
        time = str(datetime.now().microsecond)[0:4]
        time2 = str(datetime.now().microsecond)[1:5]
        for i in range(n):
            time = int(time)
            time2 = int(time2)
            new_str = str(time * time2)
            time = str(time2)
            time2 = str(new_str)[2:6]
            if time2 == "0000" or time2 == "":
                break
            l[k].append(float("0." + str(int(time2))))
    return l


def count_parameter(l):
    """
    Определяет следующие характеристики: математическое ожидание, дисперсию и среднеквадратичное отклонение
    """
    temp = 100
    for i in range(3):
        print(f"Характеристики для последовательности из {temp} чисел")
        print(f"Математическое ожидание: {np.mean(l[i])}")
        print(f"Дисперсия: {np.var(l[i])}")
        print(f"Среднеквадратичное отклонение: {np.std(l[i])}\n")
        temp *= 10


def count_uniformity(numb):
    """
    Оценка равномерности генератора случайных чисел
    """
    sequences = [[], [], [], [], [], [], [], [], [], []]
    sequences2 = sequences
    for i in range(10):
        generate_own(numb[i], i, sequences)
        generate(numb[i], i, sequences2)
        temp = np.mean(sequences[i])
        temp2 = np.mean(sequences2[i])
        print(f"{temp:6.4}", " ", f"{temp - 0.5:10.4}", f"{temp2:16.4}", " ", f"{temp2 - 0.5:10.4}")


if __name__ == '__main__':
    N = [100, 1000, 10000]
    sequences = [[], [], []]
    print("Программная реализация")
    counter = 0
    for i in N:
        generate(N[counter], counter, sequences)
        counter += 1
    count_parameter(sequences)

    print("\nГенерация последовательности методом серединных произведений")
    counter = 0
    for i in N:
        sequences[counter].clear()
        generate_own(N[counter], counter, sequences)
        counter += 1
    count_parameter(sequences)

    print("Оценка равномерности для собственной и встроенной реализации на 1000 элементов")
    print("  M1          M1-M                M1        M1-M")
    count_uniformity([1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000])

    print("Оценка равномерности для собственной и встроенной от 1000 до 10000 элементов")
    print("  M2          M2-M                M2        M2-M")
    count_uniformity([1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000])
    draw_g(sequences)
