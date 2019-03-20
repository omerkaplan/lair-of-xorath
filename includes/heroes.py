import includes.equipment as equipment
from mechanics.combat import roll_die


class hero:
    def __init__(self, name, ac,hp,initial_hp,luck,weapon,armor):
        self.name = name
        self.ac = ac
        self.hp = initial_hp
        self.initial_hp = initial_hp
        self.luck = luck
        self.weapon = weapon
        self.armor = armor

my_hero = hero('🤴 Hero',12,10,10,roll_die(2,6),equipment.iron_sword,equipment.starter_armor)
