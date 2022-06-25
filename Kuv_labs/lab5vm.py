def count_Lagranj(x, y, x_user):
    '''
    :param x: аргумент функции
    :param y: значение функции
    :param x_user: произвольная точка для подсчёта функции
    '''
    print("Коэффиценты:")
    l = []
    sum = 0
    for i in range(len(x)):
        pros = 1
        sum1 = 1
        for j in range(len(x)):
            if i != j:
                pros *= x_user - x[j]
                sum1 *= (x[i] - x[j])
        l.append((1 / sum1) * y[i])
        sum += pros * l[i]
        print(f"{l[i]: .{4}f}")
    print(f"Значение приближения в точке x0: {sum: .{4}f}")

    print("Полином Лагранжа: ")
    for i in range(len(x)):
        str = ""
        str += f"{l[i]:+.{4}f}"
        for j in range(len(x)):
            if i != j:
                str += f"(x-{x[j]})"
        print(str)


def count_Newton(x, y, x_user):
    '''
    :param x: аргумент функции
    :param y: значение функции
    :param x_user: произвольная точка для подсчёта функции
    '''
    print("\nКоэффициенты:")
    n = [[], [], [], []]
    s2 = f"{y[0]}"
    for i in range(4):
        for j in range(1, 4 - i + 1):
            if i == 0:
                n[i].append((y[j] - y[j - 1]) / (x[j] - x[j - 1]))
            else:
                n[i].append((n[i - 1][j] - n[i - 1][j - 1]) / (x[j + i] - x[j - 1]))
    sum = y[0]
    for i in range(4):
        pros = 1
        s2 += f"{n[i][0]:+.{3}f}"
        for j in range(len(n[3 - i])):
            pros *= x_user - x[j]
            s2 += f"(x-{x[j]})"
        sum += n[i][0] * pros
        print(f"{n[i][0]: .{4}f}")
    print("Полином Ньютона:", s2)
    print(f"Значение приближения в точке x0: {sum: .{4}f}")


def count_linear(x, y, x_user):
    '''
    :param x: аргумент функции
    :param y: значение функции
    :param x_user: произвольная точка для подсчёта
    '''
    print("\nКоэффициенты a и b")
    a, b, line = [], [], []
    for i in range(4):
        a.append((y[i + 1] - y[i]) / (x[i + 1] - x[i]))
        b.append(y[i] - x[i] * a[i])
        print(f"a{i + 1}={a[i]: .{4}f}, b{i + 1}={b[i]: .{4}f}")
        line.append(f"{a[i]: .{4}f}x{b[i]:+.{4}f}, {x[i]: .{4}f} <= x <={x[i+1]: .{4}f}")
    print("Линейный сплайн")
    for i in line:
        print(i)

    result = 0.0
    for i in range(4):
        if x[i] <= x_user <= x[i + 1]:
            result += a[i]*x_user+b[i]
            break
    print(f"Значение приближения в точке x0: {result: .{4}f}")


def main():
    x = [0.135, 0.876, 1.336, 2.301, 2.642]
    y = [-2.132, -2.113, -1.613, -0.842, 1.204]
    x_user = float(input("Введите x0: "))
    count_Lagranj(x, y, x_user)
    count_Newton(x, y, x_user)
    count_linear(x, y, x_user)


main()
