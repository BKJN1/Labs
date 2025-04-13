import pygame
import sys
import random
import time

# Initialize pygame
pygame.init()

# Game Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 500, 500
CELL_SIZE = 20
INITIAL_SPEED = 10

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
PURPLE = (128, 0, 128)

# Set up display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Enhanced Snake Game")
clock = pygame.time.Clock()

# Fonts
font = pygame.font.SysFont("Verdana", 20)

color = (random.randint(1, 250), random.randint(1, 250), random.randint(1, 250))

class Food:
    """Class to represent food items with different weights and timers"""
    def __init__(self, snake):
        self.types = [
            {"color": RED, "weight": 1, "lifetime": 0},       # Normal food (no timer)
            {"color": YELLOW, "weight": 2, "lifetime": 5},    # Bonus food (disappears after 5 seconds)
            {"color": PURPLE, "weight": 3, "lifetime": 3}     # Super food (disappears after 3 seconds)
        ]
        self.generate(snake)
    
    def generate(self, snake):
        """Generate new food at random position"""
        while True:
            x = random.randint(0, (SCREEN_WIDTH // CELL_SIZE) - 1) * CELL_SIZE
            y = random.randint(0, (SCREEN_HEIGHT // CELL_SIZE) - 1) * CELL_SIZE
            if (x, y) not in snake:
                self.type = random.choices(self.types, weights=[70, 20, 10])[0]  # Weighted random selection
                self.position = (x, y)
                self.spawn_time = time.time()
                break
    
    def should_disappear(self):
        """Check if timed food should disappear"""
        if self.type["lifetime"] > 0:
            return time.time() - self.spawn_time > self.type["lifetime"]
        return False
    
    def draw(self):
        """Draw the food on screen"""
        pygame.draw.rect(screen, self.type["color"], 
                         pygame.Rect(self.position[0], self.position[1], CELL_SIZE, CELL_SIZE))

def draw_snake(snake):
    """Draw the snake on screen"""
    for segment in snake:
        
        pygame.draw.rect(screen, color, pygame.Rect(segment[0], segment[1], CELL_SIZE, CELL_SIZE))

def game_over_screen(score, level):
    """Display game over screen with final stats"""
    screen.fill(BLACK)
    game_over_font = pygame.font.SysFont("Verdana", 40)
    stats_font = pygame.font.SysFont("Verdana", 30)
    
    game_over_text = game_over_font.render("GAME OVER", True, RED)
    score_text = stats_font.render(f"Final Score: {score}", True, WHITE)
    level_text = stats_font.render(f"Final Level: {level}", True, WHITE)
    
    screen.blit(game_over_text, (SCREEN_WIDTH//2 - 100, SCREEN_HEIGHT//2 - 60))
    screen.blit(score_text, (SCREEN_WIDTH//2 - 100, SCREEN_HEIGHT//2))
    screen.blit(level_text, (SCREEN_WIDTH//2 - 100, SCREEN_HEIGHT//2 + 40))
    
    pygame.display.update()
    time.sleep(3)
    pygame.quit()
    sys.exit()

# Initialize game state
snake = [(100, 100), (80, 100), (60, 100)]
direction = (CELL_SIZE, 0)
food = Food(snake)
score = 0
level = 1
speed = INITIAL_SPEED
food_timer = 0

# Game loop
running = True
while running:
    screen.fill(BLACK)
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Handle keyboard input for direction changes
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and direction != (0, CELL_SIZE):
        direction = (0, -CELL_SIZE)
    elif keys[pygame.K_DOWN] and direction != (0, -CELL_SIZE):
        direction = (0, CELL_SIZE)
    elif keys[pygame.K_LEFT] and direction != (CELL_SIZE, 0):
        direction = (-CELL_SIZE, 0)
    elif keys[pygame.K_RIGHT] and direction != (-CELL_SIZE, 0):
        direction = (CELL_SIZE, 0)
    
    # Move snake by adding new head and removing tail (unless food is eaten)
    new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
    
    # Check for collisions with walls or self
    if (new_head in snake or
        new_head[0] < 0 or new_head[0] >= SCREEN_WIDTH or
        new_head[1] < 0 or new_head[1] >= SCREEN_HEIGHT):
        game_over_screen(score, level)
    
    snake.insert(0, new_head)
    
    # Check if snake eats food
    if new_head == food.position:
        score += food.type["weight"]
        
        color = (random.randint(1, 250), random.randint(1, 250), random.randint(1, 250))
        pygame.mixer.Sound("jump.mp3").play()
        
        # Level up every 5 points (regardless of food weight)
        if score // 5 >= level:
            level += 1
            speed += 2
        
        food = Food(snake)  # Generate new food
    else:
        snake.pop()  # Remove tail if no food eaten
    
    # Check if food should disappear (for timed food)
    if food.should_disappear():
        food = Food(snake)
    
    # Draw food (with appropriate color based on type)
    food.draw()
    
    # Draw snake
    draw_snake(snake)
    
    # Display game information
    score_text = font.render(f"Score: {score}", True, WHITE)
    level_text = font.render(f"Level: {level}", True, WHITE)
    food_weight_text = font.render(f"Food Value: {food.type['weight']}", True, food.type["color"])
    
    # Show timer for timed food
    if food.type["lifetime"] > 0:
        remaining_time = max(0, food.type["lifetime"] - (time.time() - food.spawn_time))
        timer_text = font.render(f"Time: {remaining_time:.1f}s", True, WHITE)
        screen.blit(timer_text, (SCREEN_WIDTH - 100, 10))
    
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (10, 40))
    screen.blit(food_weight_text, (10, 70))
    
    pygame.display.update()
    clock.tick(speed)

pygame.quit()
sys.exit()