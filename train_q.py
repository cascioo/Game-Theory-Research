from AI import *
from Game import *

save_every = 10000
game = 0
wins = [0,0,0]
try:
    g = TicTacToe()
    table = Q_Table(start_table="Q_Table_1610000")
    opp1 = Q_Learning(g, 1, table, learning_rate=.2, discount_factor=.99, decay=0.000001, lr_decay=.000001, epsilon=.2)
    opp2 = Q_Learning(g, -1, table, learning_rate=.2, discount_factor=.99, decay=0.000001, lr_decay=.000001, epsilon=.2)
    while wins[2] <= .8*save_every:
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
        opp1.decay_epsilon()
        opp2.decay_epsilon()
        opp1.decay_lr()
        opp2.decay_lr()
        if game % save_every == 0:
            table.save_table(f"Q_Table_{game}")
            print(wins)
            print(opp1.EPSILON)
            wins = [0,0,0]
except KeyboardInterrupt:
    table.save_table(f"Q_Table_{game}")
    print(wins)
