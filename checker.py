import pygame
import sys
import random

# Constants
WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH // COLS
RADIUS = SQUARE_SIZE // 2 - 5

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Initialize Pygame
pygame.init()
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Checkers")

# Function to draw the board
def draw_board():
    for row in range(ROWS):
        for col in range(row % 2, COLS, 2):
            pygame.draw.rect(WINDOW, GRAY, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

# Class for Checkers Piece
class Piece:
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.king = False
        if self.color == RED:
            self.direction = 1
        else:
            self.direction = -1

    def make_king(self):
        self.king = True

    def draw(self):
        pygame.draw.circle(WINDOW, self.color, (self.col * SQUARE_SIZE + SQUARE_SIZE // 2, self.row * SQUARE_SIZE + SQUARE_SIZE // 2), RADIUS)
        if self.king:
            pygame.draw.circle(WINDOW, WHITE, (self.col * SQUARE_SIZE + SQUARE_SIZE // 2, self.row * SQUARE_SIZE + SQUARE_SIZE // 2), RADIUS // 2)

# Function to initialize pieces
def initialize_pieces():
    pieces = []
    for row in range(3):
        for col in range(COLS):
            if (row + col) % 2 == 0:
                pieces.append(Piece(row, col, WHITE))
    for row in range(5, ROWS):
        for col in range(COLS):
            if (row + col) % 2 == 0:
                pieces.append(Piece(row, col, RED))
    return pieces

# Function to get valid moves for a piece
def get_valid_moves(piece, pieces):
    moves = []
    directions = [-1, 1] if piece.king else [piece.direction]
    for direction in directions:
        for step in [-1, 1]:
            new_row = piece.row + direction
            new_col = piece.col + step
            if 0 <= new_row < ROWS and 0 <= new_col < COLS:
                if not any(piece.row == new_row and piece.col == new_col for piece in pieces):
                    moves.append((new_row, new_col))
    return moves

# Main game loop
def main():
    pieces = initialize_pieces()
    selected_piece = None
    turn = RED # Red goes first
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row = pos[1] // SQUARE_SIZE
                col = pos[0] // SQUARE_SIZE
                if selected_piece:
                    selected_piece.row = row
                    selected_piece.col = col
                    selected_piece = None
                else:
                    for piece in pieces:
                        if piece.row == row and piece.col == col and piece.color == turn:
                            selected_piece = piece
        
        if turn == BLUE:
            # Computer player's turn
            piece = random.choice([piece for piece in pieces if piece.color == turn])
            moves = get_valid_moves(piece, pieces)
            if moves:
                move = random.choice(moves)
                piece.row, piece.col = move
            turn = RED
        else:
            turn = BLUE

        # Draw the board and pieces
        WINDOW.fill(WHITE)
        draw_board()
        for piece in pieces:
            piece.draw()
        
        pygame.display.update()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
