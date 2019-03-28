import includes.equipment as equipment
import random

# the monster class

class Monster:
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

wererat = Monster('Wererat',1,12,10,10,random.choice(equipment.t1_weapons),equipment.natural_hide,True,'chops your head and feasts on your corpse.')
kobold = Monster('Kobold',1,12,10,10,random.choice(equipment.t1_weapons),equipment.natural_hide,True,'drags your corpse to his camp where his tribe will feast upon it for days to come.')
giant_spider = Monster('Giant Spider',1,9,10,10,equipment.bite_attack,equipment.natural_hide,False,'bites your head off.')

# t2 monsters for harder encounter types

lesser_demon = Monster('Lesser Demon',2,13,11,11,equipment.flaming_sword,equipment.demon_hide,True,"drains your life force as you lie on the ground helpless. Xorath's servants claim another victim.")
snakefolk = Monster('Snakefolk',2,12,11,11,equipment.poisoned_spear,equipment.natural_hide,True,'quickly wraps around you and start crushing. You feel your bones buckle under the pressure.')
ghost_armor = Monster('Ghost Armor',2,15,8,8,equipment.rune_sword,equipment.rusty_plate,True,'puts his weapon through your body and after it make sure you are dead, it pays you no mind.')

# xorath

xorath = Monster('Xorath, the enslaver',98,14,15,15,equipment.youth_drinker,equipment.demon_hide,False,'tell story - Xorath kills you')

monsters = [wererat,kobold,giant_spider]
monsters_t2 = [lesser_demon,snakefolk,ghost_armor]
