import math
import random as rd
import numpy as np
#ai_random, update_board, check_win, and sim are all either based or were taken from the code we were provided.
def ai_random(arg_board, player):
    board = np.copy(arg_board)
    # Collects the moves which can be played (i.e. the nonfull columns)
    nonfull_cols = np.where(board[0] == 0)[0]
    for col in nonfull_cols:
        # Creates the attack and defense moves, to check if one is a winning move
        attack_board = np.copy(update_board(board, col, player))
        defense_board = np.copy(update_board(board, col, abs(player-3)))
        # Plays if winning move for him
        if check_win(attack_board, col, player):
            #print('Plays attack move')
            return col
        # Plays if winning move for opponent
        elif check_win(defense_board, col, abs(player-3)):
            #print('Plays defense move')
            return col
    # Otherwise, plays random
    return rd.choice(nonfull_cols)

def update_board(arg_board, col, player):
    board = np.copy(arg_board)
    # The arguments are the board and the last move of the last player
    for i in range(5,-1,-1):
        if board[i][col] == 0:
            board[i][col] = player
            return board

def check_win(board, col, player):
    # This function checks if the player won with his last move.
    # The arguments are the board and the last move of the last player.
    # First, we locate the row of this last move.
    row = 6
    for i in range(6):
        if board[i][col] == player:
            row = i
            break
    # Check left
    if col > 2:
        if board[row][col-1] == player:
            if board[row][col-2] == player:
                if board[row][col-3] == player:
                    return True
    # Check 2 lefts and 1 right
    if col > 1 and col < 6:
        if board[row][col-1] == player:
            if board[row][col-2] == player:
                if board[row][col+1] == player:
                    return True
    # Check 1 left and 2 rights
    if col > 0 and col < 5:
        if board[row][col-1] == player:
            if board[row][col+1] == player:
                if board[row][col+2] == player:
                    return True
    # Check right
    if col < 4:
        if board[row][col+1] == player:
            if board[row][col+2] == player:
                if board[row][col+3] == player:
                    return True
    # Check up
    if row > 2:
        if board[row-1][col] == player:
            if board[row-2][col] == player:
                if board[row-3][col] == player:
                    return True
    # Check 2 ups and 1 down
    if row > 1 and row < 5:
        if board[row-1][col] == player:
            if board[row-2][col] == player:
                if board[row+1][col] == player:
                    return True
    # Check 1 up and 2 downs
    if row > 0 and row < 4:
        if board[row-1][col] == player:
            if board[row+1][col] == player:
                if board[row+2][col] == player:
                    return True
    # Check down
    if row < 3:
        if board[row+1][col] == player:
            if board[row+2][col] == player:
                if board[row+3][col] == player:
                    return True
    # Check NW (North West)
    if col > 2 and row > 2:
        if board[row-1][col-1] == player:
            if board[row-2][col-2] == player:
                if board[row-3][col-3] == player:
                    return True
    # Check 2 NW and 1 SE
    if col > 1 and col < 6 and row > 1 and row < 5:
        if board[row-1][col-1] == player:
            if board[row-2][col-2] == player:
                if board[row+1][col+1] == player:
                    return True
    # Check 1 NW and 2 SE
    if col > 0 and col < 5 and row > 0 and row < 4:
        if board[row-1][col-1] == player:
            if board[row+1][col+1] == player:
                if board[row+2][col+2] == player:
                    return True
    # Check SE (South East)
    if col < 4 and row < 3:
        if board[row+1][col+1] == player:
            if board[row+2][col+2] == player:
                if board[row+3][col+3] == player:
                    return True
    # Check NE
    if col < 4 and row > 2:
        if board[row-1][col+1] == player:
            if board[row-2][col+2] == player:
                if board[row-3][col+3] == player:
                    return True
    # Check 2 NE and 1 SW
    if col > 0 and col < 5 and row > 1 and row < 5:
        if board[row-1][col+1] == player:
            if board[row-2][col+2] == player:
                if board[row+1][col-1] == player:
                    return True
    # Check 1 NE and 2 SW
    if col > 1 and col < 6 and row > 0 and row < 4:
        if board[row-1][col+1] == player:
            if board[row+1][col-1] == player:
                if board[row+2][col-2] == player:
                    return True
    # Check SW
    if col > 2 and row < 3:
        if board[row+1][col-1] == player:
            if board[row+2][col-2] == player:
                if board[row+3][col-3] == player:
                    return True
    return False

def sim(brd,mvs):
    tst = np.copy(brd)
    for x in range(mvs):
      mv1 = ai_random(tst, 1)
      tst = update_board(tst, mv1, 1)
      if check_win(tst, mv1, 1):
            return 1
      mv2 = ai_random(tst, 2)
      tst = update_board(tst, mv2, 2)
      if check_win(tst, mv2, 2):
            return 2
    return 0

def ai_student(board, player):
  '''check if we can win, to do so we just yeet a coin
  in each column and check if that move wins the game
  (we do that first cuz why drag the game if we can win)
  this is given to us in the template btw'''
  opponent = 2 if player == 1 else 1
  cpBoard = np.copy(board)
  possibleColumns = np.where(cpBoard[0] == 0)[0] 
  for column in possibleColumns:
    #we create a copy of the board for both players so we can check if we can either
    #win or deny the opponent a win hehe
    atckBoard = np.copy(update_board(cpBoard, column, player))
    dfnsBoard = np.copy(update_board(cpBoard, column, opponent))
    #best case scenario, we can win the game then we just yeet a coin in that column
    if check_win(atckBoard, column, player):
      return column
    #not quite best case scenario, we can deny the opponent a win so that's always good
    if check_win(dfnsBoard, column, opponent):
      return column
  '''ok so far no one can win, so we just yeet a coin in a random column? why not
  but let's try to at least make a somewhat decent move while we're at it lol
  thanks to the 2nd point of the homework we have a good estimate of the time
  it takes to run the game x times'''
  if cpBoard[5][3] == 0 or cpBoard[4][3] == 0:
    return 3
  noAvailibleSpots = np.count_nonzero(cpBoard == 0) - 1
  x = 100 if noAvailibleSpots > 18 else 1000 #:D (we can change this value to make the AI better or worse)
  nbrWins = np.zeros(len(possibleColumns))
  for column in range(len(possibleColumns)):
    nxtBoard = np.copy(update_board(cpBoard, possibleColumns[column], player))
    for game in range(x):
      result = sim(nxtBoard,noAvailibleSpots//2)
      #we run the game x times and count the number of wins we get
      if result == player:
        nbrWins[column] += 1
  nbrWins /= x
  maxChance = np.amax(nbrWins)
  maxIndx = np.where(nbrWins == maxChance)[0]
  return possibleColumns[maxIndx[0]]





