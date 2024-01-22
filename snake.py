import random
import pygame


# Initialize pygame
pygame.init()

# Set up the game window
window_width = 640
window_height = 480
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Snake Game")

# Define colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# Define the snake
snake_size = 20
snake_speed = 15
snake_x = window_width // 2
snake_y = window_height // 2
snake_x_change = 0
snake_y_change = 0
snake_list = []
snake_length = 1

# Define the food
food_size = 20
food_x = round(random.randrange(0, window_width - food_size) / 20) * 20
food_y = round(random.randrange(0, window_height - food_size) / 20) * 20

clock = pygame.time.Clock()

# Function to display the snake
def draw_snake(snake_list):
    for x, y in snake_list:
        pygame.draw.rect(window, black, [x, y, snake_size, snake_size])

# Main game loop
game_over = False
while not game_over:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake_x_change = -snake_size
                snake_y_change = 0
            elif event.key == pygame.K_RIGHT:
                snake_x_change = snake_size
                snake_y_change = 0
            elif event.key == pygame.K_UP:
                snake_y_change = -snake_size
                snake_x_change = 0
            elif event.key == pygame.K_DOWN:
                snake_y_change = snake_size
                snake_x_change = 0
    
    # Update snake position
    snake_x += snake_x_change
    snake_y += snake_y_change

    # Check for collision with the boundaries
    if snake_x >= window_width or snake_x < 0 or snake_y >= window_height or snake_y < 0:
        game_over = True

    window.fill(white)

    # Draw the food
    pygame.draw.rect(window, red, [food_x, food_y, food_size, food_size])

    # Update snake length and add new segments
    snake_head = []
    snake_head.append(snake_x)
    snake_head.append(snake_y)
    snake_list.append(snake_head)
    if len(snake_list) > snake_length:
        del snake_list[0]

    # Check for snake collision with itself
    for segment in snake_list[:-1]:
        if segment == snake_head:
            game_over = True

    # Draw the snake
    draw_snake(snake_list)

    # Check for collision with food
    if snake_x == food_x and snake_y == food_y:
        food_x = round(random.randrange(0, window_width - food_size) / 20) * 20
        food_y = round(random.randrange(0, window_height - food_size) / 20) * 20
        snake_length += 1

    pygame.display.update()

    # Set the frame rate
    clock.tick(snake_speed)

# Quit the game
pygame.quit()
