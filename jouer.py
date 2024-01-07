import sys
import tic_tac_toe as ttt
import exception
import time

def jouer_partie(jeu : ttt.TTT):
    ''' jouer une partie en 1v1 sans IA'''

    if jeu.nb_player == 2:
        joueur = 1
        print(jeu)
        while (joueur != 0 and not(jeu.gagnant(1) or jeu.gagnant(2))):
            if joueur == 1:
                print("c'est au joueur 1 de jouer")
                lgn = int(input("Entrez le numéro de ligne (0 à {}): ".format(jeu.n - 1)))
                cln = int(input("Entrez le numéro de colonne (0 à {}): ".format(jeu.m - 1)))
                if (cln < 0 or cln > jeu.m or lgn < 0 or lgn > jeu.n):
                    print("ces coordonnées ne sont pas possibles")
                else:
                    jeu.play_move(lgn, cln)
            else:
                print("c'est au joueur 2 de jouer")
                lgn = int(input("Entrez le numéro de ligne (0 à {}): ".format(jeu.n - 1)))
                cln = int(input("Entrez le numéro de colonne (0 à {}): ".format(jeu.m - 1)))
                if (cln < 0 or cln > jeu.m or lgn < 0 or lgn > jeu.n):
                    print("ces coordonnées ne sont pas possibles")
                else:
                    jeu.play_move(lgn, cln)

            if joueur % 2 == 0:
                joueur = 1
            else:
                joueur = 2
            print(jeu)
        if jeu.gagnant(1):
            print("Le joueur 1 a gagné")
        elif jeu.gagnant(2):
            print("le joueur 2 a gagné")
        else:
            print("Match nul")
    
    elif jeu.nb_player == 3:
        joueur = 1
        print(jeu)
        while(joueur != 0 and not(jeu.gagnant(1) or jeu.gagnant(2) or jeu.gagnant(3))):
            if joueur == 1:
                print("c'est au joueur 1 de jouer")
                try:
                    lgn = int(input("Entrez le numéro de ligne (0 à {}): ".format(jeu.n - 1)))
                    cln = int(input("Entrez le numéro de colonne (0 à {}): ".format(jeu.m - 1)))
                    jeu.play_move(lgn, cln)
                    
                except (ValueError, IndexError, exception.InvalidMoveError):
                    print("Coup invalide. Veuillez réessayer.")
                    continue

            elif joueur == 2:
                print("c'est au joueur 2 de jouer")
                try:
                    lgn = int(input("Entrez le numéro de ligne (0 à {}): ".format(jeu.n - 1)))
                    cln = int(input("Entrez le numéro de colonne (0 à {}): ".format(jeu.m - 1)))
                    jeu.play_move(lgn, cln)
                    
                except (ValueError, IndexError, exception.InvalidMoveError):
                    print("Coup invalide. Veuillez réessayer.")
                    continue
            else:
                print("c'est au joueur 3 de jouer")
                try:
                    lgn = int(input("Entrez le numéro de ligne (0 à {}): ".format(jeu.n - 1)))
                    cln = int(input("Entrez le numéro de colonne (0 à {}): ".format(jeu.m - 1)))
                    jeu.play_move(lgn, cln)
                    
                except (ValueError, IndexError, exception.InvalidMoveError):
                    print("Coup invalide. Veuillez réessayer.")
                    continue

            if joueur != 3:
                joueur += 1
            else:
                joueur = 1

            print(jeu)
        if jeu.gagnant(1):
            print("Le joueur 1 a gagné")
        elif jeu.gagnant(2):
            print("le joueur 2 a gagné")
        elif jeu.gagnant(3):
            print("le joueur 3 a gagné")
        else:
            print("Match nul")



def jouer_partie_IA(jeu : ttt.TTT, heuristic):
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
                
            except (ValueError, IndexError, exception.InvalidMoveError):
                print("Coup invalide. Veuillez réessayer.")
                continue
        else: # dans cette version, l'IA est toujours le joueur max, i.e elle commence jamais
            start = time.time()
            print("\nTour de l'IA.")
            meilleur_coup = jeu.random_ai()
            meilleur_valeur = float('-inf')
            for lgn in range(jeu.n):
                for cln in range(jeu.m):
                    if jeu.grid[lgn][cln] == 0:
                        jeu.grid[lgn][cln] = 2
                        if heuristic == 1:
                            valeur = jeu.min_max_align(3, float('-inf'), float('inf'), joueur)  # Profondeur à adapter ici 3
                        elif heuristic == 2:
                            valeur = jeu.min_max_IterativDeepening(3, float('-inf'), float('inf'), joueur)  # Profondeur à adapter ici 3
                        jeu.grid[lgn][cln] = 0


                        if valeur > meilleur_valeur:
                            meilleur_valeur = valeur
                            meilleur_coup = (lgn, cln)

            jeu.play_move(meilleur_coup[0], meilleur_coup[1])
            print("durée du coup : " + str(time.time() - start))
                
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
    joueur = 1
    premier_coup = True
    
    while (jeu.nb_coup != (jeu.n * jeu.m)  and not(jeu.gagnant(1)) and not(jeu.gagnant(2))):
        if premier_coup:
            i, j = jeu.random_ai()
            jeu.play_move(i, j)        
            print(jeu)
            joueur = jeu.next_player()
            print('premier coup aléatoire')
            premier_coup = False


        if joueur == 1:
            start = time.time()

            print("\nTour du joueur 1.")
            meilleur_coup = None
            meilleur_valeur = float('-inf')
            for lgn in range(jeu.n):
                for cln in range(jeu.m):
                    if jeu.grid[lgn][cln] == 0:
                        jeu.grid[lgn][cln] = joueur
                        valeur = jeu.min_max_IterativDeepening(4, float('-inf'), float('inf'), joueur)  # Profondeur à adapter ici 3
                        jeu.grid[lgn][cln] = 0

                        if valeur >= meilleur_valeur:
                            meilleur_valeur = valeur
                            meilleur_coup = (lgn, cln)

            if meilleur_coup is not None:
                jeu.play_move(meilleur_coup[0], meilleur_coup[1])
                print("durée du coup : " + str(time.time() - start))
            else:
                break

        else:
            start = time.time()
            print("\nTour du joueur 2.")
            meilleur_coup = None
            meilleur_valeur = float('-inf')
            for lgn in range(jeu.n):
                for cln in range(jeu.m):
                    if jeu.grid[lgn][cln] == 0:
                        jeu.grid[lgn][cln] = joueur
                        valeur = jeu.min_max_align(4, float('-inf'), float('inf'), joueur)  # Profondeur à adapter ici 3
                        jeu.grid[lgn][cln] = 0

                        if valeur >= meilleur_valeur:
                            meilleur_valeur = valeur
                            meilleur_coup = (lgn, cln)
            
            if meilleur_coup is not None:
                jeu.play_move(meilleur_coup[0], meilleur_coup[1])
                print("durée du coup : " + str(time.time() - start))
            else:
                break

                
        joueur = jeu.next_player() # Passage au joueur suivant
        print(jeu)  # Affichage de la grille après le coup
        

    if jeu.gagnant(1):
        print("\niterativ deepening a gagné !")
    elif jeu.gagnant(2):
        print("\nLe min_max align a gagné !")
    else:
        print("\nMatch nul !")




def jouer_partie_monte_carlo(jeu : ttt.TTT):
    ''' jouer une partie contre l'IA en 1v1'''
    print("Vous jouez contre l'IA. Voici la grille de jeu :\n")
    print(jeu)  # Affichage de la grille de jeu initiale

    joueur = 1 # int(input("Choisir : l'humain commence (1) | l'IA commence (2)"))

    while (joueur != 0 and not(jeu.gagnant(1)) and not(jeu.gagnant(2))):
        if joueur == 1:
            print("\nTour du joueur humain.")
            try:
                lgn = int(input("Entrez le numéro de ligne (0 à {}): ".format(jeu.n - 1)))
                cln = int(input("Entrez le numéro de colonne (0 à {}): ".format(jeu.m - 1)))
                jeu.play_move(lgn, cln)
                
            except (ValueError, IndexError, exception.InvalidMoveError):
                print("Coup invalide. Veuillez réessayer.")
                continue
        else: # dans cette version, l'IA est toujours le joueur max, i.e elle commence jamais
            start = time.time()
            print("\nTour de l'IA.")
            best_move = jeu.MonteCarlo()

            jeu.play_move(*best_move)
            print("durée du coup : " + str(time.time() - start))
                
        joueur = jeu.next_player() # Passage au joueur suivant
        print(jeu)  # Affichage de la grille après le coup
        

    if jeu.gagnant(1):
        print("\nLe joueur humain a gagné !")
    elif jeu.gagnant(2):
        print("\nL'IA a gagné !")
    else:
        print("\nMatch nul !")