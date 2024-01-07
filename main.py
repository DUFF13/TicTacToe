### A tic tc toe game built for our ENAC's project
import sys
import tic_tac_toe as ttt
import jouer


choose = """
1. Player vs Player (2 or 3 player)
2. Player vs AI (minimax and choose your heuristic or Monte Carlo)
3. AI vs AI
"""



if __name__ == '__main__':
    print('Welcome to our MNK game')



    choose_game = int(input(choose))
    if choose_game == 1:
        n, m = int(input("choose m the number of rows (by default : 3)") or '3'), int(input("Choose n the number of columns (by default : 3)") or '3') # j'ai inversé car le jeu s'appelle mnk et non nmk ...
        k = int(input("Choose k (by default : 3)") or '3')
        nb_player = int(input("2 or 3 players (by default 2)"))
        jeu = ttt.TTT(n, m, nb_player, k)

        jouer.jouer_partie(jeu)

    elif choose_game == 2:
        n, m = int(input("choose m the number of rows (by default : 3)") or '3'), int(input("Choose n the number of columns (by default : 3)") or '3') # j'ai inversé car le jeu s'appelle mnk et non nmk ...
        k = int(input("Choose k (by default : 3)") or '3')
        jeu = ttt.TTT(n, m, 2, k)

        AI = int(input('Which AI do you want to try ? : (1 for Minimax, 2 for Minimax with iterativ deepening, 3 for MonteCarlo)'))
        if AI == 3:
            jouer.jouer_partie_monte_carlo(jeu)
        else:
            jouer.jouer_partie_IA(jeu, AI)


    elif choose_game == 3:
        n, m = int(input("choose m the number of rows (by default : 3)") or '3'), int(input("Choose n the number of columns (by default : 3)") or '3') # j'ai inversé car le jeu s'appelle mnk et non nmk ...
        k = int(input("Choose k (by default : 3)") or '3')
        jeu = ttt.TTT(n, m, 2, k)
        print("For the moment only minimax with iterativ deepening against minimax")
        jouer.jouer_IA_vs_IA(jeu)







'''       TODO
      Se renseigner sur le sujet : itérative deepening -> fait
#       Pour l'heuristique : 
          - tester différentes profondeur (jusqu'à p5) --> algo naif OK

          - joueur uniquement les cases continues à celles déjà jouées --> on empêche l'autre de gagner OK
          - Tester nos heuristiques les unes contres les autres OK ==> Align bien meilleure
          - Essayer de battre notre IA en 4x4 et 5x5 OK -> malheureusement fait, maintenant c'est bon normalement, pas possible de win


#        algorithme probabiliste -> monte carlo (termine mais pas forcément correct) et peut-être las vegas si je trouve des idées (l'inverse)

#       Pour l'IA : 
        Si 3 joueurs : 1 IA vs 2 humains ( min min max), deux joueurs qui s'allient pour nous faire perdre, comme deux coups à la place d'un coup
                  --> Tester avec différentes grilles (5x5 max) 
                  --> Tester grille rectangle (mais pour les stats utiliser une grille carrée)

#       Pour Interface graphique :
          - joueur avec la souris : cliquer sur case etc... (objectif final)'''


