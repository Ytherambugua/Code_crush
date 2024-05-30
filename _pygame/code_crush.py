import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BLOCK_SIZE = 50
GRID_SIZE = 10

# Colors
COLORS = {
    'variable': (255, 0, 0),
    'loop': (0, 255, 0),
    'conditional': (0, 0, 255),
    'function': (255, 255, 0),
    'background': (50, 50, 50)
}

# Define different types of code blocks
CODE_BLOCKS = ['variable', 'loop', 'conditional', 'function']

# Create the game screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Code Crush")

# Create a grid for the game board
def create_board(size):
    return [[random.choice(CODE_BLOCKS) for _ in range(size)] for _ in range(size)]

# Draw the grid
def draw_board(board):
    for row in range(len(board)):
        for col in range(len(board[0])):
            pygame.draw.rect(
                screen,
                COLORS[board[row][col]],
                (col * BLOCK_SIZE, row * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
            )

# Main game loop
def main():
    board = create_board(GRID_SIZE)
    clock = pygame.time.Clock()
    running = True

    while running:
        screen.fill(COLORS['background'])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        draw_board(board)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()

