### A tic tc toe game built for our ENAC's project
import sys
import tic_tac_toe as ttt
import jouer




if __name__ == '__main__':
    #n = int(sys.argv[1])
    #m = int(sys.argv[2])
    #nb_player = int(sys.argv[3]) # pour le moment, uniquement deux joueurs
    #k = int(sys.argv[4])

    n,m = int(input("Choisir n")), int(input("Choisir m"))
    k = int(input("Choisir le nombre de case à aligner pour gagner k :"))
    nb_player = int(2)
    
    jeu = ttt.TTT(n, m, nb_player, k)
    jouer.jouer_IA_vs_IA(jeu)



'''       TODO
      Se renseigner sur le sujet : itérative deepening -> fait
#       Pour l'heuristique : 
          - tester différentes profondeur (jusqu'à p5) --> algo naif OK

          - joueur uniquement les cases continues à celles déjà jouées --> on empêche l'autre de gagner OK
          - Tester nos heuristiques les unes contres les autres OK ==> Align bien meilleure
          - Essayer de battre notre IA en 4x4 et 5x5 OK -> malheureusement fait


#       Pour l'IA : 
        Si 3 joueurs : 1 IA vs 2 humains ( min min max), deux joueurs qui s'allient pour nous faire perdre, comme deux coups à la place d'un coup
                  --> Tester avec différentes grilles (5x5 max) 
                  --> Tester grille rectangle (mais pour les stats utiliser une grille carrée)

#       Pour Interface graphique :
          - joueur avec la souris : cliquer sur case etc... (objectif final)'''


