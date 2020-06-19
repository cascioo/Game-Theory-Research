import csv
import sys
from AI import *
from Game import *

tic = TicTacToe()

randomTic = AI(tic)
defense1 = defenseTic(tic, 1)
defense2 = defenseTic(tic, -1)
offense1 = offenseTic(tic, 1)
offense2 = offenseTic(tic, -1)
minmax1 = MiniMax(tic, 3, 1)
minmax2 = MiniMax(tic, 3, -1)
dual1 = offdefTic(tic, 1)
dual2 = offdefTic(tic, -1)
centercorner = CenterCorner(tic)
center = Center(tic)
tic_opponents_1 = [randomTic, center, centercorner, defense1, offense1, dual1, minmax1]
tic_opponents_2 = [randomTic, center, centercorner, defense2, offense2, dual2, minmax2]


con = ConnectFour()
randomCon = AI(con)
copyCon_1 = copyBlock(con, 1)
copyCon_2 = copyBlock(con, -1)
MinMax3_1 = MiniMax(con, 3, 1)
MinMax3_2 = MiniMax(con, 3, -1)
MinMax4_1 = MiniMax(con, 4, 1)
MinMax4_2 = MiniMax(con, 4, -1)
MinMax5_1 = MiniMax(con, 5, 1)
MinMax5_2 = MiniMax(con, 5, -1)
con_opponents_1 = [randomCon, copyCon_1, MinMax3_1, MinMax4_1, MinMax5_1]
con_opponents_2 = [randomCon, copyCon_2, MinMax3_2, MinMax4_2, MinMax5_2]


strat = Stratego(40)
opp1 = baseStratego(strat, 1, 'yes')
opp2 = baseStratego(strat, 2, 'yes')

player = 1
wins = [0, 0, 0]
games_played = 0


def playGame(game, opponent1, opponent2, w, p):
    while game.checkWin() is None:
        if p == 1:
            mv = opponent1.chooseMove()
            game.makeMove(mv[0], mv[1], p)
            p = p * -1
        elif p == -1:
            mv = opponent2.chooseMove()
            game.makeMove(mv[0], mv[1], p)
            p = p * -1

    if game.checkWin() == 1:
        w[0] += 1
    elif game.checkWin() == -1:
        w[1] += 1
    else:
        w[2] += 1

try:
    data = []
    for i in range(len(con_opponents_1) + 1):
        data.append([])

    data[0].append('')
    for i in con_opponents_2:
        data[0].append(i.getName())

    for i in range(len(con_opponents_1)):
        data[i + 1].append(con_opponents_1[i].getName())

    for i in range(len(con_opponents_1)):
        for j in range(len(con_opponents_2)):
            while games_played < 1000:
                playGame(con, con_opponents_1[i], con_opponents_2[j], wins, player)
                con.resetBoard()
                player = 1
                games_played += 1
            print(con_opponents_1[i], con_opponents_2[j])
            print(wins)
            data[i + 1].append(str(wins[0]) + '-' + str(wins[1]) + '-' + str(wins[2]))
            games_played = 0
            player = 1
            wins = [0, 0, 0]

    with open('con_data.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quotechar=' ', quoting=csv.QUOTE_MINIMAL, escapechar=' ',
                            skipinitialspace=True)
        writer.writerows(data)
except KeyboardInterrupt:
    with open('con_data.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quotechar=' ', quoting=csv.QUOTE_MINIMAL, escapechar=' ',
                            skipinitialspace=True)
        writer.writerows(data)