import includes.globals # globals variables
from includes.generic import pause
from includes.generic import clear_screen
from mechanics.combat import roll_die
from mechanics.combat import luck_test
from mechanics.combat import check_dead
from includes.heroes import *
from includes.world import * # get the world map
from strings.story import *
import datetime


class Trap:
    def __init__(self, name,damage,damage_description,fatality):
        self.name = name
        self.damage = damage
        self.damage_description = damage_description
        self.fatality = fatality

# some traps

trap_spike = Trap('spike trap',roll_die(1,4),'A large spike gashes your side. You groan in pain','You notice the yellow green substance at the tip of the spike. Snakefolk poison!\nYour world starts to spin and you slip into unconsciousness.')
trap_rocks = Trap('falling rocks',roll_die(1,6),'A barrage of heavy rocks falls of above, pummelling you','Suddenly, a large rock falls directly on your head, stunning you into unconsciousness.')

traps = [trap_spike,trap_rocks]

# the trap encounter

def encounter_trap(trap,player):
    if luck_test(player) is True:
        grid[includes.globals.row][includes.globals.col] = '#'
        includes.globals.traps_disarmed = includes.globals.traps_disarmed+1
        tell_story(trap_avoided)
        tell_story(advance)
    else:
        grid[includes.globals.row][includes.globals.col] = '#'
        trap_damage = trap.damage
        player.hp = player.hp-trap_damage+player.armor.damage_reduction
        tell_story(trap_triggered)
        includes.globals.traps_triggered = includes.globals.traps_triggered+1
        print ('\n'+trap.damage_description+' (you take '+str(trap_damage+player.armor.damage_reduction)+' damage)')
        if check_dead(player) is True:
            includes.globals.done = True # game over
            clear_screen()
            print ('\n'+trap.fatality+'\n\nYour adventure ends here...\n')
            includes.globals.session_end_time = datetime.datetime.now()
            includes.globals.session_duration = includes.globals.session_end_time-includes.globals.session_start_time

        else:
            tell_story(advance)
