from tabulate import tabulate
from includes.generic import clear_screen
import includes.globals
from includes.equipment import *
from includes.world import * # get the world map
import random
import numpy




def show_stats(player):
    clear_screen()
    table = [["Health Points (HP)",player.hp],["Armor Class (AC)",player.ac],["Luck",player.luck],["Weapon",player.weapon.name],["Armor",player.armor.name]]
    print ('\nYou run a quick check of your health and equipment...\n')
    print (tabulate(table)+'\n')

def loot(player):

    # compile a list of available loot

    loot_lists = []
    lootable_weapons = []
    lootable_armor = []
    lootable_potions = []
    for item in t1_weapons:
        if item.lootable is True:
            lootable_weapons.append(item)
    for item in t2_weapons:
        if item.lootable is True:
            lootable_weapons.append(item)
    for item in armors:
        if item.lootable is True:
            lootable_armor.append(item)
    for item in potions:
        lootable_potions.append(item)

    loot_lists.append(lootable_weapons)
    loot_lists.append(lootable_armor)
    loot_lists.append(lootable_potions)
    random_category = numpy.random.choice(loot_lists, p=[0.05, 0.35, 0.6]) #biased towards armor and potions since weapons we usually get from battle
    loot = random.choice(random_category) #gets the actual item from the list

    # now that we have loot, let's evaluate it

    if isinstance(loot, potion): #if this is a potion, drink it
        print ('\nYou find a vial filled with liquid and recognize it as '+loot.name+'. You drink the potion.\n')
        def drink_potion(stat,value,potion_tier):
            player.__dict__[stat] = player.__dict__[stat]+value
            if stat == 'hp':
                print ('The liquid taste like fruit and herbs and you can feel your body find some relief (🧪 Gained ' +str(value)+str(stat.upper())+')\n')
                if potion_tier is 1:
                    if player.hp > player.initial_hp:
                        player.hp = player.initial_hp # since we dont want extra HP on regular potions
            elif stat == 'ac':
                print ('The potion taste like mushrooms, earth and spices. You can feel your skin hardens (🧪 Gained '+str(value)+str(stat.upper())+')\n')
            elif stat == 'luck':
                print ("The potion taste sweet and has a calming effect on your body.\nYou feel optimistic about your future - maybe you'll make it out alive after all! (🧪 Gained "+str(value)+str(stat.upper())+')\n')


        drink_potion(loot.effect_stat,loot.effect_points,loot.tier)

    elif isinstance(loot, weapon): #if it's a weapon, evaluate it
        print ('\nFound: '+loot.name+'!\n')
        if loot.max_damage > player.weapon.max_damage:
            print ('This looks like a fine weapon that will surely aid you in your quest!\n\nYou pick it up and leave your '+player.weapon.name+' behind.')
            player.weapon = loot
        elif loot.max_damage < player.weapon.max_damage:
            print ('It looks like it would not bring you much value at its current condition, you leave it behind.')
        elif loot.max_damage == player.weapon.max_damage: #we need to evaluate roll bonus
            if loot.roll_bonus > player.weapon.roll_bonus:
                print ('This looks like a fine weapon that will surely aid you in your quest!\n\nYou pick it up and leave your '+player.weapon.name+' behind.')
                player.weapon = loot
            elif loot.roll_bonus < player.weapon.roll_bonus:
                print ('It looks like it would not bring you much value at its current condition, you leave it behind.')
            elif loot.roll_bonus == player.weapon.roll_bonus:
                print ('The weapon looks in good condition but you are better practiced with your '+player.weapon.name+'. You leave it behind')

    elif isinstance(loot, armor): #if it's an armor, evaluate it
        print ('\nFound: '+loot.name+'!\n')
        if loot.ac_bonus > player.armor.ac_bonus:
            print ('This looks like a fine armor that will surely aid you in your quest!\n\nYou pick it up and leave your '+player.armor.name+' behind.')
            player.armor = loot
        elif loot.ac_bonus < player.armor.ac_bonus:
            print ('It looks like it would not bring you much value at its current condition, you leave it behind.')
        elif loot.ac_bonus == player.armor.ac_bonus: #lets evaluate damage reduction
            if loot.damage_reduction > player.armor.damage_reduction:
                print ('This looks like a fine armor that will surely aid you in your quest!\n\nYou pick it up and leave your '+player.armor.name+' behind.')
                player.armor = loot
            elif loot.damage_reduction < player.armor.damage_reduction:
                print ('It looks like it would not bring you much value at its current condition, you leave it behind.')
            elif loot.damage_reduction == player.armor.damage_reduction:
                print ('The '+loot.name+' looks in good condition but you feel more comfortable with your '+player.armor.name+' and decide to keep it.')

    else:
        print ('Error getting loot :(')

    # burn the room so we cant exploit the encounter
    grid[includes.globals.row][includes.globals.col] = '$'
