from tkinter import *
import tic_tac_toe as ttt


class IG(ttt.TTT) :              # class qui hérite de TTT
    def __init__(self, window, game) -> None:
        super().__init__(self.n, self.m, self.nb_player, self.k) #TODO PB ICI
        self.window = window
        self.game = game
        self.buttons = []
        self.current_player = 1  # Commence par joueur 1 ==> 'X'


        self.draw_grid()
        

    def switch_player(self) :
        if self.nb_player == 2:
            self.current_player = 'O' if self.current_player == 'X' else 'X'
        elif self.nb_player == 3:
            if self.current_player == 'X':
                self.current_player = 'O'
            elif self.current_player == 'O':
                self.current_player = '▲'
            else:
                self.current_player = 'X'
        return self.current_player


    def place_symbol(self, row, col):
        print("click", row, col)

        # on récupère le bouton avec sa position
        clicked_button = self.buttons[col][row]
        clicked_button.config(text= self.current_player)
        self.switch_player()

    def draw_grid(self):
        case = [] # liste des boutons ~ cases jouées (case par colone)
        for rows in range(self.n):
            for col in range(self.m):
                button = Button(self.window, font=("Arial", 50), 
                                width = 5, height = 3, 
                                command = lambda r = rows, 
                                c = col : self.place_symbol(r, c)
                                )
                button.grid(row=rows, culumn=col)
                case.append(button) # on ajoute à la liste des cases nos cases = button
            self.buttons.append(case) # on range ensuite dans chaque ligne nos buttons/cases

    



    def check_win(self):
        if self.game.gagnant(1):
            print("Le joueur 1 a gagné")
        elif self.game.gagnant(2):
            print("le joueur 2 a gagné")
        else:
            print("Match nul")


# Création d'une instance de la classe TTT
game = ttt.TTT(3,3,2,3)
#Création d'une première fenêtre
window = Tk()

#Création d'une instance de la classe IG
interface = IG(window, game)

game_ig = IG(window, game)

#Personnalisation de la fenêtre
window.title( "Morpion ")
window.geometry("1080x720")
window.minsize(500,500)
window.iconbitmap("tic-tac-toe.ico")
window.config(background='#FFFBD6')


# Reste de la personnalisation (optionnelle)

#création d'une barre de menu
menu_bar = Menu(window)

# créer un premier menu
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Quitter", command = window.quit)
menu_bar.add_cascade(label = "Fichier", menu= file_menu)

# configuration de notre fenêtre pour ajuster ce menu bar
window.config(menu = menu_bar)

# afficher
window.mainloop()









# création de variables de stockage
#buttons = game.grid
            





    # # création de la frame ~ sorte de boite où l'on met nos éléments visuels
    # frame = Frame(window, bg = '#FFFBD6')
    # # ajouter un text
    # label_title = Label(frame, text = "Bienvenue sur le jeu", font = ("Arial", 35), bg = "#FFFBD6", fg = "#050C49" )
    # label_title.pack() # empacter, pptés de positionnement

    # # ajout d'un second text
    # label_subtitle = Label(frame, text = "Morpion", font = ("Arial", 25), bg = "#FFFBD6", fg = "#050C49" )
    # label_subtitle.pack() # empacter, pptés de positionnement


    # # Ajout d'un bouton "jouer"
    # game_button = Button(frame, text = 'Jouer', font = ('Arial',30), bg = "white", fg = "#050C49")
    # game_button.pack()





# ajout du frame dans la fenêtre
#frame.pack(expand = YES   )


