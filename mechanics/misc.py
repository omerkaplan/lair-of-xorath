from tabulate import tabulate
from includes.generic import clear_screen


def show_stats(player):
    clear_screen()
    table = [["Health Points (HP)",player.hp],["Armor Class (AC)",player.ac],["Luck",player.luck],["Weapon",player.weapon.name],["Armor",player.armor.name]]
    print ('\nYou run a quick check of your health and equipment...\n')
    print (tabulate(table)+'\n')
