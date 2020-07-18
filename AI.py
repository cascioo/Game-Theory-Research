import os
from random import choice, shuffle
from Game import *
from math import inf, pow


class AI(object):
    def __init__(self, game, player):
        self.game = game
        self.player = player

    def __repr__(self):
        return "Random"

    def getName(self):
        return 'Random'

    def chooseMove(self):
        return choice(self.game.getMoves(self.player))


class MiniMax(AI):
    def __init__(self, game, look, player):
        self.player = player
        self.name = 'MinMax'
        self.bestMove = []
        self.count = 0
        self.look = look
        super(MiniMax, self).__init__(game, player)

    def __repr__(self):
        return "MinMax" + str(self.look)

    def getName(self):
        return "MinMax" + str(self.look)

    def minimax_helper(self, maxPlayer):
        if self.game.checkWin() is not None:
            return self.game.checkWin() * 30

        if maxPlayer:
            value = -inf
            for mv in self.game.getMoves():
                self.game.makeMove(mv[0], mv[1], 1)
                value = max(value, self.minimax_helper(False))
                self.game.resetMove(mv[0], mv[1])
            return value
        else:
            value = inf
            for mv in self.game.getMoves():
                self.game.makeMove(mv[0], mv[1], -1)
                value = min(value, self.minimax_helper(True))
                self.game.resetMove(mv[0], mv[1])
            return value

    def minimax_helper_v2(self, maxPlayer, depth, alpha, beta):
        if self.game.checkWin() is not None or depth == self.look:
            self.count += 1
            if self.count % 100000 == 0:
                print(self.count)

            if self.game.checkWin() == 1:
                return 300 - depth
            elif self.game.checkWin() == -1:
                return -300 + depth
            elif self.game.checkWin() == 0:
                return 0
            else:
                return self.evaluateBoard(maxPlayer)

        if maxPlayer:
            value = -inf
            for mv in self.game.getMoves(self.player):
                self.game.makeMove(mv[0], mv[1], 1)
                val = self.minimax_helper_v2(False, depth + 1, alpha, beta)
                self.game.resetMove(mv[0], mv[1])
                value = max(val, value)
                alpha = max(alpha, val)
                if beta <= alpha:
                    break
            return value
        else:
            value = inf
            for mv in self.game.getMoves(self.player):
                self.game.makeMove(mv[0], mv[1], -1)
                val = self.minimax_helper_v2(True, depth + 1, alpha, beta)
                self.game.resetMove(mv[0], mv[1])
                value = min(val, value)
                beta = min(beta, val)
                if beta <= alpha:
                    break
            return value

    def evaluateBoard(self, player):
        score = 0
        if self.game.getName() == 'TicTacToe':
            if player == 1:
                if self.game.board[0][0] == 0:
                    if self.game.board[0][1] == 0 or self.game.board[0][1] == 1:
                        if self.game.board[0][2] == 0 or self.game.board[0][2] == 1:
                            score += 1
                    if self.game.board[1][1] == 0 or self.game.board[1][1] == 1:
                        if self.game.board[2][2] == 0 or self.game.board[2][2] == 1:
                            score += 1
                    if self.game.board[1][0] == 0 or self.game.board[1][0] == 1:
                        if self.game.board[2][0] == 0 or self.game.board[2][0] == 1:
                            score += 1
                if self.game.board[0][1] == 0:
                    if self.game.board[0][0] == 0 or self.game.board[0][0] == 1:
                        if self.game.board[0][2] == 0 or self.game.board[0][2] == 1:
                            score += 1
                    if self.game.board[1][1] == 0 or self.game.board[1][1] == 1:
                        if self.game.board[2][1] == 0 or self.game.board[2][1] == 1:
                            score += 1
                if self.game.board[0][2] == 0:
                    if self.game.board[0][1] == 0 or self.game.board[0][1] == 1:
                        if self.game.board[0][0] == 0 or self.game.board[0][0] == 1:
                            score += 1
                    if self.game.board[1][2] == 0 or self.game.board[1][2] == 1:
                        if self.game.board[2][2] == 0 or self.game.board[2][2] == 1:
                            score += 1
                    if self.game.board[1][1] == 0 or self.game.board[1][1] == 1:
                        if self.game.board[2][0] == 0 or self.game.board[2][0] == 1:
                            score += 1
                if self.game.board[1][0] == 0:
                    if self.game.board[0][0] == 0 or self.game.board[0][0] == 1:
                        if self.game.board[2][0] == 0 or self.game.board[2][0] == 1:
                            score += 1
                    if self.game.board[1][1] == 0 or self.game.board[1][1] == 1:
                        if self.game.board[1][2] == 0 or self.game.board[1][2] == 1:
                            score += 1
                if self.game.board[1][1] == 0:
                    if self.game.board[0][0] == 0 or self.game.board[0][0] == 1:
                        if self.game.board[2][2] == 0 or self.game.board[2][2] == 1:
                            score += 1
                    if self.game.board[0][1] == 0 or self.game.board[0][1] == 1:
                        if self.game.board[2][1] == 0 or self.game.board[2][1] == 1:
                            score += 1
                    if self.game.board[0][2] == 0 or self.game.board[0][2] == 1:
                        if self.game.board[2][0] == 0 or self.game.board[2][0] == 1:
                            score += 1
                    if self.game.board[1][0] == 0 or self.game.board[1][0] == 1:
                        if self.game.board[1][2] == 0 or self.game.board[1][2] == 1:
                            score += 1
                if self.game.board[1][2] == 0:
                    if self.game.board[1][0] == 0 or self.game.board[1][0] == 1:
                        if self.game.board[1][1] == 0 or self.game.board[1][1] == 1:
                            score += 1
                    if self.game.board[0][2] == 0 or self.game.board[0][2] == 1:
                        if self.game.board[2][2] == 0 or self.game.board[2][2] == 1:
                            score += 1
                if self.game.board[2][0] == 0:
                    if self.game.board[0][0] == 0 or self.game.board[0][0] == 1:
                        if self.game.board[1][0] == 0 or self.game.board[1][0] == 1:
                            score += 1
                    if self.game.board[2][1] == 0 or self.game.board[2][1] == 1:
                        if self.game.board[2][2] == 0 or self.game.board[2][2] == 1:
                            score += 1
                    if self.game.board[1][1] == 0 or self.game.board[1][1] == 1:
                        if self.game.board[0][2] == 0 or self.game.board[0][2] == 1:
                            score += 1
                if self.game.board[2][1] == 0:
                    if self.game.board[1][1] == 0 or self.game.board[1][1] == 1:
                        if self.game.board[0][1] == 0 or self.game.board[0][1] == 1:
                            score += 1
                    if self.game.board[2][0] == 0 or self.game.board[2][0] == 1:
                        if self.game.board[2][2] == 0 or self.game.board[2][2] == 1:
                            score += 1
                if self.game.board[2][2] == 0:
                    if self.game.board[0][0] == 0 or self.game.board[0][0] == 1:
                        if self.game.board[1][1] == 0 or self.game.board[1][1] == 1:
                            score += 1
                    if self.game.board[0][2] == 0 or self.game.board[0][2] == 1:
                        if self.game.board[1][2] == 0 or self.game.board[1][2] == 1:
                            score += 1
                    if self.game.board[0][0] == 0 or self.game.board[0][0] == 1:
                        if self.game.board[1][1] == 0 or self.game.board[1][1] == 1:
                            score += 1
            else:
                if self.game.board[0][0] == 0:
                    if self.game.board[0][1] == 0 or self.game.board[0][1] == -1:
                        if self.game.board[0][2] == 0 or self.game.board[0][2] == -1:
                            score -= 1
                    if self.game.board[1][1] == 0 or self.game.board[1][1] == -1:
                        if self.game.board[2][2] == 0 or self.game.board[2][2] == -1:
                            score -= 1
                    if self.game.board[1][0] == 0 or self.game.board[1][0] == -1:
                        if self.game.board[2][0] == 0 or self.game.board[2][0] == -1:
                            score -= 1
                if self.game.board[0][1] == 0:
                    if self.game.board[0][0] == 0 or self.game.board[0][0] == -1:
                        if self.game.board[0][2] == 0 or self.game.board[0][2] == -1:
                            score -= 1
                    if self.game.board[1][1] == 0 or self.game.board[1][1] == -1:
                        if self.game.board[2][1] == 0 or self.game.board[2][1] == -1:
                            score -= 1
                if self.game.board[0][2] == 0:
                    if self.game.board[0][1] == 0 or self.game.board[0][1] == -1:
                        if self.game.board[0][0] == 0 or self.game.board[0][0] == -1:
                            score -= 1
                    if self.game.board[1][2] == 0 or self.game.board[1][2] == -1:
                        if self.game.board[2][2] == 0 or self.game.board[2][2] == -1:
                            score -= 1
                    if self.game.board[1][1] == 0 or self.game.board[1][1] == -1:
                        if self.game.board[2][0] == 0 or self.game.board[2][0] == -1:
                            score -= 1
                if self.game.board[1][0] == 0:
                    if self.game.board[0][0] == 0 or self.game.board[0][0] == -1:
                        if self.game.board[2][0] == 0 or self.game.board[2][0] == -1:
                            score -= 1
                    if self.game.board[1][1] == 0 or self.game.board[1][1] == -1:
                        if self.game.board[1][2] == 0 or self.game.board[1][2] == -1:
                            score -= 1
                if self.game.board[1][1] == 0:
                    if self.game.board[0][0] == 0 or self.game.board[0][0] == -1:
                        if self.game.board[2][2] == 0 or self.game.board[2][2] == -1:
                            score -= 1
                    if self.game.board[0][1] == 0 or self.game.board[0][1] == -1:
                        if self.game.board[2][1] == 0 or self.game.board[2][1] == -1:
                            score -= 1
                    if self.game.board[0][2] == 0 or self.game.board[0][2] == -1:
                        if self.game.board[2][0] == 0 or self.game.board[2][0] == -1:
                            score -= 1
                    if self.game.board[1][0] == 0 or self.game.board[1][0] == -1:
                        if self.game.board[1][2] == 0 or self.game.board[1][2] == -1:
                            score -= 1
                if self.game.board[1][2] == 0:
                    if self.game.board[1][0] == 0 or self.game.board[1][0] == -1:
                        if self.game.board[1][1] == 0 or self.game.board[1][1] == -1:
                            score -= 1
                    if self.game.board[0][2] == 0 or self.game.board[0][2] == -1:
                        if self.game.board[2][2] == 0 or self.game.board[2][2] == -1:
                            score -= 1
                if self.game.board[2][0] == 0:
                    if self.game.board[0][0] == 0 or self.game.board[0][0] == -1:
                        if self.game.board[1][0] == 0 or self.game.board[1][0] == -1:
                            score -= 1
                    if self.game.board[2][1] == 0 or self.game.board[2][1] == -1:
                        if self.game.board[2][2] == 0 or self.game.board[2][2] == -1:
                            score -= 1
                    if self.game.board[1][1] == 0 or self.game.board[1][1] == -1:
                        if self.game.board[0][2] == 0 or self.game.board[0][2] == -1:
                            score -= 1
                if self.game.board[2][1] == 0:
                    if self.game.board[1][1] == 0 or self.game.board[1][1] == -1:
                        if self.game.board[0][1] == 0 or self.game.board[0][1] == -1:
                            score -= 1
                    if self.game.board[2][0] == 0 or self.game.board[2][0] == -1:
                        if self.game.board[2][2] == 0 or self.game.board[2][2] == -1:
                            score -= 1
                if self.game.board[2][2] == 0:
                    if self.game.board[0][0] == 0 or self.game.board[0][0] == -1:
                        if self.game.board[1][1] == 0 or self.game.board[1][1] == -1:
                            score -= 1
                    if self.game.board[0][2] == 0 or self.game.board[0][2] == -1:
                        if self.game.board[1][2] == 0 or self.game.board[1][2] == -1:
                            score -= 1
                    if self.game.board[0][0] == 0 or self.game.board[0][0] == -1:
                        if self.game.board[1][1] == 0 or self.game.board[1][1] == -1:
                            score -= 1
            return score
        elif self.game.getName() == "ConnectFour":
            if player == -1:
                if self.game.board[5][0] == 0:
                    if self.game.board[5][1] == 0 or self.game.board[5][1] == 1:
                        if self.game.board[5][2] == 0 or self.game.board[5][2] == 1:
                            if self.game.board[5][3] == 0 or self.game.board[5][3] == 1:
                                score += 1
                    if self.game.board[4][0] == 0 or self.game.board[4][0] == 1:
                        if self.game.board[3][0] == 0 or self.game.board[3][0] == 1:
                            if self.game.board[2][0] == 0 or self.game.board[2][0] == 1:
                                score += 1
                    if self.game.board[4][1] == 0 or self.game.board[4][1] == 1:
                        if self.game.board[3][2] == 0 or self.game.board[3][2] == 1:
                            if self.game.board[2][3] == 0 or self.game.board[2][3] == 1:
                                score += 1
                if self.game.board[5][1] == 0:
                    if self.game.board[5][0] == 0 or self.game.board[5][0] == 1:
                        if self.game.board[5][2] == 0 or self.game.board[5][2] == 1:
                            if self.game.board[5][3] == 0 or self.game.board[5][3] == 1:
                                score += 1
                    if self.game.board[5][2] == 0 or self.game.board[5][2] == 1:
                        if self.game.board[5][3] == 0 or self.game.board[5][3] == 1:
                            if self.game.board[5][4] == 0 or self.game.board[5][4] == 1:
                                score += 1
                    if self.game.board[4][1] == 0 or self.game.board[4][1] == 1:
                        if self.game.board[3][1] == 0 or self.game.board[3][1] == 1:
                            if self.game.board[2][1] == 0 or self.game.board[2][1] == 1:
                                score += 1
                    if self.game.board[4][2] == 0 or self.game.board[4][2] == 1:
                        if self.game.board[3][3] == 0 or self.game.board[3][3] == 1:
                            if self.game.board[2][4] == 0 or self.game.board[2][4] == 1:
                                score += 1
                if self.game.board[5][2] == 0:
                    if self.game.board[5][0] == 0 or self.game.board[5][0] == 1:
                        if self.game.board[5][1] == 0 or self.game.board[5][1] == 1:
                            if self.game.board[5][3] == 0 or self.game.board[5][3] == 1:
                                score += 1
                    if self.game.board[5][1] == 0 or self.game.board[5][1] == 1:
                        if self.game.board[5][3] == 0 or self.game.board[5][3] == 1:
                            if self.game.board[5][4] == 0 or self.game.board[5][4] == 1:
                                score += 1
                    if self.game.board[5][3] == 0 or self.game.board[5][3] == 1:
                        if self.game.board[5][4] == 0 or self.game.board[5][4] == 1:
                            if self.game.board[5][5] == 0 or self.game.board[5][5] == 1:
                                score += 1
                    if self.game.board[4][2] == 0 or self.game.board[4][2] == 1:
                        if self.game.board[3][2] == 0 or self.game.board[3][2] == 1:
                            if self.game.board[2][2] == 0 or self.game.board[2][2] == 1:
                                score += 1
                    if self.game.board[4][3] == 0 or self.game.board[4][3] == 1:
                        if self.game.board[3][4] == 0 or self.game.board[3][4] == 1:
                            if self.game.board[2][5] == 0 or self.game.board[2][5] == 1:
                                score += 1
                if self.game.board[5][3] == 0:
                    if self.game.board[5][0] == 0 or self.game.board[5][0] == 1:
                        if self.game.board[5][1] == 0 or self.game.board[5][1] == 1:
                            if self.game.board[5][2] == 0 or self.game.board[5][2] == 1:
                                score += 1
                    if self.game.board[5][1] == 0 or self.game.board[5][1] == 1:
                        if self.game.board[5][2] == 0 or self.game.board[5][2] == 1:
                            if self.game.board[5][4] == 0 or self.game.board[5][4] == 1:
                                score += 1
                    if self.game.board[5][2] == 0 or self.game.board[5][2] == 1:
                        if self.game.board[5][4] == 0 or self.game.board[5][4] == 1:
                            if self.game.board[5][5] == 0 or self.game.board[5][5] == 1:
                                score += 1
                    if self.game.board[5][4] == 0 or self.game.board[5][4] == 1:
                        if self.game.board[5][5] == 0 or self.game.board[5][5] == 1:
                            if self.game.board[5][6] == 0 or self.game.board[5][6] == 1:
                                score += 1
                    if self.game.board[4][3] == 0 or self.game.board[4][3] == 1:
                        if self.game.board[3][3] == 0 or self.game.board[3][3] == 1:
                            if self.game.board[2][3] == 0 or self.game.board[2][3] == 1:
                                score += 1
                    if self.game.board[4][4] == 0 or self.game.board[4][4] == 1:
                        if self.game.board[3][5] == 0 or self.game.board[3][5] == 1:
                            if self.game.board[2][6] == 0 or self.game.board[2][6] == 1:
                                score += 1
                    if self.game.board[4][2] == 0 or self.game.board[4][2] == 1:
                        if self.game.board[3][1] == 0 or self.game.board[3][1] == 1:
                            if self.game.board[2][0] == 0 or self.game.board[2][0] == 1:
                                score += 1
                if self.game.board[5][4] == 0:
                    if self.game.board[5][1] == 0 or self.game.board[5][1] == 1:
                        if self.game.board[5][2] == 0 or self.game.board[5][2] == 1:
                            if self.game.board[5][3] == 0 or self.game.board[5][3] == 1:
                                score += 1
                    if self.game.board[5][2] == 0 or self.game.board[5][2] == 1:
                        if self.game.board[5][3] == 0 or self.game.board[5][3] == 1:
                            if self.game.board[5][5] == 0 or self.game.board[5][5] == 1:
                                score += 1
                    if self.game.board[5][3] == 0 or self.game.board[5][3] == 1:
                        if self.game.board[5][5] == 0 or self.game.board[5][5] == 1:
                            if self.game.board[5][6] == 0 or self.game.board[5][6] == 1:
                                score += 1
                    if self.game.board[4][4] == 0 or self.game.board[4][4] == 1:
                        if self.game.board[3][4] == 0 or self.game.board[3][4] == 1:
                            if self.game.board[2][4] == 0 or self.game.board[2][4] == 1:
                                score += 1
                    if self.game.board[4][3] == 0 or self.game.board[4][3] == 1:
                        if self.game.board[3][2] == 0 or self.game.board[3][2] == 1:
                            if self.game.board[2][1] == 0 or self.game.board[2][1] == 1:
                                score += 1
                if self.game.board[5][5] == 0:
                    if self.game.board[5][2] == 0 or self.game.board[5][2] == 1:
                        if self.game.board[5][3] == 0 or self.game.board[5][3] == 1:
                            if self.game.board[5][4] == 0 or self.game.board[5][4] == 1:
                                score += 1
                    if self.game.board[5][3] == 0 or self.game.board[5][3] == 1:
                        if self.game.board[5][4] == 0 or self.game.board[5][4] == 1:
                            if self.game.board[5][6] == 0 or self.game.board[5][6] == 1:
                                score += 1
                    if self.game.board[4][5] == 0 or self.game.board[4][5] == 1:
                        if self.game.board[3][5] == 0 or self.game.board[3][5] == 1:
                            if self.game.board[2][5] == 0 or self.game.board[2][5] == 1:
                                score += 1
                    if self.game.board[4][4] == 0 or self.game.board[4][4] == 1:
                        if self.game.board[3][3] == 0 or self.game.board[3][3] == 1:
                            if self.game.board[2][2] == 0 or self.game.board[2][2] == 1:
                                score += 1
                if self.game.board[5][6] == 0:
                    if self.game.board[5][3] == 0 or self.game.board[5][3] == 1:
                        if self.game.board[5][4] == 0 or self.game.board[5][4] == 1:
                            if self.game.board[5][5] == 0 or self.game.board[5][5] == 1:
                                score += 1
                    if self.game.board[4][6] == 0 or self.game.board[4][6] == 1:
                        if self.game.board[3][6] == 0 or self.game.board[3][6] == 1:
                            if self.game.board[2][6] == 0 or self.game.board[2][6] == 1:
                                score += 1
                    if self.game.board[4][5] == 0 or self.game.board[4][5] == 1:
                        if self.game.board[3][4] == 0 or self.game.board[3][4] == 1:
                            if self.game.board[2][3] == 0 or self.game.board[2][3] == 1:
                                score += 1
                if self.game.board[4][0] == 0:
                    if self.game.board[4][1] == 0 or self.game.board[4][1] == 1:
                        if self.game.board[4][2] == 0 or self.game.board[4][2] == 1:
                            if self.game.board[4][3] == 0 or self.game.board[4][3] == 1:
                                score += 1
                    if self.game.board[5][0] == 0 or self.game.board[5][0] == 1:
                        if self.game.board[3][0] == 0 or self.game.board[3][0] == 1:
                            if self.game.board[2][0] == 0 or self.game.board[2][0] == 1:
                                score += 1
                    if self.game.board[3][0] == 0 or self.game.board[3][0] == 1:
                        if self.game.board[2][0] == 0 or self.game.board[2][0] == 1:
                            if self.game.board[1][0] == 0 or self.game.board[1][0] == 1:
                                score += 1
                    if self.game.board[3][1] == 0 or self.game.board[3][1] == 1:
                        if self.game.board[2][2] == 0 or self.game.board[2][2] == 1:
                            if self.game.board[1][3] == 0 or self.game.board[1][3] == 1:
                                score += 1
                if self.game.board[4][1] == 0:
                    if self.game.board[4][0] == 0 or self.game.board[4][0] == 1:
                        if self.game.board[4][2] == 0 or self.game.board[4][2] == 1:
                            if self.game.board[4][3] == 0 or self.game.board[4][3] == 1:
                                score += 1
                    if self.game.board[4][2] == 0 or self.game.board[4][2] == 1:
                        if self.game.board[4][3] == 0 or self.game.board[4][3] == 1:
                            if self.game.board[4][4] == 0 or self.game.board[4][4] == 1:
                                score += 1
                    if self.game.board[5][1] == 0 or self.game.board[5][1] == 1:
                        if self.game.board[3][1] == 0 or self.game.board[3][1] == 1:
                            if self.game.board[2][1] == 0 or self.game.board[2][1] == 1:
                                score += 1
                    if self.game.board[3][1] == 0 or self.game.board[3][1] == 1:
                        if self.game.board[2][1] == 0 or self.game.board[2][1] == 1:
                            if self.game.board[1][1] == 0 or self.game.board[1][1] == 1:
                                score += 1
                    if self.game.board[3][2] == 0 or self.game.board[3][2] == 1:
                        if self.game.board[2][3] == 0 or self.game.board[2][3] == 1:
                            if self.game.board[1][4] == 0 or self.game.board[1][4] == 1:
                                score += 1
                    if self.game.board[5][0] == 0 or self.game.board[5][0] == 1:
                        if self.game.board[3][2] == 0 or self.game.board[3][2] == 1:
                            if self.game.board[2][3] == 0 or self.game.board[2][3] == 1:
                                score += 1
                if self.game.board[4][2] == 0:
                    if self.game.board[4][0] == 0 or self.game.board[4][0] == 1:
                        if self.game.board[4][1] == 0 or self.game.board[4][1] == 1:
                            if self.game.board[4][3] == 0 or self.game.board[4][3] == 1:
                                score += 1
                    if self.game.board[4][1] == 0 or self.game.board[4][1] == 1:
                        if self.game.board[4][3] == 0 or self.game.board[4][3] == 1:
                            if self.game.board[4][4] == 0 or self.game.board[4][4] == 1:
                                score += 1
                    if self.game.board[4][3] == 0 or self.game.board[4][3] == 1:
                        if self.game.board[4][4] == 0 or self.game.board[4][4] == 1:
                            if self.game.board[4][5] == 0 or self.game.board[4][5] == 1:
                                score += 1
                    if self.game.board[5][2] == 0 or self.game.board[5][2] == 1:
                        if self.game.board[3][2] == 0 or self.game.board[3][2] == 1:
                            if self.game.board[2][2] == 0 or self.game.board[2][2] == 1:
                                score += 1
                    if self.game.board[3][2] == 0 or self.game.board[3][2] == 1:
                        if self.game.board[2][2] == 0 or self.game.board[2][2] == 1:
                            if self.game.board[1][2] == 0 or self.game.board[1][2] == 1:
                                score += 1
                    if self.game.board[5][1] == 0 or self.game.board[5][1] == 1:
                        if self.game.board[3][3] == 0 or self.game.board[3][3] == 1:
                            if self.game.board[2][4] == 0 or self.game.board[2][4] == 1:
                                score += 1
                    if self.game.board[3][3] == 0 or self.game.board[3][3] == 1:
                        if self.game.board[2][4] == 0 or self.game.board[2][4] == 1:
                            if self.game.board[1][5] == 0 or self.game.board[1][5] == 1:
                                score += 1
                    if self.game.board[2][0] == 0 or self.game.board[2][0] == 1:
                        if self.game.board[3][1] == 0 or self.game.board[3][1] == 1:
                            if self.game.board[5][3] == 0 or self.game.board[5][3] == 1:
                                score += 1
                if self.game.board[4][3] == 0:
                    if self.game.board[4][0] == 0 or self.game.board[4][0] == 1:
                        if self.game.board[4][1] == 0 or self.game.board[4][1] == 1:
                            if self.game.board[4][2] == 0 or self.game.board[4][2] == 1:
                                score += 1
                    if self.game.board[4][1] == 0 or self.game.board[4][1] == 1:
                        if self.game.board[4][2] == 0 or self.game.board[4][2] == 1:
                            if self.game.board[4][4] == 0 or self.game.board[4][4] == 1:
                                score += 1
                    if self.game.board[4][2] == 0 or self.game.board[4][2] == 1:
                        if self.game.board[4][4] == 0 or self.game.board[4][4] == 1:
                            if self.game.board[4][5] == 0 or self.game.board[4][5] == 1:
                                score += 1
                    if self.game.board[4][4] == 0 or self.game.board[4][4] == 1:
                        if self.game.board[4][5] == 0 or self.game.board[4][5] == 1:
                            if self.game.board[4][6] == 0 or self.game.board[4][6] == 1:
                                score += 1
                    if self.game.board[5][3] == 0 or self.game.board[5][3] == 1:
                        if self.game.board[3][3] == 0 or self.game.board[3][3] == 1:
                            if self.game.board[2][3] == 0 or self.game.board[2][3] == 1:
                                score += 1
                    if self.game.board[3][3] == 0 or self.game.board[3][3] == 1:
                        if self.game.board[2][3] == 0 or self.game.board[2][3] == 1:
                            if self.game.board[1][3] == 0 or self.game.board[1][3] == 1:
                                score += 1
                    if self.game.board[5][2] == 0 or self.game.board[5][2] == 1:
                        if self.game.board[3][4] == 0 or self.game.board[3][4] == 1:
                            if self.game.board[2][5] == 0 or self.game.board[2][5] == 1:
                                score += 1
                    if self.game.board[3][4] == 0 or self.game.board[3][4] == 1:
                        if self.game.board[2][5] == 0 or self.game.board[2][5] == 1:
                            if self.game.board[1][6] == 0 or self.game.board[1][6] == 1:
                                score += 1
                    if self.game.board[5][4] == 0 or self.game.board[5][4] == 1:
                        if self.game.board[3][2] == 0 or self.game.board[3][2] == 1:
                            if self.game.board[2][1] == 0 or self.game.board[2][1] == 1:
                                score += 1
                    if self.game.board[3][2] == 0 or self.game.board[3][2] == 1:
                        if self.game.board[2][1] == 0 or self.game.board[2][1] == 1:
                            if self.game.board[1][0] == 0 or self.game.board[1][0] == 1:
                                score += 1
                if self.game.board[4][4] == 0:
                    if self.game.board[4][1] == 0 or self.game.board[4][1] == 1:
                        if self.game.board[4][2] == 0 or self.game.board[4][2] == 1:
                            if self.game.board[4][3] == 0 or self.game.board[4][3] == 1:
                                score += 1
                    if self.game.board[4][2] == 0 or self.game.board[4][2] == 1:
                        if self.game.board[4][3] == 0 or self.game.board[4][3] == 1:
                            if self.game.board[4][5] == 0 or self.game.board[4][5] == 1:
                                score += 1
                    if self.game.board[4][3] == 0 or self.game.board[4][3] == 1:
                        if self.game.board[4][5] == 0 or self.game.board[4][5] == 1:
                            if self.game.board[4][6] == 0 or self.game.board[4][6] == 1:
                                score += 1
                    if self.game.board[5][4] == 0 or self.game.board[5][4] == 1:
                        if self.game.board[3][4] == 0 or self.game.board[3][4] == 1:
                            if self.game.board[2][4] == 0 or self.game.board[2][4] == 1:
                                score += 1
                    if self.game.board[3][4] == 0 or self.game.board[3][4] == 1:
                        if self.game.board[2][4] == 0 or self.game.board[2][4] == 1:
                            if self.game.board[1][4] == 0 or self.game.board[1][4] == 1:
                                score += 1
                    if self.game.board[5][5] == 0 or self.game.board[5][5] == 1:
                        if self.game.board[3][3] == 0 or self.game.board[3][3] == 1:
                            if self.game.board[2][3] == 0 or self.game.board[2][3] == 1:
                                score += 1
                    if self.game.board[3][3] == 0 or self.game.board[3][3] == 1:
                        if self.game.board[2][2] == 0 or self.game.board[2][2] == 1:
                            if self.game.board[1][1] == 0 or self.game.board[1][1] == 1:
                                score += 1
                    if self.game.board[5][3] == 0 or self.game.board[5][3] == 1:
                        if self.game.board[3][5] == 0 or self.game.board[3][5] == 1:
                            if self.game.board[2][6] == 0 or self.game.board[2][6] == 1:
                                score += 1
                if self.game.board[4][5] == 0:
                    if self.game.board[4][2] == 0 or self.game.board[4][2] == 1:
                        if self.game.board[4][3] == 0 or self.game.board[4][3] == 1:
                            if self.game.board[4][4] == 0 or self.game.board[4][4] == 1:
                                score += 1
                    if self.game.board[4][3] == 0 or self.game.board[4][3] == 1:
                        if self.game.board[4][4] == 0 or self.game.board[4][4] == 1:
                            if self.game.board[4][6] == 0 or self.game.board[4][6] == 1:
                                score += 1
                    if self.game.board[5][5] == 0 or self.game.board[5][5] == 1:
                        if self.game.board[3][5] == 0 or self.game.board[3][5] == 1:
                            if self.game.board[2][5] == 0 or self.game.board[2][5] == 1:
                                score += 1
                    if self.game.board[3][5] == 0 or self.game.board[3][5] == 1:
                        if self.game.board[2][5] == 0 or self.game.board[2][5] == 1:
                            if self.game.board[1][5] == 0 or self.game.board[1][5] == 1:
                                score += 1
                    if self.game.board[5][6] == 0 or self.game.board[5][6] == 1:
                        if self.game.board[3][4] == 0 or self.game.board[3][4] == 1:
                            if self.game.board[2][3] == 0 or self.game.board[2][3] == 1:
                                score += 1
                    if self.game.board[3][4] == 0 or self.game.board[3][4] == 1:
                        if self.game.board[2][3] == 0 or self.game.board[2][3] == 1:
                            if self.game.board[1][2] == 0 or self.game.board[1][2] == 1:
                                score += 1
                if self.game.board[4][6] == 0:
                    if self.game.board[4][3] == 0 or self.game.board[4][3] == 1:
                        if self.game.board[4][4] == 0 or self.game.board[4][4] == 1:
                            if self.game.board[4][5] == 0 or self.game.board[4][5] == 1:
                                score += 1
                    if self.game.board[5][6] == 0 or self.game.board[5][6] == 1:
                        if self.game.board[3][6] == 0 or self.game.board[3][6] == 1:
                            if self.game.board[2][6] == 0 or self.game.board[2][6] == 1:
                                score += 1
                    if self.game.board[3][6] == 0 or self.game.board[3][6] == 1:
                        if self.game.board[2][6] == 0 or self.game.board[2][6] == 1:
                            if self.game.board[1][6] == 0 or self.game.board[1][6] == 1:
                                score += 1
                    if self.game.board[3][5] == 0 or self.game.board[3][5] == 1:
                        if self.game.board[2][4] == 0 or self.game.board[2][4] == 1:
                            if self.game.board[1][3] == 0 or self.game.board[1][3] == 1:
                                score += 1
                if self.game.board[3][0] == 0:
                    if self.game.board[3][1] == 0 or self.game.board[3][1] == 1:
                        if self.game.board[3][2] == 0 or self.game.board[3][2] == 1:
                            if self.game.board[3][3] == 0 or self.game.board[3][3] == 1:
                                score += 1
                    if self.game.board[5][0] == 0 or self.game.board[5][0] == 1:
                        if self.game.board[4][0] == 0 or self.game.board[4][0] == 1:
                            if self.game.board[2][0] == 0 or self.game.board[2][0] == 1:
                                score += 1
                    if self.game.board[4][0] == 0 or self.game.board[4][0] == 1:
                        if self.game.board[2][0] == 0 or self.game.board[2][0] == 1:
                            if self.game.board[1][0] == 0 or self.game.board[1][0] == 1:
                                score += 1
                    if self.game.board[2][0] == 0 or self.game.board[2][0] == 1:
                        if self.game.board[1][0] == 0 or self.game.board[1][0] == 1:
                            if self.game.board[0][0] == 0 or self.game.board[0][0] == 1:
                                score += 1
                    if self.game.board[2][1] == 0 or self.game.board[2][1] == 1:
                        if self.game.board[1][2] == 0 or self.game.board[1][2] == 1:
                            if self.game.board[0][3] == 0 or self.game.board[0][3] == 1:
                                score += 1
                if self.game.board[3][1] == 0:
                    if self.game.board[3][0] == 0 or self.game.board[3][0] == 1:
                        if self.game.board[3][2] == 0 or self.game.board[3][2] == 1:
                            if self.game.board[3][3] == 0 or self.game.board[3][3] == 1:
                                score += 1
                    if self.game.board[3][2] == 0 or self.game.board[3][2] == 1:
                        if self.game.board[3][3] == 0 or self.game.board[3][3] == 1:
                            if self.game.board[3][4] == 0 or self.game.board[3][4] == 1:
                                score += 1
                    if self.game.board[5][1] == 0 or self.game.board[5][1] == 1:
                        if self.game.board[4][1] == 0 or self.game.board[4][1] == 1:
                            if self.game.board[2][1] == 0 or self.game.board[2][1] == 1:
                                score += 1
                    if self.game.board[4][1] == 0 or self.game.board[4][1] == 1:
                        if self.game.board[2][1] == 0 or self.game.board[2][1] == 1:
                            if self.game.board[1][1] == 0 or self.game.board[1][1] == 1:
                                score += 1
                    if self.game.board[2][1] == 0 or self.game.board[2][1] == 1:
                        if self.game.board[1][1] == 0 or self.game.board[1][1] == 1:
                            if self.game.board[0][1] == 0 or self.game.board[0][1] == 1:
                                score += 1
                    if self.game.board[2][2] == 0 or self.game.board[2][2] == 1:
                        if self.game.board[1][3] == 0 or self.game.board[1][3] == 1:
                            if self.game.board[0][4] == 0 or self.game.board[0][4] == 1:
                                score += 1
                    if self.game.board[4][0] == 0 or self.game.board[4][0] == 1:
                        if self.game.board[2][2] == 0 or self.game.board[2][2] == 1:
                            if self.game.board[1][3] == 0 or self.game.board[1][3] == 1:
                                score += 1
                    if self.game.board[2][0] == 0 or self.game.board[2][0] == 1:
                        if self.game.board[4][2] == 0 or self.game.board[4][2] == 1:
                            if self.game.board[5][3] == 0 or self.game.board[5][3] == 1:
                                score += 1
                if self.game.board[3][2] == 0:
                    if self.game.board[3][0] == 0 or self.game.board[3][0] == 1:
                        if self.game.board[3][1] == 0 or self.game.board[3][1] == 1:
                            if self.game.board[3][3] == 0 or self.game.board[3][3] == 1:
                                score += 1
                    if self.game.board[3][1] == 0 or self.game.board[3][1] == 1:
                        if self.game.board[3][3] == 0 or self.game.board[3][3] == 1:
                            if self.game.board[3][4] == 0 or self.game.board[3][4] == 1:
                                score += 1
                    if self.game.board[3][3] == 0 or self.game.board[3][3] == 1:
                        if self.game.board[3][4] == 0 or self.game.board[3][4] == 1:
                            if self.game.board[3][5] == 0 or self.game.board[3][5] == 1:
                                score += 1
                    if self.game.board[5][2] == 0 or self.game.board[5][2] == 1:
                        if self.game.board[4][2] == 0 or self.game.board[4][2] == 1:
                            if self.game.board[2][2] == 0 or self.game.board[2][2] == 1:
                                score += 1
                    if self.game.board[4][2] == 0 or self.game.board[4][2] == 1:
                        if self.game.board[2][2] == 0 or self.game.board[2][2] == 1:
                            if self.game.board[1][2] == 0 or self.game.board[1][2] == 1:
                                score += 1
                    if self.game.board[2][2] == 0 or self.game.board[2][2] == 1:
                        if self.game.board[1][2] == 0 or self.game.board[1][2] == 1:
                            if self.game.board[0][2] == 0 or self.game.board[0][2] == 1:
                                score += 1
                    if self.game.board[5][0] == 0 or self.game.board[5][0] == 1:
                        if self.game.board[4][1] == 0 or self.game.board[4][1] == 1:
                            if self.game.board[2][3] == 0 or self.game.board[2][3] == 1:
                                score += 1
                    if self.game.board[4][1] == 0 or self.game.board[4][1] == 1:
                        if self.game.board[2][3] == 0 or self.game.board[2][3] == 1:
                            if self.game.board[1][4] == 0 or self.game.board[1][4] == 1:
                                score += 1
                    if self.game.board[2][3] == 0 or self.game.board[2][3] == 1:
                        if self.game.board[1][4] == 0 or self.game.board[1][4] == 1:
                            if self.game.board[0][5] == 0 or self.game.board[0][5] == 1:
                                score += 1
                    if self.game.board[1][0] == 0 or self.game.board[1][0] == 1:
                        if self.game.board[2][1] == 0 or self.game.board[2][1] == 1:
                            if self.game.board[4][3] == 0 or self.game.board[4][3] == 1:
                                score += 1
                    if self.game.board[2][1] == 0 or self.game.board[2][1] == 1:
                        if self.game.board[4][3] == 0 or self.game.board[4][3] == 1:
                            if self.game.board[5][4] == 0 or self.game.board[5][4] == 1:
                                score += 1
                if self.game.board[3][3] == 0:
                    if self.game.board[3][0] == 0 or self.game.board[3][0] == 1:
                        if self.game.board[3][1] == 0 or self.game.board[3][1] == 1:
                            if self.game.board[3][2] == 0 or self.game.board[3][2] == 1:
                                score += 1
                    if self.game.board[3][1] == 0 or self.game.board[3][1] == 1:
                        if self.game.board[3][2] == 0 or self.game.board[3][2] == 1:
                            if self.game.board[3][4] == 0 or self.game.board[3][4] == 1:
                                score += 1
                    if self.game.board[3][2] == 0 or self.game.board[3][2] == 1:
                        if self.game.board[3][4] == 0 or self.game.board[3][4] == 1:
                            if self.game.board[3][5] == 0 or self.game.board[3][5] == 1:
                                score += 1
                    if self.game.board[3][4] == 0 or self.game.board[3][4] == 1:
                        if self.game.board[3][5] == 0 or self.game.board[3][5] == 1:
                            if self.game.board[3][6] == 0 or self.game.board[3][6] == 1:
                                score += 1
                    if self.game.board[5][3] == 0 or self.game.board[5][3] == 1:
                        if self.game.board[4][3] == 0 or self.game.board[4][3] == 1:
                            if self.game.board[2][3] == 0 or self.game.board[2][3] == 1:
                                score += 1
                    if self.game.board[4][3] == 0 or self.game.board[4][3] == 1:
                        if self.game.board[2][3] == 0 or self.game.board[2][3] == 1:
                            if self.game.board[1][3] == 0 or self.game.board[1][3] == 1:
                                score += 1
                    if self.game.board[2][3] == 0 or self.game.board[2][3] == 1:
                        if self.game.board[1][3] == 0 or self.game.board[1][3] == 1:
                            if self.game.board[0][3] == 0 or self.game.board[0][3] == 1:
                                score += 1
                    if self.game.board[5][1] == 0 or self.game.board[5][1] == 1:
                        if self.game.board[4][2] == 0 or self.game.board[4][2] == 1:
                            if self.game.board[2][4] == 0 or self.game.board[2][4] == 1:
                                score += 1
                    if self.game.board[4][2] == 0 or self.game.board[4][2] == 1:
                        if self.game.board[2][4] == 0 or self.game.board[2][4] == 1:
                            if self.game.board[1][5] == 0 or self.game.board[1][5] == 1:
                                score += 1
                    if self.game.board[2][4] == 0 or self.game.board[2][4] == 1:
                        if self.game.board[1][5] == 0 or self.game.board[1][5] == 1:
                            if self.game.board[0][6] == 0 or self.game.board[0][6] == 1:
                                score += 1
                    if self.game.board[0][0] == 0 or self.game.board[0][0] == 1:
                        if self.game.board[1][1] == 0 or self.game.board[1][1] == 1:
                            if self.game.board[2][2] == 0 or self.game.board[2][2] == 1:
                                score += 1
                    if self.game.board[1][1] == 0 or self.game.board[1][1] == 1:
                        if self.game.board[2][2] == 0 or self.game.board[2][2] == 1:
                            if self.game.board[4][4] == 0 or self.game.board[4][4] == 1:
                                score += 1
                    if self.game.board[2][2] == 0 or self.game.board[2][2] == 1:
                        if self.game.board[4][4] == 0 or self.game.board[4][4] == 1:
                            if self.game.board[5][5] == 0 or self.game.board[5][5] == 1:
                                score += 1
                if self.game.board[3][4] == 0:
                    if self.game.board[3][1] == 0 or self.game.board[3][1] == 1:
                        if self.game.board[3][2] == 0 or self.game.board[3][2] == 1:
                            if self.game.board[3][3] == 0 or self.game.board[3][3] == 1:
                                score += 1
                    if self.game.board[3][2] == 0 or self.game.board[3][2] == 1:
                        if self.game.board[3][3] == 0 or self.game.board[3][3] == 1:
                            if self.game.board[3][5] == 0 or self.game.board[3][5] == 1:
                                score += 1
                    if self.game.board[3][3] == 0 or self.game.board[3][3] == 1:
                        if self.game.board[3][5] == 0 or self.game.board[3][5] == 1:
                            if self.game.board[3][6] == 0 or self.game.board[3][6] == 1:
                                score += 1
                    if self.game.board[5][4] == 0 or self.game.board[5][4] == 1:
                        if self.game.board[4][4] == 0 or self.game.board[4][4] == 1:
                            if self.game.board[2][4] == 0 or self.game.board[2][4] == 1:
                                score += 1
                    if self.game.board[4][4] == 0 or self.game.board[4][4] == 1:
                        if self.game.board[2][4] == 0 or self.game.board[2][4] == 1:
                            if self.game.board[1][4] == 0 or self.game.board[1][4] == 1:
                                score += 1
                    if self.game.board[2][4] == 0 or self.game.board[2][4] == 1:
                        if self.game.board[1][4] == 0 or self.game.board[1][4] == 1:
                            if self.game.board[0][4] == 0 or self.game.board[0][4] == 1:
                                score += 1
                    if self.game.board[5][2] == 0 or self.game.board[5][2] == 1:
                        if self.game.board[4][3] == 0 or self.game.board[4][3] == 1:
                            if self.game.board[2][5] == 0 or self.game.board[2][5] == 1:
                                score += 1
                    if self.game.board[4][3] == 0 or self.game.board[4][3] == 1:
                        if self.game.board[2][5] == 0 or self.game.board[2][5] == 1:
                            if self.game.board[1][6] == 0 or self.game.board[1][6] == 1:
                                score += 1
                    if self.game.board[0][1] == 0 or self.game.board[0][1] == 1:
                        if self.game.board[1][2] == 0 or self.game.board[1][2] == 1:
                            if self.game.board[2][3] == 0 or self.game.board[2][3] == 1:
                                score += 1
                    if self.game.board[1][2] == 0 or self.game.board[1][2] == 1:
                        if self.game.board[2][3] == 0 or self.game.board[2][3] == 1:
                            if self.game.board[4][5] == 0 or self.game.board[4][5] == 1:
                                score += 1
                    if self.game.board[2][3] == 0 or self.game.board[2][3] == 1:
                        if self.game.board[4][5] == 0 or self.game.board[4][5] == 1:
                            if self.game.board[5][6] == 0 or self.game.board[5][6] == 1:
                                score += 1
                if self.game.board[3][5] == 0:
                    if self.game.board[3][2] == 0 or self.game.board[3][2] == 1:
                        if self.game.board[3][3] == 0 or self.game.board[3][3] == 1:
                            if self.game.board[3][4] == 0 or self.game.board[3][4] == 1:
                                score += 1
                    if self.game.board[3][3] == 0 or self.game.board[3][3] == 1:
                        if self.game.board[3][4] == 0 or self.game.board[3][4] == 1:
                            if self.game.board[3][6] == 0 or self.game.board[3][6] == 1:
                                score += 1
                    if self.game.board[5][5] == 0 or self.game.board[5][5] == 1:
                        if self.game.board[4][5] == 0 or self.game.board[4][5] == 1:
                            if self.game.board[2][5] == 0 or self.game.board[2][5] == 1:
                                score += 1
                    if self.game.board[4][5] == 0 or self.game.board[4][5] == 1:
                        if self.game.board[2][5] == 0 or self.game.board[2][5] == 1:
                            if self.game.board[1][5] == 0 or self.game.board[1][5] == 1:
                                score += 1
                    if self.game.board[2][5] == 0 or self.game.board[2][5] == 1:
                        if self.game.board[1][5] == 0 or self.game.board[1][5] == 1:
                            if self.game.board[0][5] == 0 or self.game.board[0][5] == 1:
                                score += 1
                    if self.game.board[5][3] == 0 or self.game.board[5][3] == 1:
                        if self.game.board[4][4] == 0 or self.game.board[4][4] == 1:
                            if self.game.board[2][6] == 0 or self.game.board[2][6] == 1:
                                score += 1
                    if self.game.board[0][2] == 0 or self.game.board[0][2] == 1:
                        if self.game.board[1][3] == 0 or self.game.board[1][3] == 1:
                            if self.game.board[2][4] == 0 or self.game.board[2][4] == 1:
                                score += 1
                    if self.game.board[1][3] == 0 or self.game.board[1][3] == 1:
                        if self.game.board[2][4] == 0 or self.game.board[2][4] == 1:
                            if self.game.board[4][6] == 0 or self.game.board[4][6] == 1:
                                score += 1
                if self.game.board[3][6] == 0:
                    if self.game.board[3][3] == 0 or self.game.board[3][3] == 1:
                        if self.game.board[3][4] == 0 or self.game.board[3][4] == 1:
                            if self.game.board[3][5] == 0 or self.game.board[3][5] == 1:
                                score += 1
                    if self.game.board[5][6] == 0 or self.game.board[5][6] == 1:
                        if self.game.board[4][6] == 0 or self.game.board[4][6] == 1:
                            if self.game.board[2][6] == 0 or self.game.board[2][6] == 1:
                                score += 1
                    if self.game.board[4][6] == 0 or self.game.board[4][6] == 1:
                        if self.game.board[2][6] == 0 or self.game.board[2][6] == 1:
                            if self.game.board[1][6] == 0 or self.game.board[1][6] == 1:
                                score += 1
                    if self.game.board[2][6] == 0 or self.game.board[2][6] == 1:
                        if self.game.board[1][6] == 0 or self.game.board[1][6] == 1:
                            if self.game.board[0][6] == 0 or self.game.board[0][6] == 1:
                                score += 1
                    if self.game.board[0][3] == 0 or self.game.board[0][3] == 1:
                        if self.game.board[1][4] == 0 or self.game.board[1][4] == 1:
                            if self.game.board[2][5] == 0 or self.game.board[2][5] == 1:
                                score += 1
                if self.game.board[2][0] == 0:
                    if self.game.board[2][1] == 0 or self.game.board[2][1] == 1:
                        if self.game.board[2][2] == 0 or self.game.board[2][2] == 1:
                            if self.game.board[2][3] == 0 or self.game.board[2][3] == 1:
                                score += 1
                    if self.game.board[5][0] == 0 or self.game.board[5][0] == 1:
                        if self.game.board[4][0] == 0 or self.game.board[4][0] == 1:
                            if self.game.board[3][0] == 0 or self.game.board[3][0] == 1:
                                score += 1
                    if self.game.board[4][0] == 0 or self.game.board[4][0] == 1:
                        if self.game.board[3][0] == 0 or self.game.board[3][0] == 1:
                            if self.game.board[1][0] == 0 or self.game.board[1][0] == 1:
                                score += 1
                    if self.game.board[3][0] == 0 or self.game.board[3][0] == 1:
                        if self.game.board[1][0] == 0 or self.game.board[1][0] == 1:
                            if self.game.board[0][0] == 0 or self.game.board[0][0] == 1:
                                score += 1
                    if self.game.board[3][1] == 0 or self.game.board[3][1] == 1:
                        if self.game.board[4][2] == 0 or self.game.board[4][2] == 1:
                            if self.game.board[5][3] == 0 or self.game.board[5][3] == 1:
                                score += 1
                if self.game.board[2][1] == 0:
                    if self.game.board[2][0] == 0 or self.game.board[2][0] == 1:
                        if self.game.board[2][2] == 0 or self.game.board[2][2] == 1:
                            if self.game.board[2][3] == 0 or self.game.board[2][3] == 1:
                                score += 1
                    if self.game.board[2][2] == 0 or self.game.board[2][2] == 1:
                        if self.game.board[2][3] == 0 or self.game.board[2][3] == 1:
                            if self.game.board[2][4] == 0 or self.game.board[2][4] == 1:
                                score += 1
                    if self.game.board[5][1] == 0 or self.game.board[5][1] == 1:
                        if self.game.board[4][1] == 0 or self.game.board[4][1] == 1:
                            if self.game.board[3][1] == 0 or self.game.board[3][1] == 1:
                                score += 1
                    if self.game.board[4][1] == 0 or self.game.board[4][1] == 1:
                        if self.game.board[3][1] == 0 or self.game.board[3][1] == 1:
                            if self.game.board[1][1] == 0 or self.game.board[1][1] == 1:
                                score += 1
                    if self.game.board[3][1] == 0 or self.game.board[3][1] == 1:
                        if self.game.board[1][1] == 0 or self.game.board[1][1] == 1:
                            if self.game.board[0][1] == 0 or self.game.board[0][1] == 1:
                                score += 1
                    if self.game.board[3][0] == 0 or self.game.board[3][0] == 1:
                        if self.game.board[1][2] == 0 or self.game.board[1][2] == 1:
                            if self.game.board[0][3] == 0 or self.game.board[0][3] == 1:
                                score += 1
                    if self.game.board[5][4] == 0 or self.game.board[5][4] == 1:
                        if self.game.board[4][3] == 0 or self.game.board[4][3] == 1:
                            if self.game.board[3][2] == 0 or self.game.board[3][2] == 1:
                                score += 1
                    if self.game.board[4][3] == 0 or self.game.board[4][3] == 1:
                        if self.game.board[3][2] == 0 or self.game.board[3][2] == 1:
                            if self.game.board[1][0] == 0 or self.game.board[1][0] == 1:
                                score += 1
                if self.game.board[2][2] == 0:
                    if self.game.board[2][0] == 0 or self.game.board[2][0] == 1:
                        if self.game.board[2][1] == 0 or self.game.board[2][1] == 1:
                            if self.game.board[2][3] == 0 or self.game.board[2][3] == 1:
                                score += 1
                    if self.game.board[2][1] == 0 or self.game.board[2][1] == 1:
                        if self.game.board[2][3] == 0 or self.game.board[2][3] == 1:
                            if self.game.board[2][4] == 0 or self.game.board[2][4] == 1:
                                score += 1
                    if self.game.board[2][3] == 0 or self.game.board[2][3] == 1:
                        if self.game.board[2][4] == 0 or self.game.board[2][4] == 1:
                            if self.game.board[2][5] == 0 or self.game.board[2][5] == 1:
                                score += 1
                    if self.game.board[5][2] == 0 or self.game.board[5][2] == 1:
                        if self.game.board[4][2] == 0 or self.game.board[4][2] == 1:
                            if self.game.board[3][2] == 0 or self.game.board[3][2] == 1:
                                score += 1
                    if self.game.board[4][2] == 0 or self.game.board[4][2] == 1:
                        if self.game.board[3][2] == 0 or self.game.board[3][2] == 1:
                            if self.game.board[1][2] == 0 or self.game.board[1][2] == 1:
                                score += 1
                    if self.game.board[3][2] == 0 or self.game.board[3][2] == 1:
                        if self.game.board[1][2] == 0 or self.game.board[1][2] == 1:
                            if self.game.board[0][2] == 0 or self.game.board[0][2] == 1:
                                score += 1
                    if self.game.board[4][0] == 0 or self.game.board[4][0] == 1:
                        if self.game.board[3][1] == 0 or self.game.board[3][1] == 1:
                            if self.game.board[1][3] == 0 or self.game.board[1][3] == 1:
                                score += 1
                    if self.game.board[3][1] == 0 or self.game.board[3][1] == 1:
                        if self.game.board[1][3] == 0 or self.game.board[1][3] == 1:
                            if self.game.board[0][4] == 0 or self.game.board[0][4] == 1:
                                score += 1
                    if self.game.board[5][5] == 0 or self.game.board[5][5] == 1:
                        if self.game.board[4][4] == 0 or self.game.board[4][4] == 1:
                            if self.game.board[3][3] == 0 or self.game.board[3][3] == 1:
                                score += 1
                    if self.game.board[4][4] == 0 or self.game.board[4][4] == 1:
                        if self.game.board[3][3] == 0 or self.game.board[3][3] == 1:
                            if self.game.board[1][1] == 0 or self.game.board[1][1] == 1:
                                score += 1
                    if self.game.board[2][2] == 0 or self.game.board[2][2] == 1:
                        if self.game.board[1][1] == 0 or self.game.board[1][1] == 1:
                            if self.game.board[0][0] == 0 or self.game.board[0][0] == 1:
                                score += 1
                if self.game.board[2][3] == 0:
                    if self.game.board[2][0] == 0 or self.game.board[2][0] == 1:
                        if self.game.board[2][1] == 0 or self.game.board[2][1] == 1:
                            if self.game.board[2][2] == 0 or self.game.board[2][2] == 1:
                                score += 1
                    if self.game.board[2][1] == 0 or self.game.board[2][1] == 1:
                        if self.game.board[2][2] == 0 or self.game.board[2][2] == 1:
                            if self.game.board[2][4] == 0 or self.game.board[2][4] == 1:
                                score += 1
                    if self.game.board[2][2] == 0 or self.game.board[2][2] == 1:
                        if self.game.board[2][4] == 0 or self.game.board[2][4] == 1:
                            if self.game.board[2][5] == 0 or self.game.board[2][5] == 1:
                                score += 1
                    if self.game.board[2][4] == 0 or self.game.board[2][4] == 1:
                        if self.game.board[2][5] == 0 or self.game.board[2][5] == 1:
                            if self.game.board[2][6] == 0 or self.game.board[2][6] == 1:
                                score += 1
                    if self.game.board[5][3] == 0 or self.game.board[5][3] == 1:
                        if self.game.board[4][3] == 0 or self.game.board[4][3] == 1:
                            if self.game.board[3][3] == 0 or self.game.board[3][3] == 1:
                                score += 1
                    if self.game.board[4][3] == 0 or self.game.board[4][3] == 1:
                        if self.game.board[3][3] == 0 or self.game.board[3][3] == 1:
                            if self.game.board[1][3] == 0 or self.game.board[1][3] == 1:
                                score += 1
                    if self.game.board[3][3] == 0 or self.game.board[3][3] == 1:
                        if self.game.board[1][3] == 0 or self.game.board[1][3] == 1:
                            if self.game.board[0][3] == 0 or self.game.board[0][3] == 1:
                                score += 1
                    if self.game.board[5][0] == 0 or self.game.board[5][0] == 1:
                        if self.game.board[4][1] == 0 or self.game.board[4][1] == 1:
                            if self.game.board[3][2] == 0 or self.game.board[3][2] == 1:
                                score += 1
                    if self.game.board[4][1] == 0 or self.game.board[4][1] == 1:
                        if self.game.board[3][2] == 0 or self.game.board[3][2] == 1:
                            if self.game.board[1][4] == 0 or self.game.board[1][4] == 1:
                                score += 1
                    if self.game.board[3][2] == 0 or self.game.board[3][2] == 1:
                        if self.game.board[1][4] == 0 or self.game.board[1][4] == 1:
                            if self.game.board[0][5] == 0 or self.game.board[0][5] == 1:
                                score += 1
                    if self.game.board[5][6] == 0 or self.game.board[5][6] == 1:
                        if self.game.board[4][5] == 0 or self.game.board[4][5] == 1:
                            if self.game.board[3][4] == 0 or self.game.board[3][4] == 1:
                                score += 1
                    if self.game.board[4][5] == 0 or self.game.board[4][5] == 1:
                        if self.game.board[3][4] == 0 or self.game.board[3][4] == 1:
                            if self.game.board[1][2] == 0 or self.game.board[1][2] == 1:
                                score += 1
                    if self.game.board[3][4] == 0 or self.game.board[3][4] == 1:
                        if self.game.board[1][2] == 0 or self.game.board[1][2] == 1:
                            if self.game.board[0][1] == 0 or self.game.board[0][1] == 1:
                                score += 1
                if self.game.board[2][4] == 0:
                    if self.game.board[2][1] == 0 or self.game.board[2][1] == 1:
                        if self.game.board[2][2] == 0 or self.game.board[2][2] == 1:
                            if self.game.board[2][3] == 0 or self.game.board[2][3] == 1:
                                score += 1
                    if self.game.board[2][2] == 0 or self.game.board[2][2] == 1:
                        if self.game.board[2][3] == 0 or self.game.board[2][3] == 1:
                            if self.game.board[2][5] == 0 or self.game.board[2][5] == 1:
                                score += 1
                    if self.game.board[2][3] == 0 or self.game.board[2][3] == 1:
                        if self.game.board[2][5] == 0 or self.game.board[2][5] == 1:
                            if self.game.board[2][6] == 0 or self.game.board[2][6] == 1:
                                score += 1
                    if self.game.board[5][4] == 0 or self.game.board[5][4] == 1:
                        if self.game.board[4][4] == 0 or self.game.board[4][4] == 1:
                            if self.game.board[3][4] == 0 or self.game.board[3][4] == 1:
                                score += 1
                    if self.game.board[4][4] == 0 or self.game.board[4][4] == 1:
                        if self.game.board[3][4] == 0 or self.game.board[3][4] == 1:
                            if self.game.board[1][4] == 0 or self.game.board[1][4] == 1:
                                score += 1
                    if self.game.board[3][4] == 0 or self.game.board[3][4] == 1:
                        if self.game.board[1][4] == 0 or self.game.board[1][4] == 1:
                            if self.game.board[0][4] == 0 or self.game.board[0][4] == 1:
                                score += 1
                    if self.game.board[5][1] == 0 or self.game.board[5][1] == 1:
                        if self.game.board[4][2] == 0 or self.game.board[4][2] == 1:
                            if self.game.board[3][3] == 0 or self.game.board[3][3] == 1:
                                score += 1
                    if self.game.board[4][2] == 0 or self.game.board[4][2] == 1:
                        if self.game.board[3][3] == 0 or self.game.board[3][3] == 1:
                            if self.game.board[1][5] == 0 or self.game.board[1][5] == 1:
                                score += 1
                    if self.game.board[3][3] == 0 or self.game.board[3][3] == 1:
                        if self.game.board[1][5] == 0 or self.game.board[1][5] == 1:
                            if self.game.board[0][6] == 0 or self.game.board[0][6] == 1:
                                score += 1
                    if self.game.board[4][6] == 0 or self.game.board[4][6] == 1:
                        if self.game.board[3][5] == 0 or self.game.board[3][5] == 1:
                            if self.game.board[1][3] == 0 or self.game.board[1][3] == 1:
                                score += 1
                    if self.game.board[3][5] == 0 or self.game.board[3][5] == 1:
                        if self.game.board[1][3] == 0 or self.game.board[1][3] == 1:
                            if self.game.board[0][2] == 0 or self.game.board[0][2] == 1:
                                score += 1
                if self.game.board[2][5] == 0:
                    if self.game.board[2][2] == 0 or self.game.board[2][2] == 1:
                        if self.game.board[2][3] == 0 or self.game.board[2][3] == 1:
                            if self.game.board[2][4] == 0 or self.game.board[2][4] == 1:
                                score += 1
                    if self.game.board[2][3] == 0 or self.game.board[2][3] == 1:
                        if self.game.board[2][4] == 0 or self.game.board[2][4] == 1:
                            if self.game.board[2][6] == 0 or self.game.board[2][6] == 1:
                                score += 1
                    if self.game.board[5][5] == 0 or self.game.board[5][5] == 1:
                        if self.game.board[4][5] == 0 or self.game.board[4][5] == 1:
                            if self.game.board[3][5] == 0 or self.game.board[3][5] == 1:
                                score += 1
                    if self.game.board[4][5] == 0 or self.game.board[4][5] == 1:
                        if self.game.board[3][5] == 0 or self.game.board[3][5] == 1:
                            if self.game.board[1][5] == 0 or self.game.board[1][5] == 1:
                                score += 1
                    if self.game.board[3][5] == 0 or self.game.board[3][5] == 1:
                        if self.game.board[1][5] == 0 or self.game.board[1][5] == 1:
                            if self.game.board[0][5] == 0 or self.game.board[0][5] == 1:
                                score += 1
                    if self.game.board[5][2] == 0 or self.game.board[5][2] == 1:
                        if self.game.board[4][3] == 0 or self.game.board[4][3] == 1:
                            if self.game.board[3][4] == 0 or self.game.board[3][4] == 1:
                                score += 1
                    if self.game.board[4][3] == 0 or self.game.board[4][3] == 1:
                        if self.game.board[3][4] == 0 or self.game.board[3][4] == 1:
                            if self.game.board[1][6] == 0 or self.game.board[1][6] == 1:
                                score += 1
                    if self.game.board[3][6] == 0 or self.game.board[3][6] == 1:
                        if self.game.board[1][4] == 0 or self.game.board[1][4] == 1:
                            if self.game.board[0][3] == 0 or self.game.board[0][3] == 1:
                                score += 1
                if self.game.board[2][6] == 0:
                    if self.game.board[2][3] == 0 or self.game.board[2][3] == 1:
                        if self.game.board[2][4] == 0 or self.game.board[2][4] == 1:
                            if self.game.board[2][5] == 0 or self.game.board[2][5] == 1:
                                score += 1
                    if self.game.board[5][6] == 0 or self.game.board[5][6] == 1:
                        if self.game.board[4][6] == 0 or self.game.board[4][6] == 1:
                            if self.game.board[3][6] == 0 or self.game.board[3][6] == 1:
                                score += 1
                    if self.game.board[4][6] == 0 or self.game.board[4][6] == 1:
                        if self.game.board[3][6] == 0 or self.game.board[3][6] == 1:
                            if self.game.board[1][6] == 0 or self.game.board[1][6] == 1:
                                score += 1
                    if self.game.board[3][6] == 0 or self.game.board[3][6] == 1:
                        if self.game.board[1][6] == 0 or self.game.board[1][6] == 1:
                            if self.game.board[0][6] == 0 or self.game.board[0][6] == 1:
                                score += 1
                    if self.game.board[5][3] == 0 or self.game.board[5][3] == 1:
                        if self.game.board[4][4] == 0 or self.game.board[4][4] == 1:
                            if self.game.board[3][5] == 0 or self.game.board[3][5] == 1:
                                score += 1
                if self.game.board[1][0] == 0:
                    if self.game.board[1][1] == 0 or self.game.board[1][1] == 1:
                        if self.game.board[1][2] == 0 or self.game.board[1][2] == 1:
                            if self.game.board[1][3] == 0 or self.game.board[1][3] == 1:
                                score += 1
                    if self.game.board[4][0] == 0 or self.game.board[4][0] == 1:
                        if self.game.board[3][0] == 0 or self.game.board[3][0] == 1:
                            if self.game.board[2][0] == 0 or self.game.board[2][0] == 1:
                                score += 1
                    if self.game.board[3][0] == 0 or self.game.board[3][0] == 1:
                        if self.game.board[2][0] == 0 or self.game.board[2][0] == 1:
                            if self.game.board[0][0] == 0 or self.game.board[0][0] == 1:
                                score += 1
                    if self.game.board[4][3] == 0 or self.game.board[4][3] == 1:
                        if self.game.board[3][2] == 0 or self.game.board[3][2] == 1:
                            if self.game.board[2][1] == 0 or self.game.board[2][1] == 1:
                                score += 1
                if self.game.board[1][1] == 0:
                    if self.game.board[1][0] == 0 or self.game.board[1][0] == 1:
                        if self.game.board[1][2] == 0 or self.game.board[1][2] == 1:
                            if self.game.board[1][3] == 0 or self.game.board[1][3] == 1:
                                score += 1
                    if self.game.board[1][2] == 0 or self.game.board[1][2] == 1:
                        if self.game.board[1][3] == 0 or self.game.board[1][3] == 1:
                            if self.game.board[1][4] == 0 or self.game.board[1][4] == 1:
                                score += 1
                    if self.game.board[4][1] == 0 or self.game.board[4][1] == 1:
                        if self.game.board[3][1] == 0 or self.game.board[3][1] == 1:
                            if self.game.board[2][1] == 0 or self.game.board[2][1] == 1:
                                score += 1
                    if self.game.board[3][1] == 0 or self.game.board[3][1] == 1:
                        if self.game.board[2][1] == 0 or self.game.board[2][1] == 1:
                            if self.game.board[0][1] == 0 or self.game.board[0][1] == 1:
                                score += 1
                    if self.game.board[4][4] == 0 or self.game.board[4][4] == 1:
                        if self.game.board[3][3] == 0 or self.game.board[3][3] == 1:
                            if self.game.board[2][2] == 0 or self.game.board[2][2] == 1:
                                score += 1
                    if self.game.board[3][3] == 0 or self.game.board[3][3] == 1:
                        if self.game.board[2][2] == 0 or self.game.board[2][2] == 1:
                            if self.game.board[0][0] == 0 or self.game.board[0][0] == 1:
                                score += 1
                if self.game.board[1][2] == 0:
                    if self.game.board[1][0] == 0 or self.game.board[1][0] == 1:
                        if self.game.board[1][1] == 0 or self.game.board[1][1] == 1:
                            if self.game.board[1][3] == 0 or self.game.board[1][3] == 1:
                                score += 1
                    if self.game.board[1][1] == 0 or self.game.board[1][1] == 1:
                        if self.game.board[1][3] == 0 or self.game.board[1][3] == 1:
                            if self.game.board[1][4] == 0 or self.game.board[1][4] == 1:
                                score += 1
                    if self.game.board[1][3] == 0 or self.game.board[1][3] == 1:
                        if self.game.board[1][4] == 0 or self.game.board[1][4] == 1:
                            if self.game.board[1][5] == 0 or self.game.board[1][5] == 1:
                                score += 1
                    if self.game.board[4][2] == 0 or self.game.board[4][2] == 1:
                        if self.game.board[3][2] == 0 or self.game.board[3][2] == 1:
                            if self.game.board[2][2] == 0 or self.game.board[2][2] == 1:
                                score += 1
                    if self.game.board[3][2] == 0 or self.game.board[3][2] == 1:
                        if self.game.board[2][2] == 0 or self.game.board[2][2] == 1:
                            if self.game.board[0][2] == 0 or self.game.board[0][2] == 1:
                                score += 1
                    if self.game.board[3][0] == 0 or self.game.board[3][0] == 1:
                        if self.game.board[2][1] == 0 or self.game.board[2][1] == 1:
                            if self.game.board[0][3] == 0 or self.game.board[0][3] == 1:
                                score += 1
                    if self.game.board[4][5] == 0 or self.game.board[4][5] == 1:
                        if self.game.board[3][4] == 0 or self.game.board[3][4] == 1:
                            if self.game.board[2][3] == 0 or self.game.board[2][3] == 1:
                                score += 1
                    if self.game.board[3][4] == 0 or self.game.board[3][4] == 1:
                        if self.game.board[2][3] == 0 or self.game.board[2][3] == 1:
                            if self.game.board[0][1] == 0 or self.game.board[0][1] == 1:
                                score += 1
                if self.game.board[1][3] == 0:
                    if self.game.board[1][0] == 0 or self.game.board[1][0] == 1:
                        if self.game.board[1][1] == 0 or self.game.board[1][1] == 1:
                            if self.game.board[1][2] == 0 or self.game.board[1][2] == 1:
                                score += 1
                    if self.game.board[1][1] == 0 or self.game.board[1][1] == 1:
                        if self.game.board[1][2] == 0 or self.game.board[1][2] == 1:
                            if self.game.board[1][4] == 0 or self.game.board[1][4] == 1:
                                score += 1
                    if self.game.board[1][2] == 0 or self.game.board[1][2] == 1:
                        if self.game.board[1][4] == 0 or self.game.board[1][4] == 1:
                            if self.game.board[1][5] == 0 or self.game.board[1][5] == 1:
                                score += 1
                    if self.game.board[1][4] == 0 or self.game.board[1][4] == 1:
                        if self.game.board[1][5] == 0 or self.game.board[1][5] == 1:
                            if self.game.board[1][6] == 0 or self.game.board[1][6] == 1:
                                score += 1
                    if self.game.board[4][3] == 0 or self.game.board[4][3] == 1:
                        if self.game.board[3][3] == 0 or self.game.board[3][3] == 1:
                            if self.game.board[2][3] == 0 or self.game.board[2][3] == 1:
                                score += 1
                    if self.game.board[3][3] == 0 or self.game.board[3][3] == 1:
                        if self.game.board[2][3] == 0 or self.game.board[2][3] == 1:
                            if self.game.board[0][3] == 0 or self.game.board[0][3] == 1:
                                score += 1
                    if self.game.board[4][0] == 0 or self.game.board[4][0] == 1:
                        if self.game.board[3][1] == 0 or self.game.board[3][1] == 1:
                            if self.game.board[2][2] == 0 or self.game.board[2][2] == 1:
                                score += 1
                    if self.game.board[3][1] == 0 or self.game.board[3][1] == 1:
                        if self.game.board[2][2] == 0 or self.game.board[2][2] == 1:
                            if self.game.board[0][4] == 0 or self.game.board[0][4] == 1:
                                score += 1
                    if self.game.board[4][6] == 0 or self.game.board[4][6] == 1:
                        if self.game.board[3][5] == 0 or self.game.board[3][5] == 1:
                            if self.game.board[2][4] == 0 or self.game.board[2][4] == 1:
                                score += 1
                    if self.game.board[3][5] == 0 or self.game.board[3][5] == 1:
                        if self.game.board[2][4] == 0 or self.game.board[2][4] == 1:
                            if self.game.board[0][2] == 0 or self.game.board[0][2] == 1:
                                score += 1
                if self.game.board[1][4] == 0:
                    if self.game.board[1][1] == 0 or self.game.board[1][1] == 1:
                        if self.game.board[1][2] == 0 or self.game.board[1][2] == 1:
                            if self.game.board[1][3] == 0 or self.game.board[1][3] == 1:
                                score += 1
                    if self.game.board[1][2] == 0 or self.game.board[1][2] == 1:
                        if self.game.board[1][3] == 0 or self.game.board[1][3] == 1:
                            if self.game.board[1][5] == 0 or self.game.board[1][5] == 1:
                                score += 1
                    if self.game.board[1][3] == 0 or self.game.board[1][3] == 1:
                        if self.game.board[1][5] == 0 or self.game.board[1][5] == 1:
                            if self.game.board[1][6] == 0 or self.game.board[1][6] == 1:
                                score += 1
                    if self.game.board[4][4] == 0 or self.game.board[4][4] == 1:
                        if self.game.board[3][4] == 0 or self.game.board[3][4] == 1:
                            if self.game.board[2][4] == 0 or self.game.board[2][4] == 1:
                                score += 1
                    if self.game.board[3][4] == 0 or self.game.board[3][4] == 1:
                        if self.game.board[2][4] == 0 or self.game.board[2][4] == 1:
                            if self.game.board[0][4] == 0 or self.game.board[0][4] == 1:
                                score += 1
                    if self.game.board[4][1] == 0 or self.game.board[4][1] == 1:
                        if self.game.board[3][2] == 0 or self.game.board[3][2] == 1:
                            if self.game.board[2][3] == 0 or self.game.board[2][3] == 1:
                                score += 1
                    if self.game.board[3][2] == 0 or self.game.board[3][2] == 1:
                        if self.game.board[2][3] == 0 or self.game.board[2][3] == 1:
                            if self.game.board[0][5] == 0 or self.game.board[0][5] == 1:
                                score += 1
                    if self.game.board[3][6] == 0 or self.game.board[3][6] == 1:
                        if self.game.board[2][5] == 0 or self.game.board[2][5] == 1:
                            if self.game.board[0][3] == 0 or self.game.board[0][3] == 1:
                                score += 1
                if self.game.board[1][5] == 0:
                    if self.game.board[1][2] == 0 or self.game.board[1][2] == 1:
                        if self.game.board[1][3] == 0 or self.game.board[1][3] == 1:
                            if self.game.board[1][4] == 0 or self.game.board[1][4] == 1:
                                score += 1
                    if self.game.board[1][3] == 0 or self.game.board[1][3] == 1:
                        if self.game.board[1][4] == 0 or self.game.board[1][4] == 1:
                            if self.game.board[1][6] == 0 or self.game.board[1][6] == 1:
                                score += 1
                    if self.game.board[4][5] == 0 or self.game.board[4][5] == 1:
                        if self.game.board[3][5] == 0 or self.game.board[3][5] == 1:
                            if self.game.board[2][5] == 0 or self.game.board[2][5] == 1:
                                score += 1
                    if self.game.board[3][5] == 0 or self.game.board[3][5] == 1:
                        if self.game.board[2][5] == 0 or self.game.board[2][5] == 1:
                            if self.game.board[0][5] == 0 or self.game.board[0][5] == 1:
                                score += 1
                    if self.game.board[4][2] == 0 or self.game.board[4][2] == 1:
                        if self.game.board[3][3] == 0 or self.game.board[3][3] == 1:
                            if self.game.board[2][4] == 0 or self.game.board[2][4] == 1:
                                score += 1
                    if self.game.board[3][3] == 0 or self.game.board[3][3] == 1:
                        if self.game.board[2][4] == 0 or self.game.board[2][4] == 1:
                            if self.game.board[0][6] == 0 or self.game.board[0][6] == 1:
                                score += 1
                if self.game.board[1][6] == 0:
                    if self.game.board[1][3] == 0 or self.game.board[1][3] == 1:
                        if self.game.board[1][4] == 0 or self.game.board[1][4] == 1:
                            if self.game.board[1][5] == 0 or self.game.board[1][5] == 1:
                                score += 1

                    if self.game.board[4][6] == 0 or self.game.board[4][6] == 1:
                        if self.game.board[3][6] == 0 or self.game.board[3][6] == 1:
                            if self.game.board[2][6] == 0 or self.game.board[2][6] == 1:
                                score += 1
                    if self.game.board[3][6] == 0 or self.game.board[3][6] == 1:
                        if self.game.board[2][6] == 0 or self.game.board[2][6] == 1:
                            if self.game.board[0][6] == 0 or self.game.board[0][6] == 1:
                                score += 1
                    if self.game.board[4][3] == 0 or self.game.board[4][3] == 1:
                        if self.game.board[3][4] == 0 or self.game.board[3][4] == 1:
                            if self.game.board[2][5] == 0 or self.game.board[2][5] == 1:
                                score += 1
                if self.game.board[0][0] == 0:
                    if self.game.board[3][0] == 0 or self.game.board[3][0] == 1:
                        if self.game.board[2][0] == 0 or self.game.board[2][0] == 1:
                            if self.game.board[1][0] == 0 or self.game.board[1][0] == 1:
                                score += 1
                    if self.game.board[0][1] == 0 or self.game.board[0][1] == 1:
                        if self.game.board[0][2] == 0 or self.game.board[0][2] == 1:
                            if self.game.board[0][3] == 0 or self.game.board[0][3] == 1:
                                score += 1
                    if self.game.board[3][3] == 0 or self.game.board[3][3] == 1:
                        if self.game.board[2][2] == 0 or self.game.board[2][2] == 1:
                            if self.game.board[1][1] == 0 or self.game.board[1][1] == 1:
                                score += 1
                if self.game.board[0][1] == 0:
                    if self.game.board[0][0] == 0 or self.game.board[0][0] == 1:
                        if self.game.board[0][2] == 0 or self.game.board[0][2] == 1:
                            if self.game.board[0][3] == 0 or self.game.board[0][3] == 1:
                                score += 1
                    if self.game.board[0][2] == 0 or self.game.board[0][2] == 1:
                        if self.game.board[0][3] == 0 or self.game.board[0][3] == 1:
                            if self.game.board[0][4] == 0 or self.game.board[0][4] == 1:
                                score += 1
                    if self.game.board[3][1] == 0 or self.game.board[3][1] == 1:
                        if self.game.board[2][1] == 0 or self.game.board[2][1] == 1:
                            if self.game.board[1][1] == 0 or self.game.board[1][1] == 1:
                                score += 1
                    if self.game.board[3][4] == 0 or self.game.board[3][4] == 1:
                        if self.game.board[2][3] == 0 or self.game.board[2][3] == 1:
                            if self.game.board[1][2] == 0 or self.game.board[1][2] == 1:
                                score += 1
                if self.game.board[0][2] == 0:
                    if self.game.board[0][0] == 0 or self.game.board[0][0] == 1:
                        if self.game.board[0][1] == 0 or self.game.board[0][1] == 1:
                            if self.game.board[0][3] == 0 or self.game.board[0][3] == 1:
                                score += 1
                    if self.game.board[0][1] == 0 or self.game.board[0][1] == 1:
                        if self.game.board[0][3] == 0 or self.game.board[0][3] == 1:
                            if self.game.board[0][4] == 0 or self.game.board[0][4] == 1:
                                score += 1
                    if self.game.board[0][3] == 0 or self.game.board[0][3] == 1:
                        if self.game.board[0][4] == 0 or self.game.board[0][4] == 1:
                            if self.game.board[0][5] == 0 or self.game.board[0][5] == 1:
                                score += 1
                    if self.game.board[3][2] == 0 or self.game.board[3][2] == 1:
                        if self.game.board[2][2] == 0 or self.game.board[2][2] == 1:
                            if self.game.board[1][2] == 0 or self.game.board[1][2] == 1:
                                score += 1
                    if self.game.board[3][5] == 0 or self.game.board[3][5] == 1:
                        if self.game.board[2][4] == 0 or self.game.board[2][4] == 1:
                            if self.game.board[1][3] == 0 or self.game.board[1][3] == 1:
                                score += 1
                if self.game.board[0][3] == 0:
                    if self.game.board[0][0] == 0 or self.game.board[0][0] == 1:
                        if self.game.board[0][1] == 0 or self.game.board[0][1] == 1:
                            if self.game.board[0][2] == 0 or self.game.board[0][2] == 1:
                                score += 1
                    if self.game.board[0][1] == 0 or self.game.board[0][1] == 1:
                        if self.game.board[0][2] == 0 or self.game.board[0][2] == 1:
                            if self.game.board[0][4] == 0 or self.game.board[0][4] == 1:
                                score += 1
                    if self.game.board[0][2] == 0 or self.game.board[0][2] == 1:
                        if self.game.board[0][4] == 0 or self.game.board[0][4] == 1:
                            if self.game.board[0][5] == 0 or self.game.board[0][5] == 1:
                                score += 1
                    if self.game.board[0][4] == 0 or self.game.board[0][4] == 1:
                        if self.game.board[0][5] == 0 or self.game.board[0][5] == 1:
                            if self.game.board[0][6] == 0 or self.game.board[0][6] == 1:
                                score += 1
                    if self.game.board[3][3] == 0 or self.game.board[3][3] == 1:
                        if self.game.board[2][3] == 0 or self.game.board[2][3] == 1:
                            if self.game.board[1][3] == 0 or self.game.board[1][3] == 1:
                                score += 1
                    if self.game.board[3][0] == 0 or self.game.board[3][0] == 1:
                        if self.game.board[2][1] == 0 or self.game.board[2][1] == 1:
                            if self.game.board[1][2] == 0 or self.game.board[1][2] == 1:
                                score += 1
                    if self.game.board[3][6] == 0 or self.game.board[3][6] == 1:
                        if self.game.board[2][5] == 0 or self.game.board[2][5] == 1:
                            if self.game.board[1][4] == 0 or self.game.board[1][4] == 1:
                                score += 1
                if self.game.board[0][4] == 0:
                    if self.game.board[0][1] == 0 or self.game.board[0][1] == 1:
                        if self.game.board[0][2] == 0 or self.game.board[0][2] == 1:
                            if self.game.board[0][3] == 0 or self.game.board[0][3] == 1:
                                score += 1
                    if self.game.board[0][2] == 0 or self.game.board[0][2] == 1:
                        if self.game.board[0][3] == 0 or self.game.board[0][3] == 1:
                            if self.game.board[0][5] == 0 or self.game.board[0][5] == 1:
                                score += 1
                    if self.game.board[0][3] == 0 or self.game.board[0][3] == 1:
                        if self.game.board[0][5] == 0 or self.game.board[0][5] == 1:
                            if self.game.board[0][6] == 0 or self.game.board[0][6] == 1:
                                score += 1
                    if self.game.board[3][4] == 0 or self.game.board[3][4] == 1:
                        if self.game.board[2][4] == 0 or self.game.board[2][4] == 1:
                            if self.game.board[1][4] == 0 or self.game.board[1][4] == 1:
                                score += 1
                    if self.game.board[3][1] == 0 or self.game.board[3][1] == 1:
                        if self.game.board[2][2] == 0 or self.game.board[2][2] == 1:
                            if self.game.board[1][3] == 0 or self.game.board[1][3] == 1:
                                score += 1
                if self.game.board[0][5] == 0:
                    if self.game.board[0][2] == 0 or self.game.board[0][2] == 1:
                        if self.game.board[0][3] == 0 or self.game.board[0][3] == 1:
                            if self.game.board[0][4] == 0 or self.game.board[0][4] == 1:
                                score += 1
                    if self.game.board[0][3] == 0 or self.game.board[0][3] == 1:
                        if self.game.board[0][4] == 0 or self.game.board[0][4] == 1:
                            if self.game.board[0][6] == 0 or self.game.board[0][6] == 1:
                                score += 1
                    if self.game.board[3][5] == 0 or self.game.board[3][5] == 1:
                        if self.game.board[2][5] == 0 or self.game.board[2][5] == 1:
                            if self.game.board[1][5] == 0 or self.game.board[1][5] == 1:
                                score += 1
                    if self.game.board[3][2] == 0 or self.game.board[3][2] == 1:
                        if self.game.board[2][3] == 0 or self.game.board[2][3] == 1:
                            if self.game.board[1][4] == 0 or self.game.board[1][4] == 1:
                                score += 1
                if self.game.board[0][6] == 0:
                    if self.game.board[0][3] == 0 or self.game.board[0][3] == 1:
                        if self.game.board[0][4] == 0 or self.game.board[0][4] == 1:
                            if self.game.board[0][5] == 0 or self.game.board[0][5] == 1:
                                score += 1
                    if self.game.board[3][6] == 0 or self.game.board[3][6] == 1:
                        if self.game.board[2][6] == 0 or self.game.board[2][6] == 1:
                            if self.game.board[1][6] == 0 or self.game.board[1][6] == 1:
                                score += 1
                    if self.game.board[3][3] == 0 or self.game.board[3][3] == 1:
                        if self.game.board[2][4] == 0 or self.game.board[2][4] == 1:
                            if self.game.board[1][5] == 0 or self.game.board[1][5] == 1:
                                score += 1
            else:
                if self.game.board[5][0] == 0:
                    if self.game.board[5][1] == 0 or self.game.board[5][1] == -1:
                        if self.game.board[5][2] == 0 or self.game.board[5][2] == -1:
                            if self.game.board[5][3] == 0 or self.game.board[5][3] == -1:
                                score -= 1
                    if self.game.board[4][0] == 0 or self.game.board[4][0] == -1:
                        if self.game.board[3][0] == 0 or self.game.board[3][0] == -1:
                            if self.game.board[2][0] == 0 or self.game.board[2][0] == -1:
                                score -= 1
                    if self.game.board[4][1] == 0 or self.game.board[4][1] == -1:
                        if self.game.board[3][2] == 0 or self.game.board[3][2] == -1:
                            if self.game.board[2][3] == 0 or self.game.board[2][3] == -1:
                                score -= 1
                if self.game.board[5][1] == 0:
                    if self.game.board[5][0] == 0 or self.game.board[5][0] == -1:
                        if self.game.board[5][2] == 0 or self.game.board[5][2] == -1:
                            if self.game.board[5][3] == 0 or self.game.board[5][3] == -1:
                                score -= 1
                    if self.game.board[5][2] == 0 or self.game.board[5][2] == -1:
                        if self.game.board[5][3] == 0 or self.game.board[5][3] == -1:
                            if self.game.board[5][4] == 0 or self.game.board[5][4] == -1:
                                score -= 1
                    if self.game.board[4][1] == 0 or self.game.board[4][1] == -1:
                        if self.game.board[3][1] == 0 or self.game.board[3][1] == -1:
                            if self.game.board[2][1] == 0 or self.game.board[2][1] == -1:
                                score -= 1
                    if self.game.board[4][2] == 0 or self.game.board[4][2] == -1:
                        if self.game.board[3][3] == 0 or self.game.board[3][3] == -1:
                            if self.game.board[2][4] == 0 or self.game.board[2][4] == -1:
                                score -= 1
                if self.game.board[5][2] == 0:
                    if self.game.board[5][0] == 0 or self.game.board[5][0] == -1:
                        if self.game.board[5][1] == 0 or self.game.board[5][1] == -1:
                            if self.game.board[5][3] == 0 or self.game.board[5][3] == -1:
                                score -= 1
                    if self.game.board[5][1] == 0 or self.game.board[5][1] == -1:
                        if self.game.board[5][3] == 0 or self.game.board[5][3] == -1:
                            if self.game.board[5][4] == 0 or self.game.board[5][4] == -1:
                                score -= 1
                    if self.game.board[5][3] == 0 or self.game.board[5][3] == -1:
                        if self.game.board[5][4] == 0 or self.game.board[5][4] == -1:
                            if self.game.board[5][5] == 0 or self.game.board[5][5] == -1:
                                score -= 1
                    if self.game.board[4][2] == 0 or self.game.board[4][2] == -1:
                        if self.game.board[3][2] == 0 or self.game.board[3][2] == -1:
                            if self.game.board[2][2] == 0 or self.game.board[2][2] == -1:
                                score -= 1
                    if self.game.board[4][3] == 0 or self.game.board[4][3] == -1:
                        if self.game.board[3][4] == 0 or self.game.board[3][4] == -1:
                            if self.game.board[2][5] == 0 or self.game.board[2][5] == -1:
                                score -= 1
                if self.game.board[5][3] == 0:
                    if self.game.board[5][0] == 0 or self.game.board[5][0] == -1:
                        if self.game.board[5][1] == 0 or self.game.board[5][1] == -1:
                            if self.game.board[5][2] == 0 or self.game.board[5][2] == -1:
                                score -= 1
                    if self.game.board[5][1] == 0 or self.game.board[5][1] == -1:
                        if self.game.board[5][2] == 0 or self.game.board[5][2] == -1:
                            if self.game.board[5][4] == 0 or self.game.board[5][4] == -1:
                                score -= 1
                    if self.game.board[5][2] == 0 or self.game.board[5][2] == -1:
                        if self.game.board[5][4] == 0 or self.game.board[5][4] == -1:
                            if self.game.board[5][5] == 0 or self.game.board[5][5] == -1:
                                score -= 1
                    if self.game.board[5][4] == 0 or self.game.board[5][4] == -1:
                        if self.game.board[5][5] == 0 or self.game.board[5][5] == -1:
                            if self.game.board[5][6] == 0 or self.game.board[5][6] == -1:
                                score -= 1
                    if self.game.board[4][3] == 0 or self.game.board[4][3] == -1:
                        if self.game.board[3][3] == 0 or self.game.board[3][3] == -1:
                            if self.game.board[2][3] == 0 or self.game.board[2][3] == -1:
                                score -= 1
                    if self.game.board[4][4] == 0 or self.game.board[4][4] == -1:
                        if self.game.board[3][5] == 0 or self.game.board[3][5] == -1:
                            if self.game.board[2][6] == 0 or self.game.board[2][6] == -1:
                                score -= 1
                    if self.game.board[4][2] == 0 or self.game.board[4][2] == -1:
                        if self.game.board[3][1] == 0 or self.game.board[3][1] == -1:
                            if self.game.board[2][0] == 0 or self.game.board[2][0] == -1:
                                score -= 1
                if self.game.board[5][4] == 0:
                    if self.game.board[5][1] == 0 or self.game.board[5][1] == -1:
                        if self.game.board[5][2] == 0 or self.game.board[5][2] == -1:
                            if self.game.board[5][3] == 0 or self.game.board[5][3] == -1:
                                score -= 1
                    if self.game.board[5][2] == 0 or self.game.board[5][2] == -1:
                        if self.game.board[5][3] == 0 or self.game.board[5][3] == -1:
                            if self.game.board[5][5] == 0 or self.game.board[5][5] == -1:
                                score -= 1
                    if self.game.board[5][3] == 0 or self.game.board[5][3] == -1:
                        if self.game.board[5][5] == 0 or self.game.board[5][5] == -1:
                            if self.game.board[5][6] == 0 or self.game.board[5][6] == -1:
                                score -= 1
                    if self.game.board[4][4] == 0 or self.game.board[4][4] == -1:
                        if self.game.board[3][4] == 0 or self.game.board[3][4] == -1:
                            if self.game.board[2][4] == 0 or self.game.board[2][4] == -1:
                                score -= 1
                    if self.game.board[4][3] == 0 or self.game.board[4][3] == -1:
                        if self.game.board[3][2] == 0 or self.game.board[3][2] == -1:
                            if self.game.board[2][1] == 0 or self.game.board[2][1] == -1:
                                score -= 1
                if self.game.board[5][5] == 0:
                    if self.game.board[5][2] == 0 or self.game.board[5][2] == -1:
                        if self.game.board[5][3] == 0 or self.game.board[5][3] == -1:
                            if self.game.board[5][4] == 0 or self.game.board[5][4] == -1:
                                score -= 1
                    if self.game.board[5][3] == 0 or self.game.board[5][3] == -1:
                        if self.game.board[5][4] == 0 or self.game.board[5][4] == -1:
                            if self.game.board[5][6] == 0 or self.game.board[5][6] == -1:
                                score -= 1
                    if self.game.board[4][5] == 0 or self.game.board[4][5] == -1:
                        if self.game.board[3][5] == 0 or self.game.board[3][5] == -1:
                            if self.game.board[2][5] == 0 or self.game.board[2][5] == -1:
                                score -= 1
                    if self.game.board[4][4] == 0 or self.game.board[4][4] == -1:
                        if self.game.board[3][3] == 0 or self.game.board[3][3] == -1:
                            if self.game.board[2][2] == 0 or self.game.board[2][2] == -1:
                                score -= 1
                if self.game.board[5][6] == 0:
                    if self.game.board[5][3] == 0 or self.game.board[5][3] == -1:
                        if self.game.board[5][4] == 0 or self.game.board[5][4] == -1:
                            if self.game.board[5][5] == 0 or self.game.board[5][5] == -1:
                                score -= 1
                    if self.game.board[4][6] == 0 or self.game.board[4][6] == -1:
                        if self.game.board[3][6] == 0 or self.game.board[3][6] == -1:
                            if self.game.board[2][6] == 0 or self.game.board[2][6] == -1:
                                score -= 1
                    if self.game.board[4][5] == 0 or self.game.board[4][5] == -1:
                        if self.game.board[3][4] == 0 or self.game.board[3][4] == -1:
                            if self.game.board[2][3] == 0 or self.game.board[2][3] == -1:
                                score -= 1
                if self.game.board[4][0] == 0:
                    if self.game.board[4][1] == 0 or self.game.board[4][1] == -1:
                        if self.game.board[4][2] == 0 or self.game.board[4][2] == -1:
                            if self.game.board[4][3] == 0 or self.game.board[4][3] == -1:
                                score -= 1
                    if self.game.board[5][0] == 0 or self.game.board[5][0] == -1:
                        if self.game.board[3][0] == 0 or self.game.board[3][0] == -1:
                            if self.game.board[2][0] == 0 or self.game.board[2][0] == -1:
                                score -= 1
                    if self.game.board[3][0] == 0 or self.game.board[3][0] == -1:
                        if self.game.board[2][0] == 0 or self.game.board[2][0] == -1:
                            if self.game.board[1][0] == 0 or self.game.board[1][0] == -1:
                                score -= 1
                    if self.game.board[3][1] == 0 or self.game.board[3][1] == -1:
                        if self.game.board[2][2] == 0 or self.game.board[2][2] == -1:
                            if self.game.board[1][3] == 0 or self.game.board[1][3] == -1:
                                score -= 1
                if self.game.board[4][1] == 0:
                    if self.game.board[4][0] == 0 or self.game.board[4][0] == -1:
                        if self.game.board[4][2] == 0 or self.game.board[4][2] == -1:
                            if self.game.board[4][3] == 0 or self.game.board[4][3] == -1:
                                score -= 1
                    if self.game.board[4][2] == 0 or self.game.board[4][2] == -1:
                        if self.game.board[4][3] == 0 or self.game.board[4][3] == -1:
                            if self.game.board[4][4] == 0 or self.game.board[4][4] == -1:
                                score -= 1
                    if self.game.board[5][1] == 0 or self.game.board[5][1] == -1:
                        if self.game.board[3][1] == 0 or self.game.board[3][1] == -1:
                            if self.game.board[2][1] == 0 or self.game.board[2][1] == -1:
                                score -= 1
                    if self.game.board[3][1] == 0 or self.game.board[3][1] == -1:
                        if self.game.board[2][1] == 0 or self.game.board[2][1] == -1:
                            if self.game.board[1][1] == 0 or self.game.board[1][1] == -1:
                                score -= 1
                    if self.game.board[3][2] == 0 or self.game.board[3][2] == -1:
                        if self.game.board[2][3] == 0 or self.game.board[2][3] == -1:
                            if self.game.board[1][4] == 0 or self.game.board[1][4] == -1:
                                score -= 1
                    if self.game.board[5][0] == 0 or self.game.board[5][0] == -1:
                        if self.game.board[3][2] == 0 or self.game.board[3][2] == -1:
                            if self.game.board[2][3] == 0 or self.game.board[2][3] == -1:
                                score -= 1
                if self.game.board[4][2] == 0:
                    if self.game.board[4][0] == 0 or self.game.board[4][0] == -1:
                        if self.game.board[4][1] == 0 or self.game.board[4][1] == -1:
                            if self.game.board[4][3] == 0 or self.game.board[4][3] == -1:
                                score -= 1
                    if self.game.board[4][1] == 0 or self.game.board[4][1] == -1:
                        if self.game.board[4][3] == 0 or self.game.board[4][3] == -1:
                            if self.game.board[4][4] == 0 or self.game.board[4][4] == -1:
                                score -= 1
                    if self.game.board[4][3] == 0 or self.game.board[4][3] == -1:
                        if self.game.board[4][4] == 0 or self.game.board[4][4] == -1:
                            if self.game.board[4][5] == 0 or self.game.board[4][5] == -1:
                                score -= 1
                    if self.game.board[5][2] == 0 or self.game.board[5][2] == -1:
                        if self.game.board[3][2] == 0 or self.game.board[3][2] == -1:
                            if self.game.board[2][2] == 0 or self.game.board[2][2] == -1:
                                score -= 1
                    if self.game.board[3][2] == 0 or self.game.board[3][2] == -1:
                        if self.game.board[2][2] == 0 or self.game.board[2][2] == -1:
                            if self.game.board[1][2] == 0 or self.game.board[1][2] == -1:
                                score -= 1
                    if self.game.board[5][1] == 0 or self.game.board[5][1] == -1:
                        if self.game.board[3][3] == 0 or self.game.board[3][3] == -1:
                            if self.game.board[2][4] == 0 or self.game.board[2][4] == -1:
                                score -= 1
                    if self.game.board[3][3] == 0 or self.game.board[3][3] == -1:
                        if self.game.board[2][4] == 0 or self.game.board[2][4] == -1:
                            if self.game.board[1][5] == 0 or self.game.board[1][5] == -1:
                                score -= 1
                    if self.game.board[2][0] == 0 or self.game.board[2][0] == -1:
                        if self.game.board[3][1] == 0 or self.game.board[3][1] == -1:
                            if self.game.board[5][3] == 0 or self.game.board[5][3] == -1:
                                score -= 1
                if self.game.board[4][3] == 0:
                    if self.game.board[4][0] == 0 or self.game.board[4][0] == -1:
                        if self.game.board[4][1] == 0 or self.game.board[4][1] == -1:
                            if self.game.board[4][2] == 0 or self.game.board[4][2] == -1:
                                score -= 1
                    if self.game.board[4][1] == 0 or self.game.board[4][1] == -1:
                        if self.game.board[4][2] == 0 or self.game.board[4][2] == -1:
                            if self.game.board[4][4] == 0 or self.game.board[4][4] == -1:
                                score -= 1
                    if self.game.board[4][2] == 0 or self.game.board[4][2] == -1:
                        if self.game.board[4][4] == 0 or self.game.board[4][4] == -1:
                            if self.game.board[4][5] == 0 or self.game.board[4][5] == -1:
                                score -= 1
                    if self.game.board[4][4] == 0 or self.game.board[4][4] == -1:
                        if self.game.board[4][5] == 0 or self.game.board[4][5] == -1:
                            if self.game.board[4][6] == 0 or self.game.board[4][6] == -1:
                                score -= 1
                    if self.game.board[5][3] == 0 or self.game.board[5][3] == -1:
                        if self.game.board[3][3] == 0 or self.game.board[3][3] == -1:
                            if self.game.board[2][3] == 0 or self.game.board[2][3] == -1:
                                score -= 1
                    if self.game.board[3][3] == 0 or self.game.board[3][3] == -1:
                        if self.game.board[2][3] == 0 or self.game.board[2][3] == -1:
                            if self.game.board[1][3] == 0 or self.game.board[1][3] == -1:
                                score -= 1
                    if self.game.board[5][2] == 0 or self.game.board[5][2] == -1:
                        if self.game.board[3][4] == 0 or self.game.board[3][4] == -1:
                            if self.game.board[2][5] == 0 or self.game.board[2][5] == -1:
                                score -= 1
                    if self.game.board[3][4] == 0 or self.game.board[3][4] == -1:
                        if self.game.board[2][5] == 0 or self.game.board[2][5] == -1:
                            if self.game.board[1][6] == 0 or self.game.board[1][6] == -1:
                                score -= 1
                    if self.game.board[5][4] == 0 or self.game.board[5][4] == -1:
                        if self.game.board[3][2] == 0 or self.game.board[3][2] == -1:
                            if self.game.board[2][1] == 0 or self.game.board[2][1] == -1:
                                score -= 1
                    if self.game.board[3][2] == 0 or self.game.board[3][2] == -1:
                        if self.game.board[2][1] == 0 or self.game.board[2][1] == -1:
                            if self.game.board[1][0] == 0 or self.game.board[1][0] == -1:
                                score -= 1
                if self.game.board[4][4] == 0:
                    if self.game.board[4][1] == 0 or self.game.board[4][1] == -1:
                        if self.game.board[4][2] == 0 or self.game.board[4][2] == -1:
                            if self.game.board[4][3] == 0 or self.game.board[4][3] == -1:
                                score -= 1
                    if self.game.board[4][2] == 0 or self.game.board[4][2] == -1:
                        if self.game.board[4][3] == 0 or self.game.board[4][3] == -1:
                            if self.game.board[4][5] == 0 or self.game.board[4][5] == -1:
                                score -= 1
                    if self.game.board[4][3] == 0 or self.game.board[4][3] == -1:
                        if self.game.board[4][5] == 0 or self.game.board[4][5] == -1:
                            if self.game.board[4][6] == 0 or self.game.board[4][6] == -1:
                                score -= 1
                    if self.game.board[5][4] == 0 or self.game.board[5][4] == -1:
                        if self.game.board[3][4] == 0 or self.game.board[3][4] == -1:
                            if self.game.board[2][4] == 0 or self.game.board[2][4] == -1:
                                score -= 1
                    if self.game.board[3][4] == 0 or self.game.board[3][4] == -1:
                        if self.game.board[2][4] == 0 or self.game.board[2][4] == -1:
                            if self.game.board[1][4] == 0 or self.game.board[1][4] == -1:
                                score -= 1
                    if self.game.board[5][5] == 0 or self.game.board[5][5] == -1:
                        if self.game.board[3][3] == 0 or self.game.board[3][3] == -1:
                            if self.game.board[2][3] == 0 or self.game.board[2][3] == -1:
                                score -= 1
                    if self.game.board[3][3] == 0 or self.game.board[3][3] == -1:
                        if self.game.board[2][2] == 0 or self.game.board[2][2] == -1:
                            if self.game.board[1][1] == 0 or self.game.board[1][1] == -1:
                                score -= 1
                    if self.game.board[5][3] == 0 or self.game.board[5][3] == -1:
                        if self.game.board[3][5] == 0 or self.game.board[3][5] == -1:
                            if self.game.board[2][6] == 0 or self.game.board[2][6] == -1:
                                score -= 1
                if self.game.board[4][5] == 0:
                    if self.game.board[4][2] == 0 or self.game.board[4][2] == -1:
                        if self.game.board[4][3] == 0 or self.game.board[4][3] == -1:
                            if self.game.board[4][4] == 0 or self.game.board[4][4] == -1:
                                score -= 1
                    if self.game.board[4][3] == 0 or self.game.board[4][3] == -1:
                        if self.game.board[4][4] == 0 or self.game.board[4][4] == -1:
                            if self.game.board[4][6] == 0 or self.game.board[4][6] == -1:
                                score -= 1
                    if self.game.board[5][5] == 0 or self.game.board[5][5] == -1:
                        if self.game.board[3][5] == 0 or self.game.board[3][5] == -1:
                            if self.game.board[2][5] == 0 or self.game.board[2][5] == -1:
                                score -= 1
                    if self.game.board[3][5] == 0 or self.game.board[3][5] == -1:
                        if self.game.board[2][5] == 0 or self.game.board[2][5] == -1:
                            if self.game.board[1][5] == 0 or self.game.board[1][5] == -1:
                                score -= 1
                    if self.game.board[5][6] == 0 or self.game.board[5][6] == -1:
                        if self.game.board[3][4] == 0 or self.game.board[3][4] == -1:
                            if self.game.board[2][3] == 0 or self.game.board[2][3] == -1:
                                score -= 1
                    if self.game.board[3][4] == 0 or self.game.board[3][4] == -1:
                        if self.game.board[2][3] == 0 or self.game.board[2][3] == -1:
                            if self.game.board[1][2] == 0 or self.game.board[1][2] == -1:
                                score -= 1
                if self.game.board[4][6] == 0:
                    if self.game.board[4][3] == 0 or self.game.board[4][3] == -1:
                        if self.game.board[4][4] == 0 or self.game.board[4][4] == -1:
                            if self.game.board[4][5] == 0 or self.game.board[4][5] == -1:
                                score -= 1
                    if self.game.board[5][6] == 0 or self.game.board[5][6] == -1:
                        if self.game.board[3][6] == 0 or self.game.board[3][6] == -1:
                            if self.game.board[2][6] == 0 or self.game.board[2][6] == -1:
                                score -= 1
                    if self.game.board[3][6] == 0 or self.game.board[3][6] == -1:
                        if self.game.board[2][6] == 0 or self.game.board[2][6] == -1:
                            if self.game.board[1][6] == 0 or self.game.board[1][6] == -1:
                                score -= 1
                    if self.game.board[3][5] == 0 or self.game.board[3][5] == -1:
                        if self.game.board[2][4] == 0 or self.game.board[2][4] == -1:
                            if self.game.board[1][3] == 0 or self.game.board[1][3] == -1:
                                score -= 1
                if self.game.board[3][0] == 0:
                    if self.game.board[3][1] == 0 or self.game.board[3][1] == -1:
                        if self.game.board[3][2] == 0 or self.game.board[3][2] == -1:
                            if self.game.board[3][3] == 0 or self.game.board[3][3] == -1:
                                score -= 1
                    if self.game.board[5][0] == 0 or self.game.board[5][0] == -1:
                        if self.game.board[4][0] == 0 or self.game.board[4][0] == -1:
                            if self.game.board[2][0] == 0 or self.game.board[2][0] == -1:
                                score -= 1
                    if self.game.board[4][0] == 0 or self.game.board[4][0] == -1:
                        if self.game.board[2][0] == 0 or self.game.board[2][0] == -1:
                            if self.game.board[1][0] == 0 or self.game.board[1][0] == -1:
                                score -= 1
                    if self.game.board[2][0] == 0 or self.game.board[2][0] == -1:
                        if self.game.board[1][0] == 0 or self.game.board[1][0] == -1:
                            if self.game.board[0][0] == 0 or self.game.board[0][0] == -1:
                                score -= 1
                    if self.game.board[2][1] == 0 or self.game.board[2][1] == -1:
                        if self.game.board[1][2] == 0 or self.game.board[1][2] == -1:
                            if self.game.board[0][3] == 0 or self.game.board[0][3] == -1:
                                score -= 1
                if self.game.board[3][1] == 0:
                    if self.game.board[3][0] == 0 or self.game.board[3][0] == -1:
                        if self.game.board[3][2] == 0 or self.game.board[3][2] == -1:
                            if self.game.board[3][3] == 0 or self.game.board[3][3] == -1:
                                score -= 1
                    if self.game.board[3][2] == 0 or self.game.board[3][2] == -1:
                        if self.game.board[3][3] == 0 or self.game.board[3][3] == -1:
                            if self.game.board[3][4] == 0 or self.game.board[3][4] == -1:
                                score -= 1
                    if self.game.board[5][1] == 0 or self.game.board[5][1] == -1:
                        if self.game.board[4][1] == 0 or self.game.board[4][1] == -1:
                            if self.game.board[2][1] == 0 or self.game.board[2][1] == -1:
                                score -= 1
                    if self.game.board[4][1] == 0 or self.game.board[4][1] == -1:
                        if self.game.board[2][1] == 0 or self.game.board[2][1] == -1:
                            if self.game.board[1][1] == 0 or self.game.board[1][1] == -1:
                                score -= 1
                    if self.game.board[2][1] == 0 or self.game.board[2][1] == -1:
                        if self.game.board[1][1] == 0 or self.game.board[1][1] == -1:
                            if self.game.board[0][1] == 0 or self.game.board[0][1] == -1:
                                score -= 1
                    if self.game.board[2][2] == 0 or self.game.board[2][2] == -1:
                        if self.game.board[1][3] == 0 or self.game.board[1][3] == -1:
                            if self.game.board[0][4] == 0 or self.game.board[0][4] == -1:
                                score -= 1
                    if self.game.board[4][0] == 0 or self.game.board[4][0] == -1:
                        if self.game.board[2][2] == 0 or self.game.board[2][2] == -1:
                            if self.game.board[1][3] == 0 or self.game.board[1][3] == -1:
                                score -= 1
                    if self.game.board[2][0] == 0 or self.game.board[2][0] == -1:
                        if self.game.board[4][2] == 0 or self.game.board[4][2] == -1:
                            if self.game.board[5][3] == 0 or self.game.board[5][3] == -1:
                                score -= 1
                if self.game.board[3][2] == 0:
                    if self.game.board[3][0] == 0 or self.game.board[3][0] == -1:
                        if self.game.board[3][1] == 0 or self.game.board[3][1] == -1:
                            if self.game.board[3][3] == 0 or self.game.board[3][3] == -1:
                                score -= 1
                    if self.game.board[3][1] == 0 or self.game.board[3][1] == -1:
                        if self.game.board[3][3] == 0 or self.game.board[3][3] == -1:
                            if self.game.board[3][4] == 0 or self.game.board[3][4] == -1:
                                score -= 1
                    if self.game.board[3][3] == 0 or self.game.board[3][3] == -1:
                        if self.game.board[3][4] == 0 or self.game.board[3][4] == -1:
                            if self.game.board[3][5] == 0 or self.game.board[3][5] == -1:
                                score -= 1
                    if self.game.board[5][2] == 0 or self.game.board[5][2] == -1:
                        if self.game.board[4][2] == 0 or self.game.board[4][2] == -1:
                            if self.game.board[2][2] == 0 or self.game.board[2][2] == -1:
                                score -= 1
                    if self.game.board[4][2] == 0 or self.game.board[4][2] == -1:
                        if self.game.board[2][2] == 0 or self.game.board[2][2] == -1:
                            if self.game.board[1][2] == 0 or self.game.board[1][2] == -1:
                                score -= 1
                    if self.game.board[2][2] == 0 or self.game.board[2][2] == -1:
                        if self.game.board[1][2] == 0 or self.game.board[1][2] == -1:
                            if self.game.board[0][2] == 0 or self.game.board[0][2] == -1:
                                score -= 1
                    if self.game.board[5][0] == 0 or self.game.board[5][0] == -1:
                        if self.game.board[4][1] == 0 or self.game.board[4][1] == -1:
                            if self.game.board[2][3] == 0 or self.game.board[2][3] == -1:
                                score -= 1
                    if self.game.board[4][1] == 0 or self.game.board[4][1] == -1:
                        if self.game.board[2][3] == 0 or self.game.board[2][3] == -1:
                            if self.game.board[1][4] == 0 or self.game.board[1][4] == -1:
                                score -= 1
                    if self.game.board[2][3] == 0 or self.game.board[2][3] == -1:
                        if self.game.board[1][4] == 0 or self.game.board[1][4] == -1:
                            if self.game.board[0][5] == 0 or self.game.board[0][5] == -1:
                                score -= 1
                    if self.game.board[1][0] == 0 or self.game.board[1][0] == -1:
                        if self.game.board[2][1] == 0 or self.game.board[2][1] == -1:
                            if self.game.board[4][3] == 0 or self.game.board[4][3] == -1:
                                score -= 1
                    if self.game.board[2][1] == 0 or self.game.board[2][1] == -1:
                        if self.game.board[4][3] == 0 or self.game.board[4][3] == -1:
                            if self.game.board[5][4] == 0 or self.game.board[5][4] == -1:
                                score -= 1
                if self.game.board[3][3] == 0:
                    if self.game.board[3][0] == 0 or self.game.board[3][0] == -1:
                        if self.game.board[3][1] == 0 or self.game.board[3][1] == -1:
                            if self.game.board[3][2] == 0 or self.game.board[3][2] == -1:
                                score -= 1
                    if self.game.board[3][1] == 0 or self.game.board[3][1] == -1:
                        if self.game.board[3][2] == 0 or self.game.board[3][2] == -1:
                            if self.game.board[3][4] == 0 or self.game.board[3][4] == -1:
                                score -= 1
                    if self.game.board[3][2] == 0 or self.game.board[3][2] == -1:
                        if self.game.board[3][4] == 0 or self.game.board[3][4] == -1:
                            if self.game.board[3][5] == 0 or self.game.board[3][5] == -1:
                                score -= 1
                    if self.game.board[3][4] == 0 or self.game.board[3][4] == -1:
                        if self.game.board[3][5] == 0 or self.game.board[3][5] == -1:
                            if self.game.board[3][6] == 0 or self.game.board[3][6] == -1:
                                score -= 1
                    if self.game.board[5][3] == 0 or self.game.board[5][3] == -1:
                        if self.game.board[4][3] == 0 or self.game.board[4][3] == -1:
                            if self.game.board[2][3] == 0 or self.game.board[2][3] == -1:
                                score -= 1
                    if self.game.board[4][3] == 0 or self.game.board[4][3] == -1:
                        if self.game.board[2][3] == 0 or self.game.board[2][3] == -1:
                            if self.game.board[1][3] == 0 or self.game.board[1][3] == -1:
                                score -= 1
                    if self.game.board[2][3] == 0 or self.game.board[2][3] == -1:
                        if self.game.board[1][3] == 0 or self.game.board[1][3] == -1:
                            if self.game.board[0][3] == 0 or self.game.board[0][3] == -1:
                                score -= 1
                    if self.game.board[5][1] == 0 or self.game.board[5][1] == -1:
                        if self.game.board[4][2] == 0 or self.game.board[4][2] == -1:
                            if self.game.board[2][4] == 0 or self.game.board[2][4] == -1:
                                score -= 1
                    if self.game.board[4][2] == 0 or self.game.board[4][2] == -1:
                        if self.game.board[2][4] == 0 or self.game.board[2][4] == -1:
                            if self.game.board[1][5] == 0 or self.game.board[1][5] == -1:
                                score -= 1
                    if self.game.board[2][4] == 0 or self.game.board[2][4] == -1:
                        if self.game.board[1][5] == 0 or self.game.board[1][5] == -1:
                            if self.game.board[0][6] == 0 or self.game.board[0][6] == -1:
                                score -= 1
                    if self.game.board[0][0] == 0 or self.game.board[0][0] == -1:
                        if self.game.board[1][1] == 0 or self.game.board[1][1] == -1:
                            if self.game.board[2][2] == 0 or self.game.board[2][2] == -1:
                                score -= 1
                    if self.game.board[1][1] == 0 or self.game.board[1][1] == -1:
                        if self.game.board[2][2] == 0 or self.game.board[2][2] == -1:
                            if self.game.board[4][4] == 0 or self.game.board[4][4] == -1:
                                score -= 1
                    if self.game.board[2][2] == 0 or self.game.board[2][2] == -1:
                        if self.game.board[4][4] == 0 or self.game.board[4][4] == -1:
                            if self.game.board[5][5] == 0 or self.game.board[5][5] == -1:
                                score -= 1
                if self.game.board[3][4] == 0:
                    if self.game.board[3][1] == 0 or self.game.board[3][1] == -1:
                        if self.game.board[3][2] == 0 or self.game.board[3][2] == -1:
                            if self.game.board[3][3] == 0 or self.game.board[3][3] == -1:
                                score -= 1
                    if self.game.board[3][2] == 0 or self.game.board[3][2] == -1:
                        if self.game.board[3][3] == 0 or self.game.board[3][3] == -1:
                            if self.game.board[3][5] == 0 or self.game.board[3][5] == -1:
                                score -= 1
                    if self.game.board[3][3] == 0 or self.game.board[3][3] == -1:
                        if self.game.board[3][5] == 0 or self.game.board[3][5] == -1:
                            if self.game.board[3][6] == 0 or self.game.board[3][6] == -1:
                                score -= 1
                    if self.game.board[5][4] == 0 or self.game.board[5][4] == -1:
                        if self.game.board[4][4] == 0 or self.game.board[4][4] == -1:
                            if self.game.board[2][4] == 0 or self.game.board[2][4] == -1:
                                score -= 1
                    if self.game.board[4][4] == 0 or self.game.board[4][4] == -1:
                        if self.game.board[2][4] == 0 or self.game.board[2][4] == -1:
                            if self.game.board[1][4] == 0 or self.game.board[1][4] == -1:
                                score -= 1
                    if self.game.board[2][4] == 0 or self.game.board[2][4] == -1:
                        if self.game.board[1][4] == 0 or self.game.board[1][4] == -1:
                            if self.game.board[0][4] == 0 or self.game.board[0][4] == -1:
                                score -= 1
                    if self.game.board[5][2] == 0 or self.game.board[5][2] == -1:
                        if self.game.board[4][3] == 0 or self.game.board[4][3] == -1:
                            if self.game.board[2][5] == 0 or self.game.board[2][5] == -1:
                                score -= 1
                    if self.game.board[4][3] == 0 or self.game.board[4][3] == -1:
                        if self.game.board[2][5] == 0 or self.game.board[2][5] == -1:
                            if self.game.board[1][6] == 0 or self.game.board[1][6] == -1:
                                score -= 1
                    if self.game.board[0][1] == 0 or self.game.board[0][1] == -1:
                        if self.game.board[1][2] == 0 or self.game.board[1][2] == -1:
                            if self.game.board[2][3] == 0 or self.game.board[2][3] == -1:
                                score -= 1
                    if self.game.board[1][2] == 0 or self.game.board[1][2] == -1:
                        if self.game.board[2][3] == 0 or self.game.board[2][3] == -1:
                            if self.game.board[4][5] == 0 or self.game.board[4][5] == -1:
                                score -= 1
                    if self.game.board[2][3] == 0 or self.game.board[2][3] == -1:
                        if self.game.board[4][5] == 0 or self.game.board[4][5] == -1:
                            if self.game.board[5][6] == 0 or self.game.board[5][6] == -1:
                                score -= 1
                if self.game.board[3][5] == 0:
                    if self.game.board[3][2] == 0 or self.game.board[3][2] == -1:
                        if self.game.board[3][3] == 0 or self.game.board[3][3] == -1:
                            if self.game.board[3][4] == 0 or self.game.board[3][4] == -1:
                                score -= 1
                    if self.game.board[3][3] == 0 or self.game.board[3][3] == -1:
                        if self.game.board[3][4] == 0 or self.game.board[3][4] == -1:
                            if self.game.board[3][6] == 0 or self.game.board[3][6] == -1:
                                score -= 1
                    if self.game.board[5][5] == 0 or self.game.board[5][5] == -1:
                        if self.game.board[4][5] == 0 or self.game.board[4][5] == -1:
                            if self.game.board[2][5] == 0 or self.game.board[2][5] == -1:
                                score -= 1
                    if self.game.board[4][5] == 0 or self.game.board[4][5] == -1:
                        if self.game.board[2][5] == 0 or self.game.board[2][5] == -1:
                            if self.game.board[1][5] == 0 or self.game.board[1][5] == -1:
                                score -= 1
                    if self.game.board[2][5] == 0 or self.game.board[2][5] == -1:
                        if self.game.board[1][5] == 0 or self.game.board[1][5] == -1:
                            if self.game.board[0][5] == 0 or self.game.board[0][5] == -1:
                                score -= 1
                    if self.game.board[5][3] == 0 or self.game.board[5][3] == -1:
                        if self.game.board[4][4] == 0 or self.game.board[4][4] == -1:
                            if self.game.board[2][6] == 0 or self.game.board[2][6] == -1:
                                score -= 1
                    if self.game.board[0][2] == 0 or self.game.board[0][2] == -1:
                        if self.game.board[1][3] == 0 or self.game.board[1][3] == -1:
                            if self.game.board[2][4] == 0 or self.game.board[2][4] == -1:
                                score -= 1
                    if self.game.board[1][3] == 0 or self.game.board[1][3] == -1:
                        if self.game.board[2][4] == 0 or self.game.board[2][4] == -1:
                            if self.game.board[4][6] == 0 or self.game.board[4][6] == -1:
                                score -= 1
                if self.game.board[3][6] == 0:
                    if self.game.board[3][3] == 0 or self.game.board[3][3] == -1:
                        if self.game.board[3][4] == 0 or self.game.board[3][4] == -1:
                            if self.game.board[3][5] == 0 or self.game.board[3][5] == -1:
                                score -= 1
                    if self.game.board[5][6] == 0 or self.game.board[5][6] == -1:
                        if self.game.board[4][6] == 0 or self.game.board[4][6] == -1:
                            if self.game.board[2][6] == 0 or self.game.board[2][6] == -1:
                                score -= 1
                    if self.game.board[4][6] == 0 or self.game.board[4][6] == -1:
                        if self.game.board[2][6] == 0 or self.game.board[2][6] == -1:
                            if self.game.board[1][6] == 0 or self.game.board[1][6] == -1:
                                score -= 1
                    if self.game.board[2][6] == 0 or self.game.board[2][6] == -1:
                        if self.game.board[1][6] == 0 or self.game.board[1][6] == -1:
                            if self.game.board[0][6] == 0 or self.game.board[0][6] == -1:
                                score -= 1
                    if self.game.board[0][3] == 0 or self.game.board[0][3] == -1:
                        if self.game.board[1][4] == 0 or self.game.board[1][4] == -1:
                            if self.game.board[2][5] == 0 or self.game.board[2][5] == -1:
                                score -= 1
                if self.game.board[2][0] == 0:
                    if self.game.board[2][1] == 0 or self.game.board[2][1] == -1:
                        if self.game.board[2][2] == 0 or self.game.board[2][2] == -1:
                            if self.game.board[2][3] == 0 or self.game.board[2][3] == -1:
                                score -= 1
                    if self.game.board[5][0] == 0 or self.game.board[5][0] == -1:
                        if self.game.board[4][0] == 0 or self.game.board[4][0] == -1:
                            if self.game.board[3][0] == 0 or self.game.board[3][0] == -1:
                                score -= 1
                    if self.game.board[4][0] == 0 or self.game.board[4][0] == -1:
                        if self.game.board[3][0] == 0 or self.game.board[3][0] == -1:
                            if self.game.board[1][0] == 0 or self.game.board[1][0] == -1:
                                score -= 1
                    if self.game.board[3][0] == 0 or self.game.board[3][0] == -1:
                        if self.game.board[1][0] == 0 or self.game.board[1][0] == -1:
                            if self.game.board[0][0] == 0 or self.game.board[0][0] == -1:
                                score -= 1
                    if self.game.board[3][1] == 0 or self.game.board[3][1] == -1:
                        if self.game.board[4][2] == 0 or self.game.board[4][2] == -1:
                            if self.game.board[5][3] == 0 or self.game.board[5][3] == -1:
                                score -= 1
                if self.game.board[2][1] == 0:
                    if self.game.board[2][0] == 0 or self.game.board[2][0] == -1:
                        if self.game.board[2][2] == 0 or self.game.board[2][2] == -1:
                            if self.game.board[2][3] == 0 or self.game.board[2][3] == -1:
                                score -= 1
                    if self.game.board[2][2] == 0 or self.game.board[2][2] == -1:
                        if self.game.board[2][3] == 0 or self.game.board[2][3] == -1:
                            if self.game.board[2][4] == 0 or self.game.board[2][4] == -1:
                                score -= 1
                    if self.game.board[5][1] == 0 or self.game.board[5][1] == -1:
                        if self.game.board[4][1] == 0 or self.game.board[4][1] == -1:
                            if self.game.board[3][1] == 0 or self.game.board[3][1] == -1:
                                score -= 1
                    if self.game.board[4][1] == 0 or self.game.board[4][1] == -1:
                        if self.game.board[3][1] == 0 or self.game.board[3][1] == -1:
                            if self.game.board[1][1] == 0 or self.game.board[1][1] == -1:
                                score -= 1
                    if self.game.board[3][1] == 0 or self.game.board[3][1] == -1:
                        if self.game.board[1][1] == 0 or self.game.board[1][1] == -1:
                            if self.game.board[0][1] == 0 or self.game.board[0][1] == -1:
                                score -= 1
                    if self.game.board[3][0] == 0 or self.game.board[3][0] == -1:
                        if self.game.board[1][2] == 0 or self.game.board[1][2] == -1:
                            if self.game.board[0][3] == 0 or self.game.board[0][3] == -1:
                                score -= 1
                    if self.game.board[5][4] == 0 or self.game.board[5][4] == -1:
                        if self.game.board[4][3] == 0 or self.game.board[4][3] == -1:
                            if self.game.board[3][2] == 0 or self.game.board[3][2] == -1:
                                score -= 1
                    if self.game.board[4][3] == 0 or self.game.board[4][3] == -1:
                        if self.game.board[3][2] == 0 or self.game.board[3][2] == -1:
                            if self.game.board[1][0] == 0 or self.game.board[1][0] == -1:
                                score -= 1
                if self.game.board[2][2] == 0:
                    if self.game.board[2][0] == 0 or self.game.board[2][0] == -1:
                        if self.game.board[2][1] == 0 or self.game.board[2][1] == -1:
                            if self.game.board[2][3] == 0 or self.game.board[2][3] == -1:
                                score -= 1
                    if self.game.board[2][1] == 0 or self.game.board[2][1] == -1:
                        if self.game.board[2][3] == 0 or self.game.board[2][3] == -1:
                            if self.game.board[2][4] == 0 or self.game.board[2][4] == -1:
                                score -= 1
                    if self.game.board[2][3] == 0 or self.game.board[2][3] == -1:
                        if self.game.board[2][4] == 0 or self.game.board[2][4] == -1:
                            if self.game.board[2][5] == 0 or self.game.board[2][5] == -1:
                                score -= 1
                    if self.game.board[5][2] == 0 or self.game.board[5][2] == -1:
                        if self.game.board[4][2] == 0 or self.game.board[4][2] == -1:
                            if self.game.board[3][2] == 0 or self.game.board[3][2] == -1:
                                score -= 1
                    if self.game.board[4][2] == 0 or self.game.board[4][2] == -1:
                        if self.game.board[3][2] == 0 or self.game.board[3][2] == -1:
                            if self.game.board[1][2] == 0 or self.game.board[1][2] == -1:
                                score -= 1
                    if self.game.board[3][2] == 0 or self.game.board[3][2] == -1:
                        if self.game.board[1][2] == 0 or self.game.board[1][2] == -1:
                            if self.game.board[0][2] == 0 or self.game.board[0][2] == -1:
                                score -= 1
                    if self.game.board[4][0] == 0 or self.game.board[4][0] == -1:
                        if self.game.board[3][1] == 0 or self.game.board[3][1] == -1:
                            if self.game.board[1][3] == 0 or self.game.board[1][3] == -1:
                                score -= 1
                    if self.game.board[3][1] == 0 or self.game.board[3][1] == -1:
                        if self.game.board[1][3] == 0 or self.game.board[1][3] == -1:
                            if self.game.board[0][4] == 0 or self.game.board[0][4] == -1:
                                score -= 1
                    if self.game.board[5][5] == 0 or self.game.board[5][5] == -1:
                        if self.game.board[4][4] == 0 or self.game.board[4][4] == -1:
                            if self.game.board[3][3] == 0 or self.game.board[3][3] == -1:
                                score -= 1
                    if self.game.board[4][4] == 0 or self.game.board[4][4] == -1:
                        if self.game.board[3][3] == 0 or self.game.board[3][3] == -1:
                            if self.game.board[1][1] == 0 or self.game.board[1][1] == -1:
                                score -= 1
                    if self.game.board[2][2] == 0 or self.game.board[2][2] == -1:
                        if self.game.board[1][1] == 0 or self.game.board[1][1] == -1:
                            if self.game.board[0][0] == 0 or self.game.board[0][0] == -1:
                                score -= 1
                if self.game.board[2][3] == 0:
                    if self.game.board[2][0] == 0 or self.game.board[2][0] == -1:
                        if self.game.board[2][1] == 0 or self.game.board[2][1] == -1:
                            if self.game.board[2][2] == 0 or self.game.board[2][2] == -1:
                                score -= 1
                    if self.game.board[2][1] == 0 or self.game.board[2][1] == -1:
                        if self.game.board[2][2] == 0 or self.game.board[2][2] == -1:
                            if self.game.board[2][4] == 0 or self.game.board[2][4] == -1:
                                score -= 1
                    if self.game.board[2][2] == 0 or self.game.board[2][2] == -1:
                        if self.game.board[2][4] == 0 or self.game.board[2][4] == -1:
                            if self.game.board[2][5] == 0 or self.game.board[2][5] == -1:
                                score -= 1
                    if self.game.board[2][4] == 0 or self.game.board[2][4] == -1:
                        if self.game.board[2][5] == 0 or self.game.board[2][5] == -1:
                            if self.game.board[2][6] == 0 or self.game.board[2][6] == -1:
                                score -= 1
                    if self.game.board[5][3] == 0 or self.game.board[5][3] == -1:
                        if self.game.board[4][3] == 0 or self.game.board[4][3] == -1:
                            if self.game.board[3][3] == 0 or self.game.board[3][3] == -1:
                                score -= 1
                    if self.game.board[4][3] == 0 or self.game.board[4][3] == -1:
                        if self.game.board[3][3] == 0 or self.game.board[3][3] == -1:
                            if self.game.board[1][3] == 0 or self.game.board[1][3] == -1:
                                score -= 1
                    if self.game.board[3][3] == 0 or self.game.board[3][3] == -1:
                        if self.game.board[1][3] == 0 or self.game.board[1][3] == -1:
                            if self.game.board[0][3] == 0 or self.game.board[0][3] == -1:
                                score -= 1
                    if self.game.board[5][0] == 0 or self.game.board[5][0] == -1:
                        if self.game.board[4][1] == 0 or self.game.board[4][1] == -1:
                            if self.game.board[3][2] == 0 or self.game.board[3][2] == -1:
                                score -= 1
                    if self.game.board[4][1] == 0 or self.game.board[4][1] == -1:
                        if self.game.board[3][2] == 0 or self.game.board[3][2] == -1:
                            if self.game.board[1][4] == 0 or self.game.board[1][4] == -1:
                                score -= 1
                    if self.game.board[3][2] == 0 or self.game.board[3][2] == -1:
                        if self.game.board[1][4] == 0 or self.game.board[1][4] == -1:
                            if self.game.board[0][5] == 0 or self.game.board[0][5] == -1:
                                score -= 1
                    if self.game.board[5][6] == 0 or self.game.board[5][6] == -1:
                        if self.game.board[4][5] == 0 or self.game.board[4][5] == -1:
                            if self.game.board[3][4] == 0 or self.game.board[3][4] == -1:
                                score -= 1
                    if self.game.board[4][5] == 0 or self.game.board[4][5] == -1:
                        if self.game.board[3][4] == 0 or self.game.board[3][4] == -1:
                            if self.game.board[1][2] == 0 or self.game.board[1][2] == -1:
                                score -= 1
                    if self.game.board[3][4] == 0 or self.game.board[3][4] == -1:
                        if self.game.board[1][2] == 0 or self.game.board[1][2] == -1:
                            if self.game.board[0][1] == 0 or self.game.board[0][1] == -1:
                                score -= 1
                if self.game.board[2][4] == 0:
                    if self.game.board[2][1] == 0 or self.game.board[2][1] == -1:
                        if self.game.board[2][2] == 0 or self.game.board[2][2] == -1:
                            if self.game.board[2][3] == 0 or self.game.board[2][3] == -1:
                                score -= 1
                    if self.game.board[2][2] == 0 or self.game.board[2][2] == -1:
                        if self.game.board[2][3] == 0 or self.game.board[2][3] == -1:
                            if self.game.board[2][5] == 0 or self.game.board[2][5] == -1:
                                score -= 1
                    if self.game.board[2][3] == 0 or self.game.board[2][3] == -1:
                        if self.game.board[2][5] == 0 or self.game.board[2][5] == -1:
                            if self.game.board[2][6] == 0 or self.game.board[2][6] == -1:
                                score -= 1
                    if self.game.board[5][4] == 0 or self.game.board[5][4] == -1:
                        if self.game.board[4][4] == 0 or self.game.board[4][4] == -1:
                            if self.game.board[3][4] == 0 or self.game.board[3][4] == -1:
                                score -= 1
                    if self.game.board[4][4] == 0 or self.game.board[4][4] == -1:
                        if self.game.board[3][4] == 0 or self.game.board[3][4] == -1:
                            if self.game.board[1][4] == 0 or self.game.board[1][4] == -1:
                                score -= 1
                    if self.game.board[3][4] == 0 or self.game.board[3][4] == -1:
                        if self.game.board[1][4] == 0 or self.game.board[1][4] == -1:
                            if self.game.board[0][4] == 0 or self.game.board[0][4] == -1:
                                score -= 1
                    if self.game.board[5][1] == 0 or self.game.board[5][1] == -1:
                        if self.game.board[4][2] == 0 or self.game.board[4][2] == -1:
                            if self.game.board[3][3] == 0 or self.game.board[3][3] == -1:
                                score -= 1
                    if self.game.board[4][2] == 0 or self.game.board[4][2] == -1:
                        if self.game.board[3][3] == 0 or self.game.board[3][3] == -1:
                            if self.game.board[1][5] == 0 or self.game.board[1][5] == -1:
                                score -= 1
                    if self.game.board[3][3] == 0 or self.game.board[3][3] == -1:
                        if self.game.board[1][5] == 0 or self.game.board[1][5] == -1:
                            if self.game.board[0][6] == 0 or self.game.board[0][6] == -1:
                                score -= 1
                    if self.game.board[4][6] == 0 or self.game.board[4][6] == -1:
                        if self.game.board[3][5] == 0 or self.game.board[3][5] == -1:
                            if self.game.board[1][3] == 0 or self.game.board[1][3] == -1:
                                score -= 1
                    if self.game.board[3][5] == 0 or self.game.board[3][5] == -1:
                        if self.game.board[1][3] == 0 or self.game.board[1][3] == -1:
                            if self.game.board[0][2] == 0 or self.game.board[0][2] == -1:
                                score -= 1
                if self.game.board[2][5] == 0:
                    if self.game.board[2][2] == 0 or self.game.board[2][2] == -1:
                        if self.game.board[2][3] == 0 or self.game.board[2][3] == -1:
                            if self.game.board[2][4] == 0 or self.game.board[2][4] == -1:
                                score -= 1
                    if self.game.board[2][3] == 0 or self.game.board[2][3] == -1:
                        if self.game.board[2][4] == 0 or self.game.board[2][4] == -1:
                            if self.game.board[2][6] == 0 or self.game.board[2][6] == -1:
                                score -= 1
                    if self.game.board[5][5] == 0 or self.game.board[5][5] == -1:
                        if self.game.board[4][5] == 0 or self.game.board[4][5] == -1:
                            if self.game.board[3][5] == 0 or self.game.board[3][5] == -1:
                                score -= 1
                    if self.game.board[4][5] == 0 or self.game.board[4][5] == -1:
                        if self.game.board[3][5] == 0 or self.game.board[3][5] == -1:
                            if self.game.board[1][5] == 0 or self.game.board[1][5] == -1:
                                score -= 1
                    if self.game.board[3][5] == 0 or self.game.board[3][5] == -1:
                        if self.game.board[1][5] == 0 or self.game.board[1][5] == -1:
                            if self.game.board[0][5] == 0 or self.game.board[0][5] == -1:
                                score -= 1
                    if self.game.board[5][2] == 0 or self.game.board[5][2] == -1:
                        if self.game.board[4][3] == 0 or self.game.board[4][3] == -1:
                            if self.game.board[3][4] == 0 or self.game.board[3][4] == -1:
                                score -= 1
                    if self.game.board[4][3] == 0 or self.game.board[4][3] == -1:
                        if self.game.board[3][4] == 0 or self.game.board[3][4] == -1:
                            if self.game.board[1][6] == 0 or self.game.board[1][6] == -1:
                                score -= 1
                    if self.game.board[3][6] == 0 or self.game.board[3][6] == -1:
                        if self.game.board[1][4] == 0 or self.game.board[1][4] == -1:
                            if self.game.board[0][3] == 0 or self.game.board[0][3] == -1:
                                score -= 1
                if self.game.board[2][6] == 0:
                    if self.game.board[2][3] == 0 or self.game.board[2][3] == -1:
                        if self.game.board[2][4] == 0 or self.game.board[2][4] == -1:
                            if self.game.board[2][5] == 0 or self.game.board[2][5] == -1:
                                score -= 1
                    if self.game.board[5][6] == 0 or self.game.board[5][6] == -1:
                        if self.game.board[4][6] == 0 or self.game.board[4][6] == -1:
                            if self.game.board[3][6] == 0 or self.game.board[3][6] == -1:
                                score -= 1
                    if self.game.board[4][6] == 0 or self.game.board[4][6] == -1:
                        if self.game.board[3][6] == 0 or self.game.board[3][6] == -1:
                            if self.game.board[1][6] == 0 or self.game.board[1][6] == -1:
                                score -= 1
                    if self.game.board[3][6] == 0 or self.game.board[3][6] == -1:
                        if self.game.board[1][6] == 0 or self.game.board[1][6] == -1:
                            if self.game.board[0][6] == 0 or self.game.board[0][6] == -1:
                                score -= 1
                    if self.game.board[5][3] == 0 or self.game.board[5][3] == -1:
                        if self.game.board[4][4] == 0 or self.game.board[4][4] == -1:
                            if self.game.board[3][5] == 0 or self.game.board[3][5] == -1:
                                score -= 1
                if self.game.board[1][0] == 0:
                    if self.game.board[1][1] == 0 or self.game.board[1][1] == -1:
                        if self.game.board[1][2] == 0 or self.game.board[1][2] == -1:
                            if self.game.board[1][3] == 0 or self.game.board[1][3] == -1:
                                score -= 1
                    if self.game.board[4][0] == 0 or self.game.board[4][0] == -1:
                        if self.game.board[3][0] == 0 or self.game.board[3][0] == -1:
                            if self.game.board[2][0] == 0 or self.game.board[2][0] == -1:
                                score -= 1
                    if self.game.board[3][0] == 0 or self.game.board[3][0] == -1:
                        if self.game.board[2][0] == 0 or self.game.board[2][0] == -1:
                            if self.game.board[0][0] == 0 or self.game.board[0][0] == -1:
                                score -= 1
                    if self.game.board[4][3] == 0 or self.game.board[4][3] == -1:
                        if self.game.board[3][2] == 0 or self.game.board[3][2] == -1:
                            if self.game.board[2][1] == 0 or self.game.board[2][1] == -1:
                                score -= 1
                if self.game.board[1][1] == 0:
                    if self.game.board[1][0] == 0 or self.game.board[1][0] == -1:
                        if self.game.board[1][2] == 0 or self.game.board[1][2] == -1:
                            if self.game.board[1][3] == 0 or self.game.board[1][3] == -1:
                                score -= 1
                    if self.game.board[1][2] == 0 or self.game.board[1][2] == -1:
                        if self.game.board[1][3] == 0 or self.game.board[1][3] == -1:
                            if self.game.board[1][4] == 0 or self.game.board[1][4] == -1:
                                score -= 1
                    if self.game.board[4][1] == 0 or self.game.board[4][1] == -1:
                        if self.game.board[3][1] == 0 or self.game.board[3][1] == -1:
                            if self.game.board[2][1] == 0 or self.game.board[2][1] == -1:
                                score -= 1
                    if self.game.board[3][1] == 0 or self.game.board[3][1] == -1:
                        if self.game.board[2][1] == 0 or self.game.board[2][1] == -1:
                            if self.game.board[0][1] == 0 or self.game.board[0][1] == -1:
                                score -= 1
                    if self.game.board[4][4] == 0 or self.game.board[4][4] == -1:
                        if self.game.board[3][3] == 0 or self.game.board[3][3] == -1:
                            if self.game.board[2][2] == 0 or self.game.board[2][2] == -1:
                                score -= 1
                    if self.game.board[3][3] == 0 or self.game.board[3][3] == -1:
                        if self.game.board[2][2] == 0 or self.game.board[2][2] == -1:
                            if self.game.board[0][0] == 0 or self.game.board[0][0] == -1:
                                score -= 1
                if self.game.board[1][2] == 0:
                    if self.game.board[1][0] == 0 or self.game.board[1][0] == -1:
                        if self.game.board[1][1] == 0 or self.game.board[1][1] == -1:
                            if self.game.board[1][3] == 0 or self.game.board[1][3] == -1:
                                score -= 1
                    if self.game.board[1][1] == 0 or self.game.board[1][1] == -1:
                        if self.game.board[1][3] == 0 or self.game.board[1][3] == -1:
                            if self.game.board[1][4] == 0 or self.game.board[1][4] == -1:
                                score -= 1
                    if self.game.board[1][3] == 0 or self.game.board[1][3] == -1:
                        if self.game.board[1][4] == 0 or self.game.board[1][4] == -1:
                            if self.game.board[1][5] == 0 or self.game.board[1][5] == -1:
                                score -= 1
                    if self.game.board[4][2] == 0 or self.game.board[4][2] == -1:
                        if self.game.board[3][2] == 0 or self.game.board[3][2] == -1:
                            if self.game.board[2][2] == 0 or self.game.board[2][2] == -1:
                                score -= 1
                    if self.game.board[3][2] == 0 or self.game.board[3][2] == -1:
                        if self.game.board[2][2] == 0 or self.game.board[2][2] == -1:
                            if self.game.board[0][2] == 0 or self.game.board[0][2] == -1:
                                score -= 1
                    if self.game.board[3][0] == 0 or self.game.board[3][0] == -1:
                        if self.game.board[2][1] == 0 or self.game.board[2][1] == -1:
                            if self.game.board[0][3] == 0 or self.game.board[0][3] == -1:
                                score -= 1
                    if self.game.board[4][5] == 0 or self.game.board[4][5] == -1:
                        if self.game.board[3][4] == 0 or self.game.board[3][4] == -1:
                            if self.game.board[2][3] == 0 or self.game.board[2][3] == -1:
                                score -= 1
                    if self.game.board[3][4] == 0 or self.game.board[3][4] == -1:
                        if self.game.board[2][3] == 0 or self.game.board[2][3] == -1:
                            if self.game.board[0][1] == 0 or self.game.board[0][1] == -1:
                                score -= 1
                if self.game.board[1][3] == 0:
                    if self.game.board[1][0] == 0 or self.game.board[1][0] == -1:
                        if self.game.board[1][1] == 0 or self.game.board[1][1] == -1:
                            if self.game.board[1][2] == 0 or self.game.board[1][2] == -1:
                                score -= 1
                    if self.game.board[1][1] == 0 or self.game.board[1][1] == -1:
                        if self.game.board[1][2] == 0 or self.game.board[1][2] == -1:
                            if self.game.board[1][4] == 0 or self.game.board[1][4] == -1:
                                score -= 1
                    if self.game.board[1][2] == 0 or self.game.board[1][2] == -1:
                        if self.game.board[1][4] == 0 or self.game.board[1][4] == -1:
                            if self.game.board[1][5] == 0 or self.game.board[1][5] == -1:
                                score -= 1
                    if self.game.board[1][4] == 0 or self.game.board[1][4] == -1:
                        if self.game.board[1][5] == 0 or self.game.board[1][5] == -1:
                            if self.game.board[1][6] == 0 or self.game.board[1][6] == -1:
                                score -= 1
                    if self.game.board[4][3] == 0 or self.game.board[4][3] == -1:
                        if self.game.board[3][3] == 0 or self.game.board[3][3] == -1:
                            if self.game.board[2][3] == 0 or self.game.board[2][3] == -1:
                                score -= 1
                    if self.game.board[3][3] == 0 or self.game.board[3][3] == -1:
                        if self.game.board[2][3] == 0 or self.game.board[2][3] == -1:
                            if self.game.board[0][3] == 0 or self.game.board[0][3] == -1:
                                score -= 1
                    if self.game.board[4][0] == 0 or self.game.board[4][0] == -1:
                        if self.game.board[3][1] == 0 or self.game.board[3][1] == -1:
                            if self.game.board[2][2] == 0 or self.game.board[2][2] == -1:
                                score -= 1
                    if self.game.board[3][1] == 0 or self.game.board[3][1] == -1:
                        if self.game.board[2][2] == 0 or self.game.board[2][2] == -1:
                            if self.game.board[0][4] == 0 or self.game.board[0][4] == -1:
                                score -= 1
                    if self.game.board[4][6] == 0 or self.game.board[4][6] == -1:
                        if self.game.board[3][5] == 0 or self.game.board[3][5] == -1:
                            if self.game.board[2][4] == 0 or self.game.board[2][4] == -1:
                                score -= 1
                    if self.game.board[3][5] == 0 or self.game.board[3][5] == -1:
                        if self.game.board[2][4] == 0 or self.game.board[2][4] == -1:
                            if self.game.board[0][2] == 0 or self.game.board[0][2] == -1:
                                score -= 1
                if self.game.board[1][4] == 0:
                    if self.game.board[1][1] == 0 or self.game.board[1][1] == -1:
                        if self.game.board[1][2] == 0 or self.game.board[1][2] == -1:
                            if self.game.board[1][3] == 0 or self.game.board[1][3] == -1:
                                score -= 1
                    if self.game.board[1][2] == 0 or self.game.board[1][2] == -1:
                        if self.game.board[1][3] == 0 or self.game.board[1][3] == -1:
                            if self.game.board[1][5] == 0 or self.game.board[1][5] == -1:
                                score -= 1
                    if self.game.board[1][3] == 0 or self.game.board[1][3] == -1:
                        if self.game.board[1][5] == 0 or self.game.board[1][5] == -1:
                            if self.game.board[1][6] == 0 or self.game.board[1][6] == -1:
                                score -= 1
                    if self.game.board[4][4] == 0 or self.game.board[4][4] == -1:
                        if self.game.board[3][4] == 0 or self.game.board[3][4] == -1:
                            if self.game.board[2][4] == 0 or self.game.board[2][4] == -1:
                                score -= 1
                    if self.game.board[3][4] == 0 or self.game.board[3][4] == -1:
                        if self.game.board[2][4] == 0 or self.game.board[2][4] == -1:
                            if self.game.board[0][4] == 0 or self.game.board[0][4] == -1:
                                score -= 1
                    if self.game.board[4][1] == 0 or self.game.board[4][1] == -1:
                        if self.game.board[3][2] == 0 or self.game.board[3][2] == -1:
                            if self.game.board[2][3] == 0 or self.game.board[2][3] == -1:
                                score -= 1
                    if self.game.board[3][2] == 0 or self.game.board[3][2] == -1:
                        if self.game.board[2][3] == 0 or self.game.board[2][3] == -1:
                            if self.game.board[0][5] == 0 or self.game.board[0][5] == -1:
                                score -= 1
                    if self.game.board[3][6] == 0 or self.game.board[3][6] == -1:
                        if self.game.board[2][5] == 0 or self.game.board[2][5] == -1:
                            if self.game.board[0][3] == 0 or self.game.board[0][3] == -1:
                                score -= 1
                if self.game.board[1][5] == 0:
                    if self.game.board[1][2] == 0 or self.game.board[1][2] == -1:
                        if self.game.board[1][3] == 0 or self.game.board[1][3] == -1:
                            if self.game.board[1][4] == 0 or self.game.board[1][4] == -1:
                                score -= 1
                    if self.game.board[1][3] == 0 or self.game.board[1][3] == -1:
                        if self.game.board[1][4] == 0 or self.game.board[1][4] == -1:
                            if self.game.board[1][6] == 0 or self.game.board[1][6] == -1:
                                score -= 1
                    if self.game.board[4][5] == 0 or self.game.board[4][5] == -1:
                        if self.game.board[3][5] == 0 or self.game.board[3][5] == -1:
                            if self.game.board[2][5] == 0 or self.game.board[2][5] == -1:
                                score -= 1
                    if self.game.board[3][5] == 0 or self.game.board[3][5] == -1:
                        if self.game.board[2][5] == 0 or self.game.board[2][5] == -1:
                            if self.game.board[0][5] == 0 or self.game.board[0][5] == -1:
                                score -= 1
                    if self.game.board[4][2] == 0 or self.game.board[4][2] == -1:
                        if self.game.board[3][3] == 0 or self.game.board[3][3] == -1:
                            if self.game.board[2][4] == 0 or self.game.board[2][4] == -1:
                                score -= 1
                    if self.game.board[3][3] == 0 or self.game.board[3][3] == -1:
                        if self.game.board[2][4] == 0 or self.game.board[2][4] == -1:
                            if self.game.board[0][6] == 0 or self.game.board[0][6] == -1:
                                score -= 1
                if self.game.board[1][6] == 0:
                    if self.game.board[1][3] == 0 or self.game.board[1][3] == -1:
                        if self.game.board[1][4] == 0 or self.game.board[1][4] == -1:
                            if self.game.board[1][5] == 0 or self.game.board[1][5] == -1:
                                score -= 1

                    if self.game.board[4][6] == 0 or self.game.board[4][6] == -1:
                        if self.game.board[3][6] == 0 or self.game.board[3][6] == -1:
                            if self.game.board[2][6] == 0 or self.game.board[2][6] == -1:
                                score -= 1
                    if self.game.board[3][6] == 0 or self.game.board[3][6] == -1:
                        if self.game.board[2][6] == 0 or self.game.board[2][6] == -1:
                            if self.game.board[0][6] == 0 or self.game.board[0][6] == -1:
                                score -= 1
                    if self.game.board[4][3] == 0 or self.game.board[4][3] == -1:
                        if self.game.board[3][4] == 0 or self.game.board[3][4] == -1:
                            if self.game.board[2][5] == 0 or self.game.board[2][5] == -1:
                                score -= 1
                if self.game.board[0][0] == 0:
                    if self.game.board[3][0] == 0 or self.game.board[3][0] == -1:
                        if self.game.board[2][0] == 0 or self.game.board[2][0] == -1:
                            if self.game.board[1][0] == 0 or self.game.board[1][0] == -1:
                                score -= 1
                    if self.game.board[0][1] == 0 or self.game.board[0][1] == -1:
                        if self.game.board[0][2] == 0 or self.game.board[0][2] == -1:
                            if self.game.board[0][3] == 0 or self.game.board[0][3] == -1:
                                score -= 1
                    if self.game.board[3][3] == 0 or self.game.board[3][3] == -1:
                        if self.game.board[2][2] == 0 or self.game.board[2][2] == -1:
                            if self.game.board[1][1] == 0 or self.game.board[1][1] == -1:
                                score -= 1
                if self.game.board[0][1] == 0:
                    if self.game.board[0][0] == 0 or self.game.board[0][0] == -1:
                        if self.game.board[0][2] == 0 or self.game.board[0][2] == -1:
                            if self.game.board[0][3] == 0 or self.game.board[0][3] == -1:
                                score -= 1
                    if self.game.board[0][2] == 0 or self.game.board[0][2] == -1:
                        if self.game.board[0][3] == 0 or self.game.board[0][3] == -1:
                            if self.game.board[0][4] == 0 or self.game.board[0][4] == -1:
                                score -= 1
                    if self.game.board[3][1] == 0 or self.game.board[3][1] == -1:
                        if self.game.board[2][1] == 0 or self.game.board[2][1] == -1:
                            if self.game.board[1][1] == 0 or self.game.board[1][1] == -1:
                                score -= 1
                    if self.game.board[3][4] == 0 or self.game.board[3][4] == -1:
                        if self.game.board[2][3] == 0 or self.game.board[2][3] == -1:
                            if self.game.board[1][2] == 0 or self.game.board[1][2] == -1:
                                score -= 1
                if self.game.board[0][2] == 0:
                    if self.game.board[0][0] == 0 or self.game.board[0][0] == -1:
                        if self.game.board[0][1] == 0 or self.game.board[0][1] == -1:
                            if self.game.board[0][3] == 0 or self.game.board[0][3] == -1:
                                score -= 1
                    if self.game.board[0][1] == 0 or self.game.board[0][1] == -1:
                        if self.game.board[0][3] == 0 or self.game.board[0][3] == -1:
                            if self.game.board[0][4] == 0 or self.game.board[0][4] == -1:
                                score -= 1
                    if self.game.board[0][3] == 0 or self.game.board[0][3] == -1:
                        if self.game.board[0][4] == 0 or self.game.board[0][4] == -1:
                            if self.game.board[0][5] == 0 or self.game.board[0][5] == -1:
                                score -= 1
                    if self.game.board[3][2] == 0 or self.game.board[3][2] == -1:
                        if self.game.board[2][2] == 0 or self.game.board[2][2] == -1:
                            if self.game.board[1][2] == 0 or self.game.board[1][2] == -1:
                                score -= 1
                    if self.game.board[3][5] == 0 or self.game.board[3][5] == -1:
                        if self.game.board[2][4] == 0 or self.game.board[2][4] == -1:
                            if self.game.board[1][3] == 0 or self.game.board[1][3] == -1:
                                score -= 1
                if self.game.board[0][3] == 0:
                    if self.game.board[0][0] == 0 or self.game.board[0][0] == -1:
                        if self.game.board[0][1] == 0 or self.game.board[0][1] == -1:
                            if self.game.board[0][2] == 0 or self.game.board[0][2] == -1:
                                score -= 1
                    if self.game.board[0][1] == 0 or self.game.board[0][1] == -1:
                        if self.game.board[0][2] == 0 or self.game.board[0][2] == -1:
                            if self.game.board[0][4] == 0 or self.game.board[0][4] == -1:
                                score -= 1
                    if self.game.board[0][2] == 0 or self.game.board[0][2] == -1:
                        if self.game.board[0][4] == 0 or self.game.board[0][4] == -1:
                            if self.game.board[0][5] == 0 or self.game.board[0][5] == -1:
                                score -= 1
                    if self.game.board[0][4] == 0 or self.game.board[0][4] == -1:
                        if self.game.board[0][5] == 0 or self.game.board[0][5] == -1:
                            if self.game.board[0][6] == 0 or self.game.board[0][6] == -1:
                                score -= 1
                    if self.game.board[3][3] == 0 or self.game.board[3][3] == -1:
                        if self.game.board[2][3] == 0 or self.game.board[2][3] == -1:
                            if self.game.board[1][3] == 0 or self.game.board[1][3] == -1:
                                score -= 1
                    if self.game.board[3][0] == 0 or self.game.board[3][0] == -1:
                        if self.game.board[2][1] == 0 or self.game.board[2][1] == -1:
                            if self.game.board[1][2] == 0 or self.game.board[1][2] == -1:
                                score -= 1
                    if self.game.board[3][6] == 0 or self.game.board[3][6] == -1:
                        if self.game.board[2][5] == 0 or self.game.board[2][5] == -1:
                            if self.game.board[1][4] == 0 or self.game.board[1][4] == -1:
                                score -= 1
                if self.game.board[0][4] == 0:
                    if self.game.board[0][1] == 0 or self.game.board[0][1] == -1:
                        if self.game.board[0][2] == 0 or self.game.board[0][2] == -1:
                            if self.game.board[0][3] == 0 or self.game.board[0][3] == -1:
                                score -= 1
                    if self.game.board[0][2] == 0 or self.game.board[0][2] == -1:
                        if self.game.board[0][3] == 0 or self.game.board[0][3] == -1:
                            if self.game.board[0][5] == 0 or self.game.board[0][5] == -1:
                                score -= 1
                    if self.game.board[0][3] == 0 or self.game.board[0][3] == -1:
                        if self.game.board[0][5] == 0 or self.game.board[0][5] == -1:
                            if self.game.board[0][6] == 0 or self.game.board[0][6] == -1:
                                score -= 1
                    if self.game.board[3][4] == 0 or self.game.board[3][4] == -1:
                        if self.game.board[2][4] == 0 or self.game.board[2][4] == -1:
                            if self.game.board[1][4] == 0 or self.game.board[1][4] == -1:
                                score -= 1
                    if self.game.board[3][1] == 0 or self.game.board[3][1] == -1:
                        if self.game.board[2][2] == 0 or self.game.board[2][2] == -1:
                            if self.game.board[1][3] == 0 or self.game.board[1][3] == -1:
                                score -= 1
                if self.game.board[0][5] == 0:
                    if self.game.board[0][2] == 0 or self.game.board[0][2] == -1:
                        if self.game.board[0][3] == 0 or self.game.board[0][3] == -1:
                            if self.game.board[0][4] == 0 or self.game.board[0][4] == -1:
                                score -= 1
                    if self.game.board[0][3] == 0 or self.game.board[0][3] == -1:
                        if self.game.board[0][4] == 0 or self.game.board[0][4] == -1:
                            if self.game.board[0][6] == 0 or self.game.board[0][6] == -1:
                                score -= 1
                    if self.game.board[3][5] == 0 or self.game.board[3][5] == -1:
                        if self.game.board[2][5] == 0 or self.game.board[2][5] == -1:
                            if self.game.board[1][5] == 0 or self.game.board[1][5] == -1:
                                score -= 1
                    if self.game.board[3][2] == 0 or self.game.board[3][2] == -1:
                        if self.game.board[2][3] == 0 or self.game.board[2][3] == -1:
                            if self.game.board[1][4] == 0 or self.game.board[1][4] == -1:
                                score -= 1
                if self.game.board[0][6] == 0:
                    if self.game.board[0][3] == 0 or self.game.board[0][3] == -1:
                        if self.game.board[0][4] == 0 or self.game.board[0][4] == -1:
                            if self.game.board[0][5] == 0 or self.game.board[0][5] == -1:
                                score -= 1
                    if self.game.board[3][6] == 0 or self.game.board[3][6] == -1:
                        if self.game.board[2][6] == 0 or self.game.board[2][6] == -1:
                            if self.game.board[1][6] == 0 or self.game.board[1][6] == -1:
                                score -= 1
                    if self.game.board[3][3] == 0 or self.game.board[3][3] == -1:
                        if self.game.board[2][4] == 0 or self.game.board[2][4] == -1:
                            if self.game.board[1][5] == 0 or self.game.board[1][5] == -1:
                                score -= 1
            return score
        elif self.game.getName() == "Stratego":
            pass
            return score
        else:
            return 0

    def chooseMove(self):
        best_move = None
        if self.player == 1:
            best_score = -inf
        else:
            best_score = inf

        for option in self.game.getMoves(self.player):
            if self.player == 1:
                self.game.makeMove(option[0], option[1], 1)
                temp = self.minimax_helper_v2(False, 0, -inf, inf)
                self.game.resetMove(option[0], option[1])
                if temp > best_score:
                    best_move = option
                    best_score = temp
            else:
                self.game.makeMove(option[0], option[1], -1)
                temp = self.minimax_helper_v2(True, 0, -inf, inf)
                self.game.resetMove(option[0], option[1])
                if temp < best_score:
                    best_move = option
                    best_score = temp

        self.count = 0
        return best_move


class CenterCorner(AI):
    def __init__(self, game, player):
        self.name = 'CenterCorner'
        super(CenterCorner, self).__init__(game, player)

    def getName(self):
        return self.name

    def __repr__(self):
        return "CenterCorner"

    def chooseMove(self):
        if (1, 1) in self.game.getMoves(1):
            return 1, 1
        elif (0, 0) in self.game.getMoves(1) or (2, 0) in self.game.getMoves(1) or (0, 2) in self.game.getMoves(1) or (
                2, 2) in self.game.getMoves(1):
            pick = choice([(0, 0), (2, 0), (0, 2), (2, 2)])
            while pick not in self.game.getMoves(1):
                pick = choice([(0, 0), (2, 0), (0, 2), (2, 2)])
            return pick
        elif (1, 0) in self.game.getMoves(1) or (0, 1) in self.game.getMoves(1) or (1, 2) in self.game.getMoves(1) or (
                2, 1) in self.game.getMoves(1):
            pick = choice([(1, 0), (0, 1), (1, 2), (2, 1)])
            while pick not in self.game.getMoves(1):
                pick = choice([(1, 0), (0, 1), (1, 2), (2, 1)])
            return pick


class Center(AI):
    def __init__(self, game, player):
        self.name = "Center"
        super(Center, self).__init__(game, player)

    def __repr__(self):
        return "Center"

    def getName(self):
        return self.name

    def chooseMove(self):
        if (1, 1) in self.game.getMoves(1):
            return 1, 1
        else:
            return choice(self.game.getMoves(1))


class baseStratego(AI):
    def __init__(self, game, player, debug):
        super(baseStratego, self).__init__(game, player)
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
        super(manual, self).__init__(game, player)
        self.player = player

    def __repr__(self):
        return "Manual"

    def getName(self):
        return self.name

    def chooseMove(self):
        print(self.game)
        if self.game.getName() == 'TicTacToe':
            print('Picking a move')
            player_choice = int(input("Make a move: "))
            self.game.makeMove(player_choice // 3, player_choice % 3, self.player)
        elif self.game.getName() == 'ConnectFour':
            print('Picking a move')
            player_choice = int(input("Make a move: "))
            self.game.makeMove(player_choice, self.player)


class defenseTic(AI):
    def __init__(self, game, player):
        super(defenseTic, self).__init__(game, player)
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

        return choice(self.game.getMoves(1))


class offenseTic(AI):
    def __init__(self, game, player):
        super(offenseTic, self).__init__(game, player)
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
        return choice(self.game.getMoves(1))


class offdefTic(AI):
    def __init__(self, game, player):
        super(offdefTic, self).__init__(game, player)
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

        return choice(self.game.getMoves(1))


class copyBlock(AI):
    def __init__(self, game, player):
        super(copyBlock, self).__init__(game, player)
        self.player = player
        self.name = 'CopyBlock'

    def __repr__(self):
        return self.name

    def getName(self):
        return self.name

    def chooseMove(self):
        if self.player == 1:
            if self.nextMoveWin() is not None:
                return self.nextMoveWin()
            else:
                if len(self.game.player2) == 0:
                    return choice(self.game.getMoves(1))
                else:
                    col = self.game.player2[-1][1]
                    for move in self.game.getMoves(1):
                        if col == move[1]:
                            return move
                    return choice(self.game.getMoves(1))
        else:
            if self.nextMoveWin() is not None:
                return self.nextMoveWin()
            else:
                if len(self.game.player1) == 0:
                    return choice(self.game.getMoves(1))
                else:
                    col = self.game.player1[-1][1]
                    for move in self.game.getMoves(1):
                        if col == move[1]:
                            return move
                    return choice(self.game.getMoves(1))

    def nextMoveWin(self):
        if self.player == 1:
            for move in self.game.getMoves(1):
                self.game.makeMove(move[0], move[1], -1)
                if self.game.checkWin() == -1:
                    self.game.resetMove(move[0], move[1])
                    return move
                self.game.resetMove(move[0], move[1])
            return None
        else:
            for move in self.game.getMoves(1):
                self.game.makeMove(move[0], move[1], 1)
                if self.game.checkWin() == 1:
                    self.game.resetMove(move[0], move[1])
                    return move
                self.game.resetMove(move[0], move[1])
            return None


class Q_Learning(AI):
    def __init__(self, game, player, table, learning_rate=.01, discount_factor=.99, epsilon=1, lr_decay=.00001, decay=.00001):
        super().__init__(game, player)
        self.name = "Q-Learning"
        self.START_LR = learning_rate
        self.LR = learning_rate
        self.LR_DECAY = lr_decay
        self.DF = discount_factor
        self.START_EPSILON = epsilon
        self.EPSILON = epsilon
        self.EPSILON_DECAY = decay
        self.MOVE_PENALTY = 1
        self.REWARD = 100
        self.q_table = table.q_table


    def getName(self):
        return self.name

    def __repr__(self):
        return self.name

    def get_state(self):
        state = ""
        for j in range(self.game.getRow()):
            for i in range(self.game.getCol()):
                state = state + str(int(self.game.board[j][i]))
        return state

    def get_actions(self):
        actions = ""
        moves = self.game.getMoves(self.player)
        for i in range(len(moves)):
            actions = actions + self.encode_action(i)
        return actions

    def encode_action(self, action):
        charlist = "0123456789abcdefghijklmnopqrstuvwxyz"
        return charlist[action]

    def decode_action(self, char_action):
        charlist = "0123456789abcdefghijklmnopqrstuvwxyz"
        for i in range(len(charlist)):
            if charlist[i] == char_action:
                return i
        return None

    def set_EPSILON(self, new_epsilon):
        self.EPSILON = new_epsilon

    def chooseMove(self):
        old_state = self.get_state()
        old_actions = self.get_actions()
        try:
            old_values = self.q_table[old_state, old_actions]
        except KeyError:
            self.q_table[old_state, old_actions] = np.zeros(len(old_actions))
            old_values = np.zeros(len(old_actions))

        random_threshold = np.random.uniform(0,1)
        if random_threshold > self.EPSILON:
            if self.player == 1:
                index = np.argmax(old_values)
            else:
                index = np.argmin(old_values)
        else:
            index = np.random.randint(0,len(old_values))
        old_q_value = old_values[index]
        decoded_index = self.decode_action(old_actions[index])
        move = self.game.getMoves(self.player)[decoded_index]

        self.game.makeMove(move[0], move[1], self.player)
        new_state = self.get_state()
        new_actions = self.get_actions()

        try:
            new_values = self.q_table[new_state, new_actions]
        except KeyError:
            self.q_table[new_state, new_actions] = np.zeros(len(new_actions))
            new_values = np.zeros(len(new_actions))

        if len(new_values) > 0:
            if self.player == 1:
                new_index = np.argmin(new_values)
            else:
                new_index = np.argmax(new_values)

            future_q_value = new_values[new_index]
            if self.game.checkWin() is not None:
                if self.game.checkWin() == self.player:
                    reward = self.REWARD * self.player
                elif self.game.checkWin() == -self.player:
                    reward = -self.REWARD * self.player
                else:
                    reward = 0
            else:
                reward = -self.MOVE_PENALTY * self.player

            new_q_value = old_q_value + self.LR * (reward + self.DF * future_q_value - old_q_value)
            self.q_table[old_state, old_actions][index] = new_q_value

        self.game.resetMove(move[0], move[1])
        return move

    def decay_epsilon(self):
        self.EPSILON = self.EPSILON * (1 - (self.EPSILON_DECAY))

    def decay_lr(self):
        self.LR = self.LR * (1 - (self.LR_DECAY))

class Q_Table:
    def __init__(self, start_table=None):
        self.q_table = self.load_table(start_table)

    def save_table(self, filename):
        with open(os.path.join(os.getcwd(), "Q Tables",filename), "w") as f:
            for i in self.q_table:
                values = ""
                for j in self.q_table[i]:
                    values = values + str(j) + " "
                f.write(i[0] + " " + i[1] + " " + values + '\n')

    def load_table(self, filename):
        temp = {}
        try:
            print(os.path.join(os.getcwd(), "Q Tables", filename))
            with open(os.path.join(os.getcwd(), "Q Tables", filename), "r", newline="\n") as f:
                print("Loading...")
                for i in f:
                    list = i.split()
                    count = len(list)
                    state = list[0]
                    actions = ""
                    values = []
                    if count > 1:
                        actions = list[1]
                        for j in range(2, count):
                            values.append(float(list[j]))
                    temp[state, actions] = values
                return temp
        except FileNotFoundError:
            print("Load failed")
            return {}
        except TypeError:
            print("Creating New Table")
            return {}

if __name__ == "__main__":
    try:
        g = ConnectFour()
        table = Q_Table()
        opp1 = Q_Learning(g, 1, table, learning_rate=0, epsilon=0)
        opp2 = Q_Learning(g, -1, table, learning_rate=0, epsilon=0)
        turn = 0
        while g.checkWin() is None:
            print(g)
            if turn % 2 == 0:
                move = opp1.chooseMove()
                g.makeMove(move[0], move[1], 1)
                turn += 1
            else:
                move = opp2.chooseMove()
                g.makeMove(move[0], move[1], -1)
                turn += 1
            input("")
        print(g)
        print(g.checkWin())
    except KeyboardInterrupt:
        pass
