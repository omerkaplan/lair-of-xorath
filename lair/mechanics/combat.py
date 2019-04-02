#from includes.generic import pause
#from includes.generic import clear_screen
from time import sleep
import os
import random
import datetime
import includes.globals as globals
from includes.world import * # get the world map
from strings.story import *
import includes.equipment
import includes.generic
from termcolor import colored, cprint



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
        print ('Luck roll - ',end='')
        cprint('succeeded! ','green',end ='')
        print('('+str(luck)+' Luck vs 🎲 '+str(roll)+')')
        player.luck = player.luck - 1
        return True
    elif roll > luck:
        print ('Luck roll - ',end='')
        cprint('failed ','red',end ='')
        print('('+str(luck)+' Luck vs 🎲 '+str(roll)+')')
        return False

def check_dead(object):
    if object.hp <=0:
        return True
    else:
        return False

def monster_reset(monster):
    monster.hp = monster.initial_hp
    if monster.tier == 1 and monster.lootable is True:
        monster.weapon = random.choice(includes.equipment.t1_weapons)

def loot_monster(player,monster):
    print ('\nYou examine the '+monster.name+ "'s corpse and find its",end=' ')
    cprint (monster.weapon.name.lower()+'\n','yellow')
    if monster.weapon.max_damage > player.weapon.max_damage:
        print ('This looks like a fine weapon that will surely aid you in your quest!\n\nYou pick it up and leave your '+player.weapon.name.lower()+' behind.')
        player.weapon = monster.weapon
    elif monster.weapon.max_damage < player.weapon.max_damage:
        print ('It looks like it would not bring you much value at its current condition, you leave it behind.')
    elif monster.weapon.max_damage == player.weapon.max_damage: #we need to evaluate roll bonus
        if monster.weapon.roll_bonus > player.weapon.roll_bonus:
            print ('This looks like a fine weapon that will surely aid you in your quest!\n\nYou pick it up and leave your '+player.weapon.name.lower()+' behind.')
            player.weapon = monster.weapon
        elif monster.weapon.roll_bonus < player.weapon.roll_bonus:
            print ('It looks like it would not bring you much value at its current condition, you leave it behind.')
        elif monster.weapon.roll_bonus == player.weapon.roll_bonus:
            print ('The weapon looks in good condition but you are better practiced with your '+player.weapon.name.lower()+'. You leave it behind')

def siphon_soul(monster, player):
    print ('\nYou feel the wrath of '+monster.weapon.name+'...\n')
    if luck_test(player) is True:
        pass
    else:
        siphon_soul_damage = 1
        cprint ("\n"+monster.weapon.name+' feeds your life force to Xorath','magenta',end=' ')
        print ('(You take '+str(siphon_soul_damage)+' damage)\n')
        player.hp = player.hp-siphon_soul_damage
        monster.hp = monster.hp+siphon_soul_damage

def combat(player,monster):

    def roll_damage(attacker,defender,crit):
        crit_roll = 0
        if crit is True:
            crit_roll = roll_die(attacker.weapon.damage_die_number,attacker.weapon.damage_die_sided)
        roll = roll_die(attacker.weapon.damage_die_number,attacker.weapon.damage_die_sided)
        weapon_damage_bonus = attacker.weapon.damage_bonus
        total_damage = roll+crit_roll+weapon_damage_bonus-defender.armor.damage_reduction
        if total_damage <= 0:
            cprint (defender.armor.name+" absorbs the damage!",'cyan',end=' ')
            print('(🎲 '+str(roll)+'+'+str(crit_roll)+'+'+str(weapon_damage_bonus)+'-'+str(defender.armor.damage_reduction)+'='+str(roll+crit_roll+weapon_damage_bonus-defender.armor.damage_reduction)+')')
        else:
            defender.hp = (defender.hp-total_damage)
            print (str(total_damage)+' Damage delt to '+defender.name+'. (🎲 '+str(roll)+'+'+str(crit_roll)+'+'+str(weapon_damage_bonus)+'-'+str(defender.armor.damage_reduction)+'='+str(roll+crit_roll+weapon_damage_bonus-defender.armor.damage_reduction)+')')
        if attacker.name == 'Xorath, the enslaver':
            siphon_soul(attacker,defender)

    def roll_attack(attacker,defender):
        roll = roll_die(1,20)
        roll_with_bonuses = roll+attacker.weapon.roll_bonus
        if roll is 1:
            cprint ('Critical Miss!','red',end=' ')
            print ('(🎲 '+str(roll)+')')
            return [False,False] # no hit no crit regardless of AC
        if roll is 20:
            cprint ('Critical Hit!','yellow',end=' ')
            print ('(🎲 '+str(roll)+')')
            return [True,True] # hit and crit regardless of AC
        elif roll_with_bonuses >= defender.ac+defender.armor.ac_bonus:
            print ("It's a hit!",end=' ')
            print ("(🎲 "+str(roll)+'+'+str(attacker.weapon.roll_bonus)+'='+str(roll_with_bonuses)+")")
            return [True,False] #hit no crit
        elif roll_with_bonuses < defender.ac+defender.armor.ac_bonus:
            print ("Miss!",end=' ')
            print ("(🎲 "+str(roll)+'+'+str(attacker.weapon.roll_bonus)+'='+str(roll_with_bonuses)+")")
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
        print ('\nYou swing your '+player.weapon.name.lower()+'...')
        attack(player,monster)
        if check_dead(monster) is True:
            if monster.tier == 98:
                print ('\n💀 '+monster.name+' is dead\n')
                pause()
                clear_screen()
                tell_story(xorath_dies)
                globals.xorath_is_dead = True
                globals.session_end_time = datetime.datetime.now()
                globals.session_duration = globals.session_end_time-globals.session_start_time
                globals.done = True # game over
                break
            else:
                cprint ('\n💀 '+monster.name+' is dead\n','green')
                pause()
                clear_screen()
                print ('\nYou wipe the remains of the '+monster.name+' from your '+player.weapon.type+'.\n')
                if monster.lootable is True:
                    loot_monster(player,monster)
                tell_story(advance)
                monster_reset(monster) # makes sure that the same monster type can fight another day
                grid[globals.row][globals.col] = '*'
                globals.monsters_killed = globals.monsters_killed+1 #for the stats
                break

        #monster turn
        if monster.lootable is True:
            print ('\n'+monster.name+' attacks with '+monster.weapon.type.lower()+'...')
        else:
            print ('\n'+monster.name+' attacks with '+monster.weapon.name.lower()+'...')

        attack(monster,player)

        if check_dead(player) is True:
            cprint ('\n💀 You died in combat\n','red')
            pause()
            clear_screen()
            if player.luck > 0:
                clear_screen()
                tell_story(saved_by_diety_monster)
                # note that when you pray the monster TYPE doesnt reset so next time you meet it
                # you will have an easier time finishing it off.
                # does NOT work on Xorath
                player.hp = player.initial_hp
                player.luck = 0
                if monster.tier == 98: # Xorath has to be beaten in a fair combat
                    monster_reset(monster)
                tell_story(frozen_in_time)
                tell_story(advance)
            else:
                print ('\n'+monster.name+' '+monster.fatality+'\n\nYour adventure ends here...\n')
                globals.session_end_time = datetime.datetime.now()
                globals.session_duration = globals.session_end_time-globals.session_start_time
                globals.done = True # game over
            break
