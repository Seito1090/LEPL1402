import math, random
import numpy as np
import connect4

def ai_student(board, player):
  def sim(brd,mvs):
    tst = np.copy(brd)
    for x in range(mvs):
      mv1 = connect4.ai_random(tst, 1)
      tst = connect4.update_board(tst, mv1, 1)
      if connect4.check_win(tst, mv1, 1):
            return 1
      mv2 = connect4.ai_random(tst, 2)
      tst = connect4.update_board(tst, mv2, 2)
      if connect4.check_win(tst, mv2, 2):
            return 2
    return 0 
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
    atckBoard = np.copy(connect4.update_board(cpBoard, column, player))
    dfnsBoard = np.copy(connect4.update_board(cpBoard, column, opponent))
    #best case scenario, we can win the game then we just yeet a coin in that column
    if connect4.check_win(atckBoard, column, player):
      return column
    #not quite best case scenario, we can deny the opponent a win so that's always good
    if connect4.check_win(dfnsBoard, column, opponent):
      return column
  '''ok so far no one can win, so we just yeet a coin in a random column? why not
  but let's try to at least make a somewhat decent move while we're at it lol
  thanks to the 2nd point of the homework we have a good estimate of the time
  it takes to run the game x times'''
  if cpBoard[5][3] == 0 or cpBoard[4][3] == 0:
    return 3
  noAvailibleSpots = np.count_nonzero(cpBoard == 0) - 1
  x = 10  #:D (we can change this value to make the AI better or worse)
  nbrWins = np.zeros(len(possibleColumns))
  for column in range(len(possibleColumns)):
    nxtBoard = np.copy(connect4.update_board(cpBoard, possibleColumns[column], player))
    for game in range(x):
      result = sim(nxtBoard,noAvailibleSpots//2)
      #we run the game x times and count the number of wins we get
      if result == player:
        nbrWins[column] += 1
  nbrWins /= x
  maxChance = np.amax(nbrWins)
  maxIndx = np.where(nbrWins == maxChance)[0]
  return possibleColumns[maxIndx[0]]


if __name__ == '__main__':
  the_board = np.full((6,7), 0)
  ai_student(the_board, 1)


