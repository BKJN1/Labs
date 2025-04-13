# snake.py — основная логика змейки

import pygame  # графика и окно
import random  # генерация еды
import sys     # выход из игры
import time    # время для исчезновения еды
from db import get_or_create_user, save_score, close_connection  # работа с БД
from levels import levels  # уровни: стены и скорость

# --- Инициализация игры ---
pygame.init()
WIDTH, HEIGHT = 600, 600  # размеры окна
CELL_SIZE = 20  # размер клетки (для змейки и еды)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)  # цвет змейки
BLACK = (0, 0, 0)    # цвет стен

# цвета еды: по весу
FOOD_COLORS = {
    1: (255, 0, 0),       # красный — 1 очко
    2: (255, 165, 0),     # оранжевый — 2 очка
    3: (255, 255, 0)      # жёлтый — 3 очка
}

# --- Настройка окна ---
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")
font = pygame.font.SysFont("Verdana", 20)
clock = pygame.time.Clock()

# --- Вход или регистрация пользователя ---
user_id, username = get_or_create_user()

# --- Переменные игры ---
snake = [(300, 300), (280, 300), (260, 300)]  # стартовая змейка
direction = (20, 0)  # движение вправо
food_pos, food_weight = (0, 0), 1  # позиция еды и её вес
score = 0
level = 1
speed = levels[level]["speed"]  # скорость из levels
food_spawn_time = 0
paused = False  # флаг паузы

# --- Генерация еды ---
def generate_food():
    while True:
        x = random.randrange(0, WIDTH, CELL_SIZE)
        y = random.randrange(0, HEIGHT, CELL_SIZE)
        if (x, y) not in snake:  # чтобы еда не была в змейке
            return (x, y), random.choice([1, 2, 3])

# --- Рисуем стены ---
def draw_walls(walls):
    for wall in walls:
        start, end = wall
        if start[0] == end[0]:  # вертикальная
            for y in range(start[1], end[1] + 1, CELL_SIZE):
                pygame.draw.rect(screen, BLACK, (start[0], y, CELL_SIZE, CELL_SIZE))
        elif start[1] == end[1]:  # горизонтальная
            for x in range(start[0], end[0] + 1, CELL_SIZE):
                pygame.draw.rect(screen, BLACK, (x, start[1], CELL_SIZE, CELL_SIZE))

# --- Проверка столкновения со стенами ---
def check_wall_collision(head, walls):
    for wall in walls:
        start, end = wall
        if start[0] == end[0]:  # вертикаль
            if head[0] == start[0] and start[1] <= head[1] <= end[1]:
                return True
        elif start[1] == end[1]:  # горизонталь
            if head[1] == start[1] and start[0] <= head[0] <= end[0]:
                return True
    return False

# --- Первичная генерация еды ---
food_pos, food_weight = generate_food()
food_spawn_time = time.time()

# --- Главный цикл игры ---
running = True
while running:
    screen.fill(WHITE)
    walls = levels.get(level, {}).get("walls", [])  # получаем стены для уровня

    # --- События клавиш и выхода ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            save_score(user_id, level, score)
            close_connection()
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:  # пауза по P
                paused = not paused
            elif not paused:
                if event.key == pygame.K_UP and direction != (0, 20):
                    direction = (0, -20)
                elif event.key == pygame.K_DOWN and direction != (0, -20):
                    direction = (0, 20)
                elif event.key == pygame.K_LEFT and direction != (20, 0):
                    direction = (-20, 0)
                elif event.key == pygame.K_RIGHT and direction != (-20, 0):
                    direction = (20, 0)

    # --- Пауза ---
    if paused:
        pause_text = font.render("Paused - Press 'P' to continue", True, BLACK)
        screen.blit(pause_text, (WIDTH // 2 - 150, HEIGHT // 2))
        pygame.display.update()
        clock.tick(5)
        continue

    # --- Движение змейки ---
    new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])

    # --- Столкновения (границы, стены, сама себя) ---
    if (
        new_head in snake or
        new_head[0] < 0 or new_head[0] >= WIDTH or
        new_head[1] < 0 or new_head[1] >= HEIGHT or
        check_wall_collision(new_head, walls)
    ):
        print("Game Over!")
        save_score(user_id, level, score)
        break

    snake.insert(0, new_head)  # двигаем вперёд

    # --- Проверка: съел ли еду ---
    if new_head == food_pos:
        score += food_weight
        if score // 5 + 1 > level:  # каждые 5 очков — новый уровень
            level += 1
            speed = levels.get(level, {}).get("speed", speed + 2)
        food_pos, food_weight = generate_food()
        food_spawn_time = time.time()
    else:
        snake.pop()  # убираем хвост (если не поел)

    # --- Проверка: еда исчезает через 5 сек ---
    if time.time() - food_spawn_time >= 5:
        food_pos, food_weight = generate_food()
        food_spawn_time = time.time()

    # --- Отрисовка змейки ---
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (*segment, CELL_SIZE, CELL_SIZE))

    # --- Отрисовка еды ---
    food_color = FOOD_COLORS[food_weight]
    pygame.draw.rect(screen, food_color, (*food_pos, CELL_SIZE, CELL_SIZE))

    draw_walls(walls)  # рисуем стены

    # --- Отображение текста ---
    score_text = font.render(f"{username} | Score: {score} | Level: {level}", True, BLACK)
    screen.blit(score_text, (10, 10))

    pygame.display.update()
    clock.tick(speed)  # скорость зависит от уровня

# --- Конец игры ---
save_score(user_id, level, score)
close_connection()
pygame.quit()
sys.exit()