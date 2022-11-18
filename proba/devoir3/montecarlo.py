import numpy as np
import matplotlib.pyplot as plt
import connect4
import time

t = time.time()

N = 10 # Nb repetitions
nb_games = [10, 100, 1000, 10000]
# Array with the percentage of success for player 1 for [10, 100, 1000, 10000] games, N times each
win1 = np.zeros((N, len(nb_games)))
# Array with the percentage of draws for player 1 for [10, 100, 1000, 10000] games, N times each
draw = np.zeros((N, len(nb_games)))

##################################
### START : To do for students ###
##################################

# To do : fill in arrays win1 and draw
# In order to do so, simulate games with the function connect4.run_game() 
for i in range(N): # N repetitions
    for j in range(len(nb_games)): # 10, 100, 1000, 10000 games
        player1_wins = 0
        draws = 0
        nbr = nb_games[j]
        for game in range(nbr):
            result = connect4.run_game()
            if result == 1:
                player1_wins += 1
            elif result == 0:
                draws += 1
        win1[i][j] =  player1_wins / nbr
        draw[i][j] =  draws / nbr
win1 *= 100
draw *= 100
print(win1)
################################
### END : To do for students ###
################################

# Computes and prints de mean for each [10, 100, 1000, 10000]
win1_mean = np.mean(win1, axis=0)
draw_mean = np.mean(draw, axis=0)
print(win1_mean)
print(draw_mean)

# Plot the results in the required format.
# Please do not modify
plt.figure()
for i in range(len(nb_games)):
    plt.scatter(np.full(N, nb_games[i]), win1[:,i], c = 'blue', s = 10)
    plt.scatter(np.full(N, nb_games[i]), draw[:,i], c = 'red', s = 10)
    plt.scatter(nb_games[i], win1_mean[i], c = 'blue', marker = 'x', s = 50)
    plt.scatter(nb_games[i], draw_mean[i], c = 'red', marker = 'x', s = 50)
plt.legend(['Victoire joueur 1', 'Ex-aequo', 'Moyenne victoire joueur 1', 'Moyenne ex-aequo'])
plt.xlabel('Nombre de parties')
plt.ylabel('Probabilite en %')
plt.xscale("log")
plt.ylim((-10,100))
# plt.show()

elapsed = time.time() - t
print(f'Elapsed time [s]: {elapsed} \nElapsed time [min]: {elapsed/60}')

#plt.savefig('MCplot.png', format='png')