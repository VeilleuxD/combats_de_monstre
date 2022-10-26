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
    numero_adversaire = 0
    compteur_boss = 0
    victoires = 0
    defaites = 0
    niveau_hp = random.randint(15, 25)
    while niveau_hp > 0:
        force_adversaire = random.randint(1, 5)
        numero_adversaire += 1
        compteur_boss += 1
        choix_action = input(f"Oh non! une momie avec une force de {force_adversaire}, vous avez {niveau_hp} HP!\n"
                             f"que faites-vous?\npour fuir, écrivez 'fuir'\npour tenter votre chance et rouler votre dé,"
                             f"écrivez 'dé'\npour abandoner, écrivez 'deez'\n-->")
        if choix_action == "fuir":
            print("vous avez fui lol")
            niveau_hp -= 1
        elif choix_action == "deez":
            niveau_hp = 0
            print(f"Vous avez abandonné :(")
    print(f"Vos victoire: {victoires}\nVos défaites: {defaites}\nCombats totaux: {numero_adversaire}\n"
          f"Votre swag: {random.randint(1, 10)}/10")


def menu():
    """
    le menu du jeux
    :return:
    """
    boucle_menu = True
    player_hp = 20

    while boucle_menu:
        print(Colors.CYAN + Colors.BOLD + "Combat de Monstres\n\n\n")
        print(Colors.LIGHT_GREEN + Colors.ITALIC + "Pour commencer, écrivez 'start'")
        print(Colors.YELLOW + Colors.ITALIC + "\n\nPour lire les règles, écrivez 'rules'\n\n")
        print(Colors.LIGHT_RED + Colors.ITALIC + "Pour quitter, écrivez 'leave'\n")
        game_menu = input(Colors.CYAN + Colors.BOLD + "--->")

        if game_menu == 'rules':
            print("BIENVENUE DANS LA PYRAMIDE M-OSH\nVous êtes un explorateur à la ''Indiana Jones'' cherchant "
                  "un trésor\ndissimulé dans la pyramide.\nPAR CONTRE, la place est infestée de momies. Oups!\n"
                  "L’usager peut tomber face à face avec une momie.\nDans ce cas, l’usager peut "
                  "contourner le monstre et aller quelque part d'autre.\nCette manœuvre coûte 1 point de vie."
                  "L’usager perd le combat si son total aux dés est inférieur (ou égal) à la force du monstre.\n "
                  "Dans ce cas l’usager perdra autant de points de vie que la force du monstre affronté.\n"
                  "le joueur peut décider de rouler un dé a 6 faces pour combattre le monstre")

            boucle_menu = True
        elif game_menu == 'leave':
            print("Au revoir!")
            boucle_menu = False
        elif game_menu == 'start':
            print("Vous rentrez dans la pyramide de M-OSH...\n\n")
            fight()
            boucle_menu = True
        else:
            boucle_menu = True


menu()
