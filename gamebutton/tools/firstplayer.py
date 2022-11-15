#!/usr/bin/env python

#libraries
import random
import data

def firstPlayer():
    player_count = len(data.Data.Config.players)
    player_num = random.randint(0, player_count - 1)
    player_cycle = []
    for i in range(player_count):
        player_cycle.append(data.Data.Config.players[player_num % player_count])
        player_num += 1

if __name__ == "__main__":
    firstPlayer()