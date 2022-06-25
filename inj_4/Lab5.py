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

    # Отрисвка линии шириной в 4 пикселя
    for i in range(-2, 2):
        for j in range(-2, 2):
            screen.set_at((int(x2 + i), int(y2 + j)), RED)

    while x1 != x2 or y1 != y2:
        for i in range(-2, 2):
            for j in range(-2, 2):
                screen.set_at((int(x1 + i), int(y1 + j)), RED)
        error_2 = error * 2

        if error_2 > -del_y:
            error -= del_y
            x1 += sign_x

        if error_2 < del_x:
            error += del_x
            y1 += sign_y


def draw_rect(x, y, a):
    """
    Функция отрисовки квадрата
    :param x: Заданная координата центра по оси X
    :param y: Заданная координата центра по оси Y
    :param a: Длина стороны квадрата
    """
    draw_line(x + a / 2, y - a / 2, x - a / 2, y - a / 2)
    draw_line(x + a / 2, y + a / 2, x - a / 2, y + a / 2)
    draw_line(x + a / 2, y - a / 2, x + a / 2, y + a / 2)
    draw_line(x - a / 2, y - a / 2, x - a / 2, y + a / 2)


# Задание базовых состояний всех величин
WIDTH, HEIGHT = 1024, 768
length = 100 # Длина отрисвываемой линии при запуске программы
speed_x, speed_y = 10, 10 # Скорость движения, с которой начинает работать программа

# Задание используемых цветов в формате RGB
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Нахождение центра экрана по осям X и Y
x, y = WIDTH/2, HEIGHT/2

# Отрисовка окна
pygame.init()
infoObject = pygame.display.Info()
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Lab5")
pygame.font.SysFont('Arial', 25)


running = True
while running:
    WIDTH, HEIGHT = pygame.display.get_surface().get_size()
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

            # Увеличение размеров квадрата
            elif event.key == pygame.K_UP:
                length += 10
            # Уменьшение размеров квадрата
            elif event.key == pygame.K_DOWN:
                length -= 10

            # Увеличение скорости
            elif event.key == pygame.K_RIGHT:
                speed_x += 5 if speed_x > 0 else -5
                speed_y += 5 if speed_y > 0 else -5
            # Снижение скорости
            elif event.key == pygame.K_LEFT:
                speed_x += -5 if speed_x > 0 else +5
                speed_y += -5 if speed_y > 0 else +5

        elif event.type == pygame.VIDEORESIZE:
            WIDTH = screen.get_width()
            HEIGHT = screen.get_height()
            x, y = int(WIDTH / 2), int(HEIGHT / 2)

        # Получение координат при щелчке мыши
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()

    # Отрисовка окна, заполненного черным цветом
    screen.fill(BLACK)

    # Реализация "отскакивания" от сторон окна
    if x - length / 2 < 0 or x + length / 2 > WIDTH:
        speed_x = -speed_x
    if y - length / 2 < 0 or y + length / 2 > HEIGHT:
        speed_y = -speed_y

    x += speed_x
    y += speed_y

    # Вызов функции отрисовки квадрата
    draw_rect(x, y, length)

    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()

pygame.quit()