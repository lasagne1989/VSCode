#!/usr/bin/env python

#libraries
import random
from data import Data

def firstPlayer():
    player_count = len(Data.Config.players)
    player_num = random.randint(0, player_count - 1)
    player_cycle = []
    for i in range(player_count):
        player_cycle.append(Data.Config.players[player_num % player_count])
        player_num += 1

if __name__ == "__main__":
    firstPlayer()