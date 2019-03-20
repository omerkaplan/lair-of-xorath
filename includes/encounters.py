import includes.globals # globals variables
from includes.generic import pause
from includes.generic import clear_screen
from mechanics.combat import roll_die
from mechanics.combat import luck_test
from mechanics.combat import check_dead
from includes.heroes import *
from includes.world import * # get the world map
from strings.story import *



# Encounter legend
# -------------------------
# 1 - Safe passage
# 2 - Monster, tier 1
# 3 - Monster, tier 2
# 4 - Treasure
# 5 - Rest site
# 6 - Trap
# 98 - Xorath encounter
# 99 - Lair entry
# * - Visited, killed monster
# $ - Visited, looted trasure
# # - Visited, springed trap


class trap:
    def __init__(self, name,damage,fatality):
        self.name = name
        self.damage = damage
        self.fatality = fatality

# list of traps

trap_spike = trap('spike trap',roll_die(1,4),'you barily notice the small spike on the floor as it penetrates your boot and injects lethal poison to your body')

# the trap encounter

def encounter_trap(trap,player):
    print ("It's a trap!")
    pause()
    if luck_test(player) is True:
        grid[includes.globals.row][includes.globals.col] = '#'
        tell_story(advance)
    else:
        grid[includes.globals.row][includes.globals.col] = '#'
        trap_damage = trap.damage
        player.hp = player.hp-trap_damage+player.armor.damage_reduction
        print ('took '+str(trap_damage+player.armor.damage_reduction)+' damage from '+trap.name+'.')
        tell_story(advance)
        if check_dead(player) is True:
            globals.done = True # game over
            clear_screen()
            print ('\n'+trap.fatality+'. Your adventure ends here...\n')

# rest site encounters
