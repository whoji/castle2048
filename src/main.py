#https://medium.com/@yvanscher/how-to-make-a-game-with-pygame-fc85159ae354
import pygame
import sys
import random
from pygame.locals import *

from board import Board
from flags import *

def eventkey_to_action(eventkey):
    action = None
    if eventkey in [K_RIGHT, K_l, K_d]:
        action = 'right'
    elif eventkey  in [K_LEFT, K_h, K_a]:
        action = 'left'
    elif eventkey in [K_DOWN, K_j, K_s]:
        action = 'down'
    elif eventkey in [K_UP, K_k, K_w]:
        action = 'up'
    else:
        print("bad event key!!")
    return action

board = Board()


pygame.init()

# add 50 pixels to the height for the inventory
DISPLAYSUR = pygame.display.set_mode((F.map_rows*F.tile_size, 
    F.map_cols*F.tile_size + 50))

# setup a font for displaying inventory numbers
INVFONT = pygame.font.Font('freesansbold.ttf', 43)
INVFONT_GG = pygame.font.Font('freesansbold.ttf', 66)


while True:
    DISPLAYSUR.fill(F.black)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            action = eventkey_to_action(event.key)
            if action in ['up','down','right','left']:
                if_moved = board.update_board(action)
            
            if if_moved:
                print("board updated !!")
                print(board)

            if event.key == pygame.K_ESCAPE or event.unicode == 'q':
                pygame.quit()
                sys.exit()

        else:
            pass
            #print("other event.type: " + str(event.type))

    # render the board
    for row in range(F.map_cols):
        for col in range(F.map_rows):
            if board.board[row][col]:
                DISPLAYSUR.blit(board.textures[board.board[row][col]],
                    (col*F.tile_size, row*F.tile_size))

    # render the text
    for row in range(F.map_cols):
        for col in range(F.map_rows):
            if board.board[row][col]:
                text_obj = INVFONT.render(str(board.board[row][col]), True, F.white, F.black)
                DISPLAYSUR.blit(text_obj,(col*F.tile_size, row*F.tile_size))

    # render gg information
    if board.if_gg:
        text_obj_gg = INVFONT_GG.render("Game Over", True, F.white, F.black)
        DISPLAYSUR.blit(text_obj_gg,(10, round(F.map_rows/2) *F.tile_size))
        print("Game Over displayed!!!")
        pygame.display.update()
        pygame.time.wait(5000)
        board.if_gg = False

    pygame.display.update()



