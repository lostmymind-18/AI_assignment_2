import pygame
import math
import os

#Width of screen
pygame.init()
WIDTH = 900

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

#Check terminate
#main
def main(win, width):
    #os.system("Clear")
    board = [[1, 1, 1, 1, 1],
            [1, 0, 0, 0, 1],
            [1, 0, 0, 0, -1],
            [-1, 0, 0, 0, -1],
            [-1, -1, -1, -1, -1]]
    while True:
        draw(win, width, board)

main(WIN, WIDTH)