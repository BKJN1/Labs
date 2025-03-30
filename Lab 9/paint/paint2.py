import pygame
import math

# Initialize pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Advanced Drawing App")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Drawing settings
radius = 15
drawing_mode = 'free'  # free, circle, rectangle, square, right_triangle, equilateral_triangle, rhombus
color_mode = 'blue'
points = []
start_pos = None
drawing = False
shapes = []
font = pygame.font.SysFont('Arial', 18)

clock = pygame.time.Clock()

def get_color(mode):
    """Return RGB color based on current mode"""
    return {
        'blue': BLUE,
        'red': RED,
        'green': GREEN,
        'eraser': BLACK
    }.get(mode, WHITE)

def draw_line_between(screen, start, end, width, color):
    """Draw a smooth line between two points"""
    dx = end[0] - start[0]
    dy = end[1] - start[1]
    distance = max(abs(dx), abs(dy))
    
    if distance == 0:
        return
        
    for i in range(distance):
        progress = i / distance
        x = int(start[0] + dx * progress)
        y = int(start[1] + dy * progress)
        pygame.draw.circle(screen, color, (x, y), width)

def draw_right_triangle(screen, color, start, end, is_preview=False):
    """Draw a right triangle with right angle at start position"""
    points = [
        start,
        (end[0], start[1]),  # Right angle point
        end
    ]
    if is_preview:
        pygame.draw.polygon(screen, color, points, 1)
    else:
        pygame.draw.polygon(screen, color, points)

def draw_equilateral_triangle(screen, color, start, end, is_preview=False):
    """Draw an equilateral triangle"""
    base = end[0] - start[0]
    height = (math.sqrt(3)/2) * abs(base)
    
    # Determine if we're drawing left or right
    if base > 0:
        apex = (start[0] + base/2, start[1] - height)
    else:
        apex = (start[0] + base/2, start[1] - height)
    
    points = [start, end, apex]
    if is_preview:
        pygame.draw.polygon(screen, color, points, 1)
    else:
        pygame.draw.polygon(screen, color, points)

def draw_rhombus(screen, color, start, end, is_preview=False):
    """Draw a proper rhombus (diamond) shape"""
    center_x = (start[0] + end[0]) / 2
    center_y = (start[1] + end[1]) / 2
    
    # Calculate vectors
    dx = end[0] - start[0]
    dy = end[1] - start[1]
    
    # Perpendicular vector
    perp_dx = -dy
    perp_dy = dx
    
    # Calculate all four points
    p1 = start
    p2 = (center_x + perp_dx * 0.5, center_y + perp_dy * 0.5)
    p3 = end
    p4 = (center_x - perp_dx * 0.5, center_y - perp_dy * 0.5)
    
    points = [p1, p2, p3, p4]
    if is_preview:
        pygame.draw.polygon(screen, color, points, 1)
    else:
        pygame.draw.polygon(screen, color, points)

# Main game loop
running = True
while running:
    screen.fill(BLACK)
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # Key presses
        if event.type == pygame.KEYDOWN:
            # Shape selection
            if event.key == pygame.K_f:
                drawing_mode = 'free'
            elif event.key == pygame.K_c:
                drawing_mode = 'circle'
            elif event.key == pygame.K_t:
                drawing_mode = 'rectangle'
            elif event.key == pygame.K_s:
                drawing_mode = 'square'
            elif event.key == pygame.K_y:
                drawing_mode = 'right_triangle'
            elif event.key == pygame.K_u:
                drawing_mode = 'equilateral_triangle'
            elif event.key == pygame.K_h:
                drawing_mode = 'rhombus'
            
            # Color selection
            elif event.key == pygame.K_r:
                color_mode = 'red'
            elif event.key == pygame.K_g:
                color_mode = 'green'
            elif event.key == pygame.K_b:
                color_mode = 'blue'
            elif event.key == pygame.K_e:
                color_mode = 'eraser'
            
            # Other controls
            elif event.key == pygame.K_n and (pygame.key.get_mods() & pygame.KMOD_CTRL):
                shapes = []  # Clear screen
            elif event.key == pygame.K_z and (pygame.key.get_mods() & pygame.KMOD_CTRL) and shapes:
                shapes.pop()  # Undo
        
        # Mouse events
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left click
                start_pos = event.pos
                drawing = True
                if drawing_mode == 'free':
                    points = [start_pos]
        
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1 and start_pos:  # Left click release
                drawing = False
                end_pos = event.pos
                
                color = get_color(color_mode)
                
                if drawing_mode == 'rectangle':
                    x = min(start_pos[0], end_pos[0])
                    y = min(start_pos[1], end_pos[1])
                    width = abs(end_pos[0] - start_pos[0])
                    height = abs(end_pos[1] - start_pos[1])
                    if width > 1 and height > 1:
                        shapes.append(('rectangle', color, pygame.Rect(x, y, width, height)))
                
                elif drawing_mode == 'square':
                    size = max(abs(end_pos[0] - start_pos[0]), abs(end_pos[1] - start_pos[1]))
                    x = start_pos[0] if end_pos[0] > start_pos[0] else start_pos[0] - size
                    y = start_pos[1] if end_pos[1] > start_pos[1] else start_pos[1] - size
                    if size > 1:
                        shapes.append(('square', color, pygame.Rect(x, y, size, size)))
                
                elif drawing_mode == 'circle':
                    radius_shape = int(math.dist(start_pos, end_pos))
                    if radius_shape > 1:
                        shapes.append(('circle', color, start_pos, radius_shape))
                
                elif drawing_mode == 'right_triangle':
                    if math.dist(start_pos, end_pos) > 10:
                        shapes.append(('right_triangle', color, start_pos, end_pos))
                
                elif drawing_mode == 'equilateral_triangle':
                    if math.dist(start_pos, end_pos) > 10:
                        shapes.append(('equilateral_triangle', color, start_pos, end_pos))
                
                elif drawing_mode == 'rhombus':
                    if math.dist(start_pos, end_pos) > 10:
                        shapes.append(('rhombus', color, start_pos, end_pos))
                
                elif drawing_mode == 'free' and len(points) > 1:
                    shapes.append(('free', color, points.copy(), radius))
                
                points = []
        
        if event.type == pygame.MOUSEMOTION and drawing:
            if drawing_mode == 'free':
                points.append(event.pos)
                points = points[-512:]  # Limit stored points
    
    # Draw all saved shapes
    for shape in shapes:
        if shape[0] == 'rectangle':
            pygame.draw.rect(screen, shape[1], shape[2])
        elif shape[0] == 'square':
            pygame.draw.rect(screen, shape[1], shape[2])
        elif shape[0] == 'circle':
            pygame.draw.circle(screen, shape[1], shape[2], shape[3])
        elif shape[0] == 'right_triangle':
            draw_right_triangle(screen, shape[1], shape[2], shape[3])
        elif shape[0] == 'equilateral_triangle':
            draw_equilateral_triangle(screen, shape[1], shape[2], shape[3])
        elif shape[0] == 'rhombus':
            draw_rhombus(screen, shape[1], shape[2], shape[3])
        elif shape[0] == 'free' and len(shape[2]) > 1:
            for i in range(len(shape[2]) - 1):
                draw_line_between(screen, shape[2][i], shape[2][i + 1], shape[3], shape[1])
    
    # Draw current freehand
    if drawing and drawing_mode == 'free' and len(points) > 1:
        for i in range(len(points) - 1):
            draw_line_between(screen, points[i], points[i + 1], radius, get_color(color_mode))
    
    # Draw preview for other shapes
    if drawing and start_pos and pygame.mouse.get_pressed()[0] and drawing_mode != 'free':
        current_pos = pygame.mouse.get_pos()
        color = get_color(color_mode)
        
        if drawing_mode == 'rectangle':
            x = min(start_pos[0], current_pos[0])
            y = min(start_pos[1], current_pos[1])
            width = abs(current_pos[0] - start_pos[0])
            height = abs(current_pos[1] - start_pos[1])
            pygame.draw.rect(screen, color, pygame.Rect(x, y, width, height), 1)
        
        elif drawing_mode == 'square':
            size = max(abs(current_pos[0] - start_pos[0]), abs(current_pos[1] - start_pos[1]))
            x = start_pos[0] if current_pos[0] > start_pos[0] else start_pos[0] - size
            y = start_pos[1] if current_pos[1] > start_pos[1] else start_pos[1] - size
            pygame.draw.rect(screen, color, pygame.Rect(x, y, size, size), 1)
        
        elif drawing_mode == 'circle':
            radius_preview = int(math.dist(start_pos, current_pos))
            pygame.draw.circle(screen, color, start_pos, radius_preview, 1)
        
        elif drawing_mode == 'right_triangle':
            draw_right_triangle(screen, color, start_pos, current_pos, True)
        
        elif drawing_mode == 'equilateral_triangle':
            draw_equilateral_triangle(screen, color, start_pos, current_pos, True)
        
        elif drawing_mode == 'rhombus':
            draw_rhombus(screen, color, start_pos, current_pos, True)
    
    # Draw status bar
    status_bar = pygame.Rect(0, SCREEN_HEIGHT - 20, SCREEN_WIDTH, 20)
    pygame.draw.rect(screen, (50, 50, 50), status_bar)
    
    # Display current settings
    status_text = (
        f"Shape: {drawing_mode.capitalize()} | "
        f"Color: {color_mode.capitalize()} | "
        f"Size: {radius} | "
        f"Shortcuts: F=Free, C=Circle, T=Rectangle, S=Square, Y=Right△, U=Equilateral△, H=Rhombus | "
        f"Colors: R=Red, G=Green, B=Blue, E=Eraser | "
        f"Ctrl+Z=Undo, Ctrl+N=Clear"
    )
    text_surface = font.render(status_text, True, WHITE)
    screen.blit(text_surface, (5, SCREEN_HEIGHT - 18))
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()