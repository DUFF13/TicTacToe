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



def jouer_partie_IA_3joueurs(jeu : ttt.TTT, heuristic):
    ''' jouer une partie contre l'IA en 1v1'''
    print("Vous jouez contre l'IA. Voici la grille de jeu :\n")
    print(jeu)  # Affichage de la grille de jeu initiale

    joueur = 1 

    while (jeu.nb_coup  < jeu.n * jeu.m and not(jeu.gagnant(1)) and not(jeu.gagnant(2)) and not(jeu.gagnant(3))):
        if joueur == 1:
            print("\nTour du joueur humain 1.")
            try:
                lgn = int(input("Entrez le numéro de ligne (0 à {}): ".format(jeu.n - 1)))
                cln = int(input("Entrez le numéro de colonne (0 à {}): ".format(jeu.m - 1)))
                jeu.play_move(lgn, cln)
                
            except (ValueError, IndexError, exception.InvalidMoveError):
                print("Coup invalide. Veuillez réessayer.")
                continue
        elif joueur == 3:
            print("\nTour du joueur humain 2.")
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
            if heuristic == 1:
                    _, meilleur_coup = jeu.min_max_align(3, float('inf'), float('-inf'), joueur)
            elif heuristic == 2:
                _, meilleur_coup = jeu.min_max_IterativDeepening(joueur)
            elif heuristic == 3:
                _, meilleur_coup = jeu.min_max_vide(3, float('-inf'), float('inf'), joueur) 
            elif heuristic == 4:
                _, meilleur_coup = jeu.MonteCarlo()


            jeu.play_move(meilleur_coup[0], meilleur_coup[1])
            print("durée du coup : " + str(time.time() - start))
                

        joueur = jeu.next_player() # Passage au joueur suivant
        print(jeu)  # Affichage de la grille après le coup
        

    if jeu.gagnant(1):
        print("\nLe joueur humain 1 a gagné !")
    elif jeu.gagnant(3):
        print("\nL'IA a gagné !")
    elif jeu.gagnant(2):
        print("\nLe joueur humain 2 a gagné")
    else:
        print("\nMatch nul !")





def jouer_IA_vs_IA(jeu : ttt.TTT, heuristic1, heuristic2):
    ''' faire jouer 2 IA l'une contre l'autre'''
    print(" H_vide (J1) VS H_align (J2). Voici la grille de jeu :\n")
    print(jeu)  
    joueur = 1
    premier_coup = True
    start_game = time.time()
    
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
            if heuristic1 == 1:
                    _, meilleur_coup = jeu.min_max_align(4, float('-inf'), float('inf'), joueur)
            elif heuristic1 == 2:
                _, meilleur_coup = jeu.min_max_IterativDeepening(joueur)
            elif heuristic1 == 3:
                _, meilleur_coup = jeu.min_max_vide(4, float('-inf'), float('inf'), joueur) 
            elif heuristic1 == 4:
                _, meilleur_coup = jeu.MonteCarlo()
      
            if meilleur_coup is None:
                print("l'IA n'a pas trouvé de meilleure position, elle joue aléatoirement")
                meilleur_coup = jeu.random_ai()
                
      
            jeu.play_move(meilleur_coup[0], meilleur_coup[1])
            print("durée du coup : " + str(time.time() - start))
            print('joueur' + str(joueur))


        else:
            start = time.time()
            print("\nTour du joueur 2.")
            if heuristic2 == 1:
                    _, meilleur_coup = jeu.min_max_align(4, float('-inf'), float('inf'), joueur)
            elif heuristic2 == 2:
                _, meilleur_coup = jeu.min_max_IterativDeepening(joueur)
            elif heuristic2 == 3:
                _, meilleur_coup = jeu.min_max_vide(4, float('-inf'), float('inf'),joueur)
            elif heuristic2 == 4:
                _, meilleur_coup = jeu.MonteCarlo()

            if meilleur_coup is None:
                print("l'IA n'a pas trouvé de meilleure position, elle joue aléatoirement")
                meilleur_coup = jeu.random_ai()

            jeu.play_move(meilleur_coup[0], meilleur_coup[1])
            print("durée du coup : " + str(time.time() - start))

                
        joueur = jeu.next_player() # Passage au joueur suivant
        print(jeu)  # Affichage de la grille après le coup
        

    if jeu.gagnant(1):
        print("\nl'IA 1 a gagné !")
    elif jeu.gagnant(2):
        print("\nL'IA 2 a gagné !")
    else:
        print("\nMatch nul !")
    print('la partie a duré : ' + str(time.time() - start_game))



def jouer_partie_IA(jeu : ttt.TTT, heuristic):
    ''' jouer une partie contre l'IA en 1v1'''
    print("Vous jouez contre l'IA. Voici la grille de jeu :\n")
    print(jeu)  # Affichage de la grille de jeu initiale

    joueur = 1 
    starter = int(input("Choisir : l'humain commence (1) | l'IA commence (2)"))

    while (jeu.nb_coup != jeu.n * jeu.m and not(jeu.gagnant(1)) and not(jeu.gagnant(2))):
        if joueur == starter:
            print("\nTour du joueur humain.")
            try:
                lgn = int(input("Entrez le numéro de ligne (0 à {}): ".format(jeu.n - 1)))
                cln = int(input("Entrez le numéro de colonne (0 à {}): ".format(jeu.m - 1)))
                jeu.play_move(lgn, cln)
                
            except (ValueError, IndexError, exception.InvalidMoveError):
                print("Coup invalide. Veuillez réessayer.")
                continue

        else: # dans cette version, l'IA est toujours le joueur max, i.e elle commence jamais
            print("\nTour de l'IA.")
            start = time.time()
            if heuristic == 1:
                    _, meilleur_coup = jeu.min_max_align(4, float('-inf'), float('inf'), joueur)
            elif heuristic == 2:
                _, meilleur_coup = jeu.min_max_IterativDeepening(joueur)
            elif heuristic == 3:
                _, meilleur_coup = jeu.min_max_vide(4, float('-inf'), float('inf'), joueur)
            elif heuristic == 4:
                _, meilleur_coup = jeu.MonteCarlo()

            if meilleur_coup is None:
                print("l'IA n'a pas trouvé de meilleure position, elle joue aléatoirement")
                meilleur_coup = jeu.random_ai()
            else:
                jeu.play_move(meilleur_coup[0], meilleur_coup[1])
                print("durée du coup : " + str(time.time() - start))
                
        joueur = jeu.next_player() # Passage au joueur suivant
        print(jeu)  # Affichage de la grille après le coup
        
    if starter == 1:
        if jeu.gagnant(1):
            print("\nLe joueur humain a gagné !")
        elif jeu.gagnant(2):
            print("\nL'IA a gagné !")
    if starter == 2:
        if jeu.gagnant(1):
            print("\nL'IA a gagné !")
        elif jeu.gagnant(2):
            print("\nLe joueur humain a gagné !")
    else:
        print("\nMatch nul !")