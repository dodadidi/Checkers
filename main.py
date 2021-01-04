import pygame
from checkers.constants import WIDTH, HEIGHT #can do it due to __init__.py
from checkers.board import Board


FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checkers')


def main():
    run = True 
    clock = pygame.time.Clock()
    
    while run:
        clock.tick(FPS)
        board = Board()

        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pass
        
        # board.draw_squares(WIN)
        board.draw(WIN)
        pygame.display.update()

    pygame.quit()
    
if __name__ == '__main__':
    main()