#all the constats values will be here
import pygame
WIDTH, HEIGHT = 700,700 #8 hundreds pixels 
ROWS, COLS = 8,8
SQUARE_SIZE = WIDTH//COLS

#rgb
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GRAY = (128,128,128,128)

#bring and resize crown image
CROWN = pygame.transform.scale(pygame.image.load('assets/crown.png'),(40,21))