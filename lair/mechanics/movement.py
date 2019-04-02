# moving and encountering in the lair

import includes.globals as globals # globals variables
from includes.world import * # get the world map
from includes.heroes import * # loads heroes
from includes.monsters import * # loads monsters
from includes.encounters import * # loads encounters
from mechanics.combat import combat # die and combat mechanics
from mechanics.combat import luck_test
from mechanics.misc import show_stats
from mechanics.misc import loot
from mechanics.rest import rest # resting at rest sites
from strings.story import * # import the long story strings
from includes.generic import clear_screen
from includes.generic import save_game
from time import sleep
import re
from tabulate import tabulate


def fight_or_flight(player,monster):
    if monster.tier == 98:
        pass # this is handled by the encounter
    else:
        print ("In the shadows you get a glimse of a "+monster.name+". It didn\'t notice you yet.")
    fof_choice = ""
    while True:
        fof_choice = input('\n(A)ttack '+monster.name+' or (F)lee from battle? >> ').lower()
        if fof_choice == 'attack' or fof_choice == 'a':
            if monster.tier == 98:
                print ("\n\"So be it...\"\n\nXorath gets up from this throne and pick up his greatsword.")
            else:
                print ("\nYou charge forward with your "+player.weapon.name.lower()+". TIME TO FIGHT!")
            combat(my_hero,monster)
            break
        elif fof_choice == 'flee' or fof_choice == 'f':
            print ("\nYou try to slip into the shadows and remain undetected...\n")
            globals.monsters_avoided = globals.monsters_avoided+1
            if luck_test(player) is True:
                print ("\nYou turn back into the room\'s entrance.\n")
                globals.monsters_avoided = globals.monsters_avoided+1
                tell_story(advance)
            else:
                if monster.tier == 98:
                    print ("\nXorath gets up from his throne and pick up his black greatsword\n\n\"On second thought, I\'ll just end you now.\"\n\nTIME TO FIGHT!")
                else:
                    print ("\nYou try to slip into the shadows but not without getting the "+monster.name+"\'s attention. TIME TO FIGHT!\n")
                combat(player,monster)
            break
        else:
            print ('\nThere is no time for that, you must choose...\n')

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
# @ - Visited, rest site
# # - Visited, springed trap

def play_encounter(map_value):
    if map_value == 1:
        globals.rooms_visited = globals.rooms_visited+1
        clear_screen()
        sleep (0.5)
        tell_story(exploring)
        tell_story(advance)

    elif map_value == 2:
        globals.rooms_visited = globals.rooms_visited+1
        clear_screen()
        sleep (0.5)
        tell_story(exploring)
        enemy = random.choice(monsters)
        monster_encounter(enemy)
        combat(my_hero,enemy)
        save_game(my_hero)

    elif map_value == 3:
        globals.rooms_visited = globals.rooms_visited+1
        clear_screen()
        sleep (0.5)
        tell_story(exploring)
        t2_monster = random.choice(monsters_t2)
        fight_or_flight(my_hero,t2_monster)
        save_game(my_hero)

    elif map_value == 4:
        globals.rooms_visited = globals.rooms_visited+1
        globals.loot_found = globals.loot_found+1
        clear_screen()
        sleep (0.5)
        tell_story(exploring)
        tell_story(loot_room)
        loot(my_hero)
        save_game(my_hero)
        tell_story(advance)

    elif map_value == 5:
        globals.rooms_visited = globals.rooms_visited+1
        clear_screen()
        sleep (0.5)
        tell_story(exploring)
        tell_story(resting)
        rest(my_hero)
        tell_story(advance)

    elif map_value == 6:
        globals.rooms_visited = globals.rooms_visited+1
        clear_screen()
        sleep (0.5)
        tell_story(exploring)
        trap = random.choice(traps)
        encounter_trap(trap,my_hero)

    elif map_value == 98:
        globals.rooms_visited = globals.rooms_visited+1
        clear_screen()
        sleep (0.5)
        tell_story(xorath_room)
        tell_story(xorath_taunt)
        fight_or_flight(my_hero,xorath)

    elif map_value == 99:
        globals.rooms_visited = globals.rooms_visited+1
        clear_screen()
        sleep (0.5)
        tell_story(lair_entrance)
        tell_story(advance)

    elif map_value == '*':
        globals.rooms_visited = globals.rooms_visited+1
        clear_screen()
        sleep (0.5)
        tell_story(exploring)
        tell_story(slain_monster)
        tell_story(advance)

    elif map_value == '$':
        clear_screen()
        sleep (0.5)
        tell_story(exploring)
        tell_story(looted_treasure)
        tell_story(advance)

    elif map_value == '#':
        clear_screen()
        sleep (0.5)
        tell_story(exploring)
        tell_story(springed_trap)
        tell_story(advance)


    elif map_value == '@':
        clear_screen()
        sleep (0.5)
        tell_story(exploring)
        tell_story(visited_rest_site)
        tell_story(advance)


    else:
        print ('DEBUG -> Playing encounter: '+str(map_value))



def move_east():

    globals.col = globals.col+1
    if globals.col > 6:
        print ("\nThe area to the east is blocked. You must find another way.\n")
        globals.col = 6
    else:
        play_encounter(grid[globals.row][globals.col])
    #print ('Column: '+str(globals.col)+' Row: '+str(globals.row))

def move_west():
    globals.col = globals.col-1
    if globals.col < 0:
        print ("\nThe area to the west is blocked. You must find another way.\n")
        globals.col = 0
    else:
        play_encounter(grid[globals.row][globals.col])

def move_north():
    globals.row = globals.row+1
    if globals.row > 5:
        print ("\nThe area to the north is blocked. You must find another way.\n")
        globals.row = 5
    else:
        #print ('Column: '+str(globals.col)+' Row: '+str(globals.row))
        play_encounter(grid[globals.row][globals.col])

def move_south():
    globals.row = globals.row-1
    if globals.row < 0 and globals.col == 3:
        clear_screen()
        tell_story(running_away)
        tell_story(advance)
        globals.row = 0
    elif globals.row < 0:
        print ("\nThe area to the south is blocked. You must find another way.\n")
        globals.row = 0
    else:
        #print ('Column: '+str(globals.col)+' Row: '+str(globals.row))
        play_encounter(grid[globals.row][globals.col])

# main game movement

def player_action():
    direction_input = input("> ").lower()
    if 'move' in direction_input or 'go' in direction_input:
        try:
            break_out = re.sub("[^\w]", " ",  direction_input).split() #putting all values in a dict
            if len(break_out) < 3:
                if break_out[1] == 'west':
                    move_west()
                elif break_out[1] == 'east':
                    move_east()
                elif break_out[1] == 'north':
                    move_north()
                elif break_out[1] == 'south':
                    move_south()
                else:
                    print ("\nThis is not a direction you can go.\n")
            else:
                print ('wrong direction')
        except IndexError: #typed 'move' with no direction
            print ('\nGood idea. Move where?\n')
    elif direction_input == 'e' or direction_input == 'east':
        move_east()
    elif direction_input == 'w' or direction_input == 'west':
        move_west()
    elif direction_input == 'n'or direction_input == 'north':
        move_north()
    elif direction_input == 's' or direction_input == 'south':
        move_south()
    elif direction_input == 'q' or direction_input == 'quit':
        clear_screen()
        includes.globals.session_end_time = datetime.datetime.now()
        includes.globals.session_duration = includes.globals.session_end_time-includes.globals.session_start_time
        includes.globals.done = True
    elif direction_input == 'reflect' or direction_input == 'r' or direction_input == 'c':
        show_stats(my_hero)
    elif direction_input == 'help' or direction_input == '?':
            table = [["Move \\ Go [north,south,east,west]","n,s,e,w","Move in the lair"],["Reflect","r \\ c","Show your hero stats"],["Quit","q","Quit the game"],["Help","?","Show this menu"]]
            print ('\nYou think about your training...\n')
            print (tabulate(table,headers=["Command","Shortcuts","What does it do"])+'\n')

    elif direction_input == 'blacksheepwall': #shows a map with encounter keys
        for column in reversed(grid):
            print (column)
        print ('')
        includes.globals.cheats_used = "Yes"
    else:
        print ("\nYou seem confused. The 'help' command may assist.\n")
