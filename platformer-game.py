import pygame
import random


pygame.init()


SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Platformer Game")


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)


player_width = 50
player_height = 50
player_x = 50
player_y = SCREEN_HEIGHT - player_height - 50
player_speed = 5
player_jump_power = 10
player_gravity = 0.5
player_jump = False
player_jump_count = 10


platform_width = 100
platform_height = 20
platforms = [[200, SCREEN_HEIGHT - 200, platform_width, platform_height],
             [400, SCREEN_HEIGHT - 300, platform_width, platform_height],
             [600, SCREEN_HEIGHT - 400, platform_width, platform_height]]


coin_radius = 15
coins = [[random.randint(50, SCREEN_WIDTH - 50), random.randint(50, SCREEN_HEIGHT - 200), coin_radius] for _ in range(10)]


power_up_radius = 15
power_ups = []


enemy_width = 50
enemy_height = 50
enemy_x = 700
enemy_y = SCREEN_HEIGHT - enemy_height - 50
enemy_speed = 3


clock = pygame.time.Clock()
running = True

while running:
    screen.fill(BLACK)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not player_jump:
                player_jump = True


    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < SCREEN_WIDTH - player_width:
        player_x += player_speed


    if player_jump:
        if player_jump_count >= -10:
            neg = 1
            if player_jump_count < 0:
                neg = -1
            player_y -= (player_jump_count ** 2) * 0.5 * neg
            player_jump_count -= 1
        else:
            player_jump = False
            player_jump_count = 10


    if player_y < SCREEN_HEIGHT - player_height:
        player_y += player_gravity


    for platform in platforms:
        pygame.draw.rect(screen, WHITE, platform)


    for coin in coins:
        pygame.draw.circle(screen, YELLOW, (coin[0], coin[1]), coin[2])


    for power_up in power_ups:
        pygame.draw.circle(screen, BLUE, (power_up[0], power_up[1]), power_up_radius)


    pygame.draw.rect(screen, RED, (enemy_x, enemy_y, enemy_width, enemy_height))


    for platform in platforms:
        if (player_y + player_height >= platform[1] and player_y + player_height <= platform[1] + platform_height
                and player_x + player_width >= platform[0] and player_x <= platform[0] + platform[2]):
            player_jump = False
            player_jump_count = 10
            player_y = platform[1] - player_height


    for coin in coins[:]:
        if (player_x + player_width >= coin[0] - coin_radius and player_x <= coin[0] + coin_radius
                and player_y + player_height >= coin[1] - coin_radius and player_y <= coin[1] + coin_radius):
            coins.remove(coin)


    for power_up in power_ups[:]:
        if (player_x + player_width >= power_up[0] - power_up_radius and player_x <= power_up[0] + power_up_radius
                and player_y + player_height >= power_up[1] - power_up_radius and player_y <= power_up[1] + power_up_radius):
            power_ups.remove(power_up)


    if (player_x + player_width >= enemy_x and player_x <= enemy_x + enemy_width
            and player_y + player_height >= enemy_y):
        running = False


    pygame.draw.rect(screen, WHITE, (player_x, player_y, player_width, player_height))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
