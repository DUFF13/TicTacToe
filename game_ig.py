from tkinter import *
import tic_tac_toe as ttt
import jouer 
import time 
from queue import Queue


""" heuristic :
    0 : Aucune c'est humain.vs.humain
    1 : Align (Minimax)
    2 : Iterative (Minimax)
    3 : Empty (Minimax)
    4 : Montecarlo"""

""" Game_mode :
    1 : humain.vs.humain
    2 : humain.vs.IA
    3 : IA.vs.IA """


class GameIG(ttt.TTT) :              
    def __init__(self, window : Tk, game : ttt.TTT, game_mode : int, heuristic : int) -> None:
        super().__init__(game.m, game.n, game.nb_player, game.k)
        self.window = window
        self.game = game
        self.game_mode = game_mode 
        self.heuristic = heuristic
        
        self.nb_player = game.nb_player
        self.current_player = 'X'  # Commence par joueur 'X'

        self.buttons = []
        self.labels_buttons = []
        self.clicked_row = IntVar()
        self.clicked_col = IntVar()
        

        # Personnalisation de la fenêtre
        self.window.title( "m, n, k - game ")
        self.window.config(background= '#3961CA')


        self.result_frame = Frame(self.window, bg = "#3961CA") # nv frame pour place msg de victoire et bouton rejouer sur la grille

        # Ajout du boutton Rejouer
        self.replay_button = Button(self.window, text = "Rejouer",
                                     font = ("Impact", 20), bg = "#3961CA",
                                     fg = '#FF0000', command = self.restart_game)
        
        self.replay_button.grid(row = self.m+1, column = 0, columnspan = self.n, pady = 10) # centre le bouton en bas de la grille
        self.replay_button["state"] = "disabled"
        self.replay_button.grid_remove()
        
        # On dessine/affiche la grille de jeu
        self.draw_grid()
     
    def draw_grid(self):
        ''' Crée et affiche la grille de jeu'''

        for rows in range(self.m):
            case = [] # liste des boutons ~ cases jouées (case par colone)
            for col in range(self.n):
                button = Button(self.window, font = ("Impact", 40),
                                bg = '#06143C', width = 5, height = 2,
                                borderwidth = 2,
                                command = lambda r = rows, 
                                c = col : self.place_symbol(r, c)
                                )
    
                button.grid(row = rows, column = col, padx = 2, pady = 2, sticky = "nsew")
                case.append(button) # on ajoute à la liste des cases nos cases = button
            self.buttons.append(case) # on range ensuite dans chaque ligne nos buttons/cases

        # Ajuster la configuration de la grille pour redimensionner les cases
        for i in range(self.m):
            self.window.grid_rowconfigure(i, weight = 1)
        for i in range(self.n):
            self.window.grid_columnconfigure(i, weight = 1)
        
    def place_symbol(self, row, col):
        print("click", row, col)

        self.clicked_row = row
        self.clicked_col = col
        
        # Vérifier si la case a déjà été jouée
        if self.grid[row][col] != 0 :
            return 
        
        if self.current_player == 'X':
            symbol_color = '#FF0000'  # Couleur pour X
            player = 1
        elif self.current_player == 'O':
            symbol_color = '#2BB48E'  # Couleur pour O
            player = 2
        elif self.current_player == '▲':
            symbol_color = '#8D00FF'  # Couleur pour ▲
            player = 3
        
        # Placement du symbole
        self.buttons[row][col].config(text = self.current_player, font = ("Impact", 40), fg = symbol_color )
        self.grid[row][col] = player
        self.switch_player() 

        # Si c'est le tour de l'IA, déclencher le coup de l'IA
        if self.game_mode == 2 and self.current_player == 'O':
            self.jouer_partie_IA_IG(self)
        
        # TODO Si c'est le tour de l'IA contre IA ==> En essaie ne fonctionne pas
        elif self.game_mode == 3 and (self.current_player == 'X' or self.current_player == 'O'):
            self.jouer_partie_IA_IG(self)
            self.switch_player()
            

        
        # Après chaque coup on vérifie s'il a été gagnant puis on change de joueur
        self.check_win()
          

    def switch_player(self) :
        if self.nb_player == 2: # Si 2 joueurs
            if self.current_player == 'O':
                self.current_player = 'X'
            else:
                self.current_player = 'O'

        elif self.nb_player == 3: # si 3 joueurs
            if self.current_player == 'X':
                self.current_player = 'O'
            elif self.current_player == 'O':
                self.current_player = '▲'
            else:
                self.current_player = 'X'

        return self.current_player
    
    def check_win(self):
        if self.gagnant(1):
            self.show_result("Le joueur 1 a gagné")
            self.replay_button["state"] = "active"
            self.replay_button.grid()

        elif self.gagnant(2):
            self.show_result("le joueur 2 a gagné")
            self.replay_button["state"] = "active"
            self.replay_button.grid()

        elif self.game_mode == 3 and self.gagnant(3): 
            self.show_result("Le joueur 3 a gagné")
            self.replay_button["state"] = "active"
            self.replay_button.grid()

        elif self.is_board_full():
            self.show_result("Match nul")
            self.replay_button["state"] = "active"
            self.replay_button.grid()

    def is_board_full(self) -> bool :
        for row in self.grid:
            for cell in row:
                if cell == 0:
                    return False  # il y a au moins case vide
        return True  #  plateau plein
        #TODO peut être créer un compteur et ajouter 1 quand une case est jouer, si compteur == n*m alors plein return True
    
    def show_result(self, result):
        result_label = Label(self.result_frame, text = result, font = ("Impact", 20), bg = "#3961CA", fg = "#00FFFF")
        result_label.grid(row = self.m + 2, column = 0, columnspan = self.n)
        

        # ajout à la liste 
        self.labels_buttons.append(result_label)

        # Désactivation des boutons à la fin de la partie
        for row in self.buttons :
            for button in row :
                button.config(state = DISABLED)
        
        # Cache le bouton Rejouer
        self.replay_button.configure(state = DISABLED)
        
        self.replay_button.grid_remove()
        self.labels_buttons.append(self.replay_button)

        self.result_frame.grid( row = self.m+2, column = 0, columnspan = self.n, sticky = "nsew")

    def restart_game(self):
        self.clear_board()
        self.current_player = "X"
        
        # Effacer les labels et buttons de fin de partie 
        for elt in self.labels_buttons:
            elt.grid_forget()

        # Détruire les anciens boutons
        for row in self.buttons :
            for b in row :
                b.config( text = "", state = NORMAL)  # 1: efface le texte du bouton, 2 : bouton peut être cliqué
        
        # Réactivation du bouton rejouer
        self.replay_button["state"] = "disabled"

        # Cacher result_frame
        self.replay_button.grid_remove() 
        self.result_frame.grid_remove()

        # # Réinitialiser la configuration de la grille pour centrer le bouton
        # self.window.grid_rowconfigure(self.m + 1, weight = 0)
        # self.window.grid_columnconfigure(0, weight = 1)
        # self.replay_button.grid(row = self.m+1, column = 0, columnspan = self.n, pady = 10)
        # self.replay_button.grid_remove()

    def clear_board(self):
        self.grid = [[0] * self.n for _ in range(self.m)]

    def jouer_partie_IA_IG(self, game : ttt.TTT):
                    
        start = time.time()
        
        # strétégie abordée
        if self.heuristic == 1:
            _, meilleur_coup = game.min_max_align(4, float('-inf'), float('inf'), 1)
        elif self.heuristic == 2:
            _, meilleur_coup = game.min_max_IterativDeepening(1)
        elif self.heuristic == 3:
            _, meilleur_coup = game.min_max_vide(4, float('-inf'), float('inf'), 1)
        elif self.heuristic == 4:
            _, meilleur_coup = game.MonteCarlo()
        
        # Choix du coup et mise à jour de la grille de jeu game: TTT
        if meilleur_coup is None:
            print("l'IA n'a pas trouvé de meilleure position, elle joue aléatoirement")
            meilleur_coup = game.random_ai()
            r, c = meilleur_coup[0], meilleur_coup[1]
            self.place_symbol(r, c)
        else:
            self.place_symbol(meilleur_coup[0], meilleur_coup[1])
            print("durée du coup : " + str(time.time() - start))
        
        


    