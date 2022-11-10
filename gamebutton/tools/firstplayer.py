#!/usr/bin/env python

#libraries
import random
from data import Config

player_count = len(Config.players)
player_num = random.randint(0, player_count - 1)
player_cycle = []
for i in range(player_count):
    player_cycle.append(Config.players[player_num % player_count])
    player_num += 1