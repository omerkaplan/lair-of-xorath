#import random
#import os
#from time import sleep
#from tabulate import tabulate
import includes.globals # globals variables, most notebly 'done' for game over
from includes.generic import title
#from includes.heroes import * # loads heroes
#from includes.monsters import * # loads monsters
from includes.world import * # loads the world map
#from mechanics.combat import combat # die and combat mechanics
from mechanics.movement import player_action
from strings.story import tell_story
import pickle
#from mechanics.misc import show_stats
#import includes.equipment


# program
title()
while not includes.globals.done:
    player_action()
