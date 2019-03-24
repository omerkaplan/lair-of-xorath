import includes.equipment as equipment
import random

# the monster class

class monster:
    def __init__(self, name, tier, ac, hp, initial_hp, weapon, armor, lootable, fatality):
        self.name = name
        self.tier = tier
        self.ac = ac
        self.hp = initial_hp
        self.initial_hp = initial_hp
        self.weapon = weapon
        self.armor = armor
        self.lootable = lootable
        self.fatality = fatality


# list of monsters and thier stats

wererat = monster('Wererat',1,12,10,10,random.choice(equipment.t1_weapons),equipment.natural_hide,True,'chops your head and feasts on your corpse.')
kobold = monster('Kobold',1,12,10,10,random.choice(equipment.t1_weapons),equipment.natural_hide,True,'drags your corpse to his camp where this tribe will feast upon it for days to come.')
giant_spider = monster('Giant Spider',1,9,10,10,equipment.bite_attack,equipment.natural_hide,False,'bites your head off.')

# t2 monsters for harder encounter types

lesser_demon = monster('Lesser Demon',2,13,11,11,equipment.flaming_sword,equipment.demon_hide,True,'tell story - demon kills you')
snakefolk = monster('Snakefolk',1,12,11,11,equipment.poisoned_spear,equipment.natural_hide,True,'quickly wraps around you and start crushing. You feel your bones buckle under the pressure.')

# xorath

xorath = monster('Xorath, the enslaver',98,16,20,20,equipment.youth_drinker,equipment.demon_hide,False,'tell story - Xorath kills you')

monsters = [wererat,kobold]
monsters_t2 = [lesser_demon,snakefolk]
