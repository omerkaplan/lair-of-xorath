import includes.equipment as equipment

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

kobold = monster('🐸 Kobold',12,10,10,equipment.rusty_spear,equipment.natural_hide,'chops your head and feasts on your corpse.')
giant_spider = monster('🕷 Giant Spider',9,10,10,equipment.bite_attack,equipment.natural_hide,'bites your head off.')
snakefolk = monster('🐍 Snakefolk',12,11,11,equipment.poisoned_spear,equipment.natural_hide,'quickly wraps around you and start crushing. You feel your bones buckle under the pressure.')

monsters = [kobold,giant_spider,snakefolk]
