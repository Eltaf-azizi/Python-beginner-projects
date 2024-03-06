import pygame
import sys


pygame.init()


SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tower Defense")


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


TILE_SIZE = 50
GRID_WIDTH = SCREEN_WIDTH // TILE_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // TILE_SIZE
BASE_X = GRID_WIDTH - 1
BASE_Y = GRID_HEIGHT // 2


TOWER_COST = 50
TOWER_UPGRADE_COST = 50
TOWER_RANGE = 100
TOWER_DAMAGE = 10


ENEMY_SIZE = 20
ENEMY_SPEED = 1
ENEMY_HEALTH = 100


paths = [[(0, GRID_HEIGHT // 2), (GRID_WIDTH // 2, GRID_HEIGHT // 2)],
         [(0, GRID_HEIGHT // 4), (GRID_WIDTH // 2, GRID_HEIGHT // 4),
          (GRID_WIDTH // 2, GRID_HEIGHT // 2)],
         [(0, 3 * GRID_HEIGHT // 4), (GRID_WIDTH // 2, 3 * GRID_HEIGHT // 4),
          (GRID_WIDTH // 2, GRID_HEIGHT // 2)]]


class Tower:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.level = 1

    def draw(self):
        pygame.draw.rect(screen, BLUE, (self.x * TILE_SIZE, self.y * TILE_SIZE, TILE_SIZE, TILE_SIZE))


class Enemy:
    def __init__(self, path_index):
        self.path_index = path_index
        self.path = paths[path_index]
        self.current_point = 0
        self.x, self.y = self.path[self.current_point]
        self.health = ENEMY_HEALTH

    def move(self):
        if self.current_point < len(self.path) - 1:
            target_x, target_y = self.path[self.current_point + 1]
            if self.x < target_x:
                self.x += ENEMY_SPEED
            elif self.x > target_x:
                self.x -= ENEMY_SPEED
            if self.y < target_y:
                self.y += ENEMY_SPEED
            elif self.y > target_y:
                self.y -= ENEMY_SPEED
            if (self.x, self.y) == (target_x, target_y):
                self.current_point += 1

    def draw(self):
        pygame.draw.circle(screen, RED, (int(self.x * TILE_SIZE + TILE_SIZE / 2),
                                          int(self.y * TILE_SIZE + TILE_SIZE / 2)), ENEMY_SIZE)


class Base:
    def __init__(self):
        self.health = 100

    def draw(self):
        pygame.draw.rect(screen, GREEN, (BASE_X * TILE_SIZE, BASE_Y * TILE_SIZE, TILE_SIZE, TILE_SIZE))


towers = []
enemies = []
base = Base()
money = 100


clock = pygame.time.Clock()
running = True

while running:
    screen.fill(BLACK)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            grid_x = x // TILE_SIZE
            grid_y = y // TILE_SIZE
            if grid_x < GRID_WIDTH - 1 and (grid_x, grid_y) not in [(BASE_X, BASE_Y)]:
                if (grid_x, grid_y) not in [(tower.x, tower.y) for tower in towers] and money >= TOWER_COST:
                    towers.append(Tower(grid_x, grid_y))
                    money -= TOWER_COST


    if len(enemies) == 0:
        for i in range(3):
            enemies.append(Enemy(i))


    for tower in towers:
        tower.draw()


    for enemy in enemies:
        enemy.move()
        enemy.draw()
        if (enemy.x, enemy.y) == (BASE_X, BASE_Y):
            base.health -= 10
            enemies.remove(enemy)
        elif enemy.current_point == len(enemy.path) - 1:
            enemies.remove(enemy)


    base.draw()


    font = pygame.font.SysFont(None, 24)
    text = font.render(f"Money: {money}", True, WHITE)
    screen.blit(text, (10, 10))
    text = font.render(f"Base Health: {base.health}", True, WHITE)
    screen.blit(text, (10, 30))


    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()
