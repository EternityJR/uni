import pygame
import math


def draw_line(x1, y1, x2, y2):
    """
    Функция отрисовки линии на основе алгоритма Брезенхема
    :param x1: Начальная координата по оси X
    :param y1: Начальная координата по оси Y
    :param x2: Конечная координата по оси X
    :param y2: Конечная координата по оси Y
    """
    del_x = abs(x2 - x1)
    del_y = abs(y2 - y1)

    sign_x = 1 if x1 < x2 else -1
    sign_y = 1 if y1 < y2 else -1

    error = del_x - del_y

    # Отрисвка линии шириной в 20 пикселей
    for i in range(-10, 10, 3):
        for j in range(-10,10, 3):
            screen.set_at((x2 + i, y2 + j), RED)

    while x1 != x2 or y1 != y2:
        for i in range(-10, 10, 3):
            for j in range(-10, 10, 3):
                screen.set_at((x1 + i, y1 + j), RED)
        error_2 = error * 2

        if error_2 > -del_y:
            error -= del_y
            x1 += sign_x

        if error_2 < del_x:
            error += del_x
            y1 += sign_y


# Задание базовых состояний всех величин
WIDTH, HEIGHT = 1024, 768
length = 100 # Длина отрисвываемой линии при запуске программы
angle = 0 # Угол, с которого начинается отрисовка линии
depth = 0.1 # Скорость вращения, с которой начинает работать программа

# Задание используемых цветов в формате RGB
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Нахождение центра экрана по осям X и Y
x, y = WIDTH/2, HEIGHT/2

# Отрисовка окна
pygame.init()
infoObject = pygame.display.Info()
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Lab4")
pygame.font.SysFont('Arial', 25)


running = True
while running:
    # Ввод процесса (события)
    for event in pygame.event.get():
        # Проверка на закритие окна
        if event.type == pygame.QUIT:
            running = False
        # Реакция на действия со стороны пользователя
        elif event.type == pygame.KEYDOWN:
            # Закрытие программы при нажатии на Эскейп
            if event.key == pygame.K_ESCAPE:
                running = False
            # Увеличение длины отрисовываемой линии
            elif event.key == pygame.K_UP:
                length += 10
            # Уменьшение длины отрисовываемой линии
            elif event.key == pygame.K_DOWN:
                if not(length < 20):
                    length -= 10
            # Увеличение скорости вращения
            elif event.key == pygame.K_RIGHT:
                depth += 0.3
            # Снижение скорости вращения
            elif event.key == pygame.K_LEFT:
                if not(depth < 0.3):
                    depth -= 0.3
        # Получение координат при щелчке мыши
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()

    if angle <= 360:
        # Подсчёт начала координат линии в зависимости от угла и заданной точки отрисовки
        x1 = x + length * math.cos(math.radians(angle))
        y1 = y + length * math.sin(math.radians(angle))

        # Подсчёт координат конца отрезка в зависимости от угла на текущей итерации
        if 0 < angle < 91:
            x2 = x - abs(x - x1)
            y2 = y - abs(y - y1)

        elif 90 < angle < 181:
            x2 = x + abs(x - x1)
            y2 = y - abs(y - y1)

        elif 180 < angle < 270:
            x2 = x + abs(x - x1)
            y2 = y + abs(y - y1)
        else:
            x2 = x - abs(x - x1)
            y2 = y + abs(y - y1)

        # Отрисовка окна, заполненного черным цветом
        screen.fill(BLACK)
        # Вызов функции отрисовки линии
        draw_line(int(x1), int(y1), int(x2), int(y2))

        angle += depth
    else:
        angle = 0

    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()


pygame.quit()