import pygame
import math

def main():
    pygame.init()  # Initialize pygame
    screen = pygame.display.set_mode((640, 480))  # Create a screen with size 640x480
    clock = pygame.time.Clock()  # Create a clock object to control frame rate
    
    radius = 15  # Default brush size for lines
    draw_mode = 'line'  # Default drawing mode is 'line'
    mode = 'blue'  # Default color is blue
    points = []  # List to store points for line drawing
    rectangles = []  # List to store rectangles
    circles = []  # List to store circles
    right_triangles = []  # List to store right triangles
    equilateral_triangles = []  # List to store equilateral triangles
    rhombuses = []  # List to store rhombuses
    eraser_mode = False  # Flag to switch to eraser mode
    
    while True:
        
        pressed = pygame.key.get_pressed()  # Get the state of all keyboard keys
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]  # Check if Alt is held
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]  # Check if Ctrl is held
        
        # Handle all events in the event queue
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:  # Handle window close event
                return
            if event.type == pygame.KEYDOWN:  # Handle key press events
                # Handle Ctrl+W or Alt+F4 or Escape to close the window
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return
                
                # Switch drawing colors using key presses
                if event.key == pygame.K_r:
                    mode = 'red'
                elif event.key == pygame.K_g:
                    mode = 'green'
                elif event.key == pygame.K_b:
                    mode = 'blue'
                
                # Switch drawing modes using key presses
                elif event.key == pygame.K_l:
                    draw_mode = 'line'
                    eraser_mode = False
                elif event.key == pygame.K_s:
                    draw_mode = 'rectangle'
                    eraser_mode = False
                elif event.key == pygame.K_o:
                    draw_mode = 'circle'
                    eraser_mode = False
                elif event.key == pygame.K_t:
                    draw_mode = 'right triangle'
                    eraser_mode = False
                elif event.key == pygame.K_q:
                    draw_mode = 'equilateral triangle'
                    eraser_mode = False
                elif event.key == pygame.K_u:
                    draw_mode = 'rhombus'
                    eraser_mode = False
                elif event.key == pygame.K_e:
                    draw_mode = 'line'  # Switch to line mode for eraser
                    eraser_mode = True
                
                # Clear the screen and all shapes when 'C' is pressed
                elif event.key == pygame.K_c:
                    screen.fill((255, 255, 255))  # Fill the screen with white
                    points.clear()  # Clear the points list for lines
                    rectangles.clear()  # Clear rectangles
                    circles.clear()  # Clear circles
                    equilateral_triangles.clear()  # Clear equilateral triangles
                    right_triangles.clear()  # Clear right triangles
            
            if event.type == pygame.MOUSEBUTTONDOWN:  # Handle mouse button press
                if event.button == 1:  # Left click increases radius or creates shapes
                    if draw_mode == 'rectangle':
                        rectangles.append((event.pos, mode))  # Store rectangle
                    elif draw_mode == 'circle':
                        circles.append((event.pos, mode))  # Store circle
                    elif draw_mode == 'right triangle':
                        right_triangles.append((event.pos, mode))  # Store right triangle
                    elif draw_mode == 'equilateral triangle':
                        equilateral_triangles.append((event.pos, mode))  # Store equilateral triangle
                    elif draw_mode == 'rhombus':
                        rhombuses.append((event.pos, mode))  # Store rhombus
                    else:
                        radius = min(200, radius + 1)  # Increase the radius for line drawing
                elif event.button == 3:  # Right click decreases radius
                    radius = max(1, radius - 1)  # Decrease the radius for line drawing
            
            if event.type == pygame.MOUSEMOTION:  # Handle mouse movement
                position = event.pos  # Get the current position of the mouse
                if draw_mode == 'line' or eraser_mode:  # If in line or eraser mode
                    if eraser_mode:  # If in eraser mode, add 'eraser' label to points
                        points.append((position, 'eraser'))
                    else:
                        points.append((position, mode))  # Add points with the selected color mode

        screen.fill((255, 255, 255))  # Clear the screen with a white background
        
        # Draw all points stored for lines
        i = 0
        while i < len(points) - 1:
            drawLineBetween(screen, points[i][0], points[i + 1][0], radius, points[i][1])  # Draw line
            i += 1

        # Draw all shapes: rectangles, circles, triangles, and rhombuses
        for i in rectangles:
            drawrect(screen, i[0], i[1])  # Draw rectangles

        for circle in circles:
            drawcircle(screen, circle[0], circle[1])  # Draw circles
        
        for triangle in right_triangles:
            draw_right_triangle(screen, triangle[0], triangle[1])  # Draw right triangles

        for triangle in equilateral_triangles:
            draw_equilateral_triangle(screen, triangle[0], triangle[1])  # Draw equilateral triangles

        for rhombus in rhombuses:
            draw_rhombus(screen, rhombus[0], rhombus[1])  # Draw rhombuses

        pygame.display.flip()  # Update the display
        clock.tick(60)  # Set the frame rate to 60 FPS

# Function to draw a line between two points
def drawLineBetween(screen, start, end, width, color_mode):
    if color_mode == 'blue':
        color = (0, 0, 255)  # Blue color for line
    elif color_mode == 'red':
        color = (255, 0, 0)  # Red color for line
    elif color_mode == 'green':
        color = (0, 255, 0)  # Green color for line
    elif color_mode == 'eraser':
        color = (255, 255, 255)  # White color for eraser (effectively erases)
    pygame.draw.line(screen, color, start, end, width)  # Draw the line

# Function to draw a rectangle
def drawrect(screen, position, color_mode):
    if color_mode == 'blue':
        color = (0, 0, 255)
    elif color_mode == 'red':
        color = (255, 0, 0)
    elif color_mode == 'green':
        color = (0, 255, 0)
    x, y = position
    pygame.draw.rect(screen, color, (x, y, 70, 70))  # Draw the rectangle

# Function to draw a circle
def drawcircle(screen, position, color_mode):
    if color_mode == 'blue':
        color = (0, 0, 255)
    elif color_mode == 'red':
        color = (255, 0, 0)
    elif color_mode == 'green':
        color = (0, 255, 0)
    x, y = position
    pygame.draw.circle(screen, color, (x, y), 30)  # Draw the circle

# Function to draw a right triangle
def draw_right_triangle(screen, position, color_mode):
    if color_mode == 'blue':
        color = (0, 0, 255)
    elif color_mode == 'red':
        color = (255, 0, 0)
    elif color_mode == 'green':
        color = (0, 255, 0)
    x, y = position
    dots = [(x, y), (x + 70, y), (x, y - 70)]  # Right triangle vertices
    pygame.draw.polygon(screen, color, dots)  # Draw the triangle

# Function to draw an equilateral triangle
def draw_equilateral_triangle(screen, position, color_mode, side_length=100):
    if color_mode == 'blue':
        color = (0, 0, 255)
    elif color_mode == 'red':
        color = (255, 0, 0)
    elif color_mode == 'green':
        color = (0, 255, 0)
    x, y = position
    height = (math.sqrt(3) / 2) * side_length  # Calculate height for equilateral triangle
    dots = [(x, y), (x + side_length, y), (x + side_length / 2, y - height)]  # Equilateral triangle vertices
    pygame.draw.polygon(screen, color, dots)  # Draw the triangle

# Function to draw a rhombus
def draw_rhombus(screen, position, color_mode, width=60, height=100):
    if color_mode == 'blue':
        color = (0, 0, 255)
    elif color_mode == 'red':
        color = (255, 0, 0)
    elif color_mode == 'green':
        color = (0, 255, 0)
    x, y = position
    dots = [(x - width // 2, y), (x, y - height // 2), (x + width // 2, y), (x, y + height // 2)]  # Rhombus vertices
    pygame.draw.polygon(screen, color, dots)  # Draw the rhombus

# Run the main function
main()