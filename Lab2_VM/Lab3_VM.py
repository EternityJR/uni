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
    return round(2 - math.sqrt(x ** 3) - 2 * math.log(x), eps)


def count_first_derivative(x, eps):
    '''
    Вычисление первой производной
    :param eps: точность вычисления
    :param x: аргумент функции
    :return: результат вычисления
    '''
    return round(-3 * math.sqrt(x ** 3)/(2 * x) - 2 / x, eps)


def count_second_derivative(x, eps):
    '''
    Вычисление первой производной
    :param eps: точность вычисления
    :param x: аргумент функции
    :return: результат вычисления
    '''
    return round(-3 * math.sqrt(x ** 3)/(4 * x) + 2 / (x * 2), eps)


z, e = count_zeros()

xn = float(input('Введите x0 '))
print(f"0  {xn:.{z}f}")
diff = 1

i = 1
while e < diff:
    xn_new = xn
    try:
        temp = 2 * (count_first_derivative(xn, z) ** 2) - count_func(xn, z) * count_second_derivative(xn, z)
        xn_new = xn - ((2 * count_func(xn, z) * count_first_derivative(xn, z)) / temp)
    except:
        exit(0)
    diff = abs(xn_new - xn)
    xn = xn_new
    print(i, f" {xn:.{z}f}", f" {diff:.{z}f}")
    i += 1
