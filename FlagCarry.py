import time
import math
import copy


class FlagCarry():
    def __init__(self,  d: int, initialBoard, isMax: bool):
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

    def check_moveable(self, board, pos):
        if (pos[0] in range(0, len(board))) and (pos[1] in range(0, len(board[0]))) and board[pos[0]][pos[1]] == 0:
            return True
        return False

    def getPossibleMoves(self, isMax, board):
        matchingVal = 1 if (isMax) else -1
        pos_move = []
        for i, row in enumerate(board):
            for j, cell in enumerate(row):
                if (cell == matchingVal):
                    if (i, j) not in ((0,1),(0,3),(1,0),(3,0),(1,4),(3,4),(4,1),(4,3),(1,2),(2,1),(2,3),(3,2)):
                        if i > 0 and j > 0:
                            if board[i-1][j-1] == 0:
                                pos_move.append(((i,j),(i-1,j-1)))
                        if i < 4 and j < 4:
                            if board[i+1][j+1] == 0:
                                pos_move.append(((i,j),(i+1,j+1)))
                        if i > 0 and j < 4:
                            if board[i-1][j+1] == 0:
                                pos_move.append(((i,j),(i-1,j+1)))
                        if i < 4 and j > 0:
                            if board[i+1][j-1] == 0:
                                pos_move.append(((i,j),(i+1,j-1)))
                    #Check doc
                    if i > 0:
                        if board[i-1][j] == 0:
                                pos_move.append(((i,j),(i-1,j)))
                    if i < 4:
                        if board[i+1][j] == 0:
                                pos_move.append(((i,j),(i+1,j)))
                    #Check ngang
                    if j > 0:
                        if board[i][j-1] == 0:
                                pos_move.append(((i,j),(i,j-1)))
                    if j < 4:
                        if board[i][j+1] == 0:
                                pos_move.append(((i,j),(i,j+1)))

        return pos_move

    def must_ganh(self, board, move, player):
        i, j  = move
        a = False
        if (i, j) in corner:
            return False
        #Check cac duong cheo
        elif (i, j) not in ((0,1),(0,3),(1,0),(3,0),(1,4),(3,4),(4,1),(4,3)):
            #Duong cheo tren xuong duoi, trai sang phai
            if not (i == 4 or j == 4 or i == 0 or j == 0):
                if board[i+1][j+1] == board[i-1][j-1] == -player:
                    a = True

                #Duong cheo len tren, phai sang trai
                if board[i-1][j+1] == board[i+1][j-1] == -player:
                    a = True
        #Check Doc
        if 0 < i < 4:
            if board[i+1][j] == board[i-1][j] == -player:
                a = True
        #Chech ngang
        if 0 < j < 4:
            if board[i][j+1] == board[i][j-1] == -player:
                a = True
        return a
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
    # Check xem 1 quan co co the di chuyen duoc hay khong

    def can_move(self, board, player, position):
        # Check duong cheo
        i = position[0]
        j = position[1]
        a = False
        if (i, j) not in ((0, 1), (0, 3), (1, 0), (3, 0), (1, 4), (3, 4), (4, 1), (4, 3), (1, 2), (2, 1), (2, 3), (3, 2)):
            if i > 0 and j > 0:
                if board[i - 1][j-1] == 0:
                    return True
                elif board[i-1][j-1] == -player:
                    a = True
            if i < 4 and j < 4:
                if board[i+1][j+1] == 0:
                    return True
                elif board[i+1][j+1] == -player:
                    a = True
            if i > 0 and j < 4:
                if board[i-1][j + 1] == 0:
                    return True
                elif board[i-1][j+1] == -player:
                    a = True
            if i < 4 and j > 0:
                if board[i+1][j-1] == 0:
                    return True
                elif board[i+1][j-1] == -player:
                    a = True
        # Check doc
        if i > 0:
            if board[i-1][j] == 0:
                return True
            elif board[i-1][j] == -player:
                a = True
        if i < 4:
            if board[i+1][j] == 0:
                return True
            elif board[i+1][j] == -player:
                a = True
        # Check ngang
        if j > 0:
            if board[i][j-1] == 0:
                return True
            elif board[i][j-1] == -player:
                a = True
        if j < 4:
            if board[i][j+1] == 0:
                return True
            elif board[i][j+1] == -player:
                a = True
        return False

    def check_vay_(self, board, player, list_, check_list, already_check):
        if list_[2] == 1:
            return 1

        # If list_ co the di chuyen,return 1
        if self.can_move(board, player, (list_[0], list_[1])):
            list_[2] = 1
            return 1

        # If list_ khong the di chuyen
        if not self.can_move(board, player, (list_[0], list_[1])):
            a = False
            i = list_[0]
            j = list_[1]
            for list__ in check_list:
                if list__ not in already_check and list__ != list_:
                    # Xet theo duong cheo
                    already_check_ = [list(x) for x in already_check]
                    already_check_.append(list__)
                    if not ((i == 0 and j == 1) or (i == 0 and j == 3) or (i == 1 and j == 0) or (i == 3 and j == 0) or (i == 1 and j == 4) or (i == 3 and j == 4) or (i == 4 and j == 1) or (i == 4 and j == 3)):
                        if i+1 == list__[0] and j+1 == list__[1]:
                            a = (a or self.check_vay_(board, player,
                                 list__, check_list, already_check_))
                        if i-1 == list__[0] and j+1 == list__[1]:
                            a = (a or self.check_vay_(board, player,
                                 list__, check_list, already_check_))
                        if i+1 == list__[0] and j-1 == list__[1]:
                            a = (a or self.check_vay_(board, player,
                                 list__, check_list, already_check_))
                        if i-1 == list__[0] and j-1 == list__[1]:
                            a = (a or self.check_vay_(board, player,
                                 list__, check_list, already_check_))
                    # Xet theo duong ngang doc
                    if i+1 == list__[0] and j == list__[1]:
                        a = (a or self.check_vay_(board, player,
                             list__, check_list, already_check_))
                    if i-1 == list__[0] and j == list__[1]:
                        a = (a or self.check_vay_(board, player,
                             list__, check_list, already_check_))
                    if i == list__[0] and j-1 == list__[1]:
                        a = (a or self.check_vay_(board, player,
                             list__, check_list, already_check_))
                    if i == list__[0] and j+1 == list__[1]:
                        a = (a or self.check_vay_(board, player,
                             list__, check_list, already_check_))
            # if list_ bi co lap
            if a == False:
                list_[2] = 0
                return 0
            elif a == True:
                list_[2] = 1
                return 1

    # Check vay
    def check_vay(self, board, player):
        check_list = []
        for i in range(5):
            for j in range(5):
                if board[i][j] == -player:
                    check_list.append([i, j, 0])
        for list_ in check_list:
            if list_[2] == 0:
                self.check_vay_(board, -player, list_, check_list, [])
        for list_ in check_list:
            if list_[2] == 0:
                board[list_[0]][list_[1]] = player

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
        self.check_vay(newBoard, myVal)

        return newBoard

    def helper(self, board, isMax: bool, currentDepth: int, alpha: int, beta: int):
        if (currentDepth >= self.d):
            return (self.countVal(board), 0)
        possibleMoves = self.getPossibleMoves(isMax, board)
        if (len(possibleMoves) == 0):
            if (isMax):
                return (0,None)
            return (16,None)
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
        possibleMoves = self.getPossibleMoves(self.isMax, self.initialBoard)
        if (possibleMoves == []):
            return None
        for move in possibleMoves:
            if must_ganh(self.initialBoard, move[1], self.isMax):
                return move
        return self.helper(self.initialBoard, self.isMax, 0, -1000, 1000)[1]


initialBoard = [
    [[1, 1, 1, 1, 1],
         [1, 0, 0, 0, 1],
         [1, 0, 0, 0, -1],
         [-1, 0, 0, 0, -1],
         [-1, -1, -1, -1, -1]]
]
# initialBoard = [[1, 1, 0, 1, 1],
#                 [-1, -1, -1, 0, 1],
#                 [0, 0, 0, 0, 1],
#                 [-1, -1, 0, 0, -1],
#                 [0, -1, -1, -1, -1]]


def move(board, player):
    return FlagCarry(6, board, player).move()


#move(initialBoard, 1)
#FlagCarry(7, initialBoard, True).move()
