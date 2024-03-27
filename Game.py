def play_game(player, boss):
    moves = []
    label = -1

    while True:
        boss.take_dmg(player)
        if boss.dead():
            label = 0
            break

        moves.append(player.take_dmg(boss))
        if player.dead():
            label = 1
            break
    
    return moves, boss.getHP(), label