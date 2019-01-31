import pygame
import sys

from flags import F
from pygame.locals import *


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
        21: 'blocks_moving',
        3: 'option',
        4: 'game_over',
        6: 'game_beat'
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
        self.big_print("(re-) Stshowarting the game...")
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

    def win_game(self):
        self.game_status = 6
        self.big_print("GAME FINISHED! AMAZING!")

    def show_game_over(self):
        #self.game_status = 4
        #pass
        GFONT = pygame.font.Font('freesansbold.ttf', 20)
        text_obj_0 = GFONT.render("GAME OVER: press enter to continue.", True, 
            F.white, None)
        text_obj_1 = GFONT.render("GAME OVER: press q/esc to quit.", True, 
            F.white, None)
        pygame.draw.rect(self.DISPLAYSUR, F.yellow, F.menu_rect)
        self.DISPLAYSUR.blit(text_obj_0,(F.menu_rect[0]+10, F.menu_rect[1]+20))
        self.DISPLAYSUR.blit(text_obj_1,(F.menu_rect[0]+10, F.menu_rect[1]+70))
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
        GFONT = pygame.font.Font('freesansbold.ttf', 20)
        text_obj_0 = GFONT.render("Press <ENTER> to continue.", True, 
            F.white, None) 
        text_obj_1 = GFONT.render("Press <Q>/<Esc> to quit.", True, 
            F.white, None)
        pygame.draw.rect(self.DISPLAYSUR, F.red, F.menu_rect)
        self.DISPLAYSUR.blit(text_obj_0,(F.menu_rect[0]+10, F.menu_rect[1]+20))
        self.DISPLAYSUR.blit(text_obj_1,(F.menu_rect[0]+10, F.menu_rect[1]+70))
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
        option_menu_bg = pygame.image.load(F.option_bg_img_path)
        option_menu_bg = pygame.transform.scale(option_menu_bg, 
            (F.tile_size*F.map_rows-40, F.tile_size*F.map_cols-40))

        GFONT = pygame.font.Font('freesansbold.ttf', 20)
        text_obj_0 = GFONT.render("OPTION: press <F1> to continue.", True, 
            F.white, None) 
        text_obj_1 = GFONT.render("OPTION: press q/esc to quit.", True, 
            F.white, None)         
        
        # self.DISPLAYSUR.blit(option_menu_bg,(20, 20))
        pygame.draw.rect(self.DISPLAYSUR, F.green, F.menu_rect)
        self.DISPLAYSUR.blit(text_obj_0,(F.menu_rect[0]+20, F.menu_rect[1]+20))
        self.DISPLAYSUR.blit(text_obj_1,(F.menu_rect[0]+20, F.menu_rect[1]+50))
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

    def show_game_finished(self, milestone = None):
        # This is game win screen. also screen for "milestone reached"
        menu_bg = pygame.image.load(F.option_bg_img_path)
        menu_bg = pygame.transform.scale(menu_bg, 
            (F.tile_size*F.map_rows-40, F.tile_size*F.map_cols-40))

        INvFONT = pygame.font.Font('freesansbold.ttf', 20)
        GFONT = pygame.font.Font('freesansbold.ttf', 15)
        text_obj_0 = INvFONT.render("CONGRATULATIONS!! YOU WON !!", True, 
            F.white, None) 
        text_obj_1 = GFONT.render("Press <ENTER> to continue the INF MODE.", True, 
            F.white, None) 
        text_obj_2 = GFONT.render("Press Q/ESC to quit the game.", True, 
            F.white, None)         

        if milestone is not None:
            text_obj_0 = INvFONT.render("MILESTONE [%d] REACHED" % milestone,
                True, F.white, None)
            text_obj_1 = GFONT.render("Press <ENTER> to continue.", True, 
                F.white, F.black) 
            text_obj_2 = GFONT.render("", True, F.white, F.black) 
        
        # self.DISPLAYSUR.blit(menu_bg,(20, 20))
        pygame.draw.rect(self.DISPLAYSUR, F.blue, F.menu_rect)
        self.DISPLAYSUR.blit(text_obj_0,(F.menu_rect[0]+20, F.menu_rect[1]+20))
        self.DISPLAYSUR.blit(text_obj_1,(F.menu_rect[0]+20, F.menu_rect[1]+50))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == QUIT:
                self.quit_game()
            elif  event.type == KEYDOWN: 
                if event.key == pygame.K_ESCAPE or event.unicode == 'q':
                    self.quit_game()
                if event.key == pygame.K_RETURN:
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
        elif self.game_status == 6:
            self.show_game_finished()
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