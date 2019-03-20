import os
import includes.globals # globals variables, most notebly 'done' for game over
from strings.story import *
from includes.heroes import my_hero

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
