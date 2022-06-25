from datetime import datetime
import matplotlib.pyplot as plt
import random as r
import math
import numpy

y0 = 1
y = (1.017, 0.013, 0.175, 0.188, 1.048)
a = []
k = (1, 1, 2, 3, 2)
v = [3.0 for i in range(5)]
print("Определение коэффициентов передач")
for i in y:
    a.append(i / y0)
    print(f"{i / y0:.3f}", end = " ")
print()
for i in range(5):
    print(f"{k[i] / (a[i] * v[i]):.3f}", end = "; ")
print()
while y0 > min([k[i] / (a[i] * v[i]) for i in range(5)]):
    for i in range(5):
        if y0 > k[i] / (a[i] * v[i]):
            v[i] -= 0.1
            break
for i in v:
    print(f"{i:.1f}", end = " ")
print()
for i in range(5):
    print(f"{k[i] / (a[i] * v[i]):.3f}", end = "; ")
b = []
print("\nСреднее число занятых каналов.")
for i in range(5):
    b.append(y[i] * v[i])
    print(f"{b[i]:.3f}", end = " ")
p = []
print("\nЗагрузка каждой СМО")
for i in range(5):
    p.append((y[i] * v[i]) / k[i])
    print(f"{p[i]:.3f}", end = " ")
print("\nВероятности состояния сети")
pi = []
for i in range(5):
    pi.append(1 - p[i])
    print(f"{pi[i]:.3f}", end = " ")
print("\nСредняя длина очереди заявок, ожидающих обслуживания в СМО.")
l = []
for i in range(5):
    l.append(0)
    l[i] = (b[i] ** (k[i] + 1)) / (math.factorial(k[i]) * k[i] * (1 - b[i] / k[i]) ** 2) * pi[i]
    print(f"{l[i]:.3f}", end = " ")
print("\nСреднее число заявок, пребывающих в каждой из систем сети.")
m = []
for i in range(5):
    m.append(l[i] + b[i])
    print(f"{m[i]:.3f}", end = " ")
print("\nСреднее время ожидания заявки в очереди системы")
w = []
for i in range(5):
    w.append(l[i] / y[i])
    print(f"{w[i]:.3f}", end = " ")
print("\nСреднее время пребывания заявок в системах")
u = []
for i in range(5):
    u.append(m[i] / y[i])
    print(f"{u[i]:.3f}", end = " ")
print(f"\nСреднее число заявок, ожидающих обслуживания в СМО: {sum(l):.2f}")
print(f"Среднее число заявок, пребывающих в сети: {sum(m):.2f}")
print(f"Среднее время ожидания заявки в сети: {sum([x * y for x, y in zip(a, w)]):.2f}")
print(f"Среднее время пребывания заявок в сети: {sum([x * y for x, y in zip(a, u)]):.2f}")
