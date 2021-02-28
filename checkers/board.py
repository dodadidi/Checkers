import pygame
from .piece import Piece
import tkinter
from .constants import BLACK, ROWS, RED, SQUARE_SIZE, COLS, WHITE, YELLOW, PITCH,GRAY
from tkinter.messagebox import showerror

class Board:

    def __init__(self):
        self.board = []
        #we would like to track how many pieces we have. the game start with 12 red, 12 white and 0 kings
        self.red_left = self.white_left = 12 
        self.red_kings = self.white_kings = 0
        self.create_board()
        self.redMoves   = 0
        self.whiteMoves = 0
        self.red_removed_counter=0
        self.white_removed_counter=0
        self.removed_moves_counter=0
    def draw_squares(self,win):
        """
        draw board squares yellow,black alternately
        """
        win.fill(BLACK)
        for row in range(ROWS):
            for col in range(row % 2,COLS,2):
                pygame.draw.rect(win, YELLOW, (row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def draw_selected_square(self,win,row,col):
        """
        draw the square of the selected piece in special color
        """
        pygame.draw.rect(win,GRAY, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def evaluate(self):#this is the evaluation function of the minimax algorithm, it return the score of each possible fisible move
        return self.white_left - self.red_left + (self.white_kings * 0.5 - self.red_kings * 0.5)

    def get_all_pieces(self, color):#this function returns all pieces on board of certain player
        pieces = []
        for row in self.board:
            for piece in row:
                if piece != 0 and piece.color == color:
                    pieces.append(piece)
        return pieces    
    
    def draw_selected(self,win,row,col): #A simple function that draws a yellow circle inside the chosen piece 
        pygame.draw.circle(win, YELLOW, (col-1 * SQUARE_SIZE + SQUARE_SIZE//2, row-1 * SQUARE_SIZE + SQUARE_SIZE//2), 8)

    def move(self, piece, row, col):#this method handles an event of moving a piece, and if a piece becomes a king then it handles this case also.
        """
        update piece curr_pos
        """
        #swap the value of 2 squares
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        piece.move(row,col)
        self.removed_moves_counter+=1
        #check if piece become a king
        if row == ROWS - 1 or row == 0:
            piece.change_to_king()
            if piece.color == WHITE:
                self.white_kings +=1
            else:
                self.red_kings +=1

    def get_piece(self, row, col):#return a "piece" object according to its location on the board.
        return self.board[row][col]

    def create_board(self): #this function creates a  checkers board from zero.
        for row in range(ROWS):
            self.board.append([]) #append empty list that represents what each row has
            for col in range(COLS):
                if col % 2 == ((row +  1) % 2): #put pieces intermittently
                    if row < 3: # rows #3 and #4 are empty in the begining
                        self.board[row].append(Piece(row, col, WHITE))
                    elif row > 4: 
                        self.board[row].append(Piece(row, col, RED))    
                    else:
                        self.board[row].append(0) 
                else:
                    self.board[row].append(0) #append 0(=blank piece) for tracking of the board what row and column each pieces in 

    def draw1(self, win,row1,col1):
        """
        draw current board FOR FIRST TWO LEVELS OF DIFFICULTY
        """
        self.draw_squares(win)
        self.draw_selected_square(win,row1,col1)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0:
                    if row==row1 and col==col1:
                        selected=True
                        if piece.color == RED:
                            piece.draw(win,selected)
                    else:
                        selected=False
                        piece.draw(win,selected)
                    if row==row1 and col==col1:           
                        pygame.draw.circle(win, YELLOW, (col * SQUARE_SIZE + SQUARE_SIZE//2, row * SQUARE_SIZE + SQUARE_SIZE//2), 8)

    def draw3(self, win,row1,col1): #draw current board FOR DIFFICULTY LEVEL NUMBER 3
        self.draw_squares(win)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0:
                    if row==row1 and col==col1:
                        selected=True
                        if piece.color == RED:
                            piece.draw(win,selected)
                    else:
                        selected=False
                        piece.draw(win,selected)
                    if row==row1 and col==col1:
                        pygame.draw.circle(win, YELLOW, (col * SQUARE_SIZE + SQUARE_SIZE//2, row * SQUARE_SIZE + SQUARE_SIZE//2), 8)
        
    def remove(self, pieces): #when piece jump above opponent's piece; remove the opponent's piece and update square and pieces
        for piece in pieces:
            self.board[piece.row][piece.col] = 0
            if piece != 0: 
                if piece.color == RED:
                    self.red_left -= 1
                    self.red_removed_counter+=1
                    self.removed_moves_counter=0
                else:
                    self.white_left -= 1
                    self.white_removed_counter+=1
                    self.removed_moves_counter=0
        
    def winner(self): #if and opponent has no pieces left then he loses the game.
        if self.red_left <= 0:
            return WHITE
        elif self.white_left <= 0:
            return RED
        elif self.removed_moves_counter==30:
            return BLACK
        i=0
        j=0  
        all_white_pieces = []#the location (row and col) of the white pieces on the current board - saved in a list
        all_red_pieces = [] #the location (row and col) of the red pieces on the current board - saved in a list
        all_white_piece = []#the white pieces on the current board saved as objects on this list
        all_red_piece = [] #the white pieces on the current board saved as objects on this list
        for i in range(8):
            for j in range(8):
                curr_piece = self.get_piece(i,j)
                if curr_piece!=0:
                    if curr_piece.color==WHITE:
                        all_white_pieces.append([i,j])
                        all_white_piece.append(curr_piece)
                    elif curr_piece.color==RED:
                        all_red_pieces.append([i,j])
                        all_red_piece.append(curr_piece)
        all_red_valid_moves = []
        all_white_valid_moves = []
        tmp_piece = Piece.__init__
        for r in range(len(all_red_piece)):
            tmp_row = all_red_pieces[r][0]
            tmp_col = all_red_pieces[r][1]
            tmp_piece.row=tmp_row
            tmp_piece.col = tmp_col
            tmp_piece.color = RED
            tmp_piece.king = False
            all_red_valid_moves.append(self.get_valid_moves(tmp_piece)) # the valid (moved of all red pieces of the current board saved on this list
        red_valid_moves_counter = 0
        for a in all_red_valid_moves:
            if bool(a):
                red_valid_moves_counter +=1
        if red_valid_moves_counter==0:
            return PITCH
        for w in   range (len(all_white_piece)):
            tmp_row = all_white_pieces[w][0]
            tmp_col = all_white_pieces[w][1]
            tmp_piece.row=tmp_row
            tmp_piece.col = tmp_col
            tmp_piece.color = WHITE
            tmp_piece.king = False
            all_white_valid_moves.append(self.get_valid_moves(tmp_piece))
            white_valid_moves_counter = 0
        for a in all_white_valid_moves:
            if bool(a):
                white_valid_moves_counter +=1
        if white_valid_moves_counter==0:
            return GRAY
        for i in range(8):
            for j in range(8):
                curr_piece = self.get_piece(i,j)
        self.redMoves=0
        self.whiteMoves=0
        return None
		
    def get_valid_moves(self, piece): # for each piece return the valid moves it can make, and later on show them on the board.
        moves = {} #empty dictionary                 
        left = piece.col - 1
        right = piece.col +1
        row = piece.row        
        if piece.color == RED or piece.king:
            moves.update(self._traverse_left(row-1, max(row-3, -1), -1, piece.color, left))
            moves.update(self._traverse_right(row-1, max(row-3, -1), -1, piece.color, right))
        if piece.color == WHITE or piece.king:
            moves.update(self._traverse_left(row+1, min(row+3, ROWS), 1, piece.color, left))
            moves.update(self._traverse_right(row+1, min(row+3, ROWS), 1, piece.color, right))
        return moves

############ algorithm to determine if valide moves base on a piece ############ 
    def _traverse_left(self, start, stop, step, color, left, skipped=[]):
        moves = {} #empty dictionary
        last = []  #empty list
        for r in range(start, stop, step):
            if left < 0:
                break
            
            current = self.board[r][left]
            if current == 0: #found an empty square
                if skipped and not last:
                    break
                elif skipped: #if we skipped over and we found a blank square and we can't skipp again we can't move there 
                    moves[(r,left)] = last + skipped
                else:
                    moves[(r,left)] = last
                if last:
                    if step == -1:
                        row = max(r-3,0)
                    else:
                        row = min(r+3, ROWS)
                    moves.update(self._traverse_left(r+step, row, step, color, left-1, skipped=last))
                    moves.update(self._traverse_right(r+step, row, step, color, left+1, skipped=last))
                break

            elif current.color == color: #couldn't find an ampty square
                break
            else:
                last = [current]
            
            left -= 1

        return moves
    
    def _traverse_right(self, start, stop, step, color, right, skipped=[]):
	#same as traverse left but to the right.
        moves = {} #empty dictionary
        last = []  #empty list
        for r in range(start, stop, step):
            if right >= COLS:
                break
            
            current = self.board[r][right]
            if current == 0: #found an empty square
                if skipped and not last:
                    break
                elif skipped: #if we skipped over and we found a blank square and we can't skipp again we can't move there 
                    moves[(r,right)] = last + skipped
                else:
                    moves[(r,right)] = last
                if last:
                    if step == -1:
                        row = max(r-3,0)
                    else:
                        row = min(r+3, ROWS)
                    moves.update(self._traverse_left(r+step, row, step, color, right-1, skipped=last))
                    moves.update(self._traverse_right(r+step, row, step, color, right+1, skipped=last))
                break

            elif current.color == color: #couldn't find an ampty square
                break
            else:
                last = [current]
            
            right += 1

        return moves
               

