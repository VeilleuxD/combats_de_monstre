"""
David A. Veilleux 405
aujourd'hui
une série de combats de monstres générés aléatoirement
amusant
"""

import random
from color import Colors
from time import sleep

def fight():
    niveau_hp = random.randint(15, 25)


def menu():
    boucle_menu = True
    player_hp = 20

    while boucle_menu:
        print(Colors.CYAN + Colors.BOLD + "Combat de Monstres\n\n\n")
        sleep(1)
        print(Colors.LIGHT_GREEN + Colors.ITALIC + "Pour commencer, écrivez 'start'")
        sleep(0.5)
        print(Colors.YELLOW + Colors.ITALIC + "\n\nPour lire les règles, écrivez 'rules'\n\n")
        sleep(0.5)
        print(Colors.LIGHT_RED + Colors.ITALIC + "Pour quitter, écrivez 'leave'\n")
        sleep(0.5)
        game_menu = input(Colors.CYAN + Colors.BOLD + "--->")

        if game_menu == 'rules':
            print("Please read later")
            boucle_menu = True
        elif game_menu == 'leave':
            print("Au revoir!")
            boucle_menu = False
        elif game_menu == 'start':
            print("Oh non, un monstre!")
            boucle_menu = True
        else:
            boucle_menu = True


menu()
