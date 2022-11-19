import numpy as np
import matplotlib.pyplot as plt
import connect4
import time
from multiprocessing import Pool


def run(N, nb_games,win1,draw):
    for i in range(N):
        player1_wins = 0
        draws = 0
        for j in range(nb_games[-1]):
            print(f"N = {i}/ j = {j}")
            result = connect4.run_game()
            if result == 1:
                player1_wins += 1
            elif result == 0:
                draws += 1
            if j+1 in nb_games:
                try:
                    win1[i][nb_games.index(j+1)] =  player1_wins / (j+1)
                    draw[i][nb_games.index(j+1)] =  draws / (j+1)
                except:
                    print(win1, j+1)
    return win1, draw

if __name__ == '__main__':
    t = time.time()
    N = 8 # Nb repetitions
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
    with Pool(4) as p:
        result1 = p.apply_async(run, (2, nb_games, win1, draw))
        result2 = p.apply_async(run, (2, nb_games, win1, draw))
        result3 = p.apply_async(run, (2, nb_games, win1, draw))
        result4 = p.apply_async(run, (2, nb_games, win1, draw))
        answer1 = result1.get(timeout=100)
        answer2 = result2.get(timeout=100)
        answer3 = result3.get(timeout=100)
        answer4 = result4.get(timeout=100)
    win1 = (answer1[0] + answer2[0] + answer3[0] + answer4[0])/4
    draw = (answer1[1] + answer2[1] + answer3[1] + answer4[1])/4
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

    plt.savefig('MCplot.png', format='png')