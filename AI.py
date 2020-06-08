from Game import *
from math import inf
from random import choice, randint, shuffle
import json
from os import path
import os
from numba import jit


class AI():
    def __init__(self, game):
        self.game = game

    def __repr__(self):
        return "Random"

    def getName(self):
        return 'Random'

    def chooseMove(self):
        return choice(self.game.getMoves())


class minimax(AI):
    def __init__(self, game, player):
        self.player = player
        self.name = 'MinMax'
        self.count = 0
        super(minimax, self).__init__(game)

    def __repr__(self):
        return "MinMax"

    def minimax_helper(self, maxPlayer):
        if self.game.checkWin() != None:
            return self.game.checkWin() * 10

        if maxPlayer:
            value = -inf
            for move in self.game.getMoves():
                self.game.makeMove(move[0], move[1], 1)
                value = max(value, self.minimax_helper(False))
                self.game.resetMove(move[0], move[1])
            return value
        else:
            value = inf
            for move in self.game.getMoves():
                self.game.makeMove(move[0], move[1], -1)
                value = min(value, self.minimax_helper(True))
                self.game.resetMove(move[0], move[1])
            return value

    def minimax_helper_v2(self, maxPlayer, depth, alpha, beta):
        if self.game.checkWin() != None:
            self.count += 1
            if self.count % 100000 == 0:
                print(self.count)
            if self.game.checkWin() == 1:
                return 10 - depth
            elif self.game.checkWin() == -1:
                return -10 + depth
            else:
                return 0
        if maxPlayer:
            value = -inf
            for move in self.game.getMoves():
                self.game.makeMove(move[0], move[1], 1)
                eval = self.minimax_helper_v2(False, depth + 1, alpha, beta)
                self.game.resetMove(move[0], move[1])
                value = max(eval, value)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
            return value
        else:
            value = inf
            for move in self.game.getMoves():
                self.game.makeMove(move[0], move[1], -1)
                eval = self.minimax_helper_v2(True, depth + 1, alpha, beta)
                self.game.resetMove(move[0], move[1])
                value = min(eval, value)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
            return value

    def chooseMove(self):

        best_score = None
        best_move = None
        if self.player == 1:
            best_score = -inf
        else:
            best_score = inf

        for move in self.game.getMoves():
            if self.player == 1:
                self.game.makeMove(move[0], move[1], 1)
                temp = self.minimax_helper_v2(False, 0, -inf, inf)
                self.game.resetMove(move[0], move[1])
                if temp > best_score:
                    best_move = move
                    best_score = temp
            else:
                self.game.makeMove(move[0], move[1], -1)
                temp = self.minimax_helper_v2(True, 0, -inf, inf)
                self.game.resetMove(move[0], move[1])
                if temp < best_score:
                    best_move = move
                    best_score = temp

        return best_move


class MatchBox(AI):
    def __init__(self, game, player):
        super(MatchBox, self).__init__(game)
        if path.exists('weights.json'):
            infile = open("weights.json", 'r')
            self.states = json.load(infile)
            self.player = player
        else:
            self.makeDefaults()
            self.__init__(game, 1)

    def playGame(self):
        turn = 0
        moves_1 = []
        moves_2 = []
        done = False
        while self.game.getMoves() or not done:
            curr_state = self.convert(self.game.board)
            options = self.states[curr_state]
            if len(options) == 0:
                done = True
                break
            choosen = choice(options)
            if turn % 2 == 0:
                moves_1.append([curr_state, choosen])
                self.makeMove(choosen, 1)
            elif turn % 2 == 1:
                moves_2.append([curr_state, choosen])
                self.makeMove(choosen, 2)
            turn += 1
            winner = self.game.checkWin()
            if winner == None:
                pass
            elif winner == 1:
                for move in moves_1:
                    for i in range(len(self.states[move[0]])):
                        if self.states[move[0]][i] == move[1]:
                            self.states[move[0]].extend([i, i, i])
                for move in moves_2:
                    continue
                    total = len(self.states[move[0]])
                    for i in range(total):
                        if self.states[move[0]][i] == move[1]:
                            self.states[move[0]].remove(i)
                            i = total
                done = True
            elif winner == -1:
                for move in moves_2:
                    for i in range(len(self.states[move[0]])):
                        if self.states[move[0]][i] == move[1]:
                            self.states[move[0]].extend([i, i, i])
                for move in moves_1:
                    continue
                    total = len(self.states[move[0]])
                    for i in range(total):
                        if self.states[move[0]][i] == move[1]:
                            self.states[move[0]].remove(i)
                            i = total
                done = True
            elif winner == 0:
                done = True

    def reset(self):
        for i in range(3):
            for j in range(3):
                self.game.board[i][j] == 0

    def train(self):
        for i in range(10000):
            self.playGame()
            # print(self.game.board)
            self.reset()
        os.remove('weights.json')
        with open('weights.json', 'w') as outfile:
            json.dump(self.states, outfile)

    def makeMove(self, a, player):
        row = a // 3
        col = a % 3
        if player == 1:
            self.game.makeMove(row, col, 1)
        elif player == 2:
            self.game.makeMove(row, col, -1)

    def convert(self, board):
        temp = ""
        for i in range(self.game.getRow()):
            for j in range(self.game.getCol()):
                if board[i][j] == -1:
                    temp = temp + '2'
                else:
                    temp = temp + str(board[i][j])[0]
        return temp

    def helper(self, array, player, outfile):
        for i in range(9):
            if array[i] == '0':
                if player == 1:
                    array[i] = '1'
                    outfile.writelines(
                        array[0] + array[1] + array[2] + array[3] + array[4] + array[5] + array[6] + array[7] + array[
                            8] + '\n')
                    self.helper(array, player * -1, outfile)
                    array[i] = '0'
                elif player == -1:
                    array[i] = '2'
                    outfile.write(
                        array[0] + array[1] + array[2] + array[3] + array[4] + array[5] + array[6] + array[7] + array[
                            8] + '\n')
                    self.helper(array, player * -1, outfile)
                    array[i] = '0'

    def makeDefaults(self):
        with open('weights.txt', 'w') as outfile:
            outfile.write('000000000\n')
            self.helper(['0', '0', '0', '0', '0', '0', '0', '0', '0'], 1, outfile)

        states = {}
        with open('weights.txt', 'r') as infile:
            for line in infile:
                moves = []
                for i in range(9):
                    if line[i] == '0':
                        moves.append(i)
                states[line[:9]] = moves

        with open('weights.json', 'w') as outfile:
            json.dump(states, outfile)


class CenterCorner(AI):
    def __init__(self, game):
        self.name = 'CenterCorner'
        super(CenterCorner, self).__init__(game)

    def getName(self):
        return self.name

    def __repr__(self):
        return "CenterCorner"

    def chooseMove(self):
        if (1, 1) in self.game.getMoves():
            return (1, 1)
        elif (0, 0) in self.game.getMoves() or (2, 0) in self.game.getMoves() or (0, 2) in self.game.getMoves() or (
        2, 2) in self.game.getMoves():
            pick = choice([(0, 0), (2, 0), (0, 2), (2, 2)])
            while pick not in self.game.getMoves():
                pick = choice([(0, 0), (2, 0), (0, 2), (2, 2)])
            return pick
        elif (1, 0) in self.game.getMoves() or (0, 1) in self.game.getMoves() or (1, 2) in self.game.getMoves() or (
        2, 1) in self.game.getMoves():
            pick = choice([(1, 0), (0, 1), (1, 2), (2, 1)])
            while pick not in self.game.getMoves():
                pick = choice([(1, 0), (0, 1), (1, 2), (2, 1)])
            return pick


class Center(AI):
    def __init__(self, game):
        self.name = "Center"
        super(Center, self).__init__(game)

    def __repr__(self):
        return "Center"

    def getName(self):
        return self.name

    def chooseMove(self):
        if (1, 1) in self.game.getMoves():
            return (1, 1)
        else:
            return choice(self.game.getMoves())


class baseStratego(AI):
    def __init__(self, game, player, debug):
        super(baseStratego, self).__init__(game)
        self.name = 'baseStratego'
        self.player = player
        if debug == "yes":
            self.setupAuto()
        else:
            self.setup()

    def getName(self):
        return self.name

    def setupAuto(self):
        spots = []
        for i in range(self.game.version):
            spots.append(i)

        shuffle(spots)

        if self.player == 1:
            for i in range(len(self.game.player1)):
                self.game.player1[i][1] = [spots[i] // 10, spots[i] % 10]
        else:
            for i in range(len(self.game.player2)):
                self.game.player2[i][1] = [spots[i] // 10 + 6, spots[i] % 10]

    def setup(self):
        if self.player == 1:
            for j in range(4):
                for i in range(10):
                    self.game.board[j][i] = j * 10 + i
        else:
            for j in range(4):
                for i in range(10):
                    self.game.board[j + 6][i] = j * 10 + i

        if self.player == 1:
            for i in range(len(self.game.player1)):
                pick = int(input("Pick a place for {}: ".format(self.game.player1[i][0])))
                self.game.player1[i][1] = [pick // 10, pick % 10]
        else:
            for i in range(len(self.game.player2)):
                print(self.game)
                pick = int(input("Pick a place for {}: ".format(self.game.player2[i][0])))
                self.game.player2[i][1] = [pick // 10 + 6, pick % 10]

    def chooseMove(self):
        moves = []
        if self.player == 1:
            for i in self.game.player1:
                possibleMoves = self.game.listMoves(i[1][0], i[1][1], self.player)
                for j in possibleMoves:
                    moves.append([i[1], j])
        else:
            for i in self.game.player2:
                possibleMoves = self.game.listMoves(i[1][0], i[1][1], self.player)
                for j in possibleMoves:
                    moves.append([i[1], j])

        pick = choice(moves)
        return pick


class manual(AI):
    def __init__(self, game, player):
        self.name = 'Manual'
        super(manual, self).__init__(game)
        self.player = player

    def __repr__(self):
        return "Manual"

    def getName(self):
        return self.name

    def chooseMove(self):
        print(game)
        if game.getName() == 'TicTacToe':
            print('Picking a move')
            move = int(input("Make a move: "))
            game.makeMove(move // 3, move % 3, self.player)
        elif game.getName() == 'ConnectFour':
            print('Picking a move')
            move = int(input("Make a move: "))
            game.makeMove(move, self.player)


class defenceTic(AI):
    def __init__(self, game, player):
        super(defenceTic, self).__init__(game)
        self.player = player
        self.name = 'Defense'

    def __repr__(self):
        return self.name

    def getName(self):
        return self.name

    def chooseMove(self):
        if self.player == 1:
            if self.game.board[0][1] == self.game.board[0][2] == -1 and self.game.board[0][0] == 0 or \
                    self.game.board[1][0] == self.game.board[2][0] == -1 and self.game.board[0][0] == 0 or \
                    self.game.board[1][1] == self.game.board[2][2] == -1 and self.game.board[0][0] == 0:
                return [0, 0]
            elif self.game.board[0][0] == self.game.board[0][2] == -1 and self.game.board[0][1] == 0 or \
                    self.game.board[1][1] == self.game.board[1][2] == -1 and self.game.board[0][1] == 0:
                return [0, 1]
            elif self.game.board[0][0] == self.game.board[0][1] == -1 and self.game.board[0][2] == 0 or \
                    self.game.board[2][0] == self.game.board[1][1] == -1 and self.game.board[0][2] == 0 or \
                    self.game.board[1][2] == self.game.board[2][2] == -1 and self.game.board[0][2] == 0:
                return [0, 2]
            elif self.game.board[1][1] == self.game.board[1][2] == -1 and self.game.board[1][0] == 0 or \
                    self.game.board[0][0] == self.game.board[2][0] == -1 and self.game.board[1][0] == 0:
                return [1, 0]
            elif self.game.board[0][0] == self.game.board[2][2] == -1 and self.game.board[1][1] == 0 or \
                    self.game.board[0][2] == self.game.board[2][0] == -1 and self.game.board[1][1] == 0 or \
                    self.game.board[1][0] == self.game.board[1][2] == -1 and self.game.board[1][1] == 0 or \
                    self.game.board[0][1] == self.game.board[2][1] == -1 and self.game.board[1][1] == 0:
                return [1, 1]
            elif self.game.board[0][2] == self.game.board[2][2] == -1 and self.game.board[1][2] == 0 or \
                    self.game.board[1][0] == self.game.board[1][1] == -1 and self.game.board[1][2] == 0:
                return [1, 2]
            elif self.game.board[0][0] == self.game.board[1][0] == -1 and self.game.board[2][0] == 0 or \
                    self.game.board[2][1] == self.game.board[2][2] == -1 and self.game.board[2][0] == 0 or \
                    self.game.board[1][1] == self.game.board[0][2] == -1 and self.game.board[2][0] == 0:
                return [2, 0]
            elif self.game.board[0][1] == self.game.board[1][1] == -1 and self.game.board[2][1] == 0 or \
                    self.game.board[2][0] == self.game.board[2][2] == -1 and self.game.board[2][1] == 0:
                return [2, 1]
            elif self.game.board[0][0] == self.game.board[1][1] == -1 and self.game.board[2][2] == 0 or \
                    self.game.board[2][0] == self.game.board[2][1] == -1 and self.game.board[2][2] == 0 or \
                    self.game.board[0][2] == self.game.board[1][2] == -1 and self.game.board[2][2] == 0:
                return [2, 2]
        else:
            if self.game.board[0][1] == self.game.board[0][2] == 1 and self.game.board[0][0] == 0 or self.game.board[1][
                0] == self.game.board[2][0] == 1 and self.game.board[0][0] == 0 or self.game.board[1][1] == \
                    self.game.board[2][2] == 1 and self.game.board[0][0] == 0:
                return [0, 0]
            elif self.game.board[0][0] == self.game.board[0][2] == 1 and self.game.board[0][1] == 0 or \
                    self.game.board[1][1] == self.game.board[1][2] == 1 and self.game.board[0][1] == 0:
                return [0, 1]
            elif self.game.board[0][0] == self.game.board[0][1] == 1 and self.game.board[0][2] == 0 or \
                    self.game.board[2][0] == self.game.board[1][1] == 1 and self.game.board[0][2] == 0 or \
                    self.game.board[1][2] == self.game.board[2][2] == 1 and self.game.board[0][2] == 0:
                return [0, 2]
            elif self.game.board[1][1] == self.game.board[1][2] == 1 and self.game.board[1][0] == 0 or \
                    self.game.board[0][0] == self.game.board[2][0] == 1 and self.game.board[1][0] == 0:
                return [1, 0]
            elif self.game.board[0][0] == self.game.board[2][2] == 1 and self.game.board[1][1] == 0 or \
                    self.game.board[0][2] == self.game.board[2][0] == 1 and self.game.board[1][1] == 0 or \
                    self.game.board[1][0] == self.game.board[1][2] == 1 and self.game.board[1][1] == 0 or \
                    self.game.board[0][1] == self.game.board[2][1] == 1 and self.game.board[1][1] == 0:
                return [1, 1]
            elif self.game.board[0][2] == self.game.board[2][2] == 1 and self.game.board[1][2] == 0 or \
                    self.game.board[1][0] == self.game.board[1][1] == 1 and self.game.board[1][2] == 0:
                return [1, 2]
            elif self.game.board[0][0] == self.game.board[1][0] == 1 and self.game.board[2][0] == 0 or \
                    self.game.board[2][1] == self.game.board[2][2] == 1 and self.game.board[2][0] == 0 or \
                    self.game.board[1][1] == self.game.board[0][2] == 1 and self.game.board[2][0] == 0:
                return [2, 0]
            elif self.game.board[0][1] == self.game.board[1][1] == 1 and self.game.board[2][1] == 0 or \
                    self.game.board[2][0] == self.game.board[2][2] == 1 and self.game.board[2][1] == 0:
                return [2, 1]
            elif self.game.board[0][0] == self.game.board[1][1] == 1 and self.game.board[2][2] == 0 or \
                    self.game.board[2][0] == self.game.board[2][1] == 1 and self.game.board[2][2] == 0 or \
                    self.game.board[0][2] == self.game.board[1][2] == 1 and self.game.board[2][2] == 0:
                return [2, 2]

        return choice(self.game.getMoves())


class offenceTic(AI):
    def __init__(self, game, player):
        super(offenceTic, self).__init__(game)
        self.player = player
        self.name = 'Offense'

    def __repr__(self):
        return self.name

    def getName(self):
        return self.name

    def chooseMove(self):
        if self.player == -1:
            if self.game.board[0][1] == self.game.board[0][2] == -1 and self.game.board[0][0] == 0 or \
                    self.game.board[1][0] == self.game.board[2][0] == -1 and self.game.board[0][0] == 0 or \
                    self.game.board[1][1] == self.game.board[2][2] == -1 and self.game.board[0][0] == 0:
                return [0, 0]
            elif self.game.board[0][0] == self.game.board[0][2] == -1 and self.game.board[0][1] == 0 or \
                    self.game.board[1][1] == self.game.board[1][2] == -1 and self.game.board[0][1] == 0:
                return [0, 1]
            elif self.game.board[0][0] == self.game.board[0][1] == -1 and self.game.board[0][2] == 0 or \
                    self.game.board[2][0] == self.game.board[1][1] == -1 and self.game.board[0][2] == 0 or \
                    self.game.board[1][2] == self.game.board[2][2] == -1 and self.game.board[0][2] == 0:
                return [0, 2]
            elif self.game.board[1][1] == self.game.board[1][2] == -1 and self.game.board[1][0] == 0 or \
                    self.game.board[0][0] == self.game.board[2][0] == -1 and self.game.board[1][0] == 0:
                return [1, 0]
            elif self.game.board[0][0] == self.game.board[2][2] == -1 and self.game.board[1][1] == 0 or \
                    self.game.board[0][2] == self.game.board[2][0] == -1 and self.game.board[1][1] == 0 or \
                    self.game.board[1][0] == self.game.board[1][2] == -1 and self.game.board[1][1] == 0 or \
                    self.game.board[0][1] == self.game.board[2][1] == -1 and self.game.board[1][1] == 0:
                return [1, 1]
            elif self.game.board[0][2] == self.game.board[2][2] == -1 and self.game.board[1][2] == 0 or \
                    self.game.board[1][0] == self.game.board[1][1] == -1 and self.game.board[1][2] == 0:
                return [1, 2]
            elif self.game.board[0][0] == self.game.board[1][0] == -1 and self.game.board[2][0] == 0 or \
                    self.game.board[2][1] == self.game.board[2][2] == -1 and self.game.board[2][0] == 0 or \
                    self.game.board[1][1] == self.game.board[0][2] == -1 and self.game.board[2][0] == 0:
                return [2, 0]
            elif self.game.board[0][1] == self.game.board[1][1] == -1 and self.game.board[2][1] == 0 or \
                    self.game.board[2][0] == self.game.board[2][2] == -1 and self.game.board[2][1] == 0:
                return [2, 1]
            elif self.game.board[0][0] == self.game.board[1][1] == -1 and self.game.board[2][2] == 0 or \
                    self.game.board[2][0] == self.game.board[2][1] == -1 and self.game.board[2][2] == 0 or \
                    self.game.board[0][2] == self.game.board[1][2] == -1 and self.game.board[2][2] == 0:
                return [2, 2]
        else:
            if self.game.board[0][1] == self.game.board[0][2] == 1 and self.game.board[0][0] == 0 or self.game.board[1][
                0] == self.game.board[2][0] == 1 and self.game.board[0][0] == 0 or self.game.board[1][1] == \
                    self.game.board[2][2] == 1 and self.game.board[0][0] == 0:
                return [0, 0]
            elif self.game.board[0][0] == self.game.board[0][2] == 1 and self.game.board[0][1] == 0 or \
                    self.game.board[1][1] == self.game.board[1][2] == 1 and self.game.board[0][1] == 0:
                return [0, 1]
            elif self.game.board[0][0] == self.game.board[0][1] == 1 and self.game.board[0][2] == 0 or \
                    self.game.board[2][0] == self.game.board[1][1] == 1 and self.game.board[0][2] == 0 or \
                    self.game.board[1][2] == self.game.board[2][2] == 1 and self.game.board[0][2] == 0:
                return [0, 2]
            elif self.game.board[1][1] == self.game.board[1][2] == 1 and self.game.board[1][0] == 0 or \
                    self.game.board[0][0] == self.game.board[2][0] == 1 and self.game.board[1][0] == 0:
                return [1, 0]
            elif self.game.board[0][0] == self.game.board[2][2] == 1 and self.game.board[1][1] == 0 or \
                    self.game.board[0][2] == self.game.board[2][0] == 1 and self.game.board[1][1] == 0 or \
                    self.game.board[1][0] == self.game.board[1][2] == 1 and self.game.board[1][1] == 0 or \
                    self.game.board[0][1] == self.game.board[2][1] == 1 and self.game.board[1][1] == 0:
                return [1, 1]
            elif self.game.board[0][2] == self.game.board[2][2] == 1 and self.game.board[1][2] == 0 or \
                    self.game.board[1][0] == self.game.board[1][1] == 1 and self.game.board[1][2] == 0:
                return [1, 2]
            elif self.game.board[0][0] == self.game.board[1][0] == 1 and self.game.board[2][0] == 0 or \
                    self.game.board[2][1] == self.game.board[2][2] == 1 and self.game.board[2][0] == 0 or \
                    self.game.board[1][1] == self.game.board[0][2] == 1 and self.game.board[2][0] == 0:
                return [2, 0]
            elif self.game.board[0][1] == self.game.board[1][1] == 1 and self.game.board[2][1] == 0 or \
                    self.game.board[2][0] == self.game.board[2][2] == 1 and self.game.board[2][1] == 0:
                return [2, 1]
            elif self.game.board[0][0] == self.game.board[1][1] == 1 and self.game.board[2][2] == 0 or \
                    self.game.board[2][0] == self.game.board[2][1] == 1 and self.game.board[2][2] == 0 or \
                    self.game.board[0][2] == self.game.board[1][2] == 1 and self.game.board[2][2] == 0:
                return [2, 2]

        return choice(self.game.getMoves())


class offdefTic(AI):
    def __init__(self, game, player):
        super(offdefTic, self).__init__(game)
        self.player = player
        self.name = 'OffenseDefense'

    def __repr__(self):
        return self.name

    def getName(self):
        return self.name

    def chooseMove(self):
        if self.player == -1:
            if self.game.board[0][1] == self.game.board[0][2] == -1 and self.game.board[0][0] == 0 or \
                    self.game.board[1][0] == self.game.board[2][0] == -1 and self.game.board[0][0] == 0 or \
                    self.game.board[1][1] == self.game.board[2][2] == -1 and self.game.board[0][0] == 0:
                return [0, 0]
            elif self.game.board[0][0] == self.game.board[0][2] == -1 and self.game.board[0][1] == 0 or \
                    self.game.board[1][1] == self.game.board[1][2] == -1 and self.game.board[0][1] == 0:
                return [0, 1]
            elif self.game.board[0][0] == self.game.board[0][1] == -1 and self.game.board[0][2] == 0 or \
                    self.game.board[2][0] == self.game.board[1][1] == -1 and self.game.board[0][2] == 0 or \
                    self.game.board[1][2] == self.game.board[2][2] == -1 and self.game.board[0][2] == 0:
                return [0, 2]
            elif self.game.board[1][1] == self.game.board[1][2] == -1 and self.game.board[1][0] == 0 or \
                    self.game.board[0][0] == self.game.board[2][0] == -1 and self.game.board[1][0] == 0:
                return [1, 0]
            elif self.game.board[0][0] == self.game.board[2][2] == -1 and self.game.board[1][1] == 0 or \
                    self.game.board[0][2] == self.game.board[2][0] == -1 and self.game.board[1][1] == 0 or \
                    self.game.board[1][0] == self.game.board[1][2] == -1 and self.game.board[1][1] == 0 or \
                    self.game.board[0][1] == self.game.board[2][1] == -1 and self.game.board[1][1] == 0:
                return [1, 1]
            elif self.game.board[0][2] == self.game.board[2][2] == -1 and self.game.board[1][2] == 0 or \
                    self.game.board[1][0] == self.game.board[1][1] == -1 and self.game.board[1][2] == 0:
                return [1, 2]
            elif self.game.board[0][0] == self.game.board[1][0] == -1 and self.game.board[2][0] == 0 or \
                    self.game.board[2][1] == self.game.board[2][2] == -1 and self.game.board[2][0] == 0 or \
                    self.game.board[1][1] == self.game.board[0][2] == -1 and self.game.board[2][0] == 0:
                return [2, 0]
            elif self.game.board[0][1] == self.game.board[1][1] == -1 and self.game.board[2][1] == 0 or \
                    self.game.board[2][0] == self.game.board[2][2] == -1 and self.game.board[2][1] == 0:
                return [2, 1]
            elif self.game.board[0][0] == self.game.board[1][1] == -1 and self.game.board[2][2] == 0 or \
                    self.game.board[2][0] == self.game.board[2][1] == -1 and self.game.board[2][2] == 0 or \
                    self.game.board[0][2] == self.game.board[1][2] == -1 and self.game.board[2][2] == 0:
                return [2, 2]
        else:
            if self.game.board[0][1] == self.game.board[0][2] == 1 and self.game.board[0][0] == 0 or self.game.board[1][
                0] == self.game.board[2][0] == 1 and self.game.board[0][0] == 0 or self.game.board[1][1] == \
                    self.game.board[2][2] == 1 and self.game.board[0][0] == 0:
                return [0, 0]
            elif self.game.board[0][0] == self.game.board[0][2] == 1 and self.game.board[0][1] == 0 or \
                    self.game.board[1][1] == self.game.board[1][2] == 1 and self.game.board[0][1] == 0:
                return [0, 1]
            elif self.game.board[0][0] == self.game.board[0][1] == 1 and self.game.board[0][2] == 0 or \
                    self.game.board[2][0] == self.game.board[1][1] == 1 and self.game.board[0][2] == 0 or \
                    self.game.board[1][2] == self.game.board[2][2] == 1 and self.game.board[0][2] == 0:
                return [0, 2]
            elif self.game.board[1][1] == self.game.board[1][2] == 1 and self.game.board[1][0] == 0 or \
                    self.game.board[0][0] == self.game.board[2][0] == 1 and self.game.board[1][0] == 0:
                return [1, 0]
            elif self.game.board[0][0] == self.game.board[2][2] == 1 and self.game.board[1][1] == 0 or \
                    self.game.board[0][2] == self.game.board[2][0] == 1 and self.game.board[1][1] == 0 or \
                    self.game.board[1][0] == self.game.board[1][2] == 1 and self.game.board[1][1] == 0 or \
                    self.game.board[0][1] == self.game.board[2][1] == 1 and self.game.board[1][1] == 0:
                return [1, 1]
            elif self.game.board[0][2] == self.game.board[2][2] == 1 and self.game.board[1][2] == 0 or \
                    self.game.board[1][0] == self.game.board[1][1] == 1 and self.game.board[1][2] == 0:
                return [1, 2]
            elif self.game.board[0][0] == self.game.board[1][0] == 1 and self.game.board[2][0] == 0 or \
                    self.game.board[2][1] == self.game.board[2][2] == 1 and self.game.board[2][0] == 0 or \
                    self.game.board[1][1] == self.game.board[0][2] == 1 and self.game.board[2][0] == 0:
                return [2, 0]
            elif self.game.board[0][1] == self.game.board[1][1] == 1 and self.game.board[2][1] == 0 or \
                    self.game.board[2][0] == self.game.board[2][2] == 1 and self.game.board[2][1] == 0:
                return [2, 1]
            elif self.game.board[0][0] == self.game.board[1][1] == 1 and self.game.board[2][2] == 0 or \
                    self.game.board[2][0] == self.game.board[2][1] == 1 and self.game.board[2][2] == 0 or \
                    self.game.board[0][2] == self.game.board[1][2] == 1 and self.game.board[2][2] == 0:
                return [2, 2]

        if self.player == 1:
            if self.game.board[0][1] == self.game.board[0][2] == -1 and self.game.board[0][0] == 0 or \
                    self.game.board[1][0] == self.game.board[2][0] == -1 and self.game.board[0][0] == 0 or \
                    self.game.board[1][1] == self.game.board[2][2] == -1 and self.game.board[0][0] == 0:
                return [0, 0]
            elif self.game.board[0][0] == self.game.board[0][2] == -1 and self.game.board[0][1] == 0 or \
                    self.game.board[1][1] == self.game.board[1][2] == -1 and self.game.board[0][1] == 0:
                return [0, 1]
            elif self.game.board[0][0] == self.game.board[0][1] == -1 and self.game.board[0][2] == 0 or \
                    self.game.board[2][0] == self.game.board[1][1] == -1 and self.game.board[0][2] == 0 or \
                    self.game.board[1][2] == self.game.board[2][2] == -1 and self.game.board[0][2] == 0:
                return [0, 2]
            elif self.game.board[1][1] == self.game.board[1][2] == -1 and self.game.board[1][0] == 0 or \
                    self.game.board[0][0] == self.game.board[2][0] == -1 and self.game.board[1][0] == 0:
                return [1, 0]
            elif self.game.board[0][0] == self.game.board[2][2] == -1 and self.game.board[1][1] == 0 or \
                    self.game.board[0][2] == self.game.board[2][0] == -1 and self.game.board[1][1] == 0 or \
                    self.game.board[1][0] == self.game.board[1][2] == -1 and self.game.board[1][1] == 0 or \
                    self.game.board[0][1] == self.game.board[2][1] == -1 and self.game.board[1][1] == 0:
                return [1, 1]
            elif self.game.board[0][2] == self.game.board[2][2] == -1 and self.game.board[1][2] == 0 or \
                    self.game.board[1][0] == self.game.board[1][1] == -1 and self.game.board[1][2] == 0:
                return [1, 2]
            elif self.game.board[0][0] == self.game.board[1][0] == -1 and self.game.board[2][0] == 0 or \
                    self.game.board[2][1] == self.game.board[2][2] == -1 and self.game.board[2][0] == 0 or \
                    self.game.board[1][1] == self.game.board[0][2] == -1 and self.game.board[2][0] == 0:
                return [2, 0]
            elif self.game.board[0][1] == self.game.board[1][1] == -1 and self.game.board[2][1] == 0 or \
                    self.game.board[2][0] == self.game.board[2][2] == -1 and self.game.board[2][1] == 0:
                return [2, 1]
            elif self.game.board[0][0] == self.game.board[1][1] == -1 and self.game.board[2][2] == 0 or \
                    self.game.board[2][0] == self.game.board[2][1] == -1 and self.game.board[2][2] == 0 or \
                    self.game.board[0][2] == self.game.board[1][2] == -1 and self.game.board[2][2] == 0:
                return [2, 2]
        else:
            if self.game.board[0][1] == self.game.board[0][2] == 1 and self.game.board[0][0] == 0 or self.game.board[1][
                0] == self.game.board[2][0] == 1 and self.game.board[0][0] == 0 or self.game.board[1][1] == \
                    self.game.board[2][2] == 1 and self.game.board[0][0] == 0:
                return [0, 0]
            elif self.game.board[0][0] == self.game.board[0][2] == 1 and self.game.board[0][1] == 0 or \
                    self.game.board[1][1] == self.game.board[1][2] == 1 and self.game.board[0][1] == 0:
                return [0, 1]
            elif self.game.board[0][0] == self.game.board[0][1] == 1 and self.game.board[0][2] == 0 or \
                    self.game.board[2][0] == self.game.board[1][1] == 1 and self.game.board[0][2] == 0 or \
                    self.game.board[1][2] == self.game.board[2][2] == 1 and self.game.board[0][2] == 0:
                return [0, 2]
            elif self.game.board[1][1] == self.game.board[1][2] == 1 and self.game.board[1][0] == 0 or \
                    self.game.board[0][0] == self.game.board[2][0] == 1 and self.game.board[1][0] == 0:
                return [1, 0]
            elif self.game.board[0][0] == self.game.board[2][2] == 1 and self.game.board[1][1] == 0 or \
                    self.game.board[0][2] == self.game.board[2][0] == 1 and self.game.board[1][1] == 0 or \
                    self.game.board[1][0] == self.game.board[1][2] == 1 and self.game.board[1][1] == 0 or \
                    self.game.board[0][1] == self.game.board[2][1] == 1 and self.game.board[1][1] == 0:
                return [1, 1]
            elif self.game.board[0][2] == self.game.board[2][2] == 1 and self.game.board[1][2] == 0 or \
                    self.game.board[1][0] == self.game.board[1][1] == 1 and self.game.board[1][2] == 0:
                return [1, 2]
            elif self.game.board[0][0] == self.game.board[1][0] == 1 and self.game.board[2][0] == 0 or \
                    self.game.board[2][1] == self.game.board[2][2] == 1 and self.game.board[2][0] == 0 or \
                    self.game.board[1][1] == self.game.board[0][2] == 1 and self.game.board[2][0] == 0:
                return [2, 0]
            elif self.game.board[0][1] == self.game.board[1][1] == 1 and self.game.board[2][1] == 0 or \
                    self.game.board[2][0] == self.game.board[2][2] == 1 and self.game.board[2][1] == 0:
                return [2, 1]
            elif self.game.board[0][0] == self.game.board[1][1] == 1 and self.game.board[2][2] == 0 or \
                    self.game.board[2][0] == self.game.board[2][1] == 1 and self.game.board[2][2] == 0 or \
                    self.game.board[0][2] == self.game.board[1][2] == 1 and self.game.board[2][2] == 0:
                return [2, 2]

        return choice(self.game.getMoves())


if __name__ == "__main__":
    try:
        g = ConnectFour()
        opp1 = minimax(g, 1)
        opp2 = minimax(g, -1)
        turn = 1
        while g.checkWin() == None:
            print(g)
            if turn % 2 == 1:
                move = opp1.chooseMove()
                opp1.game.makeMove(move[0], move[1], 1)
                turn += 1
            else:
                input("Press enter to continue: ")
                move = opp2.chooseMove()
                opp2.game.makeMove(move[0], move[1], -1)
                turn += 1
            # print(opp1.count)
            opp1.count = 0
        print(g)
    except KeyboardInterrupt:
        pass
