#PYGAME WINDOW BASIC GUI
########################

#importing essential libraries
import sys
import pygame 
import numpy as np
from constants_5X5 import *
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
        #console_board
        self.console_board = Console_Board()
        self.player = 1
        self.show_lines()

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

    def draw_figure(self,row,col):
        if self.player == 1:
            #draw cross
            #----------
            #descending line
            start_desc = (col*SQSIZE+OFFSET , row*SQSIZE+OFFSET)
            end_desc   = (col*SQSIZE+SQSIZE-OFFSET , row*SQSIZE+SQSIZE-OFFSET)
            pygame.draw.line(screen, CROSS_COLOR, start_desc, end_desc, CROSS_WIDTH)
            #ascending line
            start_asc = (col*SQSIZE+OFFSET , row*SQSIZE+SQSIZE-OFFSET)
            end_asc   = (col*SQSIZE+SQSIZE-OFFSET , row*SQSIZE+OFFSET)
            pygame.draw.line(screen, CROSS_COLOR, start_asc, end_asc, CROSS_WIDTH)

        elif self.player == 2:
            #draw circle
            center = ( col*SQSIZE+SQSIZE//2 , row*SQSIZE+SQSIZE//2 )
            pygame.draw.circle(screen,CIRCLE_COLOR,center,RADIUS,CIRCLE_WIDTH)

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

    #main loop of pygame mandatory to use
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
                    game.draw_figure(row,col)
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




