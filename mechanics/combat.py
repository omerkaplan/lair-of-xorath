#from includes.generic import pause
#from includes.generic import clear_screen
from time import sleep
import os
import random
import includes.globals as globals
from includes.world import * # get the world map
from strings.story import *


# function

def pause():
    input("\nPress ENTER to continue...")

def clear_screen():
    os.system('clear')

def roll_die(number,sided):
    score = number*(random.randint(1,sided))
    return score

def luck_test(player): # luck test, returns True if lucky or False otherwise
    luck = player.luck
    roll = roll_die(2,6)
    if roll <= luck:
        print ('\nPassed luck test '+'('+str(luck)+' Luck vs 🎲 '+str(roll)+')')
        player.luck = player.luck - 1
        return True
    elif roll > luck:
        print ('\nFailed luck test'+'('+str(luck)+' Luck vs 🎲 '+str(roll)+')')
        return False

def check_dead(object):
    if object.hp <=0:
        print ('\n💀 '+object.name+' is dead\n')
        pause()
        return True

def monster_reset(monster):
    monster.hp = monster.initial_hp

def combat(player,monster):

    def roll_damage(attacker,defender,crit):
        crit_roll = 0
        if crit is True:
            crit_roll = attacker.weapon.damage
        roll = attacker.weapon.damage
        weapon_damage_bonus = attacker.weapon.damage_bonus
        defender.hp = (defender.hp-roll-crit_roll-weapon_damage_bonus+defender.armor.damage_reduction)
        print (str(roll+crit_roll)+' Damage delt to '+defender.name+'. (🎲 '+str(roll)+'+'+str(crit_roll)+'+'+str(weapon_damage_bonus)+'-'+str(defender.armor.damage_reduction)+'='+str(roll+crit_roll+weapon_damage_bonus-defender.armor.damage_reduction)+')')

    def roll_attack(attacker,defender):
        roll = roll_die(1,20)
        roll_with_bonuses = roll+attacker.weapon.roll_bonus
        if roll is 1:
            print ('Critical Miss! (🎲 '+str(roll)+')')
            return [False,False] #no hit no crit regardless of AC
        if roll is 20:
            print ('Critial Hit! (🎲 '+str(roll)+')')
            return [True,True] #hit and crit regardless of AC
        elif roll_with_bonuses >= defender.ac+defender.armor.ac_bonus:
            print ("It's a hit! (🎲 "+str(roll)+'+'+str(attacker.weapon.roll_bonus)+'='+str(roll_with_bonuses)+")")
            return [True,False] #hit no crit
        elif roll_with_bonuses < defender.ac+defender.armor.ac_bonus:
            print ('Miss! (🎲 '+str(roll)+'+'+str(attacker.weapon.roll_bonus)+'='+str(roll_with_bonuses)+')')
            return [False,False] #no hit no crit

    def attack(attacker,defender):
        sleep(1)
        attack_roll = roll_attack(attacker,defender)
        if True in attack_roll: #it's a hit, but is it a crit
            if attack_roll == [True,True]:
                roll_damage(attacker,defender,True)
            else:
                roll_damage(attacker,defender,False)

    # combat flow

    pause()
    while monster.hp > 0 and player.hp > 0:

        #player turn
        print ('\nYou swing your '+player.weapon.name+'...')
        attack(player,monster)
        if check_dead(monster) is True:
            clear_screen()
            print ('\nYou wipe the remains of the '+monster.name+' from your '+player.weapon.type+'...\n')
            tell_story(advance)
            monster_reset(monster) # makes sure that the same monster type can fight another day
            grid[globals.row][globals.col] = '*'
            break
        #monster turn
        print ('\n'+monster.name+' attacks with '+monster.weapon.name+'...')
        attack(monster,player)
        if check_dead(player) is True:
            clear_screen()
            print ('\n'+monster.name+' '+monster.fatality+' Your adventure ends here...\n')
            includes.globals.done = True # game over
            break
