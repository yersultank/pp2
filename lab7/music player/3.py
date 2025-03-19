import pygame
import os
pygame.init()
pygame.mixer.init()
pygame.font.init()
font=pygame.font.Font(None,30)

clock=pygame.time.Clock()
width=500
player=[]
playing=False
height=500
screen=pygame.display.set_mode((width, height))
folder=r'C:\Users\Ерс\Desktop\pp2\lab7\music player\songs'
songs=os.listdir(folder)
for song in songs:
    if song.endswith('.mp3'):
        player.append(os.path.join(folder, song))

pause = pygame.image.load('pause.png')
next = pygame.image.load('next.png')
previous = pygame.image.load('previous.png')

pause=pygame.transform.scale(pause,(50,50))
next=pygame.transform.scale(next,(50,50))
previous=pygame.transform.scale(previous,(50,50))
index=0
pause_rect=pause.get_rect(center=(250,250))
next_rect=next.get_rect(center=(350,250))
previous_rect=previous.get_rect(center=(150,250))
def song_play(index):
    global playing
    pygame.mixer.music.load(os.path.join(folder, player[index]))
    pygame.mixer.music.play()
    playing=True
song_play(index)
done=True
while done:
    screen.fill((255,255,255))
    screen.blit(pause, pause_rect.topleft)
    screen.blit(next,next_rect.topleft)
    screen.blit(previous, previous_rect.topleft)

    song_name=os.path.basename(player[index])
    text=font.render(f"Playing: {song_name}", True, (0,0,0))
    screen.blit(text, (50,180))

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=False
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                if playing:
                    pygame.mixer.music.pause()
                    playing=False
                else:
                    pygame.mixer.music.unpause()
                    playing=True
            elif event.key==pygame.K_s:
                pygame.mixer.music.stop()
                playing=False
        
            elif event.key==pygame.K_RIGHT:
                index=(index+1)%len(player)
                song_play(index)

            elif event.key==pygame.K_LEFT:
                index=(index-1)%len(player)
                song_play(index)
    
    screen.blit(pause, pause_rect.topleft)
    screen.blit(next,next_rect.topleft)
    screen.blit(previous, previous_rect.topleft)
    pygame.display.flip()

