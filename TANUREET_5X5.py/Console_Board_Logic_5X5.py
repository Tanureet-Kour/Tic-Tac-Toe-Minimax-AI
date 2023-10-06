#PYGAME WINDOW BASIC GUI
########################

#importing essential libraries
import sys
import pygame 
from constants_5X5 import *
import numpy as np
#################################################################


#PYGAME SETUP
pygame.init()
screen = pygame.display.set_mode( (WIDTH,HEIGHT) )
pygame.display.set_caption("TIC TAC TOE 5X5 MINIMAX ALGORITHM")
screen.fill( BG_COLOR )
#################################################################


#Classes
class Game:

    def __init__(self):
        self.show_lines()
        #console_board
        self.console_board = Console_Board()
        self.player = 1

    def next_turn(self):
        self.player = self.player%2 + 1 #toggle between one and two

    def show_lines(self):
        #vertical lines
        pygame.draw.line(screen, LINE_COLOR, (SQSIZE   , 0), (SQSIZE   , HEIGHT), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (SQSIZE*2 , 0), (SQSIZE*2 , HEIGHT), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (SQSIZE*3 , 0), (SQSIZE*3 , HEIGHT), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (SQSIZE*4 , 0), (SQSIZE*4 , HEIGHT), LINE_WIDTH)
        #horizontal lines
        pygame.draw.line(screen, LINE_COLOR, (0 , SQSIZE  ), (WIDTH , SQSIZE  ), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (0 , SQSIZE*2), (WIDTH , SQSIZE*2), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (0 , SQSIZE*3), (WIDTH , SQSIZE*3), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (0 , SQSIZE*4), (WIDTH , SQSIZE*4), LINE_WIDTH)
########

class Console_Board:

    #creating a console_board
    def __init__(self):
        self.boxes =  np.zeros( (ROWS,COLS) )

    #marking the box
    def mark_box(self,row,col,player):#player 1 and 2
        self.boxes[row][col] = player

    #return 0 if empty
    def empty_box(self,row,col):
        return self.boxes[row][col] == 0
#################################################################




#definitions of required functions or methods
def main():

    #game object
    game = Game()
    console_board = game.console_board

    #main loop o fpygame mandatory to use
    while True:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN: 
                # print(event.pos) #pixel coordinates
                row = event.pos[1] // SQSIZE
                col = event.pos[0] // SQSIZE   

                if game.console_board.empty_box(row,col):
                    game.console_board.mark_box(row,col,game.player) 
                    game.next_turn()
                    print(game.console_board.boxes)
                    print(" ")
                    print("#-----------------#")
                    print(" ")         

        pygame.display.update()
#################################################################


#Calling main function (entrance of the programming logic)
main()
#################################################################




