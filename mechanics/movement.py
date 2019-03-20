# moving and encountering in the lair

import includes.globals as globals # globals variables
from includes.world import * # get the world map
from includes.heroes import * # loads heroes
from includes.monsters import * # loads monsters
from includes.encounters import * # loads encounters
from mechanics.combat import combat # die and combat mechanics
from mechanics.misc import show_stats
from mechanics.rest import rest # resting at rest sites
from strings.story import * # import the long story strings
from includes.generic import clear_screen
from time import sleep
import re
from tabulate import tabulate


def play_encounter(map_value):
    if map_value == 2:
        clear_screen()
        sleep (0.5)
        tell_story(exploring)
        enemy = random.choice(monsters)
        monster_encounter(enemy)
        combat(my_hero,enemy)
    elif map_value == 5:
        clear_screen()
        sleep (0.5)
        tell_story(exploring)
        tell_story(resting)
        rest(my_hero)
        tell_story(advance)
    elif map_value == 6:
        clear_screen()
        sleep (0.5)
        tell_story(exploring)
        trap = random.choice(traps)
        encounter_trap(trap,my_hero)
    else:
        print ('DEBUG -> Playing encounter: '+str(map_value))



def move_east():

    globals.col = globals.col+1
    if globals.col > 6:
        print ("Edge of map - east side")
        globals.col = 6
    play_encounter(grid[globals.row][globals.col])
    #print ('Column: '+str(globals.col)+' Row: '+str(globals.row))

def move_west():
    globals.col = globals.col-1
    if globals.col < 0:
        print ("Edge of map - west side")
        globals.col = 0
    #print ('Column: '+str(globals.col)+' Row: '+str(globals.row))
    play_encounter(grid[globals.row][globals.col])

def move_north():
    globals.row = globals.row+1
    if globals.row > 5:
        print ("Edge of map - north side")
        globals.row = 5
    #print ('Column: '+str(globals.col)+' Row: '+str(globals.row))
    play_encounter(grid[globals.row][globals.col])

def move_south():
    globals.row = globals.row-1
    if globals.row < 0 and globals.col == 3:
        print ('running out?')
        globals.row = 0
    if globals.row < 0:
        print ("Edge of map - south side")
        globals.row = 0
    #print ('Column: '+str(globals.col)+' Row: '+str(globals.row))
    play_encounter(grid[globals.row][globals.col])

# main game movement

def player_action():
    direction_input = input("> ").lower()
    if 'move' in direction_input:
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
        includes.globals.done = True
    elif direction_input == 'reflect' or direction_input == 'r':
        show_stats(my_hero)
    elif direction_input == 'help' or direction_input == '?':
            table = [["Move [north,south,east,west]","n,s,e,w","Move in the lair"],["Reflect","r","Show your hero stats"],["Quit","q","Quit the game"],["Help","?","Show this menu"]]
            print ('\nYou think about your training...\n')
            print (tabulate(table,headers=["Command","Shortcuts","What does it do"])+'\n')

    elif direction_input == 'map':
        for column in reversed(grid):
            print (column)
        print ('')
    else:
        print ("\nYou seem confused. The 'help' command may assist.\n")
