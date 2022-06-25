import numpy as np


def count_zero_eps(e):
    """
    Подсчёт количества знаков после запятой
    :param e: эпсилум
    :return: количество знаков после запятой
    """
    k = 0
    for j in range(len(e)):
        if e[j] == '0':
            k = k + 1
    return k


eps = input('Введите точность ')
k = count_zero_eps(eps)
eps = float(eps)


D = np.zeros((4, 4))
L = np.zeros((4, 4))
R = np.zeros((4, 4))
A = np.array([[3.738, 0.195, 0.275, 0.136],
               [0.519, 5.002, 0.405, 0.283],
               [0.306, 0.197, 2.875, 0.418],
               [0.272, 0.142, 0.314, 3.935]])

b = np.array([0.815, 0.191, 0.423, 0.352]).reshape(4, 1)

x = np.array([0., 0., 0., 0.]).reshape(4, 1)
srav = ''

for i in range(0, 4):
    D[i][i] = A[i][i]
for i in range(0, 4):
    for j in range(0, 4):
        if i > j:
            L[i][j] = A[i][j]
for i in range(0, 4):
    for j in range(0, 4):
        if i < j:
            R[i][j] = A[i][j]
B = -np.linalg.inv(D).dot(L + R)
for i in range(4):
    B[i][i] = abs(B[i][i])
c = np.linalg.inv(D).dot(b)


print("Измененная система:")
print(B, "\n\n", c)
for i in range(0, 4):
    srav += str(A[i][i]) + " > "
    sum = 0
    for j in range(0, 4):
        if i != j:
            sum += A[i][j]
            srav += str(A[i][j]) + " + "
    srav = srav[:-3]
    srav += ' = ' + str(np.round(sum, k)) + "\n"


print("\nПроверка сходимости:")
print(srav)
norm = np.linalg.norm(B, ord=np.inf)  # норма В
dela = (1 - norm) / norm * eps
listt = []  # трехмерный массив
listt.append(x)
temp_x = np.round(B.dot(listt[0]) + c, k)
listt.append(temp_x)
p_normx = 0

while np.linalg.norm(listt[len(listt) - 1] - listt[len(listt) - 2], ord=np.inf) > dela:
    p_normx = np.linalg.norm(listt[len(listt) - 1] - listt[len(listt) - 2], ord=np.inf)
    temp_x = B.dot(listt[len(listt) - 1]) + c
    listt.append(np.round(temp_x, k))


print('Таблица с номерами итераций, значениями вектора решений и нормы разности векторов последней и предпоследней '
      'итерации')
i = 0
print(i, " ", listt[0][0][0], " ", listt[0][1][0], " ", listt[0][2][0], " ", listt[0][3][0], " ")
for j in range(1, len(listt)):
    i += 1
    norm_x = np.round(np.linalg.norm(listt[j] - listt[j - 1], ord=np.inf), k)
    print(i, " ", listt[j][0][0], " ", listt[j][1][0], " ", listt[j][2][0], " ", listt[j][3][0], " ", norm_x)
