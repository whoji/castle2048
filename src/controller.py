import pygame
import sys

from flags import F
from pygame.locals import *
from ui import GenUI

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

    def win_game(self):
        self.game_status = 6
        self.big_print("GAME FINISHED! AMAZING!")

    def show_game_over(self):
        #self.game_status = 4
        #pass
        GFONT_b = pygame.font.Font('freesansbold.ttf', 100)
        GFONT_s = pygame.font.Font('freesansbold.ttf', 25)

        text_obj_0 = GFONT_b.render("GAME OVER", True, F.white, None)
        text_obj_0_bg = GFONT_b.render("GAME OVER", True, F.red, None)
        text_obj_1 = GFONT_s.render("Press <ENTER> to start a new game !  ", 
            True, F.white, F.red + (255,))
        text_obj_2 = GFONT_s.render("Press <Q> or <ESC> to quit ...  ", 
            True, F.white, F.red + (255,))

        pos_0 = (F.center_x - int(text_obj_0.get_size()[0] / 2),  F.center_y - 100)
        pos_1 = (F.center_x - int(text_obj_1.get_size()[0] / 2),  F.center_y + 50)
        pos_2 = (F.center_x - int(text_obj_1.get_size()[0] / 2),  F.center_y + 75)

        self.DISPLAYSUR.blit(text_obj_0_bg,(pos_0[0]-6, pos_0[1])) #for outline
        self.DISPLAYSUR.blit(text_obj_0_bg,(pos_0[0]+6, pos_0[1])) #for outline
        self.DISPLAYSUR.blit(text_obj_0_bg,(pos_0[0], pos_0[1]-6)) #for outline
        self.DISPLAYSUR.blit(text_obj_0_bg,(pos_0[0], pos_0[1]+6)) #for outline
        self.DISPLAYSUR.blit(text_obj_0,pos_0)
        self.DISPLAYSUR.blit(text_obj_1,pos_1)
        self.DISPLAYSUR.blit(text_obj_2,pos_2)

        # pos_0 = (F.center_x - int(text_obj_0.get_size()[0] / 2),  F.center_y - 100)
        # pos_1 = (F.center_x - int(text_obj_1.get_size()[0] / 2),  F.center_y + 50)
        # pos_2 = (F.center_x - int(text_obj_1.get_size()[0] / 2),  F.center_y + 75)
        # GenUI.draw_text_with_outline(self.DISPLAYSUR, GFONT_b, "GAME OVER", F.white, F.red, 10, pos_0)
        # GenUI.draw_text_with_outline(self.DISPLAYSUR, GFONT_s, "Press <ENTER> to start a new game !  ", F.white, F.red, 5, pos_1)
        # GenUI.draw_text_with_outline(self.DISPLAYSUR, GFONT_s, "Press <Q> or <ESC> to quit ...  ", F.white, F.red, 5, pos_2)
        # pygame.display.update()

        #GenUI.draw_text_with_outline(self.DISPLAYSUR, GFONT_b, "Test Text String", 
        #    F.orange, F.blue, 10, (200,200) , if8=True, if_center=True)

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

        FONT_s = pygame.font.Font('freesansbold.ttf', 15)
        FONT_m = pygame.font.Font('freesansbold.ttf', 20)
        FONT_l = pygame.font.Font('freesansbold.ttf', 80)

        text_obj_0 = FONT_m.render("CONGRATULATIONS!! YOU WON !!", True, F.white, None) 
        text_obj_1 = FONT_s.render("Press <ENTER> to continue the INFINITE mode", True, F.white, None) 
        text_obj_2 = FONT_s.render("Press <Q> or <ESC> to quit the game.", True, F.white, None)         
        text_obj_3 = FONT_s.render("Press <R> to start over the game.", True, F.white, None)         

        if milestone is not None:
            text_obj_0 = INvFONT.render("MILESTONE [%d] REACHED" % milestone,
                True, F.white, None)
            text_obj_1 = GFONT.render("Press <ENTER> to continue.", True, 
                F.white, F.black) 
            text_obj_2 = GFONT.render("", True, F.white, F.black) 
        
        # self.DISPLAYSUR.blit(menu_bg,(20, 20))
        pygame.draw.rect(self.DISPLAYSUR, F.blue, F.menu_rect)
        y_offset = 150
        self.DISPLAYSUR.blit(text_obj_0,(F.menu_rect[0]+20, F.menu_rect[1]+y_offset+20))
        self.DISPLAYSUR.blit(text_obj_1,(F.menu_rect[0]+20, F.menu_rect[1]+y_offset+60))
        self.DISPLAYSUR.blit(text_obj_2,(F.menu_rect[0]+20, F.menu_rect[1]+y_offset+90))
        self.DISPLAYSUR.blit(text_obj_3,(F.menu_rect[0]+20, F.menu_rect[1]+y_offset+120))
        GenUI.draw_text_with_outline(self.DISPLAYSUR, FONT_l, "YOU WIN !!!!", 
            F.orange, F.red, 5, (F.center_x, F.center_y-150) , if8=True, if_center=True)
        
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == QUIT:
                self.quit_game()
            elif  event.type == KEYDOWN: 
                if event.key == pygame.K_ESCAPE or event.unicode == 'r':
                    self.reset_game()
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