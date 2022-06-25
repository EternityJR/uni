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

    # Отрисвка линии шириной в 2 пикселя
    for i in range(-1, 1):
        for j in range(-1,1):
            screen.set_at((x2 + i, y2 + j), RED)

    while x1 != x2 or y1 != y2:
        for i in range(-1, 1):
            for j in range(-1, 1):
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
length = 100 # Длина при запуске программы
angle = 0 # Угол, с которого начинается отрисовка
depth = 0.01 # Скорость вращения, с которой начинает работать программа

# Задание используемых цветов в формате RGB
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Нахождение центра экрана по осям X и Y
x, y = WIDTH/2, HEIGHT/2

# Отрисовка окна
pygame.init()
infoObject = pygame.display.Info()
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Lab6")
pygame.font.SysFont('Arial', 25)


running = True
while running:
    screen.fill(BLACK)
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
            # Увеличение размера звезды
            elif event.key == pygame.K_UP:
                length += 10
            # Уменьшение размера звезды
            elif event.key == pygame.K_DOWN:
                if not(length < 20):
                    length -= 10

            # Увеличение скорости вращения
            elif event.key == pygame.K_RIGHT:
                depth += 0.2
            # Снижение скорости вращения
            elif event.key == pygame.K_LEFT:
                if not(depth < 0.2):
                    depth -= 0.2

        # Получение координат при щелчке мыши
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()

    step = (1 / 7) * math.pi
    R1 = length # Большой радиус
    R2 = length / 2 # Малый радиус
    points = [] # Хранение точек для отрисовки линий

    if angle <= 360:
        # Получение угла в радианах
        angle_rad = angle * math.pi

        # Вычисление координат для отрисовки граней звезды
        for u in range(14):
            points.append((x + R2 * math.sin(angle_rad), y - R2 * math.cos(angle_rad)))
            angle_rad += step
            points.append((x + R1 * math.sin(angle_rad), y - R1 * math.cos(angle_rad)))
            angle_rad += step
        # Отрисовка звезды
        for u in range(14):
            draw_line(int(points[u][0]), int(points[u][1]), int(points[u + 1][0]), int(points[u + 1][1]))

        angle += depth
    else:
        angle = 0

    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()


pygame.quit()