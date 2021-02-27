from copy import deepcopy
import pygame

RED = (255,0,0)
WHITE = (255, 255, 255)

#curr_pos is the current position of the player, depth is the current depth we're at, 
# max player: is boolean, if it's max we'll take the maximal "son", if not then the minimal, game: the current game being player.
def minimax(curr_pos, depth, max_player, game):
    #check status game and depth of the tree
    #depth = 0 - finished testing of all possible moves.
    if depth == 0 or curr_pos.winner() != None:
        return curr_pos.evaluate(), curr_pos
    if max_player:
        maxEval = float('-inf') #this is - infinum so if we wont find any maximal value we'll know that there's no point to continue searching the tree.
        best_move = None
        for move in get_all_moves(curr_pos, WHITE, game):#get all_moves: returns all possible moves for a piece.
            evaluation = minimax(move, depth-1, False, game)[0] #recursive call for minimax function
            maxEval = max(maxEval, evaluation) #maxEval: if the evaluation function which takes the value of the minimax (the highest current son value) returned a number then amxEvaluation will change now to an int instead of minus infinity.
            if maxEval == evaluation: #meaning that it's not infinity anymore.
                best_move = move
        
        return maxEval, best_move
    else:#if the player is minimum now.
        minEval = float('inf')
        best_move = None
        for move in get_all_moves(curr_pos, RED, game):
            evaluation = minimax(move, depth-1, True, game)[0]
            minEval = min(minEval, evaluation)
            if minEval == evaluation:
                best_move = move
        
        return minEval, best_move

#the following simulates a move on board - used for debugging
def simulate_move(piece, move, board, game, skip):
    board.move(piece, move[0], move[1])
    if skip:
        board.remove(skip)

    return board


	#returns all possible moves for certain player on current board.
def get_all_moves(board, color, game):
    moves = []
    for piece in board.get_all_pieces(color):
        valid_moves = board.get_valid_moves(piece)
        for move, skip in valid_moves.items():
            temp_board = deepcopy(board) #copy of board
            temp_piece = temp_board.get_piece(piece.row, piece.col) #copy of piece
            new_board = simulate_move(temp_piece, move, temp_board, game, skip)
            moves.append(new_board)
    
    return moves

