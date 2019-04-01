from mechanics.combat import roll_die

# equipment classes

class Weapon:
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

class Armor:
    def __init__(self, name, type, tier, ac_bonus, damage_reduction,lootable):
        self.name = name
        self.type = type
        self.tier = tier
        self.ac_bonus = ac_bonus # magical armor will increase your AC
        self.damage_reduction = damage_reduction # magical armor can reduce points of damage
        self.lootable = lootable


class Potion:
    def __init__(self, name , tier,effect_stat ,effect_points):
        self.name = name
        self.tier = tier
        self.effect_stat = effect_stat
        self.effect_points = effect_points



# list of martial weapons

#tier 1 - basic stuff

starter_weapon = Weapon('iron sword','sword',1,1,3,0,0,3,False) #hero only

silver_sword = Weapon('silver sword','sword',1,1,4,0,1,4,True)
rusty_spear = Weapon('rusty spear','spear',1,1,4,0,0,4,True)
heavy_club = Weapon('heavy club','club',1,1,6,0,0,6,True)
long_sword = Weapon('longsword','sword',1,1,6,0,0,6,True)
iron_axe = Weapon('iron axe','axe',1,1,3,0,1,3,True)
morning_star = Weapon('morning star','flail',1,2,3,0,0,6,True)

#tier 2 -
poisoned_spear = Weapon('poisoned spear','spear',2,1,4,1,0,5,True)
flaming_sword = Weapon('flaming sword','sword',2,1,6,0,1,6,True)
rune_sword = Weapon('rune sword','sword',2,1,6,1,1,7,True)
dwarven_handaxe = Weapon('dwarven hand axe','axe',2,1,8,1,0,9,True)
sword_of_arran = Weapon('sword of Arran','sword',2,1,8,1,1,9,True) # Arran is the goddess of Justice

#tier 3 -

youth_drinker = Weapon('The Youth Drinker','sword',98,1,8,0,1,8,False)

# list of natural weapons

bite_attack = Weapon('ferocious bite','natural',1,1,4,0,0,4,False)

# list of hero armors

starter_armor = Armor('iron braces','armor',1,0,0,False)
elven_cape = Armor ('elven cape','armor',1,0,1,True)
elvenkind_hood = Armor ('elvenkind hood','armor',1,0,1,True)
steel_breastplate = Armor ('steel breastplate','armor',1,1,0,True)
steel_helmet = Armor('steel helmet','armor',1,1,0,True)
dwarven_breastplate = Armor('dwarven breastplate','armor',2,2,0,True)
dwarven_helmet = Armor('dwarven helmet','armor',2,0,2,True)
demonhide_gloves = Armor('demonhide gloves','armor',2,1,1,True)
gloves_of_endurance = Armor('gloves of endurance','armor',2,2,1,True)
braces_of_protection = Armor('braces of protection','armor',2,1,2,True)
ring_of_hera = Armor('ring of Hera','ring',3,2,2,True) # Hera is the goddess of Mercy


# list of monster armors

natural_hide = Armor('Monster hide','armor',1,0,0,False)
demon_hide = Armor('Demon hide','armor',1,0,1,False)
rusty_plate = Armor('Rusty plate','armor',1,0,0,False)

# list of potions

potion_health_minor = Potion('Potion of minor healing',1,'hp',5)
potion_health_major = Potion('Potion of major healing',1,'hp',10)
potion_health_super = Potion('Elixir of rejuvination',2,'hp',10)
potion_armor_minor = Potion('Potion of barskin',1,'ac',1)
potion_armor_major = Potion('Potion of stone skin',1,'ac',2)
potion_armor_super = Potion('Elixir of protection',2,'ac',3)
potion_luck_minor = Potion('Potion of minor luck',1,'luck',2)
potion_luck_major = Potion('Potion of major luck',1,'luck',5)


# lists

t1_weapons = [silver_sword,rusty_spear,heavy_club,iron_axe,long_sword,morning_star]

t2_weapons = [poisoned_spear,flaming_sword,rune_sword,dwarven_handaxe,sword_of_arran]

armors = [elven_cape,elvenkind_hood,steel_breastplate,steel_helmet,dwarven_helmet,dwarven_breastplate,demonhide_gloves,gloves_of_endurance,braces_of_protection,ring_of_hera]

potions = [potion_health_minor,potion_health_major,potion_health_super,potion_armor_minor,potion_armor_major,potion_armor_super,potion_luck_minor,potion_luck_major]
