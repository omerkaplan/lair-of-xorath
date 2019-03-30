import os
import includes.globals # globals variables, most notebly 'done' for game over
from strings.story import *
from includes.heroes import my_hero
import pickle

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
    print ("\n\nToday is your 18th birthday. It is night time it's quiet.\n\nWith a torch one hand and a "+my_hero.weapon.type+" in the other, wearing a leather armor bearing your\nfamily's crest and "+my_hero.armor.name+", you have one goal in mind -\nvanquish Xorath and set the people of Hillsbard free.")
    tell_story(advance)
    try:
        with open('save_game.pkl', 'rb') as input:
            pass
    except FileNotFoundError:
        print ("\nTIP: use '?' for list of avilable commands\n")

def credits():
    clear_screen()
    print ("\n\n------------------------------------------")
    print ("Thank you for playing Lair of Xorath!")
    print ("Version "+includes.globals.game_version+"\n")
    print ("Brought to you by Omer Kaplan")
    print ("https://github.com/omerkaplan/\n")
    print ("In memory of Kevin Slattery (1977-2018)")
    print ("------------------------------------------\n\n")
