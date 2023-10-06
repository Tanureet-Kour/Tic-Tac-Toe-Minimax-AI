#MINIMAX AI
###########

#importing essential libraries
import sys
import pygame 
import numpy as np
import random
import copy

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
        self.board = Board()
        self.ai = AI()
        self.player = 1
        self.gamemode = 'ai' #pvp or ai
        self.running = True
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

    def next_turn(self):
        self.player = self.player%2 + 1 #toggle between one and two

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
            #-----------
            center = ( col*SQSIZE+SQSIZE//2 , row*SQSIZE+SQSIZE//2 )
            pygame.draw.circle(screen,CIRCLE_COLOR,center,RADIUS,CIRCLE_WIDTH)

########

class Board:

    #creating a console_board
    def __init__(self):
        self.boxes =  np.zeros( (ROWS,COLS) )
        self.empty_boxes = self.boxes
        self.marked_boxes = 0

    #marking the box
    def mark_box(self,row,col,player):#player 1 and 2
        self.boxes[row][col] = player
        self.marked_boxes +=1

    #return 0 if empty
    def empty_box(self,row,col):
        return self.boxes[row][col] == 0
    
    #Board Utility Methods
    #---------------------

    def isFull(self):
        return self.marked_boxes==25
    
    def isEmpty(self):
        return self.marked_boxes==0
    
    def get_empty_boxes(self):
        empty_boxes = []
        for row in range(ROWS):
            for col in range(COLS):
                if self.empty_box(row,col):
                    empty_boxes.append((row,col))
       
        return empty_boxes

    def final_state(self):
        # return 0     if there is no win doesn't mean it is a draw
        # return 1     if player 1 wins
        # return 2     if player 2 wins
        
        #vertical wins
        for col in range(COLS):
            if self.boxes[0][col] == self.boxes[1][col] == self.boxes[2][col] == self.boxes[3][col] ==  self.boxes[4][col] != 0 :
                return self.boxes[0][col]
            
        #horizontal wins
        for row in range(ROWS):
            if self.boxes[row][0] == self.boxes[row][1] == self.boxes[row][2] == self.boxes[row][3] == self.boxes[row][4] != 0 :
                return self.boxes[row][0]
        
        #desc diagonal wins
        if self.boxes[0][0] == self.boxes[1][1] == self.boxes[2][2] == self.boxes[3][3] ==  self.boxes[4][4] != 0:
            return self.boxes[1][1]

        #asc diagonal wins
        if self.boxes[4][0] == self.boxes[3][1] == self.boxes[2][2] == self.boxes[1][3] == self.boxes[0][4] != 0:
            return self.boxes[2][2]

        #no win yet
        return 0 
    
########

#Random AI
class AI:

    #level 0 : RANDOM AI
    #level 1 : MINIMAX AI
    def __init__(self, level=1, player=2):
        self.level  = level
        self.player = player

    def rnd(self, board):
        empty_boxes = board.get_empty_boxes()
        idx         = random.randrange(0,len(empty_boxes))
        return empty_boxes[idx]
    
    def eval(self,main_board):
        if self.level == 0:
            #randomm choice
            eval = 'random'
            move = self.rnd(main_board)

        else:
            #minimax algorithm
            eval,move = self.minimax(main_board, False)

        print(f'AI has chosen to mark square in pos {move} with an eval of {eval}')

        return move # [row,col]
    

    def minimax(self, board, maximizing):
        
        #terminal case
        case = board.final_state

        #player 1 wins
        if case == 1:
            return 1, None
        #player 2 wins
        if case == 2:
            return -1, None
        #draw
        elif board.isFull():
            return 0, None
        

        if maximizing:
            max_eval =  -100 #any number less than 0
            base_move = None
            empty_boxes = board.get_empty_boxes()

            for (row,col) in empty_boxes:
                temp_board = copy.deepcopy(board)
                temp_board.mark_box(row, col, 1)
                eval = self.minimax(temp_board, False)[0]
                if eval > max_eval:
                    max_eval = eval
                    best_move = (row,col)

            return max_eval, best_move

        elif not maximizing:
            min_eval =  100 #any number gretaer than 1
            base_move = None
            empty_boxes = board.get_empty_boxes()

            for (row,col) in empty_boxes:
                temp_board = copy.deepcopy(board)
                temp_board.mark_box(row, col, self.player)
                eval = self.minimax(temp_board, True)[0]
                if eval < min_eval:
                    min_eval = eval
                    best_move = (row,col)

            return min_eval, best_move
#################################################################


#definitions of required functions or methods
def main():

    #game object
    game  = Game()
    board = game.board
    ai    = game.ai

    #main loop of pygame mandatory to use
    while True:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN: 
                # print(event.pos) #pixel coordinates
                pos = event.pos
                row = pos[1] // SQSIZE
                col = pos[0] // SQSIZE   

                if game.board.empty_box(row,col):
                    game.board.mark_box(row,col,game.player) 
                    game.draw_figure(row,col)
                    game.next_turn()       

        if game.gamemode == 'ai' and game.player == ai.player:
            #update the screen
            pygame.display.update()

            #ai methods
            row,col = ai.eval(board)

            game.board.mark_box(row, col, ai.player)
            game.draw_figure(row, col)
            game.next_turn()
  

        pygame.display.update()
#################################################################


#Calling main function (entrance of the programming logic)
main()
#################################################################




