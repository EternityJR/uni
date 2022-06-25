import math


def count_zeros():
    '''
    Определение точности числа
    :return: zeros - количество чисел, после запятой, eps - точность вычислений
    '''
    eps = input('Введите точность ')
    zeros = int(eps.count('0', 0, len(eps)))
    eps = float(eps)
    return zeros, eps


def count_first_gradient(x, s, eps):
    '''
    Вычисление результата первого градиента
    :param eps: точность вычисления
    :param x: аргумент функции x1
    :param s: аргумент функции x2
    :return: результат вычисления функции
    '''
    return round(2 * (math.sin(x - 1) + s - 0.8) * math.cos(1 - x) + 2 * (math.cos(s - 2) + x) * (-math.sin(s - 2)),
                 eps)


def count_second_gradient(x, s, eps):
    '''
    Вычисление результата второго градиента
    :param eps: точность вычисления
    :param x: аргумент функции x1
    :param s: аргумент функции x2
    :return: результат вычисления функции
    '''
    return round(2 * (math.sin(x - 1) + s - 0.8) +
                 2 * (math.cos(s - 2) + x) * math.sin(2 - s), eps)


a = 0.57
print('Шаговый множитель равен: ', a)

z, e = count_zeros()
xnf, xns = float(input('Введите x1: ')), float(input('Введите x2: '))

print('0', f" {xnf:.{z}f}", f" {xns:.{z}f}")
i, diff = 1, 1.0
while e < diff:
    try:
        xnf_t = xnf - count_first_gradient(xnf, xns, z) * a
        xns_t = xns - count_second_gradient(xnf, xns, z) * a
    except:
        exit(0)
    diff = max(abs(xnf - xnf_t), abs(xns - xns_t))
    xnf = xnf_t
    xns = xns_t
    print(i, f" {xnf:.{z}f}", f" {xns:.{z}f}", f" {diff:.{z}f}")
    i += 1
