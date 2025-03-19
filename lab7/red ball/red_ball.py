import pygame
pygame.init()
radius=25
screen=pygame.display.set_mode((700,700))
done=True
color=(255,0,0)
x=25
y=25
clock=pygame.time.Clock()
while done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=False
    pressed=pygame.key.get_pressed()
    if pressed[pygame.K_UP] and y-radius-20>=0: y-=20
    if pressed[pygame.K_DOWN]and y+radius<=700: y+=20
    if pressed[pygame.K_LEFT] and x-radius-20>=0: x-=20
    if pressed[pygame.K_RIGHT] and x+radius<=700: x+=20
    screen.fill((255,255,255))
    pygame.draw.circle(screen, color, [x,y], radius, 0)
    pygame.display.flip()
    clock.tick(60)