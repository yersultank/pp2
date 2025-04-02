import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    
    radius = 15
    draw_mode='line'
    x = 0
    y = 0
    mode = 'blue'
    points = []
    rectangles=[]
    circles=[]
    while True:
        
        pressed = pygame.key.get_pressed()
        
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
        
        for event in pygame.event.get():
            
            # determin if X was clicked, or Ctrl+W or Alt+F4 was used
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return
            
                # determine if a letter key was pressed
                if event.key == pygame.K_r:
                    mode = 'red'
                elif event.key == pygame.K_g:
                    mode = 'green'
                elif event.key == pygame.K_b:
                    mode = 'blue'
                elif event.key==pygame.K_l:
                    draw_mode='line'
                    points.clear()
                elif event.key==pygame.K_t:
                    draw_mode='rectangle'
                elif event.key==pygame.K_o:
                    draw_mode='circle'
                elif event.key==pygame.K_c:
                    screen.fill((0,0,0))
                    points.clear()
                    rectangles.clear()
                    circles.clear()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: # left click grows radius
                    if draw_mode=='rectangle':
                        rectangles.append((event.pos, mode))
                    elif draw_mode=='circle':
                        circles.append((event.pos, mode))
                    else:
                        radius = min(200, radius + 1)
                elif event.button == 3: # right click shrinks radius
                    radius = max(1, radius - 1)
            
            if event.type == pygame.MOUSEMOTION and draw_mode=='line':
                # if mouse moved, add point to list
                position = event.pos
                points = points + [position]
                

        screen.fill((0, 0, 0))
        
        # draw all points
        i = 0
        while i < len(points) - 1:
            drawLineBetween(screen, points[i], points[i + 1], radius, mode)
            i += 1

        for i in rectangles:
            drawrect(screen, i[0], i[1])

        for circle in circles:
            drawcircle(screen,circle[0], circle[1])
        
        pygame.display.flip()
        
        clock.tick(60)

def drawLineBetween(screen, start, end, width, color_mode):
    if color_mode == 'blue':
        color = (0, 0, 255)
    elif color_mode == 'red':
        color = (255, 0, 0)
    elif color_mode == 'green':
        color = (0, 255, 0)
    pygame.draw.line(screen, color, start, end, width)
def drawrect(screen, position, color_mode):
    if color_mode == 'blue':
        color = (0, 0, 255)
    elif color_mode == 'red':
        color = (255, 0, 0)
    elif color_mode == 'green':
        color = (0, 255, 0)
    x,y=position
    pygame.draw.rect(screen, color, (x,y,70,70))

def drawcircle(screen, position, color_mode):
    if color_mode == 'blue':
        color = (0, 0, 255)
    elif color_mode == 'red':
        color = (255, 0, 0)
    elif color_mode == 'green':
        color = (0, 255, 0)
    x,y=position
    pygame.draw.circle(screen, color, (x,y),30)
main()