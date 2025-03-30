# Import required libraries
import pygame
import sys
import random
import time

# Initialize pygame library
pygame.init()

# Game configuration constants
SCREEN_WIDTH, SCREEN_HEIGHT = 400, 600  # Screen dimensions
SPEED = 5  # Initial speed of enemy cars
SCORE = 0  # Player's starting score
FPS = 60  # Frames per second for game loop

# Color definitions (RGB values)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Font setup for game text
font = pygame.font.SysFont("Verdana", 60)  # Large font for game over
font_small = pygame.font.SysFont("Verdana", 20)  # Small font for score
game_over_text = font.render("Game Over", True, BLACK)  # Pre-render game over text

# Load background image
background = pygame.image.load("AnimatedStreet.png")

# Initialize game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Game")  # Window title
clock = pygame.time.Clock()  # Create clock object for FPS control

# Load and play background music
pygame.mixer.music.load("background.wav")
pygame.mixer.music.play(-1)  # -1 makes the music loop indefinitely

class Entity(pygame.sprite.Sprite):
    """
    Base class for all game entities (player, enemies, etc.)
    Inherits from pygame.sprite.Sprite for sprite functionality
    """
    def __init__(self, image_path, position):
        """
        Initialize entity with image and position
        Args:
            image_path: Path to the sprite image file
            position: (x,y) tuple for initial position
        """
        super().__init__()  # Initialize parent class
        self.image = pygame.image.load(image_path)  # Load sprite image
        self.rect = self.image.get_rect(center=position)  # Create rect at position

    def draw(self, surface):
        """Draw the entity on the given surface"""
        surface.blit(self.image, self.rect)

class Enemy(Entity):
    """Class representing enemy cars"""
    def __init__(self):
        """Initialize enemy at random x position at top of screen"""
        super().__init__("Enemy.png", (random.randint(40, SCREEN_WIDTH - 40), 0))

    def move(self):
        """
        Move enemy down the screen
        If enemy goes off bottom, respawn at top with new random x position
        """
        global SCORE
        self.rect.y += SPEED  # Move down at current speed
        
        # If enemy moves off bottom of screen
        if self.rect.top > SCREEN_HEIGHT:
            SCORE += 1  # Increment score
            # Respawn at top with new random x position
            self.rect.topleft = (random.randint(40, SCREEN_WIDTH - 40), 0)

class Player(Entity):
    """Class representing the player's car"""
    def __init__(self):
        """Initialize player at starting position"""
        super().__init__("Player.png", (160, 520))  # Center bottom of screen

    def move(self):
        """Handle player movement based on keyboard input"""
        keys = pygame.key.get_pressed()  # Get current key states
        
        # Move left if LEFT key pressed and not at left edge
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= 5
            
        # Move right if RIGHT key pressed and not at right edge
        if keys[pygame.K_RIGHT] and self.rect.right < SCREEN_WIDTH:
            self.rect.x += 5

# Create player and first enemy instances
player = Player()
enemy = Enemy()

# Create sprite groups for drawing and collision detection
all_sprites = pygame.sprite.Group(player, enemy)  # Group for all sprites to draw
enemies = pygame.sprite.Group(enemy)  # Separate group just for enemies

# Custom event for increasing game speed
INC_SPEED = pygame.USEREVENT + 1
# Set timer to trigger speed increase every 1000ms (1 second)
pygame.time.set_timer(INC_SPEED, 1000)

# Main game loop
running = True
while running:
    # Draw background first (clears previous frame)
    screen.blit(background, (0, 0))
    
    # Event handling loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Window close button clicked
            running = False
        if event.type == INC_SPEED:  # Speed increase event triggered
            SPEED += 0.5  # Increase enemy speed

    # Update game objects
    player.move()  # Handle player movement
    enemy.move()  # Move enemy cars
    
    # Draw all sprites
    all_sprites.draw(screen)
    
    # Render and display current score
    score_text = font_small.render(str(SCORE), True, BLACK)
    screen.blit(score_text, (10, 10))

    # Check for collisions between player and enemies
    if pygame.sprite.spritecollideany(player, enemies):
        # Play crash sound
        pygame.mixer.Sound("crash.wav").play()
        
        # Brief pause before game over screen
        time.sleep(0.5)
        
        # Show game over screen
        screen.fill(RED)  # Red background
        screen.blit(game_over_text, (30, 250))  # Center game over text
        pygame.display.update()  # Update display
        
        # Wait 2 seconds before closing
        time.sleep(2)
        running = False  # Exit game loop

    # Update display
    pygame.display.update()
    
    # Maintain consistent frame rate
    clock.tick(FPS)

# Clean up pygame and exit
pygame.quit()
sys.exit()