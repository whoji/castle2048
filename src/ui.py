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
        if F.if_star:
            self.star_score = 0
            self.top_star_score = 0
            self.milestone_str = ""

    def update_status(self):
        self.moves = self.board.total_moves
        self.cur_score = self.get_board_total_sum(self.board.board)
        if self.cur_score > self.top_score:
            self.top_score = self.cur_score
        if F.if_star:
            self.star_score = self.board.board[F.star_pos[0]][F.star_pos[1]]
            if self.star_score > self.top_star_score:
                self.top_star_score = self.star_score

    def render(self, DISPLAYSUR):    
        bg = pygame.image.load(F.option_bg_img_path)
        bg = pygame.transform.scale(bg, self.size)

        GFONT = pygame.font.Font('freesansbold.ttf', 15)
        text_obj_0 = GFONT.render("moves:[ %d ]     score:[%d]    top:[%d] " % 
            (self.moves, self.cur_score, self.top_score), 
            True, F.white, F.black) 
 
        DISPLAYSUR.blit(bg,self.pos)
        DISPLAYSUR.blit(text_obj_0, self.apply_offset(self.pos, F.text_offset))

        if F.if_star:
            self.milestone_str = '* '*  (F.milestone.index(self.star_score)+1)
            text_obj_1 = GFONT.render("castle:[ %d ]     top casle:[ %d ]    %s" % 
                (self.star_score, self.top_star_score, self.milestone_str),
                True, F.white, F.black)
            DISPLAYSUR.blit(text_obj_1, self.apply_offset(self.pos, (10, 30) ))

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

class GenUI():
    """docstring for ClassName"""
    def __init__(self):
        self.GFONTS = None

    @staticmethod
    def shorten_block_text(n):
        if n > 1000000:
            return str(int(n / 1000000))+"m" # e.g. 1048576 -> 1m
        if n > 10000:
            return str(int(n / 1000))+"k" # e.g. 16384 -> 16k
        return str(n)

    #@staticmethod
    def generate_block_text_obj_obsolete(self, FONT, n):
        text_str = self.shorten_block_text(n)
        digits = len(text_str)        
        text_obj = FONT.render(text_str, True, F.block_text_fg, F.block_text_bg)
        text_obj_size = text_obj.get_rect().size
        text_obj_size = [int(s*F.block_font_size_perc[digits-1]) for s in text_obj_size]
        text_obj = pygame.transform.scale(text_obj, text_obj_size)
        return text_obj

    def generate_block_text_obj(self, FONTS, n):
        text_str = self.shorten_block_text(n)
        digits = len(text_str)
        FONT = FONTS[digits-1]
        text_obj = FONT.render(text_str, True, F.block_text_fg, F.block_text_bg)
        return text_obj
