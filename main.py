from Game import *
from AI import *
from math import pow
import numpy as np
import sys, csv

tic = TicTacToe()
con = ConnectFour()
strat = Stratego(40)

randomTic = AI(tic)
randomCon = AI(con)
defence1 = defenceTic(tic, 1)
defence2 = defenceTic(tic, -1)
offence1 = offenceTic(tic, 1)
offence2 = offenceTic(tic, -1)
minmax1 = minimax(tic, 1)
minmax2 = minimax(tic, -1)
dual1 = offdefTic(tic, 1)
dual2 = offdefTic(tic, -1)
centercorner = CenterCorner(tic)
center = Center(tic)

opp1 = baseStratego(strat, 1, 'yes')
opp2 = baseStratego(strat, 2, 'yes')
player = 1
wins = [0,0,0]
games_played = 0
opponents_1 = [randomTic, center, centercorner, defence1, offence1, dual1, minmax1]
opponents_2 = [randomTic, center, centercorner, defence2, offence2, dual2, minmax2]

def playGame(game, opponent1, opponent2, wins, player):
    if sys.argv[1] == 'tic':
        while game.checkWin() == None:
            if player == 1:
                move = opponent1.chooseMove()
                game.makeMove(move[0], move[1], player)
                player = player * -1
            elif player == -1:
                move = opponent2.chooseMove()
                game.makeMove(move[0], move[1], player)
                player = player * -1

        if game.checkWin() == 1:
            wins[0] += 1
        elif game.checkWin() == -1:
            wins[1] += 1
        else:
            wins[2] += 1
    elif sys.argv[1] == 'connect':
        while game.checkWin() == None:
            if player == 1:
                move = opponent1.chooseMove()
                game.makeMove(move, player)
                player = player * -1
            elif player == -1:
                move = opponent2.chooseMove()
                game.makeMove(move, player)
                player = player * -1

        if game.checkWin() == 1:
            wins[0] += 1
        elif game.checkWin() == -1:
            wins[1] += 1
        else:
            wins[2] += 1
    elif sys.argv[1] == 'stratego':
        while game.checkWin() == None:
            if player == 1:
                move = opponent1.chooseMove()
                game.makeMove(move[0], move[1], opponent1.player)
                player = player * -1
            elif player == -1:
                move = opponent2.chooseMove()
                game.makeMove(move[0], move[1], opponent2.player)
                player = player * -1

        if game.checkWin() == 1:
            wins[0] += 1
        elif game.checkWin() == -1:
            wins[1] += 1
        else:
            wins[2] += 1

'''
while games_played < 1000:
    if sys.argv[1] == 'stratego':
        if sys.argv[2] == 'yes': print(game)
        else: print(games_played)
        playGame(game, opp1, opp2, wins, player)
        if sys.argv[2] == 'yes': print(game)

        game.resetBoard()
        if sys.argv[1] == 'stratego':
            opp1 = baseStratego(game, 1, 'yes')
            opp2 = baseStratego(game, 2, 'yes')
        player = 1
        games_played += 1
print(wins)
'''
data = []
for i in range(len(opponents_1)+1):
    data.append([])

data[0].append('')
for i in opponents_2:
    data[0].append(i.getName())

for i in range(len(opponents_1)):
    data[i+1].append(opponents_1[i].getName())


for i in range(len(opponents_1)):
    for j in range(len(opponents_2)):
        while games_played < 1000:
            playGame(tic, opponents_1[i], opponents_2[j], wins, player)
            tic.resetBoard()
            player = 1
            games_played += 1
            #print(games_played)
        print(opponents_1[i], opponents_2[j])
        print(wins)
        data[i+1].append(str(wins[0])+'-'+str(wins[1])+'-'+str(wins[2]))
        games_played = 0
        player = 1
        wins = [0,0,0]

with open('data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',', quotechar=' ', quoting=csv.QUOTE_MINIMAL, escapechar = ' ', skipinitialspace = True)
    writer.writerows(data)