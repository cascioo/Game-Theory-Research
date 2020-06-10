import csv
import sys
from AI import *
from Game import *

tic = TicTacToe()
con = ConnectFour()
strat = Stratego(40)

randomTic = AI(tic)
randomCon = AI(con)
defence1 = defenceTic(tic, 1)
defence2 = defenceTic(tic, -1)
offence1 = offenceTic(tic, 1)
offence2 = offenceTic(tic, -1)
minmax1 = MiniMax(tic, 1)
minmax2 = MiniMax(tic, -1)
dual1 = offdefTic(tic, 1)
dual2 = offdefTic(tic, -1)
centercorner = CenterCorner(tic)
center = Center(tic)

opp1 = baseStratego(strat, 1, 'yes')
opp2 = baseStratego(strat, 2, 'yes')
player = 1
wins = [0, 0, 0]
games_played = 0
opponents_1 = [randomTic, center, centercorner, defence1, offence1, dual1, minmax1]
opponents_2 = [randomTic, center, centercorner, defence2, offence2, dual2, minmax2]


def playGame(game, opponent1, opponent2, w, p):
    if sys.argv[1] == 'tic':
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
    elif sys.argv[1] == 'connect':
        while game.checkWin() is None:
            if p == 1:
                mv = opponent1.chooseMove()
                game.makeMove(mv, p)
                p = p * -1
            elif p == -1:
                mv = opponent2.chooseMove()
                game.makeMove(mv, p)
                p = p * -1

        if game.checkWin() == 1:
            w[0] += 1
        elif game.checkWin() == -1:
            w[1] += 1
        else:
            w[2] += 1
    elif sys.argv[1] == 'stratego':
        while game.checkWin() is None:
            if p == 1:
                mv = opponent1.chooseMove()
                game.makeMove(mv[0], mv[1], opponent1.player)
                p = p * -1
            elif p == -1:
                mv = opponent2.chooseMove()
                game.makeMove(mv[0], mv[1], opponent2.player)
                p = p * -1

        if game.checkWin() == 1:
            w[0] += 1
        elif game.checkWin() == -1:
            w[1] += 1
        else:
            w[2] += 1


data = []
for i in range(len(opponents_1) + 1):
    data.append([])

data[0].append('')
for i in opponents_2:
    data[0].append(i.getName())

for i in range(len(opponents_1)):
    data[i + 1].append(opponents_1[i].getName())

for i in range(len(opponents_1)):
    for j in range(len(opponents_2)):
        while games_played < 1000:
            if i == 6 or j == 6:
                pass
                # print(games_played)
            playGame(tic, opponents_1[i], opponents_2[j], wins, player)
            tic.resetBoard()
            player = 1
            games_played += 1
        print(opponents_1[i], opponents_2[j])
        print(wins)
        data[i + 1].append(str(wins[0]) + '-' + str(wins[1]) + '-' + str(wins[2]))
        games_played = 0
        player = 1
        wins = [0, 0, 0]

with open('data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',', quotechar=' ', quoting=csv.QUOTE_MINIMAL, escapechar=' ',
                        skipinitialspace=True)
    writer.writerows(data)
