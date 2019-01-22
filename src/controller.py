import pygame
import sys

from flags import F
from pygame.locals import *
from board import Board


class Controller(object):
    """
    this is the flow controller of the game, 
    when to main screen, when to game over, etc
    it has the application status (var game_status)
    """
    game_status_dict = {
        0: 'initial',
        1: 'main_menu',
        5: 'starting_board',
        2: 'playing',
        3: 'option',
        4: 'game_over'
    }

    def __init__(self, DISPLAYSUR):
        self.game_status = 0 
        self.DISPLAYSUR = DISPLAYSUR

    def start_application(self):
        self.game_status = 1

    def quit_game(self):
        self.big_print("QUITTING THE GAME. 3Q4 PLAYING")
        pygame.quit()
        sys.exit()

    def reset_game(self):
        self.big_print("(re-) Starting the game...")
        self.game_status = 5

    def call_option(self):
        print("bringing up the pop up option window....")
        self.game_status = 3

    def resume_game(self):
        print("going back to the game...")        
        self.game_status = 2

    def lose_game(self):
        self.game_status = 4
        self.big_print("GAME OVER")

    def show_game_over(self):
        #self.game_status = 4
        #pass
        INVFONT = pygame.font.Font('freesansbold.ttf', 20)
        text_obj_0 = INVFONT.render("GAME OVER: press enter to continue.", True, 
            F.white, F.black) 
        text_obj_1 = INVFONT.render("GAME OVER: press q/esc to quit.", True, 
            F.white, F.black)         
        self.DISPLAYSUR.blit(text_obj_0,(0, 0))
        self.DISPLAYSUR.blit(text_obj_1,(0, 50))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == QUIT:
                self.quit_game()
            elif  event.type == KEYDOWN: 
                if event.key == pygame.K_ESCAPE or event.unicode == 'q':
                    self.quit_game()
                if event.key == pygame.K_RETURN:
                    self.reset_game()
            else:
                pass


    def show_main_menu(self):
        #self.game_status = 1
        #pass
        INVFONT = pygame.font.Font('freesansbold.ttf', 20)
        text_obj_0 = INVFONT.render("press enter to continue.", True, 
            F.white, F.black) 
        text_obj_1 = INVFONT.render("press q/esc to quit.", True, 
            F.white, F.black)         
        self.DISPLAYSUR.blit(text_obj_0,(0, 0))
        self.DISPLAYSUR.blit(text_obj_1,(0, 50))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == QUIT:
                self.quit_game()
            elif  event.type == KEYDOWN: 
                if event.key == pygame.K_ESCAPE or event.unicode == 'q':
                    self.quit_game()
                if event.key == pygame.K_RETURN:
                    self.reset_game()
            else:
                pass


    def show_option(self):
        option_menu_bg = Board.textures[-1]
        option_menu_bg = pygame.transform.scale(option_menu_bg, 
            (F.tile_size*F.map_rows-40, F.tile_size*F.map_cols-40))

        INVFONT = pygame.font.Font('freesansbold.ttf', 20)
        text_obj_0 = INVFONT.render("OPTION: press <F1> to continue.", True, 
            F.white, F.black) 
        text_obj_1 = INVFONT.render("OPTION: press q/esc to quit.", True, 
            F.white, F.black)         
        
        self.DISPLAYSUR.blit(option_menu_bg,(20, 20))
        self.DISPLAYSUR.blit(text_obj_0,(20, 20))
        self.DISPLAYSUR.blit(text_obj_1,(20, 50))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == QUIT:
                self.quit_game()
            elif  event.type == KEYDOWN: 
                if event.key == pygame.K_ESCAPE or event.unicode == 'q':
                    self.quit_game()
                if event.key == pygame.K_F1:
                    self.resume_game()
            else:
                pass

    def render_pop_window(self):
        if self.game_status == 1:
            self.show_main_menu()
        elif self.game_status == 3:
            self.show_option()
        elif self.game_status == 4:
            self.show_game_over()
        else:
            pass

    @staticmethod        
    def big_print(str1):
        print()
        print("========================================")
        print("  " + str(str1))
        print("========================================")
        print()


    def show_help(self):
        raise NotImplementedError
        '''
        Enter: start        : start the game / confirm
        asdw / hjkl / arrow : play the game
        F1                  : call the option menu
        ESC / q             : quit the game
        '''