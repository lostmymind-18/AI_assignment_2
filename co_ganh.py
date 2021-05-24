import pygame
import math
import os

#Width of screen
pygame.init()
WIDTH = 900
DEPTH = 5
best_move = ((),())
#Set display window
WIN = pygame.display.set_mode((WIDTH,WIDTH))
pygame.display.set_caption("Vietnamese chess")

#Set colour
WHITE = (255, 255, 255)
GREY = (128, 128, 128)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)

#Draw grid
def draw(win, width, board):
    gap = (width - 100) // 4
    win.fill(YELLOW)
    #Draw lines
    for i in range(5):
        pygame.draw.line(win, GREY, (50, 50+i * gap), (width-50, 50+i * gap))#horizontal lines
        for j in range(5):
            pygame.draw.line(win, GREY, (50+j * gap, 50), (50+j * gap, width-50))#vertical lines
    #Left to right diagonal lines
    pygame.draw.line(win, GREY, (50, 50+2 * gap), (50+2*gap, 50))
    pygame.draw.line(win, GREY, (50, 50+4 * gap), (width-50, 50))
    pygame.draw.line(win, GREY, (50+2*gap, width-50), (width-50, 50+2 * gap))

    #Right to left diagonal lines
    pygame.draw.line(win, GREY, (width-50, 50+2*gap), (50+2*gap, 50))
    pygame.draw.line(win, GREY, (50, 50), (width-50, width-50))
    pygame.draw.line(win, GREY, (50+2*gap, width-50), (50, 50+2*gap))
    
    #Draw pieces
    for i in range(5):
        for j in range(5):
            if board[i][j] == 1:
                pygame.draw.circle(win, WHITE,(50+j*gap,50+i*gap),30)
            if board[i][j] == -1:
                pygame.draw.circle(win, BLACK,(50+j*gap,50+i*gap),30)
    pygame.display.update()

#Check ganh
def check_ganh(board, player, move):
    if 
    return board


#Check vay
def check_vay(board, player, move):
    return board


#Check terminate
def terminate(board):
    player1 = False
    player2 = False
    for row in board:
        for cell in board:
            if cell == 1:
                player1 = True
            elif cell == -1:
                player2 = True
    if (not player1) or (not player2):
        return True
    return False


#posible moves for AI
def posible_moves(board, player):
    pos_move = []
    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            if cell == player:
                start = (i, j) 
                #Khong the di chuyen theo duong cheo
                if (i == 0 and j == 1) or (i == 0 and j == 3) or (i == 1 and j == 0) or (i == 3 and j == 0) or (i == 1 and j == 4) or (i == 3 and j == 4) or (i == 4 and j == 1) or (i == 4 and j == 3):
                    if(i-1 >= 0):
                        des = (i-1,j)
                        pos_move.append(start, des)
                    if(j-1 >= 0):
                        des = (i,j-1)
                        pos_move.append(start, des)
                    if(i+1 <= 4):
                        des = (i+1,j)
                        pos_move.append(start, des)
                    if(j+1 <= 4):
                        des = (i,j+1)
                        pos_move.append(start, des)
                #Co the di chuyen theo duong cheo
                else:
                    if(i-1 >= 0):
                        des = (i-1,j)
                        pos_move.append(start, des)
                    if(j-1 >= 0):
                        des = (i,j-1)
                        pos_move.append(start, des)
                    if(i+1 <= 4):
                        des = (i+1,j)
                        pos_move.append(start, des)
                    if(j+1 <= 4):
                        des = (i,j+1)
                        pos_move.append(start, des)


                    if(i-1>=0 and j-1>=0):
                        des = (i-1,j-1)
                        pos_move.append(start,des)
                    if(i-1>=0 and j+1<=4):
                        des = (i-1,j+1)
                        pos_move.append(start,des)
                    if(i+1<=4 and j-1>=0):
                        des = (i+1,j-1)
                        pos_move.append(start,des)
                    if(i+1<=4 and j+1<=4):
                        des = (i+1,j+1)
                        pos_move.append(start,des)
    return pos_move
                


#Check legal move for AI 
def legal_move(board, player, tuple_):
    #put position not empty
    if (board[tuple_[1][0]][tuple_[1][1]] != 0):
        return False
    #TODO bat buoc phai ganh
    return True


#humanmove #TODO need to improve it later
def human_move(board, player):
    print("chose a piece(y,x): ")#pick up position
    y = int(input())
    x = int(input())
    while board[y][x] != player:
        print("chose again: ")
        y = int(input())
        x = int(input())
    print("chose new position(y,x): ")#put on position
    y_ = int(input())
    x_ = int(input())
    tuple_ = ((y,x),(y_,x_))
    while not legal_move(board, player, tuple_):
        print("chose new position(y,x): ")#put on position
        y_ = int(input())
        x_ = int(input())
        tuple_ = ((y,x),(y_,x_))
    return tuple_



#board change after a legal move
def board_change(board, player, move):
    board[move[0][0]][move[0][1]] = 0
    board[move[1][0]][move[1][1]] = player
    return board

#algorithm -- minimax

def algorithm(board, player, depth)
    #move:
    moves = posible_moves(board, player) 
    #valuation 
    if depth == 0 or terminate(board):
        a = 0
        for row in board:
            for cell in row:
                a = a + cell
        return a

    #Max
    if player == 1:
        max = -math.inf
        for move in moves:
            if legal_move(board, player, move):
                board = board_change(board, move)
                a = algorithm(board, -player, depth-1):
                if max < a:
                    max = a
                    best_move = move
        return max

    #Min
    elif player == -1:
        min = math.inf
        for move in moves:
            if legal_move(board, player, move):
                board = board_change(board, move)
                a = algorithm(board, -player, depth-1):
                if min > a:
                    min = a
                    best_move = move   
        return min

    

#aimove
def ai_move(board, player):
    
    a = algorithm(board, player, DEPTH)
    return best_move

#move 
def move(board, player):
    if(player == 1):
        print("It's white's move ")
        return human_move(board, player)
    else:
        print("It's black's move ")
        #AI move for later
        return human_move(board, player)
    


#main
def main(win, width):
    #os.system("Clear")
    board = [[1, 1, 1, 1, 1],
            [1, 0, 0, 0, 1],
            [1, 0, 0, 0, -1],
            [-1, 0, 0, 0, -1],
            [-1, -1, -1, -1, -1]]
    player = 0
    while True:
        draw(win, width, board)
        if player == 0:
            player = 1
        elif player == 1:
            player = -1
        elif player == -1:
            player = 1
        tuple_ = move(board, player)
        board[tuple_[0][0]][tuple_[0][1]] = 0
        board[tuple_[1][0]][tuple_[1][1]] = player
        #check_ganh(board)

main(WIN, WIDTH)