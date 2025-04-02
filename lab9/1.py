import pygame
from pygame.locals import *
import random
import time
import sys
pygame.init()
width=400
height=600 # window size
clock=pygame.time.Clock()
display=pygame.display.set_mode((width,height))
black=pygame.Color(0,0,0)
white=pygame.Color(255,255,255)
grey=pygame.Color(128,128,128)
red=pygame.Color(255,0,0)
speed=1 # speed of enemies
score=0 # number of enemy cars passed
coins=0 # number of collected coins
display.fill(white)
new_size=(100,100)

font=pygame.font.SysFont("Verdana",60)
font_small=pygame.font.SysFont("Verdana",20)
game_over=font.render("Game Over", True, black) # the black "Game Over" text

backround=pygame.image.load("AnimatedStreet.png") # background image


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("enemy.png") # loading enemy car image
        self.rect=self.image.get_rect() # get a rectangle of image
        self.rect.center=(random.randint(40,width-40),0) # place the image randomly by x-axis
    
    def move(self):
        global score
        self.rect.move_ip(0,speed) # moves the enemy car vertically in current speed
        if self.rect.bottom>600: # if enemy car passes the player's car
            score+=1 # score++
            self.rect.top=0 # place enemy car back to the top of the window after
            self.rect.center=(random.randint(30,370),0) # randomly by x-axis


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("player.png") # loading player's car image
        self.rect=self.image.get_rect() # get a rectangle of image
        self.rect.center=(160,520) # place it in this coordinate
    
    def move(self):
        pressed=pygame.key.get_pressed()
        if self.rect.left>0:
            if pressed[K_LEFT]:
                self.rect.move_ip(-20,0) # if left keyboard is pressed move the car by 20 pixels left by x-axis
        
        if self.rect.right<width:
            if pressed[K_RIGHT]:
                self.rect.move_ip(20,0) # if right keyboard is pressed move the car by 20 pixels right by x-axis


class Bigcoin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("diamond.png") # loading image of big coin
        self.image=pygame.transform.scale(self.image, (50,50)) # resizing the image
        self.rect=self.image.get_rect() # get a rectangle of image
        self.rect.center=(random.randint(40,width-40), 520) # place it randomly by x-axis
    
    def move(self):
        global coins
        global speed
        if pygame.sprite.spritecollide(P1,monety,True): # if the player's car's rectangle and big coin's rectangle collide with each other
            coins+=2 # increase coins count by 2
            speed+=0.2 # increase enemy speed
            self.kill() # delete the big coin from the screen
            pygame.time.set_timer(pygame.USEREVENT+2,500,1) # 0.5 sec timer to draw new coin in random position
            self.rect.center=(random.randint(40,width-40),520)

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("coin.png") # loading image of coin
        self.image = pygame.transform.scale(self.image, (40, 40)) # resizing the image
        self.rect=self.image.get_rect() # get a rectangle of image
        self.rect.center=(random.randint(40,width-40),520) # place it randomly by x-axis

    def move(self):
        global coins
        global speed
        if pygame.sprite.spritecollide(P1, monety, True): # if the player's car's rectangle and coin's rectangle collide with each other
            coins+=1 # increase coins count by 1
            speed+=0.2 # increase enemy speed
            self.kill() # delete the coin from the screen
            pygame.time.set_timer(pygame.USEREVENT+2,500,1) # 0.5 sec timer to draw new coin in random position
            self.rect.center=(random.randint(40,width-40),520)

    def update(self):
        self.move()
P1=Player() # instance of Player class
E1=Enemy() # instance of Enemy class
C1=Coin() # instance of Coin class
C2=Bigcoin() # instance of Bigcoin class
enemies=pygame.sprite.Group()
enemies.add(E1) # created group and added E1 to manage enemy cars
all_sprites=pygame.sprite.Group()
monety=pygame.sprite.Group()
monety.add(C1) # created group and added C1 to manage coins
monety.add(C2) # created group and added C2 to manage big coins
all_sprites.add(E1)
all_sprites.add(P1)
all_sprites.add(C1)
all_sprites.add(C2) #group containing every object of the game to manage them
inc_speed=pygame.USEREVENT+1
pygame.time.set_timer(inc_speed,1000) # increase speed every 1 second


done=True
while done:
    for event in pygame.event.get():
        
        if event.type==pygame.QUIT:
            done=False
            pygame.quit()

        if event.type == pygame.USEREVENT + 2: # triggers when timer in Coin(move) reaches 0.5 seconds
            x=random.randint(1,4) #75% chance of small coin appearing and 25% chance of big coin appearing
            if x==1:
                new_coin = Bigcoin() # create a new Bigcoin instance
                monety.add(new_coin) # add new big coin to the coins group
                all_sprites.add(new_coin) # add new big coin to the all_sprites group
            else:
                new_coin=Coin() # create a new Coin instance
                monety.add(new_coin) # add new coin to the coins group
                all_sprites.add(new_coin) # add new coin to the all_sprites group

    display.blit(backround,(0,0)) # draw background to full size of window
    scores=font_small.render(str(score), True, black) # renders a black string of score number
    display.blit(scores,(10,10)) # draws scores in position 10x10
    coinss=font_small.render(str(coins), True, black) # renders a black string of coins number
    display.blit(coinss,(365,10)) # draws coins number in position 365x10

    for entity in all_sprites: #iterate through all game objects (player, enemies, coins)
        display.blit(entity.image,entity.rect) #draw each sprite at its current position
        entity.move()
    
    if pygame.sprite.spritecollideany(P1, enemies): # if player's car hits the enemy car
        pygame.mixer.Sound("crash.wav").play()
        time.sleep(0.5)

        display.fill(red) #fill the window in red color
        display.blit(game_over,(30,250)) #draw the Game Over string on 30x250 position
        pygame.display.update() #update the screen
        for entity in all_sprites:
            entity.kill() #delete every object of the game
        time.sleep(2) #wait for 2 seconds
        pygame.quit() #quitting the game
        sys.exit()
    E1.move() #calls move() function to make enemy car move downward
    monety.update()  # updates all coin objects, checking for collisions with the player and spawning new coins
    clock.tick(60)
    pygame.display.update()