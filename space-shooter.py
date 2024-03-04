import pygame
import random

# Initialize pygame
pygame.init()

# Set up the screen
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space Shooter")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Player settings
player_width = 50
player_height = 50
player_x = SCREEN_WIDTH // 2 - player_width // 2
player_y = SCREEN_HEIGHT - player_height - 50
player_speed = 5
player_bullet_speed = 10
player_health = 100

# Bullet settings
bullet_width = 5
bullet_height = 15
bullets = []

# Enemy settings
enemy_width = 50
enemy_height = 50
enemy_speed = 3
enemies = []

# Boss settings
boss_width = 200
boss_height = 200
boss_x = SCREEN_WIDTH // 2 - boss_width // 2
boss_y = -boss_height
boss_health = 200
boss_speed = 2
boss_active = False

# Game loop
clock = pygame.time.Clock()
running = True

while running:
    screen.fill(BLACK)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullets.append([player_x + player_width // 2 - bullet_width // 2, player_y])

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < SCREEN_WIDTH - player_width:
        player_x += player_speed
    if keys[pygame.K_UP] and player_y > 0:
        player_y -= player_speed
    if keys[pygame.K_DOWN] and player_y < SCREEN_HEIGHT - player_height:
        player_y += player_speed

    # Draw player
    pygame.draw.rect(screen, WHITE, (player_x, player_y, player_width, player_height))

    # Draw bullets
    for bullet in bullets:
        bullet[1] -= player_bullet_speed
        pygame.draw.rect(screen, YELLOW, (bullet[0], bullet[1], bullet_width, bullet_height))

    # Draw enemies
    for enemy in enemies:
        enemy[1] += enemy_speed
        pygame.draw.rect(screen, RED, (enemy[0], enemy[1], enemy_width, enemy_height))

    # Spawn enemies randomly
    if random.randint(0, 100) < 3:
        enemy_x = random.randint(0, SCREEN_WIDTH - enemy_width)
        enemy_y = -enemy_height
        enemies.append([enemy_x, enemy_y])

    # Collision detection for bullets and enemies
    for bullet in bullets[:]:
        for enemy in enemies[:]:
            if (bullet[0] > enemy[0] and bullet[0] < enemy[0] + enemy_width and
                bullet[1] > enemy[1] and bullet[1] < enemy[1] + enemy_height):
                bullets.remove(bullet)
                enemies.remove(enemy)

    # Spawn boss
    if len(enemies) > 10 and not boss_active:
        boss_active = True
        boss_y = -boss_height

    # Draw boss
    if boss_active:
        boss_y += boss_speed
        pygame.draw.rect(screen, BLUE, (boss_x, boss_y, boss_width, boss_height))

    # Collision detection for player and boss
    if (player_x + player_width > boss_x and player_x < boss_x + boss_width
            and player_y + player_height > boss_y and player_y < boss_y + boss_height):
        player_health -= 10

    # Check boss health
    if boss_active and boss_health <= 0:
        boss_active = False

    # Check player health
    if player_health <= 0:
        running = False

    # Update the display
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
