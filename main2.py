### A tic tc toe game built for our ENAC's project
import sys
import tic_tac_toe as ttt
import jouer
import interface_graphique as ig
from tkinter import *



def main(n,m,nb_player,k):
    #n = int(sys.argv[1])
    #m = int(sys.argv[2])
    #nb_player = int(sys.argv[3]) # pour le moment, uniquement deux joueurs
    #k = int(sys.argv[4])

        
    #Création d'une instance de la classe TTT
    
    game = ttt.TTT(n, m, nb_player, k)

    # Création de la fenêtre principale
    window = Tk()
    #Personnalisation de la fenêtre
    window.title( "Morpion ")
    window.geometry("1080x720")
    window.minsize(500,500)
    window.iconbitmap("tic-tac-toe.ico")
    window.config(background='#FFFBD6')

    # Création de l'interface graphique 
    interface = ig.IG(window, game)
    interface.setup_interface()

    #lancement du jeu
    window.mainloop()
    

# Verification 
if __name__ =="__main__":
    n = int(input("Choisir n"))
    m = int(input("Choisir m"))
    k = int(input("Choisir le nombre de case à aligner pour gagner k :"))
    nb_player = int(2)
    main(n,m,nb_player,k)




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

