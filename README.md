A simple generalized tic tac toe game (nmk game) with AI (minimax) with basic heuristic and iterativ deepening

2 PLAYERS:
- 1 human vs 1 human
- 1 human vs 1 AI
- 1 AI vs 1 AI

3 PLAYERS :
- 1 human vs 1 human vs 1 human
- 1 human vs 1 AI vs 1 human

TO PLAY :
- Execute the main file to play in the terminal (finished), use it to try everything
- Execute the main_ig file to play with graphics mode (tkinter but not finished)

ALGORITHM :
(all algorithm are in tic_tac_toe file)
  - Minimax with heuristic which compare the best possible alignments for the player and his opponent
  - Minimax with heuristic which compare the number of free case around the last played
  - Minimax with iterative deepening search (time limited) using the alignment heuristic
  - Basic MCTS which gives a score to each free cells in function of a number of randoms simulations


FILE FOR EACH MOD:
- Graphics mode uses the files main_ig.py, parameters.py, welcome_page.py and game_ig.py
- Terminal mode uses the files tic_tac_toe.py, jouer.py, exception.py and main.py


This is not optimized and well-written, I should have used more class like at least one for TicTacToe game, one for my heuristics and one for AIs
