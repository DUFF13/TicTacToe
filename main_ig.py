from tkinter import *
# from firstpage import Firstpage 
import tic_tac_toe as ttt
from welcome_page import WelcomePage
import game_ig

def main():
    #Création d'une première fenêtre
    window = Tk()    
    # Création d'une instance de la classe TTT
    #welcome_page = firstpage(window)
    welcome_page = WelcomePage(window)
    
    
    #Personnalisation de la fenêtre
    window.title( "Morpion ")
    window.geometry("800x800")
    window.config(background= '#050C49')

    # Pas de redimmention de la fenêtre possible
    window.resizable(False, False)

    #création d'une barre de menu
    menu_bar = Menu(window)

    # créer un premier menu
    file_menu = Menu(menu_bar, tearoff = 0)
    file_menu.add_command(label = "Quitter", command = window.quit)
    menu_bar.add_cascade(label = "Fichier", menu = file_menu)

    # configuration de notre fenêtre pour ajuster ce menu bar
    window.config(menu = menu_bar)

    # afficher
    window.mainloop()



if __name__ == "__main__":
    main()
    


