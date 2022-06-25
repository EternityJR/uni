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


def count_func(x, eps):
    '''
    Вычисление результата функции
    :param eps: точность вычисления
    :param x: аргумент функции
    :return: результат вычисления функции
    '''
    return round(3 - math.sqrt(x ** 3) + 0.5 * math.log(x), eps)


z, e = count_zeros()

xnf, xns = float(input('Введите x0 ')), float(input('Введите x1 '))
diff = abs(xns-xnf)
print(f"0 {xnf:.{z}f}")

i = 1
while e < diff:
    try:
        xn = xns - (count_func(xns, z) * (xnf - xns)) / (count_func(xnf, z) - count_func(xns, z))
    except:
        exit(0)
    diff = abs(xns - xnf)
    xnf = xns
    xns = xn
    print(i, f" {xnf:.{z}f}", f" {diff:.{z}f}")
    i += 1
