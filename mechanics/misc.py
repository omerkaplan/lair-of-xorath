from tabulate import tabulate
from includes.generic import clear_screen
from includes.equipment import *
import random



def show_stats(player):
    clear_screen()
    table = [["Health Points (HP)",player.hp],["Armor Class (AC)",player.ac],["Luck",player.luck],["Weapon",player.weapon.name],["Armor",player.armor.name]]
    print ('\nYou run a quick check of your health and equipment...\n')
    print (tabulate(table)+'\n')

def loot(player):
    loot = random.choice(potions)
    if isinstance(loot, potion): #if this is a potion
        print ('\nYou find '+loot.name+' and drink it.\n')
        def drink_potion(stat,value,potion_tier):
            player.__dict__[stat] = player.__dict__[stat]+value
            if stat == 'hp':
                print ('The potion taste sweet and you can feel healier (🧪 Gained ' +str(value)+str(stat.upper())+')\n')
                if potion_tier is 1:
                    if player.hp > player.initial_hp:
                        player.hp = player.initial_hp # since we dont want extra HP on regular potions
            elif stat == 'ac':
                print ('The potion taste slightly bitter and you can feel your skin hardens (🧪 Gained '+str(value)+str(stat.upper())+')\n')

        drink_potion(loot.effect_stat,loot.effect_points,loot.tier)

    else:
        print ('not a potion')
