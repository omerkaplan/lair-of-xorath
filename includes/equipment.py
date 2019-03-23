from mechanics.combat import roll_die

# equipment classes

class weapon:
    def __init__(self, name, type, tier, damage_die_number, damage_die_sided ,damage_bonus, roll_bonus,max_damage,):
        self.name = name
        self.type = type
        self.tier = tier
        self.damage_die_number = damage_die_number
        self.damage_die_sided = damage_die_sided
        self.damage_bonus = damage_bonus # magical weapons can maybe have an extra roll of damage - roll_die(1,2)
        self.roll_bonus = roll_bonus # +1 on a magical weapon will give a bonus to attack roll
        self.max_damage = max_damage

class armor:
    def __init__(self, name, type, tier, ac_bonus, damage_reduction):
        self.name = name
        self.type = type
        self.tier = tier
        self.ac_bonus = ac_bonus # magical armor will increase your AC
        self.damage_reduction = damage_reduction # magical armor can reduce points of damage



# list of martial weapons

#tier 1 - basic stuff

starter_sword = weapon('iron sword','sword',1,1,3,0,0,3) #hero only

silver_sword = weapon('silver sword','sword',1,1,4,0,1,4)
rusty_spear = weapon('rusty spear','spear',1,1,4,0,0,4)
heavy_club = weapon('heavy club','club',1,1,6,0,0,6)
long_sword = weapon('longsword','sword',1,1,6,0,0,6)
iron_axe = weapon('iron axe','axe',1,1,3,0,1,3)
morning_star = weapon('morning star','flail',1,2,3,0,0,6)

t1_weapons = [silver_sword,rusty_spear,heavy_club,iron_axe,long_sword,morning_star]

#tier 2 -
poisoned_spear = weapon('poisoned spear','spear',2,1,4,1,0,5)
flaming_sword = weapon('flaming sword','sword',2,1,6,0,1,6)

#tier 3 -

# list of natural weapons

bite_attack = weapon('ferocious bite','natural',1,1,4,0,0,4)

# list of hero armors

starter_armor = armor('iron braces','armor',1,0,0)

# list of monster armors

natural_hide = armor('Monster hide','armor',1,0,0)
demon_hide = armor('Demon hide','armor',1,0,1)
