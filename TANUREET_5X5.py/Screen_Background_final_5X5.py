#PYGAME WINDOW BASIC GUI
########################

#importing essential libraries
import sys
import pygame 
from constants_5 import *
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
#################################################################




#definitions of required functions or methods
def main():

    #game object
    game = Game()

    #main loop o fpygame mandatory to use
    while True:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
#################################################################


#Calling main function (entrance of the programming logic)
main()
#################################################################




