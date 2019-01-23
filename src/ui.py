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

    def update_status(self):
        self.moves = self.board.total_moves
        self.cur_score = self.get_board_total_sum(self.board.board)
        if self.cur_score > self.top_score:
            self.top_score = self.cur_score

    def render(self, DISPLAYSUR):    
        bg = pygame.image.load(F.option_bg_img_path)
        bg = pygame.transform.scale(bg, 
            (F.tile_size*F.map_cols, F.status_bar_size))

        INVFONT = pygame.font.Font('freesansbold.ttf', 15)
        text_obj_0 = INVFONT.render("moves:%d score:%d top:%d " % 
            (self.moves, self.cur_score, self.top_score), 
            True, F.white, F.black) 

        DISPLAYSUR.blit(bg,(10, F.map_rows*F.tile_size+1))
        DISPLAYSUR.blit(text_obj_0,(10, F.map_rows*F.tile_size+1))
        #pygame.display.update()

    @staticmethod
    def get_board_total_sum(b):
        ret = sum([sum(r) for r in b])
        return ret
