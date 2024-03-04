import pygame
import random

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space Invaders")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

player_width = 50
player_height = 50
player_x = SCREEN_WIDTH // 2 - player_width // 2
player_y = SCREEN_HEIGHT - 100
player_speed = 5

enemy_width = 50
enemy_height = 50
enemy_speed = 2
enemy_spawn_delay = 60
enemies = []

bullet_width = 5
bullet_height = 15
bullet_speed = 7
bullets = []

clock = pygame.time.Clock()
running = True

while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < SCREEN_WIDTH - player_width:
        player_x += player_speed

    if random.randint(0, enemy_spawn_delay) == 0:
        enemy_x = random.randint(0, SCREEN_WIDTH - enemy_width)
        enemy_y = -enemy_height
        enemies.append([enemy_x, enemy_y])

    for enemy in enemies:
        enemy[1] += enemy_speed
        pygame.draw.rect(screen, WHITE, (enemy[0], enemy[1], enemy_width, enemy_height))

    pygame.draw.rect(screen, WHITE, (player_x, player_y, player_width, player_height))

    for bullet in bullets:
        bullet[1] -= bullet_speed
        pygame.draw.rect(screen, WHITE, (bullet[0], bullet[1], bullet_width, bullet_height))

    for enemy in enemies[:]:
        for bullet in bullets[:]:
            if (bullet[0] > enemy[0] and bullet[0] < enemy[0] + enemy_width and
                bullet[1] > enemy[1] and bullet[1] < enemy[1] + enemy_height):
                enemies.remove(enemy)
                bullets.remove(bullet)

    for bullet in bullets[:]:
        if bullet[1] < 0:
            bullets.remove(bullet)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
