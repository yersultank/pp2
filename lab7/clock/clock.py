import pygame
import time
pygame.init()
clock=pygame.time.Clock()
width=800
height=600
screen=pygame.display.set_mode((width, height))
img=pygame.image.load('mickey.jpg')
second_img=pygame.image.load('leftarm.png')
minute_img=pygame.image.load('rightarm.png')
img=pygame.transform.scale(img, (800,600))
done=True
x=0
y=0
while done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=False
    time_now=time.localtime()
    minute=time_now.tm_min
    second=time_now.tm_sec
    minute_angle=minute*6+(6*(second/60))
    second_angle=second*6

    screen.blit(img,(x,y))
    
    updated_minute=pygame.transform.rotate(pygame.transform.scale(minute_img, (600,800)), -minute_angle)
    minute_rect=updated_minute.get_rect(center=(400,312))
    screen.blit(updated_minute,minute_rect)

    updated_second=pygame.transform.rotate(pygame.transform.scale(second_img,(40,680)), -second_angle)
    second_rect=updated_second.get_rect(center=(400,310))
    screen.blit(updated_second,second_rect)
    
    pygame.display.flip()
    clock.tick(60)
