import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Drawing App")
    clock = pygame.time.Clock()
    
    # Default settings
    radius = 15
    mode = 'blue'
    shape = 'free'
    points = []
    start_pos = None
    drawing = False
    shapes = []
    font = pygame.font.SysFont('Arial', 18)
    
    while True:
        pressed = pygame.key.get_pressed()
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return
                if event.key == pygame.K_n and ctrl_held:
                    # Clear screen
                    shapes = []
                    points = []
                
                # Color selection
                if event.key == pygame.K_r:
                    mode = 'red'
                elif event.key == pygame.K_g:
                    mode = 'green'
                elif event.key == pygame.K_b:
                    mode = 'blue'
                elif event.key == pygame.K_e:
                    mode = 'eraser'
                
                # Shape selection
                if event.key == pygame.K_f:
                    shape = 'free'
                elif event.key == pygame.K_c:
                    shape = 'circle'
                elif event.key == pygame.K_t:
                    shape = 'rectangle'
                
                # Undo functionality
                if event.key == pygame.K_z and ctrl_held and shapes:
                    shapes.pop()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left click to start drawing
                    start_pos = event.pos
                    drawing = True
                    if shape == 'free':
                        points = [start_pos]  # Start new stroke
                elif event.button == 3:  # Right click to shrink radius
                    radius = max(1, radius - 1)
                elif event.button == 4:  # Mouse wheel up to increase radius
                    radius = min(100, radius + 1)
                elif event.button == 5:  # Mouse wheel down to decrease radius
                    radius = max(1, radius - 1)
            
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1 and start_pos:  # Left click release
                    drawing = False
                    if shape == 'rectangle':
                        x = min(start_pos[0], event.pos[0])
                        y = min(start_pos[1], event.pos[1])
                        width = abs(event.pos[0] - start_pos[0])
                        height = abs(event.pos[1] - start_pos[1])
                        if width > 1 and height > 1:
                            shapes.append(('rectangle', get_color(mode), pygame.Rect(x, y, width, height)))
                    elif shape == 'circle':
                        radius_circle = int(((event.pos[0] - start_pos[0])**2 + (event.pos[1] - start_pos[1])**2)**0.5)
                        if radius_circle > 1:
                            shapes.append(('circle', get_color(mode), start_pos, radius_circle))
                    elif shape == 'free' and len(points) > 1:
                        # Save the freehand stroke
                        shapes.append(('free', get_color(mode), points.copy(), radius))
                    points = []  # Clear points after shape is completed
            
            if event.type == pygame.MOUSEMOTION and drawing:
                if shape == 'free':
                    points.append(event.pos)
                    points = points[-512:]  # Limit stored points
        
        # Draw everything
        screen.fill((0, 0, 0))
        
        # Draw all saved shapes
        for s in shapes:
            if s[0] == 'rectangle':
                pygame.draw.rect(screen, s[1], s[2])
            elif s[0] == 'circle':
                pygame.draw.circle(screen, s[1], s[2], s[3])
            elif s[0] == 'free' and len(s[2]) > 1:
                # Draw saved freehand strokes
                for i in range(len(s[2]) - 1):
                    draw_line_between(screen, i, s[2][i], s[2][i + 1], s[3], s[1])
        
        # Draw current freehand (while drawing)
        if shape == 'free' and len(points) > 1:
            for i in range(len(points) - 1):
                draw_line_between(screen, i, points[i], points[i + 1], radius, get_color(mode))
        
        # Draw preview for rectangle and circle
        if drawing and start_pos and pygame.mouse.get_pressed()[0]:
            current_pos = pygame.mouse.get_pos()
            if shape == 'rectangle':
                x = min(start_pos[0], current_pos[0])
                y = min(start_pos[1], current_pos[1])
                width = abs(current_pos[0] - start_pos[0])
                height = abs(current_pos[1] - start_pos[1])
                pygame.draw.rect(screen, get_color(mode), pygame.Rect(x, y, width, height), 1)
            elif shape == 'circle':
                radius_preview = int(((current_pos[0] - start_pos[0])**2 + (current_pos[1] - start_pos[1])**2)**0.5)
                pygame.draw.circle(screen, get_color(mode), start_pos, radius_preview, 1)
        
        # Draw status bar
        status_bar = pygame.Rect(0, 580, 800, 20)
        pygame.draw.rect(screen, (50, 50, 50), status_bar)
        
        # Display current settings
        status_text = f"Shape: {shape.capitalize()} | Color: {mode.capitalize()} | Radius: {radius} | LClick+Drag: Draw | RClick: Radius- | Wheel: Radius+ | Ctrl+Z: Undo | Ctrl+N: New"
        text_surface = font.render(status_text, True, (255, 255, 255))
        screen.blit(text_surface, (5, 582))
        
        pygame.display.flip()
        clock.tick(60)

def draw_line_between(screen, index, start, end, width, color):
    """Draw a line between two points"""
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))
    
    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(screen, color, (x, y), width)

def get_color(mode):
    """Get RGB color based on current mode"""
    if mode == 'blue':
        return (0, 0, 255)
    elif mode == 'red':
        return (255, 0, 0)
    elif mode == 'green':
        return (0, 255, 0)
    elif mode == 'eraser':
        return (0, 0, 0)
    return (255, 255, 255)

if __name__ == "__main__":
    main()