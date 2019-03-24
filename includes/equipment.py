from mechanics.combat import roll_die

# equipment classes

class weapon:
    def __init__(self, name, type, tier, damage_die_number, damage_die_sided ,damage_bonus, roll_bonus,max_damage,lootable):
        self.name = name
        self.type = type
        self.tier = tier
        self.damage_die_number = damage_die_number
        self.damage_die_sided = damage_die_sided
        self.damage_bonus = damage_bonus # magical weapons can maybe have an extra roll of damage - roll_die(1,2)
        self.roll_bonus = roll_bonus # +1 on a magical weapon will give a bonus to attack roll
        self.max_damage = max_damage
        self.lootable = lootable

class armor:
    def __init__(self, name, type, tier, ac_bonus, damage_reduction,lootable):
        self.name = name
        self.type = type
        self.tier = tier
        self.ac_bonus = ac_bonus # magical armor will increase your AC
        self.damage_reduction = damage_reduction # magical armor can reduce points of damage
        self.lootable = lootable


class potion:
    def __init__(self, name , tier,effect_stat ,effect_points):
        self.name = name
        self.tier = tier
        self.effect_stat = effect_stat
        self.effect_points = effect_points



# list of martial weapons

#tier 1 - basic stuff

starter_sword = weapon('iron sword','sword',1,1,3,0,0,3,False) #hero only

silver_sword = weapon('silver sword','sword',1,1,4,0,1,4,True)
rusty_spear = weapon('rusty spear','spear',1,1,4,0,0,4,True)
heavy_club = weapon('heavy club','club',1,1,6,0,0,6,True)
long_sword = weapon('longsword','sword',1,1,6,0,0,6,True)
iron_axe = weapon('iron axe','axe',1,1,3,0,1,3,True)
morning_star = weapon('morning star','flail',1,2,3,0,0,6,True)

#tier 2 -
poisoned_spear = weapon('poisoned spear','spear',2,1,4,1,0,5,True)
flaming_sword = weapon('flaming sword','sword',2,1,6,0,1,6,True)

#tier 3 -

youth_drinker = weapon('The Youth Drinker','sword',98,1,8,0,1,8,False)

# list of natural weapons

bite_attack = weapon('ferocious bite','natural',1,1,4,0,0,4,False)

# list of hero armors

starter_armor = armor('iron braces','armor',1,0,0,False)
elven_cape = armor ('elven cape','armor',1,0,1,True)
elvenkind_hood = armor ('elvenkind hood','armor',1,0,1,True)
steel_breastplate = armor ('steel breastplate','armor',1,1,0,True)
steel_helmet = armor ('steel helmet','armor',1,1,0,True)


# list of monster armors

natural_hide = armor('Monster hide','armor',1,0,0,False)
demon_hide = armor('Demon hide','armor',1,0,1,False)

# list of potions

potion_health_minor = potion('Potion of minor healing',1,'hp',5)
potion_health_major = potion('Potion of major healing',1,'hp',10)
potion_health_super = potion('Elixir of rejuvination',2,'hp',10)
potion_armor_minor = potion('Potion of barskin',1,'ac',1)
potion_armor_major = potion('Elixir of protection',2,'ac',2)


# lists

t1_weapons = [silver_sword,rusty_spear,heavy_club,iron_axe,long_sword,morning_star]

t2_weapons = [poisoned_spear,flaming_sword]

armors = [elven_cape]

potions = [potion_health_minor,potion_health_major,potion_health_super,potion_armor_minor,potion_armor_major]
