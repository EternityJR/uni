import numpy as np


def count_dif(spi, spi2):
    return max(abs(spi2[0] - spi[0]), abs(spi2[1] - spi[1]), abs(spi2[2] - spi[2]), abs(spi2[3] - spi[3]))


def count_zero_eps(e):
    k = 0
    for j in range(len(e)):
        if e[j] == '0':
            k = k + 1
    return k


eps = input('Введите точность ')
kolvo = count_zero_eps(eps)
eps = float(eps)

mx = np.array([[4.238, 0.339, 0.256, 0.425],
               [0.249, 2.964, 0.351, 0.127],
               [0.365, 0.217, 2.897, 0.168],
               [0.178, 0.294, 0.432, 3.701]])
b = np.array([0.56, 0.38, 0.778, 0.749])

print('Условия сходимости')
if (mx[0][0] < mx[0][1] + mx[0][2] + mx[0][3]) or (mx[1][1] < mx[1][0] + mx[1][2] + mx[1][3]) or (
        mx[2][2] < mx[2][0] + mx[2][1] + mx[2][3]) or (mx[3][3] < mx[3][0] + mx[3][1] + mx[3][2]):
    print('Условие не выполнено')
    exit(0)

print(mx[0][0], '>', mx[0][1], '+', mx[0][2], '+', mx[0][3], '=', round(mx[0][1] + mx[0][2] + mx[0][3], kolvo))
print(mx[1][1], '>', mx[1][0], '+', mx[1][2], '+', mx[1][3], '=', round(mx[1][0] + mx[1][2] + mx[1][3], kolvo))
print(mx[2][2], '>', mx[2][0], '+', mx[2][1], '+', mx[2][3], '=', round(mx[2][0] + mx[2][1] + mx[2][3], kolvo))
print(mx[3][3], '>', mx[3][0], '+', mx[3][1], '+', mx[3][2], '=', round(mx[3][0] + mx[3][1] + mx[3][2], kolvo))

for i in range(0, 4):
    b[i] /= mx[i][i]

spisok = []


maxi1 = mx[0][1] / mx[0][0] + mx[0][2] / mx[0][0] + mx[0][3] / mx[0][0]
maxi2 = mx[1][0] / mx[1][1] + mx[1][2] / mx[1][1] + mx[1][3] / mx[1][1]
maxi3 = mx[2][0] / mx[2][2] + mx[2][1] / mx[2][2] + mx[2][3] / mx[2][2]
maxi4 = mx[3][0] / mx[3][3] + mx[3][1] / mx[3][3] + mx[3][2] / mx[3][3]

bnorm = max(maxi1, maxi2, maxi3, maxi4)

print('\nПреобразованная система')
print('x1 = ', round(b[0], kolvo), round(- mx[0][1] / mx[0][0], kolvo), '* x2',
      - round(mx[0][2] / mx[0][0], kolvo), '* x3', - round(mx[0][3] / mx[0][0], kolvo), '* x4')
print('x2 = ', round(b[1], kolvo), - round(mx[1][0] / mx[1][1], kolvo), '* x1',
      - round(mx[1][2] / mx[1][1], kolvo), '* x3', - round(mx[1][3] / mx[1][1], kolvo), '* x4')
print('x3 = ', round(b[2], kolvo), - round(mx[2][0] / mx[2][2], kolvo), '* x1',
      - round(mx[2][1] / mx[2][2], kolvo), '* x2', - round(mx[2][3] / mx[2][2], kolvo), '* x4')
print('x4 = ', round(b[3], kolvo), - round(mx[3][0] / mx[3][3], kolvo), '* x1',
      - round(mx[3][1] / mx[3][3], kolvo), '* x2', - round(mx[3][2] / mx[3][3], kolvo), '* x3')

spisok.append([0., 0., 0., 0.])
i = 1
x1 = b[0] - mx[0][1] / mx[0][0] * spisok[0][1] \
         - mx[0][2] / mx[0][0] * spisok[0][2] - mx[0][3] / mx[0][0] * spisok[0][3]
x2 = b[1] - mx[1][0] / mx[1][1] * spisok[0][0] \
         - mx[1][2] / mx[1][1] * spisok[0][2] - mx[1][3] / mx[1][1] * spisok[0][3]
x3 = b[2] - mx[2][0] / mx[2][2] * spisok[0][0] \
         - mx[2][1] / mx[2][2] * spisok[0][1] - mx[2][3] / mx[2][2] * spisok[0][3]
x4 = b[3] - mx[3][0] / mx[3][3] * spisok[0][0] \
         - mx[3][1] / mx[3][3] * spisok[0][1] - mx[3][2] / mx[3][3] * spisok[0][2]
spisok.append([x1, x2, x3, x4])

while count_dif(spisok[i], spisok[i - 1]) > (1 - bnorm) / bnorm * eps:
    x1 = b[0] - mx[0][1] / mx[0][0] * spisok[i][1] \
         - mx[0][2] / mx[0][0] * spisok[i][2] - mx[0][3] / mx[0][0] * spisok[i][3]
    x2 = b[1] - mx[1][0] / mx[1][1] * spisok[i][0] \
         - mx[1][2] / mx[1][1] * spisok[i][2] - mx[1][3] / mx[1][1] * spisok[i][3]
    x3 = b[2] - mx[2][0] / mx[2][2] * spisok[i][0] \
         - mx[2][1] / mx[2][2] * spisok[i][1] - mx[2][3] / mx[2][2] * spisok[i][3]
    x4 = b[3] - mx[3][0] / mx[3][3] * spisok[i][0] \
         - mx[3][1] / mx[3][3] * spisok[i][1] - mx[3][2] / mx[3][3] * spisok[i][2]
    spisok.append([x1, x2, x3, x4])
    i += 1

print('\nТаблица с номерами итераций, значениями вектора решений и нормы разности векторов последней и предпоследней '
      'итерации')
print('0   ', round(0, kolvo), '  ', round(0, kolvo), '  ', round(0, kolvo), '  ', round(0, kolvo))
for i in range(1, len(spisok)):
    print(i, " ".join([str(round(num, kolvo)) for num in spisok[i]]),
          round(count_dif(spisok[i], spisok[i - 1]), kolvo))
