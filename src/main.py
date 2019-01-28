#https://medium.com/@yvanscher/how-to-make-a-game-with-pygame-fc85159ae354
import pygame
import sys
import random
from pygame.locals import *

from board import Board
from flags import F
from controller import Controller
from ui import StatusBar
from mover import Mover

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


pygame.init()

board = Board()

status_bar = StatusBar()

#DISPLAYSUR = pygame.display.set_mode((F.map_rows*F.tile_size, 
#    F.map_cols*F.tile_size + F.status_bar_size))

DISPLAYSUR = pygame.display.set_mode((F.window_w, F.window_h))


controller = Controller(DISPLAYSUR)

# setup a font for displaying inventory numbers
INVFONT = pygame.font.Font('freesansbold.ttf', 43)
INVFONT_GG = pygame.font.Font('freesansbold.ttf', 66)


while True:
    DISPLAYSUR.fill(F.grey2)

    # when the app started
    if controller.game_status == 0:
        controller.start_application()
        continue

    # at main menu
    elif controller.game_status == 1:
        controller.show_main_menu()
        continue

    # starting the board
    elif controller.game_status == 5:
        board = Board()
        controller.game_status = 2
        status_bar.board = board
        status_bar.update_status()
        #status_bar.controller = controller
        continue

    # playing the game (at board view)
    elif controller.game_status == 2:

        for event in pygame.event.get():
            if event.type == QUIT:
                controller.quit_game()
            elif event.type == KEYDOWN:
                action = eventkey_to_action(event.key)
                if action in ['up','down','right','left']:
                    if_moved = board.update_board(action)

                if if_moved:
                    print("board updated !!")
                    print(board)
                    mover = Mover(board.prev_board, action)
                    controller.game_status = 21
                    status_bar.update_status()

                if event.key == pygame.K_ESCAPE or event.unicode == 'q':
                    controller.quit_game()

                if event.key == pygame.K_F1:
                    controller.call_option()
            else:
                pass
                #print("other event.type: " + str(event.type))

        if board.if_gg:
            controller.lose_game()
        elif board.if_win:
            controller.win_game()
            board.if_win = False

    else:
        pass

    # ===================================
    # part 2. render everything
    # ===================================

    # render the board bg
    pygame.draw.rect(DISPLAYSUR, F.board_frame_color, F.board_outer_rect)
    for row in range(F.map_cols):
        for col in range(F.map_rows):
            pygame.draw.rect(DISPLAYSUR, F.board_frame_color,
                (col*F.tile_size+F.board_offset_x, row*F.tile_size+
                    F.board_offset_y, F.tile_size, F.tile_size))
            pygame.draw.rect(DISPLAYSUR, F.board_color,(
                col*F.tile_size+F.board_offset_x+F.board_frame_px,
                row*F.tile_size+F.board_offset_y+F.board_frame_px, 
                F.tile_size-2*F.board_frame_px, 
                F.tile_size-2*F.board_frame_px))
    
    pygame.draw.rect(DISPLAYSUR, F.star_tile_color,(
            F.star_pos[1]*F.tile_size+F.board_offset_x-F.board_frame_px,
            F.star_pos[0]*F.tile_size+F.board_offset_y-F.board_frame_px, 
            F.tile_size+2*F.board_frame_px, 
            F.tile_size+2*F.board_frame_px))

    # render the moving blocks
    if controller.game_status == 21:
        if mover.remain_moving_frames > 0:
            mover.move_all()
            for row in range(F.map_rows):
                for col in range(F.map_cols):
                    if mover.blocks[row][col]:
                        # the tile background
                        moving_tile_pos = (mover.blocks[row][col].y*F.tile_size+F.board_offset_x+F.board_frame_px,
                             mover.blocks[row][col].x*F.tile_size+F.board_offset_y+F.board_frame_px)
                        DISPLAYSUR.blit(board.textures[board.prev_board[row][col]], moving_tile_pos)
                        # the text (number) 
                        text_obj = INVFONT.render(str(board.prev_board[row][col]), True, F.white, F.black)
                        DISPLAYSUR.blit(text_obj,moving_tile_pos)
        else:
            controller.game_status = 2

    # render the board
    if controller.game_status != 21:
        for row in range(F.map_cols):
            for col in range(F.map_rows):
                if board.board[row][col]:
                    DISPLAYSUR.blit(board.textures[board.board[row][col]],
                        (col*F.tile_size+F.board_offset_x+F.board_frame_px, 
                            row*F.tile_size+F.board_offset_y+F.board_frame_px))

    # render the text
    if controller.game_status != 21:
        for row in range(F.map_cols):
            for col in range(F.map_rows):
                if board.board[row][col]:
                    text_obj = INVFONT.render(str(board.board[row][col]), True, F.white, F.black)
                    DISPLAYSUR.blit(text_obj,(col*F.tile_size+F.board_offset_x+F.board_frame_px, 
                        row*F.tile_size+F.board_offset_y+F.board_frame_px))

    # render the status bar
    status_bar.render(DISPLAYSUR)

    # render the pop up window (option menu / game over / etc)
    controller.render_pop_window()


    pygame.display.update()

    # ===================================
    # end of each frame
    # ===================================



