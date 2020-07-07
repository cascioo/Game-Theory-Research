import csv
import datetime
from AI import *
from Game import *
from tqdm import tqdm
tic = TicTacToe()
con = ConnectFour
strat = Stratego(40)
check = Checkers()

randomTic1 = AI(tic, 1)
randomTic2 = AI(tic, -1)
defense1 = defenseTic(tic, 1)
defense2 = defenseTic(tic, -1)
offense1 = offenseTic(tic, 1)
offense2 = offenseTic(tic, -1)
minmax1 = MiniMax(tic, 3, 1)
minmax2 = MiniMax(tic, 3, -1)
dual1 = offdefTic(tic, 1)
dual2 = offdefTic(tic, -1)
centercorner1 = CenterCorner(tic, 1)
centercorner2 = CenterCorner(tic, -1)
center1 = Center(tic, 1)
center2 = Center(tic, -1)
tic_opponents_1 = [randomTic1, center1, centercorner1, defense1, offense1, dual1, minmax1]
tic_opponents_2 = [randomTic2, center2, centercorner2, defense2, offense2, dual2, minmax2]

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
con_opponents_1 = [randomCon_1, copyCon_1, MinMax2_1, MinMax3_1, MinMax4_1]
con_opponents_2 = [randomCon_2, copyCon_2, MinMax2_2, MinMax3_2, MinMax4_2]

opp1 = baseStratego(strat, 1, 'yes')
opp2 = baseStratego(strat, 2, 'yes')

check_opp1 = AI(check, 1)
check_opp2 = AI(check, -1)
check_opponents_1 = [check_opp1]
check_opponents_2 = [check_opp2]


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
    for i in range(len(check_opponents_1) + 1):
        data.append([])

    data[0].append('')
    for i in check_opponents_2:
        data[0].append(i.getName())

    for i in range(len(check_opponents_1)):
        data[i + 1].append(check_opponents_2[i].getName())

    for i in range(len(check_opponents_1)):
        for j in range(len(check_opponents_2)):
            for game_play in tqdm(range(1000)):
                playGame(check, check_opponents_1[i], check_opponents_2[j], wins, player)
                check.resetBoard()
                player = 1
            print(check_opponents_1[i], check_opponents_2[j])
            print(wins)
            data[i + 1].append(str(wins[0]) + '-' + str(wins[1]) + '-' + str(wins[2]))
            player = 1
            wins = [0, 0, 0]

    with open('check_data.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quotechar=' ', quoting=csv.QUOTE_MINIMAL, escapechar=' ',
                            skipinitialspace=True)
        writer.writerows(data)
except KeyboardInterrupt:
    with open('con_data.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quotechar=' ', quoting=csv.QUOTE_MINIMAL, escapechar=' ',
                            skipinitialspace=True)
        writer.writerows(data)