import random

def tell_story(segment):
    text = random.choice(segment)
    print (text)


exposition = [".:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:._.\n\n\nYou stand before the entrance to the lair of Xorath, a demon from the depths of the fire plains who made\nit his home decades ago next to the peaceful village of Hillsbard, your birthplace.\n\nFor the so called 'protection' of Hillsbard Xorath demanded one thing - the firstborn of every family at his or \nher's 18th birthday as a tribute. The people of Hillsbard unwillingly complied.\n\nMany brave women and men, champions and commoners alike, tried to set on a journey to slay the demon - none returned.\n\n.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:._.\n "]

exploring = [
'\nYou go deeper into the lair, passing along hallways and spaces.\nThe space seems to be twisting and turning\n',
'\nYou walk carefully through several passages, going into a larger space.\nYou can barely make out your surrounding and you vision becomes limited\n',
'\nThe path forward seems to last forever, going through smaller and larger spaces.\nOne could easily get lost or get mad in those tight halls\n',
'\nYou walk for several minutes until you reach another space, you examine your surroundings\n'
]

resting = [
'\nYou rest to pick up strength...\n'
]

advance = [
'\nYou consider your next move...\n',
'\nNo time to waste, time to move on...\n',
'\nYou venture forth...\n',
'\nTime to advance...\n',
'\nYour destiny awaits, time to move...\n'
]

trap_avoided = [
'\n\nYou notice a pressure plate on the floor and carefully mark it with some rocks. You can only imagine what\nwould have happened if one would be unfortunate to step on it.\n'
]

trap_triggered = [
'\nYou move as carefully as you can, holding the torch tight. Suddenly, you feel your boot sinking ever so\nslightly into the floor. A pressure plate!',
'\nThe lair is dark and you cross a small overhead pass on your way forward. You notice small string attahced\nto the floor a second too late. A trap!'
]

def monster_encounter(monster):
    list = [
    'A '+monster.name+' appears!',
    'You must fight a '+monster.name+' and his '+monster.weapon.name
    ]
    text = random.choice(list)
    print (text)
