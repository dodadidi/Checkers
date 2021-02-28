import pygame
from .constants import RED,WHITE, YELLOW, SQUARE_SIZE, BLUE, PITCH,GRAY
from checkers.board import Board

class Game:
    def __init__(self,win):
        self._init()
        self.win = win
        self.removed_counter=0    
        self.valid_moves = {}
    def winner(self):
        return self.board.winner()

    def _is_stuck(self,matchWinner):
        return matchWinner

    def update_board(self,row,col):
        self.board.draw1(self.win,row,col)
        self.draw_valid_moves(self.valid_moves)
        pygame.display.update()
    
    def update3(self,row3,col3):
        self.board.draw3(self.win,row3,col3)
        
        self.board.draw_selected(self.win,row3,col3)
        pygame.display.update()
        
    def _init(self):
        self.selected = None
        self.board = Board()
        self.turn = RED
        self.valid_moves = {} #a dictionary of current vallid moves
        
    def reset(self):
        self._init() 

    def select(self,row,col):
        """
        get here when the player press on piece
        if selected is vallid move piece if not (=not result) try again
        """
        if self.selected:
            rectOne = (100,100,100,100)
            pygame.draw.circle(self.win, BLUE, (col * SQUARE_SIZE + SQUARE_SIZE//2, row * SQUARE_SIZE + SQUARE_SIZE//2), 8)
            pygame.draw.circle(self.win, GRAY, (col * SQUARE_SIZE , row * SQUARE_SIZE ), 14)
            result = self.move(row,col) #try to move
            if not result:
                self.selected = None #delete invalid selected
                self.select(row,col) #reselect

        piece = self.board.get_piece(row,col)
        
        self.board.draw_selected(self.win,row,col)
        if piece != 0 and piece.color == self.turn:
            self.selected = piece
            self.valid_moves = self.board.get_valid_moves(piece)
            if not self.valid_moves:
                self._is_stuck("WHITE")
            return True

        return False

    def move(self,row,col):
        piece = self.board.get_piece(row,col)

        pygame.draw.circle(self.win, YELLOW, (col * SQUARE_SIZE + SQUARE_SIZE//2, row* SQUARE_SIZE + SQUARE_SIZE//2), 8)
        #if the player selected an empty square and it's valid move
        if self.selected and piece == 0 and (row,col) in self.valid_moves:
            pygame.draw.circle(self.win, BLUE, (col * SQUARE_SIZE + SQUARE_SIZE//2, row * SQUARE_SIZE + SQUARE_SIZE//2), 8)
            self.board.move(self.selected, row,col)
            skipped = self.valid_moves[(row, col)]
            if skipped:
                self.removed_counter=0
                self.board.remove(skipped)
            else:                
                self.removed_counter=self.removed_counter+1
            self.change_turn()
        else: 
            return False
        return True

    def draw_valid_moves(self,moves):
        for move in moves:
            row, col = move
            pygame.draw.circle(self.win, BLUE, (col * SQUARE_SIZE + SQUARE_SIZE//2, row * SQUARE_SIZE + SQUARE_SIZE//2), 8)
    def change_turn(self):
        self.valid_moves = {}
        if self.turn == RED:
            self.turn = WHITE
        else:
            self.turn = RED

    def get_board(self):
        return self.board

    def ai_move(self, board): #Since Game is a Controller class, it connects between the Board class (The View)
        # and  the Model- the Minimax Algorithm Class.
        self.board = board
        self.change_turn()