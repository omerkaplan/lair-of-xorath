#from includes.generic import pause
#from includes.generic import clear_screen
from time import sleep
import os
import random
import includes.globals as globals
from includes.world import * # get the world map
from strings.story import *
import includes.equipment


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
        print ('Luck roll - success! '+'('+str(luck)+' Luck vs 🎲 '+str(roll)+')')
        player.luck = player.luck - 1
        return True
    elif roll > luck:
        print ('Luck roll - failed '+'('+str(luck)+' Luck vs 🎲 '+str(roll)+')')
        return False

def check_dead(object):
    if object.hp <=0:
        print ('\n💀 '+object.name+' is dead\n')
        pause()
        return True

def monster_reset(monster):
    monster.hp = monster.initial_hp
    if monster.tier == 1 and monster.lootable is True:
        monster.weapon = random.choice(includes.equipment.t1_weapons)

def loot_monster(player,monster):
    print ('tell story - you look at '+monster.name+ "'s corpse and find a "+monster.weapon.name)
    if monster.weapon.max_damage > player.weapon.max_damage:
        print ('\ntell story - monsters weapon is better - LOOT IT!')
        player.weapon = monster.weapon
    elif monster.weapon.max_damage < player.weapon.max_damage:
        print ('\ntell story - Your weapon is better')
    elif monster.weapon.max_damage == player.weapon.max_damage: #we need to evaluate roll bonus
        if monster.weapon.roll_bonus > player.weapon.roll_bonus:
            print ('tell story - monsters weapons is better based on roll bonus - LOOT IT!')
            player.weapon = monster.weapon
        elif monster.weapon.roll_bonus < player.weapon.roll_bonus:
            print ('tell story - your weapon is better from damage and roll bonus standpoint')
        elif monster.weapon.roll_bonus == player.weapon.roll_bonus:
            print ('both weapons are equal - keep yours')

def combat(player,monster):

    def roll_damage(attacker,defender,crit):
        crit_roll = 0
        if crit is True:
            crit_roll = roll_die(attacker.weapon.damage_die_number,attacker.weapon.damage_die_sided)
        roll = roll_die(attacker.weapon.damage_die_number,attacker.weapon.damage_die_sided)
        weapon_damage_bonus = attacker.weapon.damage_bonus
        defender.hp = (defender.hp-roll-crit_roll-weapon_damage_bonus+defender.armor.damage_reduction)
        print (str(roll+crit_roll+weapon_damage_bonus)+' Damage delt to '+defender.name+'. (🎲 '+str(roll)+'+'+str(crit_roll)+'+'+str(weapon_damage_bonus)+'-'+str(defender.armor.damage_reduction)+'='+str(roll+crit_roll+weapon_damage_bonus-defender.armor.damage_reduction)+')')

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
            print ('\nYou wipe the remains of the '+monster.name+' from your '+player.weapon.type+'.\n')
            if monster.lootable is True:
                loot_monster(player,monster)
            tell_story(advance)
            monster_reset(monster) # makes sure that the same monster type can fight another day
            grid[globals.row][globals.col] = '*'
            break

        #monster turn
        if monster.lootable is True:
            print ('\n'+monster.name+' attacks with '+monster.weapon.type+'...')
        else:
            print ('\n'+monster.name+' attacks with '+monster.weapon.name+'...')
        attack(monster,player)
        if check_dead(player) is True:
            clear_screen()
            print ('\n'+monster.name+' is landing the final hit...\n')
            if player.luck > 0:
                pause()
                clear_screen()
                print ('\ntell story - you pray and your diety saves you. You are in the room with the monster, cannot attack but can go anywhere\n')
                player.hp = player.initial_hp
                player.luck = 0
                tell_story(advance)
            else:
                print ('\n'+monster.name+' '+monster.fatality+'\n\nYour adventure ends here...\n')
                globals.done = True # game over
            break
