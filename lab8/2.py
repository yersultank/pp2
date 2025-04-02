import pygame
#R-red color
#G-green color
#B-blue color
#O-circle mode
#T-rectangle mode
#L-line mode
def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))  # Create game window
    clock = pygame.time.Clock()  # Initialize clock for frame rate control
    
    radius = 15  # Default brush size
    draw_mode = 'line'  # Default drawing mode
    mode = 'blue'  # Default drawing color
    points = []  # Stores points for line drawing
    rectangles = []  # Stores rectangle data
    circles = []  # Stores circle data
    
    while True:
        pressed = pygame.key.get_pressed()
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
        
        for event in pygame.event.get():
            # Handle window close event
            if event.type == pygame.QUIT:
                return
            
            # Handle key presses
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return
                
                # Change drawing color
                if event.key == pygame.K_r:
                    mode = 'red'
                elif event.key == pygame.K_g:
                    mode = 'green'
                elif event.key == pygame.K_b:
                    mode = 'blue'
                
                # Change drawing mode
                elif event.key == pygame.K_l:
                    draw_mode = 'line'
                elif event.key == pygame.K_t:
                    draw_mode = 'rectangle'
                elif event.key == pygame.K_o:
                    draw_mode = 'circle'
                elif event.key == pygame.K_c:
                    screen.fill((255, 255, 255))  # Clear screen
                    points.clear()
                    rectangles.clear()
                    circles.clear()
            
            # Handle mouse button events
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left click
                    if draw_mode == 'rectangle':
                        rectangles.append((event.pos, mode))
                    elif draw_mode == 'circle':
                        circles.append((event.pos, mode))
                    else:
                        radius = min(200, radius + 1)  # Increase brush size
                elif event.button == 3:  # Right click
                    radius = max(1, radius - 1)  # Decrease brush size
            
            # Handle mouse movement for line drawing
            if event.type == pygame.MOUSEMOTION and draw_mode == 'line':
                position = event.pos
                points.append((position, mode))
                
        screen.fill((255, 255, 255))  # Clear the screen each frame
        
        # Draw lines between stored points
        i = 0
        while i < len(points) - 1:
            drawLineBetween(screen, points[i][0], points[i + 1][0], radius, points[i][1])
            i += 1
        
        # Draw stored rectangles and circles
        for rect in rectangles:
            drawrect(screen, rect[0], rect[1])
        
        for circle in circles:
            drawcircle(screen, circle[0], circle[1])
        
        pygame.display.flip()  # Refresh the screen
        clock.tick(60)  # Limit frame rate to 60 FPS

def drawLineBetween(screen, start, end, width, color_mode):
    """Draws a line between two points with the given width and color."""
    if color_mode == 'blue':
        color = (0, 0, 255)
    elif color_mode == 'red':
        color = (255, 0, 0)
    elif color_mode == 'green':
        color = (0, 255, 0)  # Default to white if invalid
    pygame.draw.line(screen, color, start, end, width)

def drawrect(screen, position, color_mode):
    """Draws a rectangle at the specified position with the given color."""
    if color_mode == 'blue':
        color = (0, 0, 255)
    elif color_mode == 'red':
        color = (255, 0, 0)
    elif color_mode == 'green':
        color = (0, 255, 0)
    x, y = position
    pygame.draw.rect(screen, color, (x, y, 70, 70))

def drawcircle(screen, position, color_mode):
    """Draws a circle at the specified position with the given color."""
    if color_mode == 'blue':
        color = (0, 0, 255)
    elif color_mode == 'red':
        color = (255, 0, 0)
    elif color_mode == 'green':
        color = (0, 255, 0)
    x, y = position
    pygame.draw.circle(screen, color, (x, y), 30)

main()