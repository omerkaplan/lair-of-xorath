import random

def tell_story(segment):
    text = random.choice(segment)
    print (text)


exposition = [".:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:._.\n\n\nYou stand before the entrance to the lair of Xorath, a demon from the depths of the fire plains who made\nit his home decades ago next to the peaceful village of Hillsbard, your birthplace.\n\nFor the so called 'protection' of Hillsbard Xorath demanded one thing - the firstborn of every family at his or \nher's 18th birthday as a tribute. The people of Hillsbard unwillingly complied.\n\nMany brave women and men, champions and commoners alike, tried to set on a journey to slay the demon - none returned.\n\n.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:._.\n "]

running_away = ["\n\nTo the south, you see a dim moon light pouring through the gate in which you came into Xorath's lair.\n\nRunning away will be your demise as the townsfolk has no choice but offering you to the demon as tribute.\n"]

exploring = [
'\n\nYou go deeper into the lair, passing along hallways and spaces.\nThe space seems to be twisting and turning\n',
'\n\nYou walk carefully through several passages, going into a larger space.\nYou can barely make out your surrounding and you vision becomes limited\n',
'\n\nThe path forward seems to last forever, going through smaller and larger spaces.\nOne could easily get lost or get mad in those tight halls\n',
'\n\nYou walk for several minutes until you reach another space, you examine your surroundings\n'
]

resting = [
'\nThis area seems good enough to stop and rest. You set down on the ground and eat one of your rations\nThe taste reminds you of home and you feel much better.\n',
'\nYou stop in an area that seems safe enough to catch your breath.\nIt has been quite the journey so far and you take a moment to rest and reflect.\n',
]

visited_rest_site = ["\nYou go through your previous rest site. Everything looks undisturbed and you decide to move forward.\n"]

advance = [
'\nYou consider your next move...\n',
'\nNo time to waste, time to move on...\n',
'\nYou venture forth...\n',
'\nTime to advance...\n',
'\nYour destiny awaits, time to move...\n',
'\nTime to move...\n',
'\nYou look around, considering your next move...\n',
'\nYour mind is focused, ready for what is ahead...\n'
]

trap_avoided = [
'\n\nYou notice a pressure plate on the floor and carefully mark it with some rocks. You can only imagine what\nwould have happened if one would be unfortunate to step on it.\n'
]

trap_triggered = [
'\nYou move as carefully as you can, holding the torch tight. Suddenly, you feel your boot sinking ever so\nslightly into the floor. A pressure plate!',
'\nThe lair is dark and you cross a small overhead pass on your way forward. You notice small string attahced\nto the floor a second too late. A trap!'
]

springed_trap = ["\nYou went through a room with a springed trap. You been here before.\n\nAfter double checking for additional traps you move forward\n"]

saved_by_diety_monster = [".:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:._.\n\n\nAs the monster lands its final blow, your world fades to white.\n\nWhen you open your eyes, or at least you think that is what you did, you find yourself in\nan unfamilar place - you are everywhere and you are nowhere.\n\n\"I have been following you mortal\" says a voice in the distance. \n\n\"Know that I am Hera, the diety of mercy and I have chosen to aid you in your quest\"\n\n\"When you wake up I will grant you safe passage. Gather your strength and end the blight that plagues your world!\"\n\nEndless colors fills your view and your world spins\n\n\n.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:._.\n "]

frozen_in_time = ['\nYou are in the room where you were struck down. The monster seems to be gone but you better hurry up and leave.\n']

loot_room = ["\nYou keep moving through some tight spaces and your eye catches something glittering.\nA closer look reveals a stash hidden inside the wall. You dig through the various items...\n",
"\nAll of a sudden, your arm bumps against something hard. You turn your head and see a wooden drawer built in the wall!\nYou open it and start rvaging through the various items...\n"
]

looted_treasure = ["\nYou walk past a pile of rubble and equipment you went through before. A quick search does\'t come up with anything new.\n"]

lair_entrance = ["\nYou stand at the entrance to Xorath's lair, it seems like you went in just minutes ago? Or was it hours?\n",
"\nYou stand at the entrance to Xorath's lair. As bleek and awe inspiring as you remember it coming in\n"
]

slain_monster = ["\nYou go past a corpse of a monster you recently slain. It is barely recognizable\nand being devored by insects and other lair dwellers\n"]

xorath_room = [".:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:._.\n\n\nYou reach a large opening in the lair, lit with dim trochlight. At the end of this grand space \nis a black throne surrounded by a pile of human bones.\n\nXoarth, the enslaver is sitting on the throne."]

xorath_taunt =["\"You are here at last, human.\", Xorath\'s voice is booming through the throne room.\n\n\"Run away now and leave with your life.\"\n\n.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:._.\n"]

xorath_dies =[".:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:._.\n\n\nAs you lift up your weapon and land the final blow though the demon's skull, a sense of relief spreads through your body.\n\nYou have slain Xorath the enslaver and liberated the people of Hillsbard from his opression for generations to come.\n\nOther demons or dangers may once again threten your birth place but tonight...\n\nTonight we celebrate.\n\n\n.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:._.\n"]

def monster_encounter(monster):
    list = [
    'A '+monster.name+' jumps from the shadows, YOU MUST FIGHT!',
    'You run head on into a '+monster.name+' and his '+monster.weapon.type+" - It's a fight to the death!",
    'A '+monster.name+' notices you cresting the corner. YOU MUST FIGHT!',
    "From the darkness ahead you see a "+monster.name+". You ready your weapon..."
    ]
    text = random.choice(list)
    print (text)
