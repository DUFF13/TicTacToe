import numpy as np
import exception
import time
import random

DureeMaximalDeRecherche = 2.5

class TTT():

    ''' Class pour le jeu ou n et m sont les dimensions du jeu et k le nombre de symbole à aligner pour gagner'''

    def __init__(self, n : int, m: int, nb_player : int, k : int) -> None:
        self.n = n  # grid size -- lines
        self.m = m  # grid size -- columns
        self.nb_player = nb_player
        self.k = k  # k symbol to win
        self.grid = np.zeros((n,m), dtype= int) # game grid
        self.nb_coup = 0


    def __repr__(self) -> str:
        ''' méthode pour afficher la grille dans le terminal'''
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


    def copy(self):
        ''' méthode pour créer une copie de notre grille'''
        ttt = TTT(self.n, self.m, self.nb_player, self.k)
        grid = np.copy(self.grid)

        ttt.grid = grid
        ttt.nb_coup = self.nb_coup
        return ttt


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


    def is_valid_move(self, row : int, column : int) -> bool:
        ''' méthode pour savoir si le coup est possible '''

        if ((row < 0) or (row >= self.n) or (column < 0) or (column >= self.m)):
            return False
        else:
            return self.grid[row][column] == 0
        


    def play_move(self, row : int, column : int) -> None:
        ''' méthode pour jouer un coup'''
        
        player = self.next_player()
        if self.is_valid_move(row, column):
            self.grid[row][column] = player
            self.nb_coup +=1
        else:
            raise exception.InvalidMoveError()
        

    ''' Directions:
            - east: cln + 1                -> di = (0, 1)
            - south-east: cln + 1, lgn + 1 -> di = (1, 1)
            - sud: cln + 1                 -> di = (1, 0)
            - south-west: cln + 1, lgn -1  -> di = (1 ,-1)
    '''

    def alignement(self, i : tuple, di : tuple, joueur : int) -> bool: # i and di are type (int * int)
        ''' methode  pour savoir si il y a un alignement pour le joueur dans une direction donnée à partir de la case i'''

        (row, col) = i
        (dl, dc) = di

        # east  :
        if (di == (0, 1)):
            if col + self.k > self.m:
                return False
            
        # south : 
        if (di == (1, 0)):
            if row + self.k > self.n:
                return False
                
        # south-east :
        if (di == (1, 1)):
            if ((row + self.k > self.n) or (col + self.k > self.m)) :
                return False
            
        # south-west :
        if (di == (1, -1)):
            if ((col - self.k < 0) or (row + self.k > self.n)):
                return False
            

        for _ in range(self.k):
            if (col < 0 or col >= self.m or row < 0 or row >= self.n):
                return False
            if (self.grid[row][col] != joueur):
                return False
            col += dc
            row += dl
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


    def get_winner(self):
        ''' renvoie le numéro du vainqueur ou 0 si aucun gagnant'''
        for i in range(self.nb_player + 1):
            if self.gagnant(i):
                return i
        return 0


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
        '''renvoie le nb de cases libres autour de la case i''' 

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
        ''' vérifie qu'un coup est gagnant '''
        x, y = i
        tab_direction = [(0,1), (0,-1), (1,0), (-1,0), (1,1), (1,-1), (-1,1), (-1,-1)]
        
        for dir in tab_direction:
            l = self.longueur_alignement((x, y), dir, joueur)
            if l == self.k :
                return True
        return False



    def heuristique_vide(self, joueur : int): 
        ''' heuristique pour min_max, à déterminer (Continue : compare le nombre de cases libres autour de la case jouée)'''
        w_max_joueur = 0
        w_max_adversaire = 0
        adversaire = 3 - joueur # joueur = 1 ou 2 ...

        for i in range(self.n):
            for j in range(self.m):
                if self.grid[i][j] == joueur:
                    if self.coup_gagnant((i, j), joueur) : # Si le coup est gagnant on oublie la défense et on joue
                        return float('inf')
                    w = self.cases_vides((i, j))
                    if w > w_max_adversaire:
                        w_max_joueur += self.cases_vides((i, j)) 
                
                                
                elif (self.grid[i][j] == adversaire):
                    if self.coup_gagnant((i, j), adversaire) :
                        return float('-inf')
                    w = self.cases_vides((i, j))
                    if w > w_max_adversaire:
                        w_max_adversaire += self.cases_vides((i, j))
                    
        return  (self.k * (w_max_joueur - w_max_adversaire) * w_max_joueur) # plus c'est grand, plus le joueur a une position favorable


    def heuristique_align(self, joueur): 
        ''' heuristique pour min_max, à déterminer (assez naïve, elle compare les longueurs d'alignements possible) '''
        algn_max_joueur = 0
        algn_max_adversaire = 0
        adversaire = 3 - joueur # joueur = 1 ou 2 ...
        tab_direction = [(1, 0), (1, 1), (0, 1), (-1, 1)]


        def alignement_possible(position, direction : tuple,  joueur : int) -> bool:
            ''' Vérifie que l'alignement comprenant la case position dans une direction est possible '''
            compteur = 0
            i, j = position
            while (0 <= i and i < self.n and 0 <= j and j < self.m and (self.grid[i][j] == joueur or self.grid[i][j] == 0)):

                i, j = i + direction[0], j + direction[1]
                compteur +=1

            a, b = position

            i, j = a - direction[0], b - direction[1]

            while (0 <= i and i < self.n and 0 <= j and j < self.m and (self.grid[i][j] == 0 or self.grid[i][j] == joueur)):
                compteur += 1
                i, j = i - direction[0], j - direction[1]

            return compteur >= self.k
        
        if self.gagnant(adversaire):
            return float('-inf')

        for i in range(self.n):
            for j in range(self.m):
                if self.grid[i][j] == joueur:
                    for a in range(4):
                        if alignement_possible((i, j),tab_direction[a], joueur): # si l'alignement n'est pas possible, inutile de considérer cette case
                            l = self.longueur_alignement((i, j), tab_direction[a], joueur)
                            if (l == self.k):
                                return float('inf')
                            if (l > algn_max_joueur): 
                                algn_max_joueur = l

                elif (self.grid[i][j] == adversaire):
                    for a in range(4):
                        if alignement_possible((i, j),tab_direction[a], adversaire):
                            l = self.longueur_alignement((i, j), tab_direction[a], adversaire)
                            if (l == self.k):
                                return float('-inf')
                            if (l > algn_max_adversaire):
                                algn_max_adversaire = l
                


        score_joueur = self.k * (algn_max_joueur - algn_max_adversaire) 
        score_adversaire = self.k * (algn_max_adversaire - algn_max_joueur)
        return (score_joueur - score_adversaire)

        


    def min_max_vide(self, p : int, alpha : int, beta : int, joueur : int):
            ''' algorithme minimax avec l'heuristique vide avec alpha beta élagage'''

            j = self.next_player()
            best_move = None
            
            if (self.gagnant(joueur) or self.gagnant(3 - joueur) or j == 0 or p == 0):
                return self.heuristique_vide(joueur), best_move
            
            if j == joueur: # Noeud Max
                m = float('-inf')
                for lgn in range(self.n):
                    for cln in range(self.m):
                        if self.grid[lgn][cln] == 0:
                            self.grid[lgn][cln] = joueur
                            score, _ = self.min_max_vide(p - 1, alpha, beta, joueur)
                            self.grid[lgn][cln] = 0
                            if score != None:
                                if score == m:
                                    if random.randint(0, 1) == 1:
                                        best_move = (lgn, cln)
                                if score > m:
                                    m = score
                                    best_move = (lgn, cln)
                                alpha = max(alpha, score)
                                if alpha >= beta:
                                    break
            
            else: # Noeud min
                m = float('inf')      
                for lgn in range(self.n):
                    for cln in range(self.m):
                        if self.grid[lgn][cln] == 0:
                            self.grid[lgn][cln] = 3 - joueur
                            score, _ = self.min_max_vide(p - 1, alpha, beta, joueur)
                            self.grid[lgn][cln] = 0
                            if score != None:
                                if score == m:
                                    if random.randint(0, 1) == 1:
                                        best_move = (lgn, cln   )
                                if score < m:
                                    m = score
                                    best_move = (lgn, cln)
                                beta = min(beta, score)
                                if alpha >= beta:
                                    break
            return m, best_move


            
    def random_ai(self): 
        ''' génére une position aléatoire possible '''
        row = random.randrange(self.n)
        col = random.randrange(self.m)

        while not(self.is_valid_move(row, col)):
            row = random.randrange(self.n)
            col = random.randrange(self.m)

        return row, col
            
        


    def MonteCarlo(self): # nul mais fonctionne 
        ''' algorithme probabiliste de type monte carlo '''
        num_simulations = 100
        j = self.next_player()
        valid_moves = [(i, j) for i in range(self.m) for j in range(self.n) if self.is_valid_move(i, j)]

        scores = []
        for move in valid_moves:
            score = 0
            for i in range(num_simulations):
                simulation_game = self.copy()
                simulation_game.play_move(*move)
                while not (simulation_game.gagnant(j) or simulation_game.gagnant(3 - j) or simulation_game.nb_coup == self.n * self.m):

                    valid_moves_simulation = [(i, j) for i in range(simulation_game.m) for j in range(simulation_game.n) if simulation_game.is_valid_move(i, j)]

                    random_move = random.choice(valid_moves_simulation)
                    simulation_game.play_move(*random_move)
                
                    if not(simulation_game.gagnant(3 - j)):
                        score += 5
                        if simulation_game.gagnant(j):
                            score += 15
                    else:
                        score -= 20

            scores.append(score)

        best_move = valid_moves[scores.index(max(scores))]

        return 0, best_move # 0 pour correspondre au prototype des fonctions minimax
    


    def min_max_align(self, p : int, alpha : int, beta : int, joueur : int):
            ''' algorithme minimax avec l'heuristique align, et alpha béta élagage'''

            j = self.next_player()
            best_move = None
            
            if (self.gagnant(3 - joueur) or self.gagnant(joueur) or j == 0 or p == 0):
                return self.heuristique_align(joueur), best_move

            if j == joueur: # noeud max
                m = float('-inf')
                for lgn in range(self.n):
                    for cln in range(self.m):
                        if self.grid[lgn][cln] == 0:                                
                            self.grid[lgn][cln] = joueur                            
                            score, _ = self.min_max_align(p - 1, alpha, beta, joueur)
                            self.grid[lgn][cln] = 0
                            if score > m:                            
                                m = score
                                best_move = (lgn, cln)
                                alpha = max(alpha, score)
                            if alpha >= beta:
                                break

            else: # noeud min
                m = float('inf') 
                for lgn in range(self.n):
                    for cln in range(self.m):
                        if self.grid[lgn][cln] == 0:                                
                            self.grid[lgn][cln] = 3 - joueur                            
                            score, _ = self.min_max_align(p - 1, alpha, beta, joueur)
                            self.grid[lgn][cln] = 0
                            if score < m:
                                m = score
                                best_move = (lgn, cln)
                            beta = min(beta, score)
                            if alpha >= beta:
                                break            
            return m, best_move



    def min_max_IterativDeepening(self, joueur : int):
            ''' algorithme minimax avec iterativ deepening search, on utilise la condition de temps, pas de profondeur max'''
            best_move = None
            m = float('-inf')
            start = time.time()
            endtime = start + DureeMaximalDeRecherche
            depth = 1
            while(True):
                current_time = time.time()

                if current_time > endtime:
                    print("durée dépassée")
                    break

                value, move = self.min_max_align(depth, float('-inf'), float('inf'), joueur)

                if joueur == 2 and value == float('inf'):
                    print('profondeur de recherche : ' + str(depth))
                    return value, move
                if joueur == 1 and value == float('-inf'):
                    print('profondeur de recherche : ' + str(depth))
                    return value, move
                else:
                    m = value
                    best_move = move
        
                
                if self.n * self.m - self.nb_coup < depth: # rien ne sert de continuer si on arrive à une feuille
                    break

                depth += 1


            print('profondeur de recherche : ' + str(depth - 1))
            return m, best_move

