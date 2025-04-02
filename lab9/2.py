import pygame
import random
import sys
pygame.init()

# Define colors
blue = (50, 153, 213)
black = (0, 0, 0)
white = (255, 255, 255)

# Screen dimensions
dis_width = 600
dis_height = 400

# Size of each snake segment
snake_block = 10

# Timer for apple repositioning
timer = pygame.USEREVENT + 1
pygame.time.set_timer(timer, 6000)

# Frames per second
fps = 10

display = pygame.display.set_mode((dis_width, dis_height))
clock = pygame.time.Clock()

game_over = False

# Initial position of the snake head
x1 = dis_width / 2
y1 = dis_height / 2

# Initial movement direction
x1_change = snake_block  # Moving right at the start
y1_change = 0

current_apple_type = "normal"

# Snake body list and length
snake_list = [[x1, y1 - 10], [x1, y1]]  # Initial snake position
snake_length = 2

def print_snake(snake_block, snake_list):
    """Draws the snake on the screen"""
    for x in snake_list:
        pygame.draw.rect(display, black, [x[0], x[1], snake_block, snake_block])

class GoldApple(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("golden apple.jpeg")  # Load golden apple image
        self.image = pygame.transform.scale(self.image, (10, 10))  # Resize the image
        self.reposition(snake_list)
    
    def draw(self):
        display.blit(self.image, (self.x, self.y))  # Draw the apple on the screen
    
    def reposition(self, snake_list):
        """Randomly positions the apple, avoiding collision with the snake"""
        pygame.time.set_timer(timer, 0)  # Reset timer
        while True:
            self.x = random.randint(0, (dis_width // 10) - 1) * 10
            self.y = random.randint(0, (dis_height // 10) - 1) * 10
            if [self.x, self.y] not in snake_list:
                break  # Ensure apple does not spawn on the snake
        pygame.time.set_timer(timer, 10000)  # Restart timer

class Apple(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("apple2.png")  # Load normal apple image
        self.image = pygame.transform.scale(self.image, (10, 10))  # Resize the image
        self.reposition(snake_list)
    
    def draw(self):
        display.blit(self.image, (self.x, self.y))  # Draw the apple on the screen
    
    def reposition(self, snake_list):
        """Randomly positions the apple, avoiding collision with the snake"""
        pygame.time.set_timer(timer, 0)  # Reset timer
        while True:
            self.x = random.randint(0, (dis_width // 10) - 1) * 10
            self.y = random.randint(0, (dis_height // 10) - 1) * 10
            if [self.x, self.y] not in snake_list:
                break  # Ensure apple does not spawn on the snake
        pygame.time.set_timer(timer, 6000)  # Restart timer

# Create apple instances
apple = Apple()
gold_apple = GoldApple()

# Randomly select initial apple type
x = random.randint(1, 4)
if x == 1:
    current_apple = gold_apple
    current_apple_type = "gold"
else:
    current_apple = apple
    current_apple_type = "normal"

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True  # Exit game loop
        
        if event.type == pygame.USEREVENT + 1:
            current_apple.reposition(snake_list)  # Move apple after timer expires
        
        if event.type == pygame.KEYDOWN:
            # Change direction, but prevent reversing direction
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
        else:
            snake_length += 2  # Golden apple increases length by 2
        fps += 3  # Increase game speed
        pygame.time.set_timer(timer, 0)  # Reset timer

        # Randomly select new apple type
        if random.randint(1, 4) == 1:
            current_apple = gold_apple
            current_apple_type = "gold"
        else:
            current_apple = apple
            current_apple_type = "normal"
        current_apple.reposition(snake_list)
    
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
pygame.quit()
sys.exit()