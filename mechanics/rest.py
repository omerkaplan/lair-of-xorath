from mechanics.combat import roll_die

def rest(player):
    roll = roll_die(1,6)
    player.hp = player.hp+roll
    if player.hp > player.initial_hp:
        player.hp = player.initial_hp # You can't regain HP over your initial amount
        print ('\nYou feel refreshed\n')
    else:
        print ('\nRegained '+str(roll)+'HP\n')
