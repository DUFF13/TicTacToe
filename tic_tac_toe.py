import sys
import numpy as np
import exception
import time

class TTT():

    ''' Class pour le jeu ou n et m sont les dimensions du jeu et k le nombre de symbole à aligner pour gagner'''

    def __init__(self, n : int, m: int, nb_player : int, k : int) -> None:
        self.n = n  # grid size -- lines
        self.m = m  # grid size -- columns
        self.nb_player = nb_player
        self.k = k  # k symbol to win
        self.grid = np.zeros((n,m), dtype= int) # game grid


    def __repr__(self) -> str:
        ''' méthode pour afficher la grille '''
        grid = "    " + "  | ".join(str(i) for i in range(self.m)) + "  |" 
        grid += "\n  " + "+----" * (self.m) + "\n"
        for i in range(self.n):
            grid += f" {i}|" # n° ligne
            for j in range(self.m):
                if self.grid[i][j] == 0:
                    grid += "    |"
                elif self.grid[i][j] == 1:
                    grid += " X  |"    # Symbole joueur 1
                elif self.grid[i][j] == 2 :
                    grid +=  " O  |"     # symbole joueur 2
                else:
                    grid +=  " ▲  |"      # Symbole joueur 3
            grid += "\n  " + "+----" * (self.m) + "\n" if i < self.n - 1 else ""

        return grid


    def repartition(self) -> np.ndarray:
        ''' tabbleau contenant le nombre de coups joué pour chaque joueur '''

        game = np.zeros(self.nb_player +1)

        for i in range(self.n):
            for j in range(self.m):
                game[self.grid[i][j]] += 1

        return game # O(n*m)


    def next_player(self) -> int:
        ''' méthode pour savoir qui est le prochain joueur à jouer '''

        game = self.repartition()
        res = 2
        if (game[0] == 0): # si la partie est terminé
            res = 0

        if len(game) == 3:
            if (game[1] == game[2]):
                res = 1

        if len(game) == 4:
            if (game[1] == game[2]):
                if game[1] == game[3]:
                    res = 1
                else:
                    res = 3
        return res


    def play_move(self, rows : int, columns : int) -> None:
        ''' méthode pour jouer un coup'''
        
        player = self.next_player()
        if (player == 0) or (self.grid[rows][columns] != 0): # si le coup est impossible
            raise exception.InvalidMoveError()

        else:
            self.grid[rows][columns] = player
            
    ''' Directions:
            - east: cln + 1                -> di = (0, 1)
            - south-east: cln + 1, lgn + 1 -> di = (1, 1)
            - sud: cln + 1                 -> di = (1, 0)
            - south-west: cln + 1, lgn -1  -> di = (1 ,-1)
    '''

    def alignement(self, i : tuple, di : tuple, joueur : int) -> bool: # i and di are type (int * int)
        ''' methode  pour savoir si il y a un alignement pour le joueur dans une direction donnée à partir de la case i'''

        (lgn, cln) = i
        (dl, dc) = di

        for j in range(self.k):
            if (cln < 0 or cln >= self.m or lgn < 0 or lgn >= self.n):
                return False
            if (self.grid[lgn][cln] != joueur):
                return False
            cln += dc
            lgn += dl
        return True # O(k)


    def gagnant(self, joueur : int) -> bool:
        ''' méthode pour savoir si un joueur est gagnant '''

        tab_direction = [(1, 0), (1, 1), (0, 1), (-1, 1)]

        for i in range(self.n):
            for l in range(self.m):
                for j in range(4):
                    if self.alignement((i, l), tab_direction[j], joueur):
                        return True
        return False # O(4*n*m*k) = O(n*m*k)


    def longueur_alignement(self, i : tuple, di : tuple, joueur : int) -> int:
        ''' méthode pour connaître la longueur d'un alignement, utile pour coder minimax par la suite pour connaitre quel joueur est favori'''
        lgn, cln = i
        dl, dc = di
        l = 0
        while (l < self.k):
            if (cln < 0 or cln >= self.m or lgn < 0 or lgn >= self.n):
                break 
            if self.grid[lgn][cln] != joueur:
                break
            cln += dc
            lgn += dl
            l += 1
        return l # O(k)


    def cases_vides (self, i : tuple) -> int:
        '''renvoie les voisins de la case donnée en entrée sous forme d'une liste''' # c'est faux, ça ne renvoie pas ça 
        lgn, cln = i
        tab_direction = [(0,1), (0,-1), (1,0), (-1,0), (1,1), (1,-1), (-1,1), (-1,-1)]
        free_box = 0
        for dir in tab_direction :
            x, y = dir 
            if (0 <= lgn + x < self.n) and (0 <= cln + y < self.m): # si les indices de cases sont envisageables
                voisin = self.grid[lgn + x ][cln +y]
                if voisin == 0 :
                    free_box += 1
        return free_box


    def coup_gagnant(self, i : tuple, joueur) -> bool :
        x, y = i
        tab_direction = [(0,1), (0,-1), (1,0), (-1,0), (1,1), (1,-1), (-1,1), (-1,-1)]
        
        for dir in tab_direction:
            l = self.longueur_alignement((x, y), dir, joueur)
            if l == self.k :
                return True
        return False



    def heuristique_vide(self, joueur : int) -> int: # nul, perd même en commençant ...
        ''' heuristique pour min_max, à déterminer (Continue : compare le nombre de cases libres autour de la case jouée)'''
        w_max_joueur = 0
        w_max_adversaire = 0
        adversaire = 3 - joueur # joueur = 1 ou 2 ...

        for i in range(self.n):
            for j in range(self.m):
                if self.grid[i][j] == joueur:
                    if self.coup_gagnant((i, j), joueur) : # Si le coup est gagnant on oublie la défence et on joue
                        return sys.maxsize
                    else :
                        w_max_joueur += self.cases_vides((i, j)) 
                
                                
                elif (self.grid[i][j] == adversaire):
                    if self.coup_gagnant((i, j), adversaire) :
                        return -sys.maxsize
                    else :
                        w_max_adversaire += self.cases_vides((i, j))
                    
        return  (self.k * (w_max_joueur - w_max_adversaire) * w_max_joueur) # plus c'est grand, plus le joueur a une position favorable


    def heuristique_align(self, joueur) -> int: 
        ''' heuristique pour min_max, à déterminer (naîve : compare les longueurs d'alignement max) '''
        algn_max_joueur = 0
        algn_max_adversaire = 0
        adversaire = 3 - joueur # joueur = 1 ou 2 ...
        tab_direction = [(1, 0), (1, 1), (0, 1), (-1, 1)]

        def alignement_possible(position, direction,  joueur):
            compteur = 0
            i, j = position
            while (0 <= i and i < self.n and 0 <= j and j < self.m and self.grid[i][j] == joueur):
                i, j = i + direction[0], j + direction[1]
                compteur +=1
            return compteur >= self.k

        for i in range(self.n):
            for j in range(self.m):
                if self.grid[i][j] == joueur:
                    for a in range(4):
                        if alignement_possible((i, j),tab_direction[a], joueur):
                            l = self.longueur_alignement((i, j), tab_direction[a], joueur)
                            if (l == self.k):
                                return sys.maxsize # si le joueur est gagnant on renvoie MAX_INT (pas trop équivalent du C mais ça fait l'affaire)
                            if (l > algn_max_joueur): # demander à Aubry
                                algn_max_joueur = l

                elif (self.grid[i][j] == adversaire):
                    for a in range(4):
                        if alignement_possible((i, j),tab_direction[a], adversaire):
                            l = self.longueur_alignement((i, j), tab_direction[a], adversaire)
                            if (l == self.k):
                                return (- sys.maxsize) # à modifier
                            if (l > algn_max_adversaire):
                                algn_max_adversaire = l

        return  (self.k * ((algn_max_joueur - algn_max_adversaire) * algn_max_joueur))# plus c'est grand, plus le joueur a une position favorable
         # on renvoie un résulat un peu quelconque qui juste plus grand si joueur est favorable



    def min_max_align(self, p : int, alpha : int, beta : int, joueur : int) -> int:
            ''' algorithme minimax '''

            j = self.next_player()
            
            if (self.gagnant(joueur) or self.gagnant(3 - joueur) or j == 0 or p == 0):
                return self.heuristique_align(joueur)

            if (j == joueur): # noeud max
                m = - sys.maxsize
                for lgn in range(self.n):
                    for cln in range(self.m):
                        if self.grid[lgn][cln] == 0:
                            self.grid[lgn][cln] = joueur
                            v = self.min_max_align(p-1, alpha, beta, joueur)
                            self.grid[lgn][cln] = 0
                            if v > m:
                                m = v
                                if m >= beta:
                                    return m
                                if m > alpha:
                                    alpha = m
                return m

            else: # noeud min
                m = sys.maxsize # essaie de modifier
                for lgn in range(self.n):
                    for cln in range(self.m):
                        if self.grid[lgn][cln] == 0:
                            self.grid[lgn][cln] = 3 - joueur
                            v = self.min_max_align(p - 1, alpha, beta, joueur)
                            self.grid[lgn][cln] = 0
                            if v < m:
                                m = v
                                if m <= alpha:
                                    return m
                                if m < beta:
                                    beta = m
                return m



    def min_max_vide(self, p : int, alpha : int, beta : int, joueur : int) -> int:
            ''' algorithme minimax '''

            j = self.next_player()
            
            if (self.gagnant(joueur) or self.gagnant(3 - joueur) or j == 0 or p == 0):
                return self.heuristique_vide(joueur)

            if (j == joueur): # noeud max
                m = - sys.maxsize
                for lgn in range(self.n):
                    for cln in range(self.m):
                        if self.grid[lgn][cln] == 0:
                            self.grid[lgn][cln] = joueur
                            v = self.min_max_vide(p-1, alpha, beta, joueur)
                            self.grid[lgn][cln] = 0
                            if v > m:
                                m = v
                                if m >= beta:
                                    return m
                                if m > alpha:
                                    alpha = m
                return m

            else: # noeud min
                m = sys.maxsize # essaie de modifier
                for lgn in range(self.n):
                    for cln in range(self.m):
                        if self.grid[lgn][cln] == 0:
                            self.grid[lgn][cln] = 3 - joueur
                            v = self.min_max_vide(p - 1, alpha, beta, joueur)
                            self.grid[lgn][cln] = 0
                            if v < m:
                                m = v
                                if m <= alpha:
                                    return m
                                if m < beta:
                                    beta = m
                return m


    def min_max_IterativDeepening(self, p : int, alpha : int, beta : int, joueur : int) -> int:
            ''' algorithme minimax avec iterativ deepening search'''
            start = time.time()
            j = self.next_player()


            for depth in range(1, p + 1):
                if (self.gagnant(joueur) or self.gagnant(3 - joueur) or j == 0 or p == 0):
                    return self.heuristique_align(joueur)
                    
                if j == joueur: # Noeud Max
                    m = -sys.maxsize

                    for lgn in range(self.n):
                        for cln in range(self.m):
                            if self.grid[lgn][cln] == 0:
                                self.grid[lgn][cln] = joueur
                                v = self.min_max_IterativDeepening(depth, alpha, beta, joueur)
                                self.grid[lgn][cln] = 0
                                if v > m:
                                    m = v
                                    if m >= beta:
                                        return m
                                    if m > alpha:
                                        alpha = m
                
                
                else: # Noeud min
                    m = sys.maxsize
                    for lgn in range(self.n):
                        for cln in range(self.m):
                            if self.grid[lgn][cln] == 0:
                                self.grid[lgn][cln] = 3 - joueur
                                v = self.min_max_IterativDeepening(depth, alpha, beta, joueur)
                                self.grid[lgn][cln] = 0
                                if v > m:
                                    m = v
                                    if m <= alpha:
                                        return m
                                    if m < alpha:
                                        beta = m
            return m



            

        