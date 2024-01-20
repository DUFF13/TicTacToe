from tkinter import *
from game_ig import GameIG
import tic_tac_toe as ttt
import parameters as par



class WelcomePage():
    def __init__(self, window) -> None:
        self.window = window
        self.window.minsize(1600, 900)
        self.selected_button = None 
        
        # Création d'une Frame pour tout centrer sur la page d'acceuil
        self.frame_welcome = Frame(window, bg = '#050C49')
        self.frame_welcome.grid_columnconfigure(0, weight = 1)
        self.frame_welcome.grid_columnconfigure(1, weight = 1)
        self.frame_welcome.grid_columnconfigure(2, weight = 1)
        self.frame_welcome.grid(row = 0, column = 0, padx = (180,180), pady = (200,200), sticky = "nsew")

        # Ajouter un titre
        label_title = Label(self.frame_welcome, text = "Bienvenue sur le jeu", font = ("Impact", 40), bg = "#050C49", fg = "#FF0000")
        label_title.grid(row = 0, column = 0, columnspan = 3) # empacter, pptés de positionnement
                       
        # Bouton "Paramètres"
        parameters_but = Button(self.frame_welcome, text = "Paramètres", 
                                font = ("Impact", 20), bg = '#071061', fg = "#FF0000", 
                                command = lambda : self.open_parameters())
        parameters_but.grid(row = 3, column = 0, columnspan = 3)

        # Bouton "Commencer la partie"
        play_button = Button(self.frame_welcome, text = "Commencer le jeu", 
                             font = ("Impact", 20), bg = '#071061', fg = "#FF0000", 
                             command = lambda : self.start_game())
        play_button.grid(row = 1, column = 0, columnspan = 3, pady = 50)




    def open_parameters(self) :
        self.frame_welcome.grid_forget()
        self.parameters_frame = par.Parameters(self.window) # créé un nouvel objet parameters

    def start_game(self):
        n = 3
        m = 3
        k = 3
        game_mode = 2
        nb_player = 2
        
        self.window.destroy()  # Ferme la fenêtre d'accueil

        game = ttt.TTT(n, m, nb_player, k)
        game_ig = GameIG(Tk(), game, 0, 0) # créé un nouvel objet GameIG
        # game_mode = 0 <=> humain.vs.humain
        # heuristic = 0 <=> aucun ia sélectionnée puisque pas besoin d'ia
