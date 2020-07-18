from AI import *
from Game import *
iterations = 10000000
save_every = 10000
game = 0
wins = [0,0,0]
try:
    g = ConnectFour()
    table = Q_Table()
    opp1 = Q_Learning(g, 1, table, learning_rate=.1, discount_factor=.99, decay=0.0000003, lr_decay=0, epsilon=1)
    opp2 = Q_Learning(g, -1, table, learning_rate=.1, discount_factor=.99, decay=0.0000003, lr_decay=0, epsilon=1)
    while game <= iterations:
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
    table.save_table(f"Q_Table_{game}")
except KeyboardInterrupt:
    table.save_table(f"Q_Table_{game}")
    print(wins)
