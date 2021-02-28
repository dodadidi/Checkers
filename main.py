import pygame
from checkers.kinter import MyDialog
from checkers.constants import WIDTH, HEIGHT, SQUARE_SIZE, RED, WHITE,BLACK,PITCH,GRAY #can do it due to __init__.py
from checkers.game import Game
from model.minimax import minimax
from checkers.board import Board
from checkers.piece import Piece
from tkinter import simpledialog #tkinter from simpledialog library is used to take from the human the difficulty level he wantsthe game to be.
import tkinter as tk
from tkinter import messagebox #messagebox is used to display a message of who won in the end of the game.

from tkinter.messagebox import showerror
FPS = 60
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
                       
#The following gets from the user the difficulty level of the game
# Player can choose beteen 3 difficulty levels from 1 till 3 where 1 is easy, 2 is intermediate and 3 is the hardest
def get_level():
    pygame.display.set_caption('Welcome to SmartCheckers') #name of our game will display at the top of board  
    opening_window = tk.Tk() 
    opening_window.withdraw()
    userinput = MyDialog(opening_window, "Welcome To SmartCheckers")
    #now testing if it's an int and between 1-3
    #boolean variable that gets true if user enetered a valid digit or not
    gotInt=False
    while (not gotInt):
        try:
            difficultyLevel= int(userinput.result)
        
        except ValueError:
        #When user enters a char or string which is(are) not integer - an error message appears asking him to enter and int
            showerror('Non-Int Error', 'Please enter an integer between 1-3')
            opening_window = tk.Tk() 
            opening_window.withdraw()
            userinput = MyDialog(opening_window, "Welcome To SmartCheckers")
        else: # if the user enters an int which is not 1 or 2 or 3 - an error message appears asking him to enter right value
            if (difficultyLevel<1 or difficultyLevel>3):
                showerror('Wrong Number', 'Please enter an integer between 1-3')
                opening_window = tk.Tk() 
                opening_window.withdraw()
                userinput = MyDialog(opening_window, "Welcome To SmartCheckers")
            else:
                gotInt=True

    return difficultyLevel
    
def get_row_col_from_mouse(pos):
    x,y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def main():
    """
    run this function to run the game.
    event loop. 
    will run every x time per second and check if the player pressed on something and update the display
    """
    run = True #boolean variable - remains true as long as there's no winner.
    clock = pygame.time.Clock() 
    game = Game(WIN) #is for game window
    board = Board() 
    difficultyLevel= get_level()
    
    while run:
        clock.tick(FPS)

        if game.turn == WHITE: #there are two palyers: White and Red
            value, new_board = minimax(game.get_board(), difficultyLevel+1, WHITE, game)
            game.ai_move(new_board)
           
        if game.winner() != None:            
            run = False
        
        for event in pygame.event.get():
            #check if events have happened at the current time
            if event.type ==pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN: #player press on mouse
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row,col)
        
            pos = pygame.mouse.get_pos()
            row, col = get_row_col_from_mouse(pos)
        if (difficultyLevel<3):
            game.update_board(row,col)
        else:
            game.update3(row,col)
   
    if game.winner()== WHITE:
        messagebox.showinfo("Game Over", "White is Winner")
    elif game.winner()== RED:
        messagebox.showinfo("Game Over", "RED is Winner")
    elif game.winner()==BLACK:
        messagebox.showinfo("Game Over", "Too many moves with no change\n Result: Draw")
    elif game.winner()==PITCH:
        messagebox.showinfo("Game Over", "Red has no more valid moves\nWhite is Winner\n")
    elif game.winner()==GRAY:
        messagebox.showinfo("Game Over", "White has no more valid moves\nRed is Winner\n")
    pygame.quit() #close board window 
    
if __name__ == '__main__':
    main()