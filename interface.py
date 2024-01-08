import tkinter as tk
from functools import partial
import numpy as np
import tic_tac_toe as ttt
import random
import time

# Votre code pour la classe TTT ici...

class JeuInterface(tk.Tk):
    def __init__(self, jeu):
        super().__init__()
        self.title("Jeu Tic-Tac-Toe")
        self.jeu = jeu
        self.button_clicked_var = tk.StringVar()

        self.buttons = [[None for _ in range(self.jeu.m)] for _ in range(self.jeu.n)]

        for i in range(self.jeu.n):
            for j in range(self.jeu.m):
                self.buttons[i][j] = tk.Button(self, text="", font=('normal', 20), width=5, height=2, command=partial(self.on_button_click, i, j))
                self.buttons[i][j].grid(row=i, column=j)

        # self.jouer_partie_IA()

    def print_board(self):
        print(self)

    def on_button_click(self, row, col):
        if not self.jeu.is_valid_move(row, col):
            return

        self.jeu.play_move(row, col)
        self.buttons[row][col].config(text=self.symbol_for_player(self.jeu.next_player()))

        if self.jeu.gagnant(1) or self.jeu.gagnant(2) or self.jeu.nb_coup == self.jeu.n * self.jeu.m:
            self.show_winner()

        self.jeu.next_player()
        self.jeu.print_board()

        # Ajoutez ici l'appel à la fonction pour que l'IA joue automatiquement
        self.play_ia_move()


    def symbol_for_player(self, player):
        if player == 1:
            return 'X'
        elif player == 2:
            return "O"
        elif player == 3:
            return "▲"


    def show_winner(self):
        winner = self.jeu.get_winner()
        if winner == 0:
            result_text = "Match nul !"
        else:
            result_text = f"Joueur {winner} a gagné !"

        result_label = tk.Label(self, text=result_text, font=('normal', 14))
        result_label.grid(row=self.jeu.n, column=0, columnspan=self.jeu.m)


    def play_ia_move(self):
        # Ajoutez ici l'appel à la fonction de l'IA pour jouer automatiquement
        meilleur_coup = jeu.random_ai()
        meilleur_valeur = float('-inf')
        joueur = 2
        for lgn in range(jeu.n):
            for cln in range(jeu.m):
                if jeu.grid[lgn][cln] == 0:
                    jeu.grid[lgn][cln] = 2
                    valeur = jeu.min_max_IterativDeepening(3, float('-inf'), float('inf'), joueur)  # Profondeur à adapter ici 3
                    jeu.grid[lgn][cln] = 0

                    if valeur > meilleur_valeur:
                        meilleur_valeur = valeur
                        meilleur_coup = (lgn, cln)

        self.jeu.play_move(*meilleur_coup)
        self.buttons[lgn][cln].config(text=self.symbol_for_player(self.jeu.current_player()))

        if self.jeu.gagnant(1) or self.jeu.gagnant(2) or self.jeu.nb_coup == self.jeu.n * self.jeu.m:
            self.show_winner()

        self.jeu.next_player()
        self.jeu.print_board()



    def jouer_partie_IA(self):
        print("Vous jouez contre l'IA. Voici la grille de jeu :\n")
        print(self.jeu)

        joueur = int(input("Choisir : l'humain commence (1) | l'IA commence (2)"))

        while joueur != 0 and not self.jeu.gagnant(1) and not self.jeu.gagnant(2):
            if joueur == 1:
                print("\nTour du joueur humain.")
                self.wait_for_human_move()
            else:
                print("\nTour de l'IA.")
                self.play_ia_move()

            joueur = self.jeu.next_player()
            self.jeu.print_board()

        if self.jeu.gagnant(1):
            print("\nLe joueur humain a gagné !")
        elif self.jeu.gagnant(2):
            print("\nL'IA a gagné !")
        else:
            print("\nMatch nul !")

        
    def on_button_click(self, row, col):
        if not self.jeu.is_valid_move(row, col):
            return

        self.jeu.play_move(row, col)
        self.buttons[row][col].config(text=self.symbol_for_player(self.jeu.next_player()))

        if self.jeu.gagnant(1) or self.jeu.gagnant(2) or self.jeu.nb_coup == self.jeu.n * self.jeu.m:
            self.show_winner()

        self.jeu.next_player()
        self.jeu.print_board()

        # Mettre à jour la variable pour indiquer que le bouton a été cliqué
        self.button_clicked_var.set('clicked')


    def wait_for_human_move(self):
        # Désactiver tous les boutons pendant l'attente de l'entrée de l'utilisateur
        for i in range(self.jeu.n):
            for j in range(self.jeu.m):
                self.buttons[i][j].config(state=tk.DISABLED)

        # Variable pour stocker la position du coup de l'humain
        human_move = None

        # Fonction appelée lorsqu'un bouton est cliqué
        def on_button_click(row, col):
            nonlocal human_move
            human_move = (row, col)

        # Configurer les gestionnaires de clics pour chaque bouton
        for i in range(self.jeu.n):
            for j in range(self.jeu.m):
                self.buttons[i][j].config(command=partial(on_button_click, i, j))

        # Attendre que l'utilisateur clique sur un bouton
        self.wait_variable(self.button_clicked_var)

        # Réinitialiser les gestionnaires de clics
        for i in range(self.jeu.n):
            for j in range(self.jeu.m):
                self.buttons[i][j].config(command=lambda row=i, col=j: self.on_button_click(row, col))

        # Réactiver tous les boutons
        for i in range(self.jeu.n):
            for j in range(self.jeu.m):
                self.buttons[i][j].config(state=tk.NORMAL)

        return human_move
    

if __name__ == "__main__":
    # Supposons que vous ayez déjà votre classe de jeu (TTT) initialisée.
    jeu = ttt.TTT(4, 4, 3, 4)
    interface = JeuInterface(jeu)
    interface.jouer_partie_IA()
    print('problem')
    interface.mainloop()