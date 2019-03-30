import includes.globals # globals variables, most notebly 'done' for game over
from includes.generic import title
from includes.generic import load_game
from includes.heroes import my_hero # loads heroes
from includes.world import * # loads the world map
from mechanics.movement import player_action


# a new hope...
load_game(my_hero) #loads the save file
title()
while not includes.globals.done:
    player_action()
