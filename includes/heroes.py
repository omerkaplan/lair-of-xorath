import includes.equipment
from mechanics.combat import roll_die
import pickle


class Hero:
    def __init__(self, name, ac,hp,initial_hp,luck,weapon,armor):
        self.name = name
        self.ac = ac
        self.hp = hp
        self.initial_hp = initial_hp
        self.luck = luck
        self.weapon = weapon
        self.armor = armor

    def reset(self):
        self.weapon = includes.equipment.starter_weapon
        self.armor = includes.equipment.starter_armor

my_hero = Hero('hero',12,15,15,roll_die(2,6),includes.equipment.starter_weapon,includes.equipment.starter_armor)
