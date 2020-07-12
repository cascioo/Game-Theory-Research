from AI import *
from Game import *

iteration = 100000
save_every = 1000
game = 0
wins = [0,0,0]
try:
    g = TicTacToe()
    opp1 = MiniMax(g, 4, 1)
    opp2 = Q_Learning(g, -1, start_table="Q_Table_10000_-1")
    while game <= iteration:
        turn = 0
        while g.checkWin() is None:
            if turn % 2 == 0:
                move = opp1.chooseMove()
                g.makeMove(move[0], move[1], 1)
                turn += 1
            else:
                move = opp2.chooseMove()
                g.makeMove(move[0], move[1], -1)
                turn += 1
        if g.checkWin() == 1:
            wins[0] += 1
        elif g.checkWin() == -1:
            wins[1] += 1
        else:
            wins[2] += 1
        g.resetBoard()
        game += 1
        if game % save_every == 0:
            opp2.save_table(f"Q_Table_{game}_{opp2.player}")
            print(wins)
except KeyboardInterrupt:
    opp2.save_table(f"Q_Table_{game}_{opp2.player}")
    print(wins)
