import includes.globals # globals variables, most notebly 'done' for game over
from includes.generic import title
from includes.generic import load_game
from includes.generic import credits
from includes.generic import reset_game
from includes.generic import show_session_stats
from includes.heroes import my_hero # loads heroes
from includes.world import * # loads the world map
from mechanics.movement import player_action


# a new hope...
load_game(my_hero) #loads the save file

title()

# the actual game loop

while not includes.globals.done:
    player_action()

#once the game is over...

show_session_stats(my_hero)
credits()
if includes.globals.xorath_is_dead is True:
    reset_game(my_hero)
