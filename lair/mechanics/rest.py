from mechanics.combat import roll_die
import includes.globals
from includes.world import * # loads the world map



def rest(player):
    roll = roll_die(1,6)
    player.hp = player.hp+roll
    if player.hp > player.initial_hp:
        player.hp = player.initial_hp # You can't regain HP over your initial amount
        print ('\nYou feel refreshed\n')
    else:
        print ('\nRegained '+str(roll)+'HP\n')

    # burn the room so we cant exploit the encounter
    grid[includes.globals.row][includes.globals.col] = '@'

    # increment stats
    includes.globals.times_rested = includes.globals.times_rested+1
