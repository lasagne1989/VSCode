#!/usr/bin/env python

#libraries
import random
from main import players

player_count = len(players)
player_num = random.randint(0, player_count - 1)
player_cycle = []
for i in range(player_count):
    player_cycle.append(players[player_num % player_count])
    player_num += 1