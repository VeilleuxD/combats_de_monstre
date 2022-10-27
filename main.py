"""
David A. Veilleux 405
aujourd'hui
une série de combats de monstres générés aléatoirement
amusant
"""

import random
from color import Colors
from time import sleep

def turn(data_game):
    data_game['numero_adversaire'] += 1
    # compteur_boss += 1 (pour une autre étape du projet)
    choix_action = input(f"Oh non! une momie avec une force de {data_game['force']}, vous avez {data_game['niveau_hp']} HP!\n"
                         f"que faites-vous?\npour fuir, écrivez 'fuir'\npour tenter votre chance et rouler votre de"
                         f", écrivez 'de'\npour abandoner, écrivez 'deez'\n-->")
    if choix_action == "fuir":
        print("vous avez fui lol, 1 hp en moins pour avoir fui")
        data_game['niveau_hp'] -= 1
        data_game['force'] = random.randint(1, 5)
        return data_game
    elif choix_action == "deez":
        data_game['abandon'] = True
        print(f"Vous avez abandonné :(")
        return data_game
    elif choix_action == "de":
        print("Vous frappez la momie avec votre sabre...")
        dice_roll = random.randint(1, 6)
        if dice_roll > data_game['force']:
            print(f"La momie tombe raide mort! \nVous gagnez {data_game['force']}HP!\n")
            data_game['niveau_hp'] += data_game['force']
            data_game['victoires'] += 1
        elif dice_roll <= data_game['force']:
            print(f"La momie ne réagit pas. Elle vous attaque\nVous perdez {data_game['force']}HP!\n")
            data_game['niveau_hp'] -= data_game['force']
            data_game['defaites'] += 1

        data_game['force'] = random.randint(1, 5)
        return data_game
    else:
        return turn(data_game)


def logic():
    data_game = {'numero_adversaire': 0, 'victoires':  0, 'defaites': 0, 'niveau_hp': 20, 'force': random.randint(1, 5), 'abandon': False}
    while data_game['niveau_hp'] > 0 and not data_game['abandon']:
        data_game = turn(data_game)

    print(f"Game Over!\nVos victoires: {data_game['victoires']}\nVos défaites: {data_game['defaites']}\nCombats totaux: {data_game['numero_adversaire']}\n"
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
            logic()
            boucle_menu = True
        else:
            boucle_menu = True


menu()
