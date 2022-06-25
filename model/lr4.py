import random
import numpy as np
import math


class Queue:
    def __init__(self, id, type, length):
        self.id = id
        self.type = type
        self.t_in = 0
        self.start = 0
        self.end = 0
        self.t_out = 0  # время простоя
        self.spent = math.ceil(length / 10)

    def __repr__(self):
        return f"{self.id:3} {self.t_in:5} {self.start:5} {self.end:5} {self.t_out:5} {self.spent:5}"


class CountMath:
    def __init__(self, list_0, gl):
        self.req_list = gl
        self.gen_list = list_0
        self.n_type = [0, 0, 0]

    def count_average(self):
        """
        Подсчёт средней длины сообщений и вероятности поступления сообщения для потока заявок
        """
        len_average = [0, 0, 0]
        print("Пункт 1.\nСредняя длина сообщений")
        for i in range(3):
            for j in self.gen_list:
                if j.type == i + 1:
                    self.n_type[i] += 1
                    len_average[i] += j.length
            len_average[i] /= self.n_type[i]
            print(f"{len_average[i]:5.4}", end=" ")
        print("\nВероятность поступления сообщения")
        for i in range(3):
            print(f"{self.n_type[i] / 100:4}", end=" ")
        print()

    def count_queue_stats(self):
        """
        Подсчёт характеристик очереди заявок
        """
        lam = 0  # интенсивность поступления заявок
        wi = [0, 0, 0]  # среднее время пребывания заявки i-го типа в очереди
        ti = [0, 0, 0]  # средний промежуток времени между поступлением заявок i-го типа
        ui = [0, 0, 0]  # среднее время пребывания заявки в системе
        temp_list = []
        lambda_i = [1, 1, 1]  # интенсивность поступления заявок i-го типа
        li = [0, 0, 0]  # средняя длина очереди заявок i-го типа
        pi_i = [0, 0, 0]  # коэффициент загрузки оборудования заявками i-го типа
        pi = [0, 0, 0]  # вероятность поступления заявки i-го типа
        mi = [1, 1, 1]  # интенсивность обслуживания
        ni = [0, 0, 0]  # коэффициент простоя
        w = 0  # среднее время пребывания заявки в очереди
        u = 0  # среднее время пребывания заявки в системе
        l = 0  # среднее число заявок в системе
        r = 0  # коэффициент загрузки
        print("Пункт 2.\nСредняя длина очереди: ")
        for i in range(3):
            for j in self.req_list:
                if j.type == i + 1:
                    wi[i] += j.t_out
                    ui[i] += j.spent
            wi[i] /= self.n_type[i]
            ui[i] /= self.n_type[i]
            temp_list.clear()
            temp_list = [j.t_in for j in self.req_list if j.type - 1 == i]
            for j in range(1, self.n_type[i]):
                ti[i] += temp_list[j] - temp_list[j - 1]
            ti[i] /= self.n_type[i]
            lambda_i[i] /= ti[i]
            li[i] = wi[i] * lambda_i[i]
            print(f"{li[i]:6.04}", end=' ')
            lam += self.n_type[i] * (i+1)/100
            mi[i] /= ui[i]
            pi_i[i] = self.n_type[i] * (i+1)/ mi[i]/100
            r += pi_i[i]
            ni[i] = 1 - pi_i[i]
            pi[i] = lambda_i[i]/lam
            w += pi[i] * wi[i]
            u += pi[i] * ui[i]
            l += self.n_type[i] * (i+1) * ui[i]
        print(f"\nW = {w}\nU = {u}\nL = {l}\nПункт 3.")
        vi = ui  # среднее время обслуживания заявки i-го типа, второй начальный момент времени обслуживания
        for j in range(3):
            print(f"{self.n_type[j] * (j+1)/100}", end=" ")
        print()
        for j in range(3):
            print(f"{pi_i[j]:.05}", end=" ")
        print()
        for j in range(3):
            print(f"{ni[j]:.05}", end=" ")
        print()
        for j in range(3):
            print(f"{ui[j]:.04}", end=" ")
        print()
        for j in range(3):
            print(f"{mi[j]:.04}", end=" ")
        print(f"\nR={r:.05}")


class Sys:
    def __init__(self, l):
        self.l = l
        self.req_list = []

    def process_req(self):
        """
        Обработка исходных заявок и регистрация их в очереди
        :return: очередь заявок
        """
        req_list = []
        t0 = math.ceil(self.l[0].time * 60)
        for id, val in enumerate(self.l):
            temp = Queue(id + 1, val.type, val.length)
            if val.type == 1:
                temp.t_in = t0
                temp.start = t0 + 1
                temp.end = temp.start + temp.spent
                temp.t_out = temp.start - temp.t_in
                t0 = temp.end + 1
            else:
                temp.t_in = t0
                t0 += 1
            req_list.append(temp)
        for i in range(2, 4):
            for j in req_list:
                if j.type == i:
                    j.start = t0
                    j.end = j.start + j.spent
                    j.t_out = j.start - j.t_in
                    t0 = j.end + 1
        self.req_list = req_list

    def get_req_list(self):
        """
        Вывод результата моделирования
        """
        for i in self.req_list:
            print(i)


class Req():
    def __init__(self):
        self.type = 0
        self.address = 0
        self.length = 0
        self.time = 0

    def __repr__(self):
        return f"{self.type} {self.address} {self.length} {self.time}"


def create_req():
    """
    Генерация заявок
    :return: лист заявок
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
    s = Sys(l)
    s.process_req()
    s.get_req_list()
    cm = CountMath(l, s.req_list)
    cm.count_average()
    cm.count_queue_stats()
