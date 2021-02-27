########### file of all the constats values ########### 
import pygame

WIDTH, HEIGHT = 700,700 #pixels 
ROWS, COLS = 8,8 #number of rows and cols of board
SQUARE_SIZE = WIDTH//COLS #size of each square in board

#rgb
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GRAY = (128,128,128,128)
YELLOW = (255, 204, 0)

LIGHT_BLUE = (51, 153, 255)
DARK_BLUE = (0, 38, 77)
PINK = (204, 0, 153)
DARK_PINK = (128, 0, 94)
LIGHT_PINK = (255, 179, 235)
ORANGE = (255, 140, 26)
PITCH = (255, 153, 153)


#bring and resize crown image
CROWN = pygame.transform.scale(pygame.image.load('images/crown.png'),(40,21))