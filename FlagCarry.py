from typing import List
import copy


class FlagCarry():
    def __init__(self,  d: int, initialBoard: List[List[int]], isMax: bool):
        self.d = d
        self.initialBoard = initialBoard
        self.isMax = isMax

    def countVal(self, board):
        matchingVal = 1 if (self.isMax) else -1
        sumOfMatchingVal = 0
        for row in board:
            for cell in row:
                if (cell == matchingVal):
                    sumOfMatchingVal += 1
        return sumOfMatchingVal

    def getPossibleMoves(self, isMax, board):
        matchingVal = 1 if (isMax) else -1
        possibleMoves = []
        for i, row in enumerate(board):
            for j, cell in enumerate(row):
                if (cell == matchingVal):
                    start = (i, j)
                    possibleEndFromCell = [
                        (i+1, j), (i+1, j+1), (i+1, j-1),
                        (i, j+1), (i, j-1),
                        (i-1, j), (i-1, j+1), (i-1, j-1),
                    ]
                    # Check if end is inside board
                    for end in possibleEndFromCell:
                        if (end[0] in range(0, len(board))) and (end[1] in range(0, len(row))) and (board[end[0]][end[1]] == 0):
                            possibleMoves.append((start, end))

        return possibleMoves

    def checkGanh(self, newBoard, myVal, enemyVal, posA, posB):
        # Check inside
        if (posA[0] in range(0, len(newBoard))) and (posA[1] in range(0, len(newBoard[0]))):
            if (posB[0] in range(0, len(newBoard))) and (posB[1] in range(0, len(newBoard[0]))):
                # Check matching
                if (newBoard[posA[0]][posA[1]] == newBoard[posB[0]][posB[1]] == enemyVal):
                    newBoard[posA[0]][posA[1]] = myVal
                    newBoard[posB[0]][posB[1]] = myVal

    def checkVay(self, newBoard):
        for i, row in enumerate(newBoard):
            for j, cell in enumerate(row):
                if (cell == 0):
                    continue
                my_val = cell
                enemy_val = -my_val
                surroundingOfPos = [
                    (i+1, j), (i+1, j+1), (i+1, j-1),
                    (i, j+1), (i, j-1),
                    (i-1, j), (i-1, j+1), (i-1, j-1),
                ]
                # Check inside
                for surround in surroundingOfPos:
                    allAreEnemies = True
                    if (surround[0] in range(0, len(newBoard))) and (surround[1] in range(0, len(newBoard[0]))):
                        if (newBoard[surround[0]][surround[1]] != enemy_val):
                            allAreEnemies = False
                            break
                    if (allAreEnemies):
                        newBoard[i][j] = enemy_val

    def getNewBoard(self, board, move, isMax):
        newBoard = copy.deepcopy(board)
        start, end = move
        myVal = 1 if (isMax) else -1
        enemyVal = 1 if not (isMax) else -1
        newBoard[start[0]][start[1]] = 0
        newBoard[end[0]][end[1]] = myVal

        # Check ganh
        posA, posB = ((end[0]+1, end[1]+1), (end[0]-1, end[1]-1))
        self.checkGanh(newBoard, myVal, enemyVal, posA, posB)

        posA, posB = ((end[0]+1, end[1]-1), (end[0]-1, end[1]+1))
        self.checkGanh(newBoard, myVal, enemyVal, posA, posB)

        posA, posB = ((end[0], end[1]-1), (end[0], end[1]+1))
        self.checkGanh(newBoard, myVal, enemyVal, posA, posB)

        posA, posB = ((end[0] + 1, end[1]), (end[0]-1, end[1]))
        self.checkGanh(newBoard, myVal, enemyVal, posA, posB)

        # TODO: Check vay

        return newBoard

    def helper(self, board: List[List[int]], isMax: bool, currentDepth: int, alpha: int, beta: int):
        if (currentDepth >= self.d):
            return (self.countVal(board), 0)
        possibleMoves = self.getPossibleMoves(isMax, board)
        best_move = possibleMoves[0]

        if (isMax):
            val = -1000
            best_val = -1000
            for move in possibleMoves:
                newBoard = self.getNewBoard(board, move, isMax)
                val = self.helper(newBoard, not isMax,
                                  currentDepth+1, alpha, beta)[0]
                if (best_val < val):
                best_move = move
                    best_val = val
                if (alpha < val):
                    alpha = val
                # Minimum won't allow max to go this way
                if (alpha >= beta):
                    break
            return (best_val, best_move)

        # Minimum
        val = 1000
        best_val = 1000
        for move in possibleMoves:
            newBoard = self.getNewBoard(board, move, isMax)
            val = self.helper(newBoard, not isMax,
                              currentDepth+1, alpha, beta)[0]
            if (best_val > val):
            best_move = move
                best_val = val 
            if (beta > val):
                beta = val
            # Maximum won't allow min to go this way
            if (beta >= alpha):
                break
        return (val, best_move)

    def move(self):
        return self.helper(self.initialBoard, self.isMax, 0, -1000, 1000)[1]


initialBoard = [[1, 1, 0, 1, 1],
                [-1, 0, 1, -1, 1],
                [-1, 0, 1, -1, 1],
                [-1, 0, 1, -1, 1],
                [-1, -1, 1, 1, 1]]

FlagCarry(7, initialBoard, True).move()
