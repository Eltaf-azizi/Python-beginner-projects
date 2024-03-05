import pygame
import random


pygame.init()


SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Match-3 Game")


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)


TILE_SIZE = 50
GRID_WIDTH = SCREEN_WIDTH // TILE_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // TILE_SIZE
NUM_COLORS = 4
MATCH_THRESHOLD = 3


GEM_COLORS = [RED, GREEN, BLUE, YELLOW]


grid = [[random.randint(0, NUM_COLORS - 1) for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]


clock = pygame.time.Clock()
running = True

while running:
    screen.fill(BLACK)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            color = GEM_COLORS[grid[y][x]]
            pygame.draw.rect(screen, color, (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))


    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            color = grid[y][x]
            if color == -1:
                continue


            if x < GRID_WIDTH - 2 and grid[y][x + 1] == color and grid[y][x + 2] == color:
                grid[y][x] = grid[y][x + 1] = grid[y][x + 2] = -1


            if y < GRID_HEIGHT - 2 and grid[y + 1][x] == color and grid[y + 2][x] == color:
                grid[y][x] = grid[y + 1][x] = grid[y + 2][x] = -1


    for x in range(GRID_WIDTH):
        for y in range(GRID_HEIGHT - 1, -1, -1):
            if grid[y][x] == -1:
                for y_above in range(y, 0, -1):
                    grid[y_above][x] = grid[y_above - 1][x]
                grid[0][x] = random.randint(0, NUM_COLORS - 1)

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
