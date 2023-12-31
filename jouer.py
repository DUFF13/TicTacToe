import sys
import tic_tac_toe as ttt

def jouer_partie_IA(jeu : ttt.TTT):
    ''' jouer une partie contre l'IA en 1v1'''
    print("Vous jouez contre l'IA. Voici la grille de jeu :\n")
    print(jeu)  # Affichage de la grille de jeu initiale

    joueur = int(input("Choisir : l'humain commence (1) | l'IA commence (2)"))
    

    while (joueur != 0 and not(jeu.gagnant(1)) and not(jeu.gagnant(2))):
        if joueur == 1:
            print("\nTour du joueur humain.")
            try:
                lgn = int(input("Entrez le numéro de ligne (0 à {}): ".format(jeu.n - 1)))
                cln = int(input("Entrez le numéro de colonne (0 à {}): ".format(jeu.m - 1)))
                jeu.play_move(lgn, cln)
                
            except (ValueError, IndexError, ttt.InvalidMoveError):
                print("Coup invalide. Veuillez réessayer.")
                continue
        else:
            print("\nTour de l'IA.")
            meilleur_coup = None
            meilleur_valeur = -sys.maxsize
            for lgn in range(jeu.n):
                for cln in range(jeu.m):
                    if jeu.grid[lgn][cln] == 0:
                        jeu.grid[lgn][cln] = 2
                        valeur = jeu.min_max(3, -sys.maxsize, sys.maxsize, 2)  # Profondeur à adapter ici 3
                        jeu.grid[lgn][cln] = 0

                        if valeur > meilleur_valeur:
                            meilleur_valeur = valeur
                            meilleur_coup = (lgn, cln)

            # if meilleur_coup:
            jeu.play_move(meilleur_coup[0], meilleur_coup[1])
                
        joueur = jeu.next_player() # Passage au joueur suivant
        print(jeu)  # Affichage de la grille après le coup
        

    if jeu.gagnant(1):
        print("\nLe joueur humain a gagné !")
    elif jeu.gagnant(2):
        print("\nL'IA a gagné !")
    else:
        print("\nMatch nul !")


def jouer_IA_vs_IA(jeu : ttt.TTT):
    ''' faire jouer 2 IA l'une contre l'autre'''
    print(" H_vide (J1) VS H_align (J2). Voici la grille de jeu :\n")
    print(jeu)  
    player = 1
    
    while (player != 0 and not(jeu.gagnant(1)) and not(jeu.gagnant(2))):
        if player == 1:
            print("\nTour du joueur 1.")
            meilleur_coup = None
            meilleur_valeur = -sys.maxsize
            for lgn in range(jeu.n):
                for cln in range(jeu.m):
                    if jeu.grid[lgn][cln] == 0:
                        jeu.grid[lgn][cln] = 2
                        valeur = jeu.min_max_align(2, -sys.maxsize, sys.maxsize, 2 )  # Profondeur à adapter ici 3
                        jeu.grid[lgn][cln] = 0

                        if valeur > meilleur_valeur:
                            meilleur_valeur = valeur
                            meilleur_coup = (lgn, cln)

            if meilleur_coup != None :
                jeu.play_move(meilleur_coup[0], meilleur_coup[1])
            else :
                break
            
        else:
            print("\nTour du joueur 2.")
            meilleur_coup = None
            meilleur_valeur = -sys.maxsize
            for lgn in range(jeu.n):
                for cln in range(jeu.m):
                    if jeu.grid[lgn][cln] == 0:
                        jeu.grid[lgn][cln] = 2
                        valeur = jeu.min_max_vide(2, -sys.maxsize, sys.maxsize, 2)  # Profondeur à adapter ici 3
                        jeu.grid[lgn][cln] = 0

                        if valeur > meilleur_valeur:
                            meilleur_valeur = valeur
                            meilleur_coup = (lgn, cln)

            if meilleur_coup != None :
                jeu.play_move(meilleur_coup[0], meilleur_coup[1])
            else :
                break
                
        player = jeu.next_player() # Passage au joueur suivant
        print(jeu)  # Affichage de la grille après le coup
        

    if jeu.gagnant(1):
        print("\nLe H_vide a gagné !")
    elif jeu.gagnant(2):
        print("\nLe H_align a gagné !")
    else:
        print("\nMatch nul !")

