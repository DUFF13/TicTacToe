### A tic tc toe game built for our ENAC's project
import tic_tac_toe as ttt
import jouer


choose = """
1. Player vs Player (2 or 3 player)
2. Player vs AI (minimax and choose your heuristic or Monte Carlo)
3. AI vs AI
"""


if __name__ == '__main__':
    print('Welcome to our MNK game')



    choose_game = int(input(choose))
    if choose_game == 1:
        n, m = int(input("choose m the number of rows (by default : 3)") or '3'), int(input("Choose n the number of columns (by default : 3)") or '3') # j'ai inversé car le jeu s'appelle mnk et non nmk ...
        k = int(input("Choose k (by default : 3)") or '3')
        nb_player = int(input("2 or 3 players (by default 2)" or '2'))
        jeu = ttt.TTT(n, m, nb_player, k)

        jouer.jouer_partie(jeu)


    elif choose_game == 2:
        n, m = int(input("choose m the number of rows (by default : 3)") or '3'), int(input("Choose n the number of columns (by default : 3)") or '3') # j'ai inversé car le jeu s'appelle mnk et non nmk ...
        k = int(input("Choose k (by default : 3)") or '3')
        nb_player = (int(input("2 or 3 players (by default 2)" or '2')))
        jeu = ttt.TTT(n, m, nb_player, k)

        AI = int(input('Which AI do you want to try ? : (1 for Minimax with align heuristic, 2 for Minimax with iterativ deepening, 3 for minimax with empty_heuristic or 4 for MonteCarlo)'))
        if nb_player == 2:
            jouer.jouer_partie_IA(jeu, AI)
        else:
            jouer.jouer_partie_IA_3joueurs(jeu, AI)


    elif choose_game == 3:
        n, m = int(input("choose m the number of rows (by default : 3)") or '3'), int(input("Choose n the number of columns (by default : 3)") or '3') # j'ai inversé car le jeu s'appelle mnk et non nmk ...
        k = int(input("Choose k (by default : 3)") or '3')
        jeu = ttt.TTT(n, m, 2, k)
        print("For the moment only minimax with iterativ deepening against minimax")
        choose_h = "choose the heurisitc 1 and 2 : 1 for minimax with align heurisitc, 2 for minimax with iterativ deepening, 3 for empty_heuristic or 4 for MCTS"
        h1, h2 = int(input(choose_h)), int(input(choose_h))
        jouer.jouer_IA_vs_IA(jeu, h1, h2)





