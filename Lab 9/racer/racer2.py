import pygame
import sys
import random
import time

# Initialize pygame
pygame.init()

# Game constants
SCREEN_WIDTH, SCREEN_HEIGHT = 400, 600
SPEED = 5  # Initial enemy speed
SCORE = 0  # Player score
COINS_COLLECTED = 0  # Track collected coins
FPS = 60  # Frames per second

# Color definitions
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# Font setup
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over_text = font.render("Game Over", True, BLACK)

# Load background image
background = pygame.image.load("AnimatedStreet.png")

# Initialize screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Racing Game")
clock = pygame.time.Clock()

# Load and play background music
pygame.mixer.music.load("background.wav")
pygame.mixer.music.play(-1)  # -1 makes the music loop indefinitely

class Entity(pygame.sprite.Sprite):
    """Base class for all game entities"""
    def __init__(self, image_path, position):
        super().__init__()
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect(center=position)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

class Enemy(Entity):
    """Enemy car class"""
    def __init__(self):
        super().__init__("Enemy.png", (random.randint(40, SCREEN_WIDTH - 40), 0))

    def move(self):
        global SCORE
        self.rect.y += SPEED
        if self.rect.top > SCREEN_HEIGHT:
            SCORE += 1
            self.rect.topleft = (random.randint(40, SCREEN_WIDTH - 40), 0)

class Player(Entity):
    """Player controlled car"""
    def __init__(self):
        super().__init__("Player.png", (160, 520))

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT] and self.rect.right < SCREEN_WIDTH:
            self.rect.x += 5

class Coin(Entity):
    """Simple coin class worth 1 point"""
    def __init__(self):
        super().__init__("coin2.png", (random.randint(30, SCREEN_WIDTH - 30), 0))
        # Scale coin to consistent size
        self.image = pygame.transform.scale(self.image, (20, 20))
        self.rect = self.image.get_rect(center=(random.randint(30, SCREEN_WIDTH - 30), 0))

    def move(self):
        self.rect.y += 3
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.topleft = (random.randint(30, SCREEN_WIDTH - 30), 0)

# Create game objects
player = Player()
enemy = Enemy()

# Create sprite groups
all_sprites = pygame.sprite.Group(player, enemy)
enemies = pygame.sprite.Group(enemy)
coins = pygame.sprite.Group()

# Create first coin
new_coin = Coin()
coins.add(new_coin)
all_sprites.add(new_coin)

# Custom events
INC_SPEED = pygame.USEREVENT + 1  # Event to increase enemy speed over time
SPAWN_COIN = pygame.USEREVENT + 2  # Event to spawn new coins

# Set timers for events
pygame.time.set_timer(INC_SPEED, 1000)  # Increase speed every second
pygame.time.set_timer(SPAWN_COIN, 2000)  # Spawn new coin every 2 seconds

# Game loop
running = True
while running:
    # Draw background
    screen.blit(background, (0, 0))
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == INC_SPEED:
            SPEED += 0.2  # Gradually increase enemy speed
        if event.type == SPAWN_COIN:
            # Spawn new coin only if there are less than 3 coins on screen
            if len(coins) < 3:
                new_coin = Coin()
                coins.add(new_coin)
                all_sprites.add(new_coin)

    # Update game objects
    player.move()
    enemy.move()
    
    # Move all coins
    for coin in coins:
        coin.move()
    
    # Draw all sprites
    all_sprites.draw(screen)
    
    # Display score and coins collected
    score_text = font_small.render(f"Score: {SCORE}", True, BLACK)
    coins_text = font_small.render(f"Coins: {COINS_COLLECTED}", True, BLACK)
    screen.blit(score_text, (10, 10))
    screen.blit(coins_text, (10, 40))

    # Check for collisions with coins
    coins_collected = pygame.sprite.spritecollide(player, coins, True)
    for coin in coins_collected:
        COINS_COLLECTED += 1  # Each coin is worth 1 point
        # Increase enemy speed every 5 coins collected
        if COINS_COLLECTED % 5 == 0:
            SPEED += 1
    
    # Check for collision with enemy
    if pygame.sprite.spritecollideany(player, enemies):
        pygame.mixer.Sound("crash.wav").play()
        time.sleep(0.5)
        screen.fill(RED)
        screen.blit(game_over_text, (30, 250))
        # Display final score and coins
        final_score = font_small.render(f"Final Score: {SCORE}", True, WHITE)
        final_coins = font_small.render(f"Coins Collected: {COINS_COLLECTED}", True, WHITE)
        screen.blit(final_score, (100, 350))
        screen.blit(final_coins, (80, 400))
        pygame.display.update()
        time.sleep(3)
        running = False

    # Update display
    pygame.display.update()
    clock.tick(FPS)

# Clean up
pygame.quit()
sys.exit()