from mechanics.combat import roll_die

# equipment classes

class weapon:
    def __init__(self, name, type, tier, damage, damage_bonus, roll_bonus):
        self.name = name
        self.type = type
        self.tier = tier
        self.damage = roll_die(1,4)
        self.damage_bonus = damage_bonus # magical weapons can maybe have an extra roll of damage - roll_die(1,2)
        self.roll_bonus = roll_bonus # +1 on a magical weapon will give a bonus to attack roll

class armor:
    def __init__(self, name, type, tier, ac_bonus, damage_reduction):
        self.name = name
        self.type = type
        self.tier = tier
        self.ac_bonus = ac_bonus # magical armor will increase your AC
        self.damage_reduction = damage_reduction # magical armor can reduce points of damage



# list of martial weapons

iron_sword = weapon('iron sword','sword',1,roll_die(1,4),0,1)
rusty_spear = weapon('rusty spear','spear',1,roll_die(1,4),0,0)
poisoned_spear = weapon('poisoned spear','spear',1,roll_die(1,4),1,0)

# list of natural

bite_attack = weapon('ferocious bite','natural',1,roll_die(1,4),0,0)

# list of hero armors

starter_armor = armor('iron braces','armor',1,0,0)

# list of monster armors

natural_hide = armor('Monster hide','armor',1,0,0)
