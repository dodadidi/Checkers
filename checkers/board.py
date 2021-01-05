import pygame
from .piece import Piece
from .constants import BLACK, ROWS, RED, SQUARE_SIZE, COLS, WHITE

class Board:
    def __init__(self):
        # self.board = [[WHITE, 0 WHITE , 0 WHITE],[RED, 0 RED, 0, WHITE]]
        self.board = []
        # self.selected_piece = None 
        self.red_left = self.white_left = 12
        self.red_kings = self.white_kings = 0
        self.create_board()
    
    def draw_squares(self,win):
        win.fill(BLACK)
        for row in range(ROWS):
            for col in range(row % 2,COLS,2):
                pygame.draw.rect(win, RED, (row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def move(self, piece, row, col):
        #swap the value of 2 squares
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        piece.move(row,col)
        #check if piece become to king
        if row==ROWS or row == 0:
            piece.make_king()
            if piece.color == WHITE:
                self.white_kings +=1
            else:
                self.red_kings +=1

    def get_piece(self, row, col):
        return self.board[row][col]


    def create_board(self):
        for row in range(ROWS):
            self.board.append([]) #append empty list that represents what each row has
            for col in range(COLS):
                if col % 2 == ((row +  1) % 2):
                    if row < 3:
                        self.board[row].append(Piece(row, col, WHITE))
                    elif row > 4: 
                        self.board[row].append(Piece(row, col, RED))    
                    else:
                        self.board[row].append(0)
                else:
                    self.board[row].append(0)

    def draw(self, win):
        self.draw_squares(win)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(win)                        

