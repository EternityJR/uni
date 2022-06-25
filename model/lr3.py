import random
import numpy as np
import math


class CountMath:
    def __init__(self, l):
        self.temp = [0, 0, 0]
        self.l = l
        self.t_max = max(self.l, key=lambda x: x.time).time

    def count_mdi(self):
        """
        Вычисление мат.ожидания, дисперсии, стандартного отклонения и интенсивности
        """
        print("Числовые характеристики для типов событий")
        for i in range(3):
            if self.temp[i] != 0:
                temp_list = [j.time for j in self.l if j.type - 1 == i]
                print(f"Тип {i+1}.\nМат.ожидание: {np.mean(temp_list)}\nДисперсия: {np.var(temp_list)}\n"
                      f"Ср кв отклонение: {np.std(temp_list)}\nИнтенсивность: {1/np.mean(temp_list)}")
            else:
                print(f"Тип {i+1}.\nМат.ожидание: 0\nДисперсия: 0\n"
                      f"Ср кв отклонение: 0\nИнтенсивность: 0")

    def count_numbers(self):
        """
        Сравнение вероятностей появления сообщений (заданная и полученная)
        """
        VER = [0.05, 0.17, 0.78]
        for i in range(100):
            self.temp[self.l[i].type-1] += 1
        print("Тип заявки  Кол-во заявок  Полученная p(x)  Заданная p(x)")
        for i in range(3):
            print(f"{i+1:5} {self.temp[i]:15} {self.temp[i]/100:15} {VER[i]:15}")

    def count_length(self):
        """
        Сравнение средней длины заявки
        """
        av_len = [0, 0, 0]
        max_len = [0, 0, 0]
        print("Тип заявки    Ср.длина  Предельная длина")
        for i in range(100):
            av_len[self.l[i].type-1] +=self.l[i].length
        for i in range(3):
            max_len[i] = max([j for j in self.l if j.type-1 == i], key=lambda x: x.length).length
            print(f"{i+1:5} {av_len[i]/self.temp[i]:15.4} {max_len[i]:10}")

    def count_address(self):
        """
        Вычисление средней частоты вычисления заявок
        """
        c = [0, 0, 0, 0, 0]
        for i in range(100):
            c[self.l[i].address-1] += 1
        print("Номер адреса  Кол-во заявок  Средняя частота поступления")
        for i in range(5):
            print(f"{i+1:6} {c[i]:16} {c[i]/self.t_max:20.03}")

    def count_p(self):
        """
        Данные о вероятности и числе заявок в потоке
        """
        print("Данные о вероятности и числе заявок в потоке")
        for i in range(3):
            n_req = [0, 0, 0, 0, 0]
            for j in range(100):
                if i == self.l[j].type - 1:
                    n_req[self.l[j].address - 1] += 1
            for j in range(len(n_req)):
                print(f"{n_req[j]:10}", end=' ')
            print()
            for j in range(len(n_req)):
                print(f"{n_req[j]/self.temp[i]:10.03}", end=' ')
            print()


class Req():
    def __init__(self):
        self.type = 0
        self.address = 0
        self.length = 0
        self.time = 0

    def __repr__(self):
        return f"{self.type} {self.address} {self.length} {self.time:.03}"


def create_req():
    """
    Генерация заявок
    """
    l = []
    for i in range(100):
        example = Req()
        temp = random.random()
        example.length = random.randint(14, 244)
        example.time = abs(np.random.normal(6, math.sqrt(4.7)))
        if 0 <= temp <= 0.05:
            example.type = 1
            example.address = np.random.choice(range(1, 6), p=(0.22, 0.26, 0.29, 0.03, 0.2))
        if 0.05 < temp <= 0.22:
            example.type = 2
            example.address = np.random.choice(range(1, 6), p=(0.21, 0.47, 0.05, 0.13, 0.14))
        if 0.22 < temp <= 1:
            example.type = 3
            example.address = np.random.choice(range(1, 6), p=(0.62, 0.13, 0.02, 0.19, 0.04))
        l.append(example)
    l = sorted(l, key=lambda x: x.time)
    return l


if __name__ == '__main__':
    l = create_req()
    cm = CountMath(l)
    cm.count_numbers()
    cm.count_length()
    print(f"t_max={cm.t_max}")
    cm.count_address()
    cm.count_p()
    cm.count_mdi()
