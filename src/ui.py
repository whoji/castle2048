import pygame
from flags import F
from pygame.locals import *


class StatusBar(object):
    """docstring for StatusBar"""
    def __init__(self):
        #self.controller = None
        self.board = None
        self.top_score = 0
        self.cur_score = 0
        self.moves = 0
        self.pos = (0, F.window_h - F.status_bar_size)
        self.size = (F.window_w, F.status_bar_size)

    def update_status(self):
        self.moves = self.board.total_moves
        self.cur_score = self.get_board_total_sum(self.board.board)
        if self.cur_score > self.top_score:
            self.top_score = self.cur_score

    def render(self, DISPLAYSUR):    
        bg = pygame.image.load(F.option_bg_img_path)
        bg = pygame.transform.scale(bg, self.size)

        INVFONT = pygame.font.Font('freesansbold.ttf', 15)
        text_obj_0 = INVFONT.render("moves:%d score:%d top:%d " % 
            (self.moves, self.cur_score, self.top_score), 
            True, F.white, F.black) 

        DISPLAYSUR.blit(bg,self.pos)
        DISPLAYSUR.blit(text_obj_0, self.apply_offset(self.pos, F.text_offset))


        #pygame.display.update()

    @staticmethod
    def get_board_total_sum(b):
        ret = sum([sum(r) for r in b])
        return ret

    @staticmethod
    def apply_offset(pos,offset):
        return (pos[0]+offset[0], pos[1]+offset[1])

    def __draw_text_center():
        raise NotImplementedError
        # font = pygame.font.Font(None, 25)
        # text = font.render("You win!", True, BLACK)
        # text_rect = text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
        # screen.blit(text, text_rect)