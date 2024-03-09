import pygame
import random
import sys


pygame.init()


WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Endless Runner")


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


player_width = 50
player_height = 50
player_color = (0, 128, 0)
player_speed = 5 


obstacle_width = 50
obstacle_height = 50
obstacle_color = (255, 0, 0)
obstacle_speed = 5


coin_width = 30
coin_height = 30
coin_color = (255, 255, 0)


player_x = WIDTH // 2
player_y = HEIGHT - 100


obstacles = []
coins = []


clock = pygame.time.Clock()


def generate_obstacle():
    x = random.randint(0, WIDTH - obstacle_width)
    y = random.randint(-HEIGHT, 0)
    obstacles.append(pygame.Rect(x, y, obstacle_width, obstacle_height))


def generate_coin():
    x = random.randint(0, WIDTH - coin_width)
    y = random.randint(-HEIGHT, 0)
    coins.append(pygame.Rect(x, y, coin_width, coin_height))


def main():
    global player_x, player_y
    score = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            player_y -= player_speed
        if keys[pygame.K_DOWN]:
            player_y += player_speed
        if keys[pygame.K_LEFT]:
            player_x -= player_speed
        if keys[pygame.K_RIGHT]:
            player_x += player_speed


        for obstacle in obstacles:
            obstacle.y += obstacle_speed
            if obstacle.y > HEIGHT:
                obstacles.remove(obstacle)
                score += 1

        for coin in coins:
            coin.y += obstacle_speed
            if coin.y > HEIGHT:
                coins.remove(coin)


        if len(obstacles) < 5:
            generate_obstacle()

        if len(coins) < 3:
            generate_coin()


        player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
        for obstacle in obstacles:
            if player_rect.colliderect(obstacle):
                print("Game Over! Score:", score)
                pygame.quit()
                sys.exit()


        for coin in coins:
            if player_rect.colliderect(coin):
                coins.remove(coin)
                score += 10


        screen.fill(WHITE)
        pygame.draw.rect(screen, player_color, (player_x, player_y, player_width, player_height))

        for obstacle in obstacles:
            pygame.draw.rect(screen, obstacle_color, obstacle)

        for coin in coins:
            pygame.draw.rect(screen, coin_color, coin)

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
