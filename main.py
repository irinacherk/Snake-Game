import pygame
import time
import random

pygame.init()

# Определение цветов
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (50, 153, 213)

# Размеры окна
width = 600
height = 400

# Создание игрового окна
dis = pygame.display.set_mode((width, height))
pygame.display.set_caption('Змейка')

# Время и скорость
clock = pygame.time.Clock()
snake_speed = 5
snake_block = 10

# Шрифт для текста
font_style = pygame.font.SysFont("bahnschrift", 35)
score_font = pygame.font.SysFont("bahnschrift", 25)

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, green, [x[0], x[1], snake_block, snake_block])

def message(msg1, msg2, msg3, color):
    mesg1 = font_style.render(msg1, True, color)
    mesg2 = font_style.render(msg2, True, color)
    mesg3 = font_style.render(msg3, True, color)
    dis.blit(mesg1, [width / 6, height / 3])
    dis.blit(mesg2, [width / 6, height / 3 + 30])
    dis.blit(mesg3, [width / 6, height / 3 + 60])  # Перенос "или" на новую строку

def your_score(score):
    value = score_font.render(f"Счет: {score}", True, yellow)
    dis.blit(value, [0, 0])

def gameLoop():
    game_over = False
    game_close = False

    x1 = width / 2
    y1 = height / 2

    x1_change = 0
    y1_change = 0

    snake_list = []
    length_of_snake = 1

    foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

    current_score = 0  # Начальный счет

    while not game_over:

        while game_close == True:
            dis.fill(black)
            message("Игра окончена!", "Нажмите Q для выхода", "или C для продолжения", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x1_change == 0:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT and x1_change == 0:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP and y1_change == 0:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN and y1_change == 0:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        dis.fill(black)
        pygame.draw.rect(dis, red, [foodx, foody, snake_block, snake_block])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        our_snake(snake_block, snake_list)
        your_score(current_score)  # Отображение счета

        if current_score == 10:
            dis.fill(black)
            message("Поздравляем!", "Вы выиграли!", "", red)  # Сообщение выводится по центру
            pygame.display.update()
            time.sleep(3)
            game_over = True
            break

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
            length_of_snake += 1
            current_score += 1  # Увеличиваем счет

        clock.tick(snake_speed)

    pygame.quit()
    qui

gameLoop()
