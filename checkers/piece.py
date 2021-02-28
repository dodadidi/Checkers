from .constants import RED, WHITE, SQUARE_SIZE, GRAY, CROWN, GRAY
import pygame

class Piece:
    PADDING = 15
    OUTLINE = 2

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.king = False
        self.x = 0
        self.y = 0
        self.calculate_curr_pos()
    
    def calculate_curr_pos(self):
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

    def change_to_king(self):
        self.king = True
    
	#the following draws a piece on the board.
    def draw(self, win,selected):
        """ 
        draw piece as a circle with the right color and gray border at the middle of square
        """
        radius = SQUARE_SIZE // 2 - self.PADDING
        pygame.draw.circle(win, self.color, (self.x, self.y), radius)
        if self.king:
            win.blit(CROWN, (self.x - CROWN.get_width()//2, self.y - CROWN.get_height()//2))

    def move(self, row, col):
        """
        update piece curr_pos and call to calculate_curr_pos()
        """
        self.row = row
        self.col = col
        self.calculate_curr_pos()
        
    #def get_piece_color(self,row,col):
     #   return self.color
   
#for debugging
    def __repr__(self):
        return str(self.color)