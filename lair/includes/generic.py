import os
import includes.globals # globals variables, most notebly 'done' for game over
from strings.story import *
from includes.heroes import my_hero
import pickle
import datetime
import math
from tabulate import tabulate
from termcolor import colored, cprint

def save_game(hero_object):
    with open('save_game.pkl', 'wb') as output:
        hero_save = hero_object
        pickle.dump(hero_save, output, pickle.HIGHEST_PROTOCOL)

def load_game(hero_object):
    try:
        with open('save_game.pkl', 'rb') as input:
            load_object = pickle.load(input)
            print ('game loaded')
            hero_object.weapon = load_object.weapon
            hero_object.armor = load_object.armor
    except FileNotFoundError:
        pass

def reset_game(hero_object):
    hero_object.reset()
    save_game(hero_object)

def clear_screen():
    os.system('clear')

def pause():
    input("\nPress ENTER to continue...")

def title():
    clear_screen()
    print ("##          ###    #### ########      #######  ########    ##     ##  #######  ########     ###    ######## ##     ## ")
    print ("##         ## ##    ##  ##     ##    ##     ## ##           ##   ##  ##     ## ##     ##   ## ##      ##    ##     ## ")
    print ("##        ##   ##   ##  ##     ##    ##     ## ##            ## ##   ##     ## ##     ##  ##   ##     ##    ##     ## ")
    print ("##       ##     ##  ##  ########     ##     ## ######         ###    ##     ## ########  ##     ##    ##    ######### ")
    print ("##       #########  ##  ##   ##      ##     ## ##            ## ##   ##     ## ##   ##   #########    ##    ##     ## ")
    print ("##       ##     ##  ##  ##    ##     ##     ## ##           ##   ##  ##     ## ##    ##  ##     ##    ##    ##     ## ")
    print ("######## ##     ## #### ##     ##     #######  ##          ##     ##  #######  ##     ## ##     ##    ##    ##     ## ")
    print ('\nLair of Xorath - a roguelike text-based RPG\n')
    print ('\n')
    tell_story(exposition)
    pause()
    clear_screen()
    print ("\n\nToday is your 18th birthday. It is night time it's quiet.\n\nWith a torch one hand and a ",end ='')
    cprint(my_hero.weapon.name.lower(),'yellow', end = '')
    print(" in the other, wearing a leather armor bearing your\nfamily's crest and ",end ='')
    cprint(my_hero.armor.name.lower(),'yellow',end='')
    print(", you have one goal in mind -\nvanquish Xorath and set the people of Hillsbard free.")
    tell_story(advance)
    includes.globals.session_start_time = datetime.datetime.now() #timestamp session start
    try:
        with open('save_game.pkl', 'rb') as input:
            pass
    except FileNotFoundError:
        print ("\nTIP: use '?' for list of avilable commands\n")

def credits():
    print ("\n\n------------------------------------------")
    print ("Thank you for playing Lair of Xorath!")
    print ("Version "+includes.globals.game_version+"\n")
    print ("Brought to you by Omer Kaplan")
    print ("For game updates visit:")
    print ("https://github.com/omerkaplan/\n")
    print ("In memory of Kevin Slattery (1977-2018)")
    print ("------------------------------------------\n\n")

def show_session_stats(player):
    pause()
    clear_screen()

    duration_object = includes.globals.session_duration.seconds
    if duration_object < 60:
        total_duration = str(duration_object)+" seconds"
    elif duration_object > 60:
        minutes = math.floor(duration_object/60)
        if minutes == 1:
            total_duration = "1 minute"
        else:
            total_duration = str(minutes)+" minutes"
    elif duration_object == 60:
        total_duration = "1 minute"
    if includes.globals.xorath_is_dead is False:
        xorath_status = "is alive"
    else:
        xorath_status = "is dead!"

    print ("\n\nSession stats")
    table = [["Xorath",xorath_status],["Session Duration",total_duration],["Rooms discovered",str(includes.globals.rooms_visited)+" ("+str(math.floor(includes.globals.rooms_visited/49*100))+"%)"],["Monsters Killed",includes.globals.monsters_killed],["Combat avoided",includes.globals.monsters_avoided],["Traps disarmed",includes.globals.traps_disarmed],["Traps triggered",includes.globals.traps_triggered],["Loot found",includes.globals.loot_found],["Times rested",includes.globals.times_rested],["Weapon",player.weapon.name],["Armor",player.armor.name],["Cheats used",includes.globals.cheats_used]]
    print(tabulate(table))
