The details of this project are listed in the document "TicTacMinimaxAB". This assignment contains some code and test programs written and provided by Dr. Frank Coyle, Associate Professor at SMU's Lyle School of Engineering. All the python code that he provided can be found in the folder "ABTicTac" I have built upon the base code to implement my own solution to the problems. A list of what I did in the project is below. 

This project aims to implement a smart bot for the multiplayer game Tic Tac Toe for which I used the Minimax algorithm, and then used alpha beta pruning to improve it's performance. The bot will hope to make each move so that each move takes it closer to victory.

1. I wrote the code for functions in RunMiniMax and RunMiniMaxAB classes. RunMiniMax class contains code for the implementation of a bot using Minimax algorithm. RunMiniMaxAB class improves the implementation of Minimax by adding alpha beta pruning to it.
   a. get_child_boards(board, char) - Return a list of the child boards as NumPy arrays where 1 means 'X' and -1 means 'O'. 
   b. evaluate(board) - Checks for winning condition. returns 1 for an X win, -1 for an O win or 0 for no win. 
   c. is_terminal_node(board) of the RunMiniMax and RunMiniMaxAB classes - checks if there is a winner or all positions filled.
2. ExtraCredit classes contains my own implementation to solve the problem. This further improves the performance of the code to finish off the game in less moves. 

