import includes.equipment as equipment
import random

# the monster class

class monster:
    def __init__(self, name, ac,hp,initial_hp,weapon,armor,fatality):
        self.name = name
        self.ac = ac
        self.hp = initial_hp
        self.initial_hp = initial_hp
        self.weapon = weapon
        self.armor = armor
        self.fatality = fatality


# list of monsters and thier stats

wererat = monster('Wererat',12,10,10,random.choice(equipment.t1_weapons),equipment.natural_hide,'chops your head and feasts on your corpse.')
kobold = monster('Kobold',12,10,10,random.choice(equipment.t1_weapons),equipment.natural_hide,'drags your corpse to his camp where this tribe will feast upon it for days to come.')
giant_spider = monster('Giant Spider',9,10,10,equipment.bite_attack,equipment.natural_hide,'bites your head off.')
snakefolk = monster('Snakefolk',12,11,11,equipment.poisoned_spear,equipment.natural_hide,'quickly wraps around you and start crushing. You feel your bones buckle under the pressure.')

monsters = [wererat,giant_spider,snakefolk,kobold]
