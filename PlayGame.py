from AI import *
from Game import *

# Games to play
tic = TicTacToe()
con = ConnectFour()

# Various opponents for TicTacToe
randomTic1 = AI(tic, 1)
randomTic2 = AI(tic, -1)
defense1 = defenseTic(tic, 1)
defense2 = defenseTic(tic, -1)
offense1 = offenseTic(tic, 1)
offense2 = offenseTic(tic, -1)
minmax1 = MiniMax(tic, 5, 1)
minmax2 = MiniMax(tic, 5, -1)
dual1 = offdefTic(tic, 1)
dual2 = offdefTic(tic, -1)
centercorner1 = CenterCorner(tic, 1)
centercorner2 = CenterCorner(tic, -1)
center1 = Center(tic, 1)
center2 = Center(tic, -1)
table1 = Q_Table("Q_Table_TicTacToe")
q1 = Q_Learning(tic, 1, table1, learning_rate=0, epsilon=0)
q2 = Q_Learning(tic, -1, table1, learning_rate=0, epsilon=0)

# Various opponents for Connect Four
randomCon_1 = AI(con, 1)
randomCon_2 = AI(con, -1)
copyCon_1 = copyBlock(con, 1)
copyCon_2 = copyBlock(con, -1)
MinMax2_1 = MiniMax(con, 2, 1)
MinMax2_2 = MiniMax(con, 2, -1)
MinMax3_1 = MiniMax(con, 3, 1)
MinMax3_2 = MiniMax(con, 3, -1)
MinMax4_1 = MiniMax(con, 4, 1)
MinMax4_2 = MiniMax(con, 4, -1)
table_c = Q_Table("Q_Table_570000")
qc1 = Q_Learning(con, 1, table_c, learning_rate=0, epsilon=0)
qc2 = Q_Learning(con, -1, table_c, learning_rate=0, epsilon=0)

# Choose game you want to play
g = con
# choose opponent from above list
opp1 = qc1
# Choose a second opponent if you want to watch it play
opp2 = qc2
# Change turn to set who goes first, 0 is computer, 1 is you
turn = 0
try:

    while g.checkWin() is None:
        print(g)
        if turn % 2 == 0:
            move = opp1.chooseMove()
            opp1.game.makeMove(move[0], move[1], 1)
            turn += 1
        else:
            if opp2:
                move = opp2.chooseMove()
                opp2.game.makeMove(move[0], move[1], -1)
                turn += 1
            else:
                move_row = int(input("Pick a row: "))
                move_col = int(input("Pick a column: "))
                g.makeMove(move_row, move_col, -1)
                turn += 1

    print(g)
except KeyboardInterrupt:
    pass