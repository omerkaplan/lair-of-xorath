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
giant_spider = monster('🕷 Giant Spider',16,5,5,equipment.bite_attack,equipment.natural_hide,'bites your head off.')

monsters = [kobold,giant_spider]
