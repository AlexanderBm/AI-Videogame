import numpy as np
from Boss import Boss 
from Player import Player
from Game import play_game
from MaxProb import get_max
from WeightedAverage import weighted_avg

if __name__ == "__main__":
    moves, labels, moves_np, labels_np, run_p2 = [], [], [], [], [0.5]

    n_iter = 30 # the higher the more accurate
    data_in = 1 # amount of data received per training (works best at 1)
    for i in range(1,n_iter):
        for j in range(1, data_in+1):
            p2 = weighted_avg(run_p2)
            p1 = 1 - p2

            player = Player()
            boss = Boss(p1, p2)
            move, label = play_game(player, boss)
            moves.append(move)
            labels.append(label)

            # needed so it doesn't get stuck
            player_50 = Player()
            boss_50 = Boss(.5, .5)
            move_50, label_50 = play_game(player_50, boss_50)
            moves.append(move_50)
            labels.append(label_50)

        moves_np = np.asarray(moves)
        labels_np = np.asarray(labels)

        max_moves, max_p =  get_max(moves_np, labels_np)
        new_p2 = np.sum(max_moves == 2)/(10 - np.sum(max_moves == 0))
        run_p2.append(new_p2)

        print("ITERATION " + str(i))
        print("Moves " + str(max_moves))
        print("Prob of Boss Winning " + str(max_p))
        print("Iterations Prob of using Stun Attack " + str(new_p2))
        print("Running/True Prob of using Stun Attack " + str(weighted_avg(run_p2)))
        print("------------------------------------------------")
    
    optimized_boss = Boss(1 - weighted_avg(run_p2), weighted_avg(run_p2))
    opt_p_basic, opt_p_stun = optimized_boss.getProbs()
    print("PROBABILITY OF THE OPTIMIZED BOSS USING THE BASIC ATTACK: " + str(opt_p_basic))
    print("PROBABILITY OF THE OPTIMIZED BOSS USING THE STUN ATTACK: " + str(opt_p_stun))

