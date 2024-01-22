from tkinter import *
import game_ig as ig
import tic_tac_toe as ttt
from game_ig import GameIG

rouge = "#FF0000"
vert = "#2BB48E"
violet = "#8D00FF"
bleu_marine = "#050C49"

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

class Parameters():
    def __init__(self, parameter_window):
        self.parameter_window = parameter_window
        
        # Paramètres par défaut
        self.nb_player = 2 
        self.entry_n = 3
        self.entry_m = 3
        self.entry_k = 3 
        self.game_mode = IntVar()
        self.heuristic = 0

        # Création d'une frame pour regrouper les labels/boutons
        self.frame_parametres = Frame(self.parameter_window, bg = "#050C49")       
        
        # Affichage
        self.frame_parametres.grid(row = 0, column = 0, padx = 5, pady = 70, sticky = "nsew")
        self.frame_parametres.grid(row = 0, column = 0, padx = 15, pady = 15, sticky = "nsew")
        self.frame_parametres.grid(row = 1, column = 0, padx = 15, pady = 0, sticky = "nsew") 
        
        # self.parameter_window.grid_rowconfigure(0, weight = 1)
        # self.parameter_window.grid_columnconfigure(0, weight = 1)
        self.frame_parametres.grid_rowconfigure(0, weight = 1)
        self.frame_parametres.grid_columnconfigure(0, weight = 1)
        
        # Ajouter un titre
        title = Label(self.frame_parametres, text = "Paramètres de jeu", font = ("Impact", 30), bg = bleu_marine, fg = vert)
        title.grid(row = 0, column = 0, columnspan = 4, pady = (75, 100)) # empacter, pptés de positionnement
        
        # Bloc 1: Définir la grille
        self.grille = Label(self.frame_parametres, text = "Définir la grille:", font = ("Impact", 15), bg = "#050C49", fg = "#FF0000" )
        self.grille.grid(row = 1, column = 0, pady = 5)

        self.entry_n = Entry(self.frame_parametres, font = ("Impact", 15), bg = "#050C49", fg = "#FF0000", width = 5)
        self.entry_n.grid(row = 1, column = 1, pady = 5)

        self.entry_m = Entry(self.frame_parametres,font = ("Impact", 15), bg = "#050C49", fg = "#FF0000", width=5)
        self.entry_m.grid(row = 1, column = 2, pady = 5)

        self.entry_k = Entry(self.frame_parametres, font = ("Impact", 15), bg = "#050C49", fg = "#FF0000", width = 5)
        self.entry_k.grid(row = 1, column = 3, pady = 5)

        # Bloc 2: Définir le nombre de joueurs
        self.joueurs = Label(self.frame_parametres, text = "Définir le nombre de joueurs:", font = ("Impact", 15), bg = "#050C49", fg = "#FF0000" )
        self.joueurs.grid(row = 2, column = 0, pady = 5)

        self.but_player2 = Button(self.frame_parametres, text = "2 joueurs", font = ("Impact", 15), bg = "#050C49", fg = "#FF0000", relief = "raised", command = lambda: self.nb_player_choice(self.but_player2))
        self.but_player2.grid(row = 2, column = 1, pady = 5)

        self.but_player3 = Button(self.frame_parametres, text = "3 joueurs", font = ("Impact", 15), bg = "#050C49", fg = "#FF0000", relief = "raised", command = lambda: self.nb_player_choice(self.but_player3))
        self.but_player3.grid(row = 2, column = 2, pady = 5)

        # Bloc 3: Choisir le mode de jeu
        ''' 1: Humain.vs.Humain
            2: Humain.vs.IA
            3: IA.vs.IA '''
        
        self.label_game_mode = Label(self.frame_parametres, text = "Choisir le mode de jeu:", font = ("Impact", 15), bg = "#050C49", fg = "#FF0000")
        self.label_game_mode.grid(row = 3, column = 0, pady = 5)

        self.button1 = Button(self.frame_parametres, text = "Humain .vs. Humain", 
                              font = ("Impact", 15), bg = "#050C49", 
                              fg = "#FF0000", relief = "raised", 
                              command = lambda : self.is_clicked(self.button1))
        self.button1.grid(row = 3, column = 1, pady = 5)

        self.button2 = Button(self.frame_parametres, text = "Humain .vs. IA", 
                              font = ("Impact", 15), bg = "#050C49", 
                              fg = "#FF0000", relief = "raised", 
                              command = lambda :self.is_clicked(self.button2))
        self.button2.grid(row=3, column=2, pady=5)

        self.button3 = Button(self.frame_parametres, text = "IA .vs. IA", 
                              font = ("Impact", 15), bg = "#050C49", relief = "raised", 
                              fg = "#FF0000", command = lambda :self.is_clicked(self.button3))
        self.button3.grid(row = 3, column = 3, pady = 5)

        # Bloc 4: Quelle IA souhaitez-vous tester ?
        self.label_heuristic = Label(self.frame_parametres, text = "Quelle heuristique souhaitez-vous tester?", font = ("Impact", 15), bg = "#050C49", fg = "#FF0000")
                                      
        self.label_heuristic.grid(row = 4, column = 0, pady = 5)

        self.button_minimax = Button(self.frame_parametres, text = "Minimax-alignement", font = ("Impact", 15), bg = "#050C49", fg = "#FF0000", relief = "raised", command = lambda : self.is_clicked(self.button_minimax))
        self.button_minimax['state'] = "disabled" # on désactive les options ia tant que l'utilisateur est en h.vs.h
        
        self.button_iterative = Button(self.frame_parametres, text = "Minimax-iterative Deepening", font = ("Impact", 15), bg = "#050C49", fg = "#FF0000", relief = "raised", command = lambda : self.is_clicked(self.button_iterative))
        self.button_iterative['state'] = "disabled"

        self.button_empty = Button(self.frame_parametres, text = "Minimax-empty_heuristic", font = ("Impact", 15), bg = "#050C49", fg = "#FF0000", relief = "raised", command = lambda : self.is_clicked(self.button_empty))
        self.button_empty['state'] = "disabled"
        
        self.button_montecarlo = Button(self.frame_parametres, text = "Montecarlo", font = ("Impact", 15), bg = "#050C49", fg = "#FF0000", relief = "raised", command = lambda : self.is_clicked(self.button_montecarlo))
        self.button_montecarlo['state'] = "disabled"
        
        # Affichage des boutons
        self.button_minimax.grid(row = 4, column = 1, padx =(15,0), pady = 5)
        self.button_iterative.grid(row = 4, column = 2, pady = 5)
        self.button_empty.grid(row = 4, column = 3, pady = 5)
        self.button_montecarlo.grid(row = 4, column = 4, pady = 5)



        # Lancer la partie 
        self.play_button = Button(self.frame_parametres, text = "Commencer le jeu", 
                             font = ("Impact", 20), bg = '#071061', fg = "#FF0000",
                             command = lambda : upgrade_parameters_and_start(self.frame_parametres, self.entry_n, self.entry_m, self.entry_k, self.game_mode, self.nb_player, self.heuristic))
        self.play_button.grid( row = 6, column = 0, columnspan = 4, padx = (200,200), pady = (100, 0))
    
    
    def is_clicked(self, button):
            # game_mode
        if button == self.button1 :
            self.game_mode = 1
        elif button == self.button2 :
            self.game_mode = 2
        elif button == self.button3 :
            self.game_mode = 3

            # heuristic
        elif button == self.button_minimax :
            self.heuristic = 1
        elif button == self.button_iterative :
            self.heuristic = 2
        elif button == self.button_empty :
            self.heuristic = 3
        elif button == self.button_montecarlo :
            self.heuristic = 4

        if self.game_mode in [2,3]:# si on a choisi un mode avec IA
            self.activer_heuristic_choice()
        else : 
            self.desactiver_heuristic_choice()
        
        # # Changer le bg du bouton cliqué 
        # button["bg"] = "#5B3DBD"
        
        # Changer le relief du bouton cliqué à "sunken" et les autres à "raised"
        for other_button in [self.button1, self.button2, self.button3] :
            if other_button == button:
                other_button["relief"] = "sunken"
            else:
                other_button["relief"] = "raised"
    


    def nb_player_choice(self, button):
        if button == self.but_player3 :
            self.nb_player = 3 # mise à jour du nombre de joueur dans la variable
            self.but_player3["relief"] = "sunken"
            self.but_player2["relief"] = "raised"
        else : 
            self.nb_player = 2
            self.but_player3["relief"] = "raised"
            self.but_player2["relief"] = "sunken"

    def activer_heuristic_choice(self):
        ia_list = [self.button_minimax,self.button_iterative, self.button_empty, self.button_montecarlo]
        for button in ia_list :
            button['state'] = "normal"

    def desactiver_heuristic_choice(self):
        ia_list = [self.button_minimax,self.button_iterative, self.button_empty, self.button_montecarlo]
        for button in ia_list :
            button['state'] = "disabled"

            
    
# Mise à jour des paramètres :
            
def upgrade_parameters_and_start(parameter_window, entry_n : int, entry_m : int, entry_k : int, game_mode : int, nb_player : int, heuristic : int) :
    try : 
        n = int(entry_n.get())
        m = int(entry_m.get())
        k = int(entry_k.get())
        game_mode = int(game_mode)
        nb_player = int(nb_player)
        heuristic = int(heuristic)
    except ValueError:
        raise ValueError("Veuillez saisir les valeurs entières pour n, m et k svp")
    
    
    parameter_window.destroy()  # Ferme la fenêtre des paramètres 
    
    game = ttt.TTT(n, m, nb_player, k)

    if game_mode == 1 : 
        GameIG(Tk(), game, game_mode, 0)
        
    else : 
        game_ig = GameIG(Tk(), game, game_mode, heuristic)

      

    

