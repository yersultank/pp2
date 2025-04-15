import pygame
import random
import sys
import psycopg2
from config import load_config
pygame.init()

def create_user_table():
    conn=psycopg2.connect(host="localhost", database="suppliers", user="postgres", password="ersultan7")
    cur=conn.cursor()
    cur.execute("""
                CREATE TABLE IF NOT EXISTS users  (
                id SERIAL PRIMARY KEY,
                user_name VARCHAR(20)
                );
                """)
    conn.commit()
    cur.close()
    

def create_score_table():
    conn=psycopg2.connect(host="localhost", database="suppliers", user="postgres", password="ersultan7")
    cur=conn.cursor()
    cur.execute("""
                CREATE TABLE IF NOT EXISTS user_score  (
                id SERIAL PRIMARY KEY,
                user_id INTEGER,
                score VARCHAR(20),
                level VARCHAR(10),
                snake_length INTEGER,
                FOREIGN KEY(user_id) REFERENCES users(id)
                );
                """)
    conn.commit()
    cur.close()

def add_user_name(name):
    config=load_config()
    conn=psycopg2.connect(**config)
    cur=conn.cursor()
    cur.execute("SELECT id FROM users WHERE user_name=%s",(name,))
    user=cur.fetchone()
    if user:
        user_id=user[0]
        print("user already exists with id:", user_id)
        cur.execute("SELECT score,level,snake_length FROM user_score WHERE id=%s ORDER BY id DESC LIMIT 1", (user_id,))
        last_result=cur.fetchone()
        if last_result:
            score=int(last_result[0])
            level=int(last_result[1])
            snake_length=int(last_result[2])
        else:
            score=0
            level=1
            snake_length=2
    else:
        cur.execute("INSERT INTO users (user_name) VALUES (%s) RETURNING id", (name,))
        user_id=cur.fetchone()[0]
        conn.commit()
        print("user has been added, his id:", user_id)
        score=0
        level=1
        snake_length=2
    cur.close()
    conn.close()
    return user_id,score,level,snake_length

def add_score(score,level,snake_length,user_id):
    config=load_config()
    conn=psycopg2.connect(**config)
    cur=conn.cursor()
    cur.execute("INSERT INTO user_score (score, level, snake_length, user_id) VALUES (%s, %s,%s,%s)", (score,level,snake_length,user_id))
    conn.commit()
    cur.close()
    conn.close()
    print("score saved")

create_user_table()
create_score_table()
name=input("write your name:")
user_id,score,level,snake_length=add_user_name(name)
if name:
    game_over=False
    game_started=False
    paused=True
    killer_visible=False
    killer_timer=0
    killer_interval=10000
# Define colors
blue = (0, 0, 255)
black = (0, 0, 0)
white = (255, 255, 255)

# Screen dimensions
dis_width = 600
dis_height = 400

# Size of each snake segment
snake_block = 20

# Timer for apple repositioning
timer = pygame.USEREVENT + 1
pygame.time.set_timer(timer, 6000)

# Frames per second
fps = 10

display = pygame.display.set_mode((dis_width, dis_height))
clock = pygame.time.Clock()


# Initial position of the snake head
x1 = dis_width / 2
y1 = dis_height / 2

# Initial movement direction
x1_change = snake_block  # Moving right at the start
y1_change = 0

current_apple_type = "normal"

# Snake body list and length
snake_list = [[x1, y1 - 10], [x1, y1]]  # Initial snake position

def print_snake(snake_block, snake_list):
    """Draws the snake on the screen"""
    for x in snake_list:
        pygame.draw.rect(display, black, [x[0], x[1], snake_block, snake_block])

class Killer(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("killer.png")
        self.image=pygame.transform.scale(self.image,(20,20))
        self.reposition(snake_list)
        
    def draw(self):
        display.blit(self.image,(self.x,self.y))

    def reposition(self,snake_list):
        pygame.time.set_timer(timer, 0)  # Reset timer
        while True:
            self.x=random.randint(0,(dis_width//20)-1)*20
            self.y=random.randint(0,(dis_height//20)-1)*20
            if [self.x,self.y] not in snake_list:
                break
        pygame.time.set_timer(timer, 10000) 

class GoldApple(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("golden apple.jpeg")  # Load golden apple image
        self.image = pygame.transform.scale(self.image, (20, 20))  # Resize the image
        self.reposition(snake_list)
    
    def draw(self):
        display.blit(self.image, (self.x, self.y))  # Draw the apple on the screen
    
    def reposition(self, snake_list):
        """Randomly positions the apple, avoiding collision with the snake"""
        pygame.time.set_timer(timer, 0)  # Reset timer
        while True:
            self.x = random.randint(0, (dis_width // 20) - 1) * 20
            self.y = random.randint(0, (dis_height // 20) - 1) * 20
            if [self.x, self.y] not in snake_list:
                break  # Ensure apple does not spawn on the snake
        pygame.time.set_timer(timer, 10000)  # Restart timer

class Apple(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("apple2.png")  # Load normal apple image
        self.image = pygame.transform.scale(self.image, (20, 20))  # Resize the image
        self.reposition(snake_list)
    
    def draw(self):
        display.blit(self.image, (self.x, self.y))  # Draw the apple on the screen
    
    def reposition(self, snake_list):
        """Randomly positions the apple, avoiding collision with the snake"""
        pygame.time.set_timer(timer, 0)  # Reset timer
        while True:
            self.x = random.randint(0, (dis_width // 20) - 1) * 20
            self.y = random.randint(0, (dis_height // 20) - 1) * 20
            if [self.x, self.y] not in snake_list:
                break  # Ensure apple does not spawn on the snake
        pygame.time.set_timer(timer, 6000)  # Restart timer

# Create apple instances
apple = Apple()
gold_apple = GoldApple()
killer=Killer()
# Randomly select initial apple type
x = random.randint(1, 4)
if x == 1:
    current_apple = gold_apple
    current_apple_type = "gold"
else:
    current_apple = apple
    current_apple_type = "normal"

def pause():
    paused=True
    while paused:
            display.fill(blue)
            font = pygame.font.SysFont("Verdana", 60)
            game_interface_text = font.render("Start? Press Z", True, black)
            display.blit(game_interface_text, (100, 150))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()  # Exit game loop
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_z:
                        paused=False
while not game_over:
    if not game_started:
            display.fill(blue)
            font = pygame.font.SysFont("Verdana", 60)
            font_small = pygame.font.SysFont("Verdana", 20)
            game_interface_text = font.render("Start? Press Z", True, black)
            display.blit(game_interface_text, (100, 150))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True  # Exit game loop
                    break
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_z:
                        game_started=True
            continue
    for event in pygame.event.get():
        if event.type == pygame.USEREVENT + 1:
            current_apple.reposition(snake_list)  # Move apple after timer expires
        
        if event.type == pygame.KEYDOWN:
            # Change direction, but prevent reversing direction
            if event.key==pygame.K_p:
                pause()
            if event.key==pygame.K_s:
                add_score(score, level,snake_length, user_id)
                game_over=True
            if event.key == pygame.K_LEFT and x1_change == 0:
                x1_change = -snake_block
                y1_change = 0
            elif event.key == pygame.K_RIGHT and x1_change == 0:
                x1_change = snake_block
                y1_change = 0
            elif event.key == pygame.K_UP and y1_change == 0:
                y1_change = -snake_block
                x1_change = 0
            elif event.key == pygame.K_DOWN and y1_change == 0:
                y1_change = snake_block
                x1_change = 0
    
    # Update snake head position
    x1 += x1_change
    y1 += y1_change

    # Check for collision with walls
    if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
        game_over = True
        break
    
    display.fill(white)  # Clear screen
    current_apple.draw()  # Draw apple
    
    # Check for collision with apple
    if x1 == current_apple.x and y1 == current_apple.y:
        if current_apple_type == "normal":
            snake_length += 1  # Normal apple increases length by 1
            score+=1
        else:
            snake_length += 2  # Golden apple increases length by 2
            score+=2
        # Increase game speed
        pygame.time.set_timer(timer, 0)  # Reset timer

        # Randomly select new apple type
        if random.randint(1, 4) == 1:
            current_apple = gold_apple
            current_apple_type = "gold"
        else:
            current_apple = apple
            current_apple_type = "normal"
        current_apple.reposition(snake_list)
    if score<5:
        fps=10
        level=1
    elif score>=5 and score<10:
        fps=15
        level=2
    elif score>=10 and score<30:
        fps=20
        level=3
        if not killer_visible:
            killer.reposition(snake_list)
            killer_visible=True
            killer_timer=pygame.time.get_ticks()
        if killer_visible:
            killer.draw()
            if x1==killer.x and y1==killer.y:
                game_over=True
                break
            if pygame.time.get_ticks()-killer_timer>killer_interval:
                killer.reposition(snake_list)
                killer_timer=pygame.time.get_ticks()

    # Update snake list
    snake_head = [x1, y1]
    snake_list.append(snake_head)
    
    # Remove extra segments to maintain correct length
    if len(snake_list) > snake_length:
        del snake_list[0]
    
    # Check for collision with itself
    for segment in snake_list[:-1]:
        if segment == snake_head:
            game_over = True
            break
    print_snake(snake_block, snake_list)  # Draw the snake
    pygame.display.update()  # Refresh screen
    clock.tick(fps)  # Control speed

# Display game over screen
display.fill((255, 0, 0))
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over_text = font.render("Game Over", True, black)
display.blit(game_over_text, (dis_width / 4, dis_height / 2))
pygame.display.update()
pygame.time.delay(2000)  # Show the screen for 2 seconds before closing
add_score(score, level,snake_length, user_id)
pygame.quit()
sys.exit()