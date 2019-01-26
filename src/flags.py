import math


class Flags(object):
    """docstring for Flags"""

    def __init__(self):
        self.proj_path = '/home/whoji/Desktop/ILC_2019/2048/'
        self.option_bg_img_path = self.proj_path + 'asset/water.png'
        self.debug_mod = True

        # size and menu conf
        self.window_w = 800
        self.window_h = 600
        self.tile_size = 100
        self.map_rows = 5
        self.map_cols = 5
        self.status_bar_size = 60
        self.board_offset_x, self.board_offset_y = self.__calculate_board_offset()
        self.text_offset_x = 10
        self.text_offset_y = 10
        self.text_offset = (10,10)
        self.board_rect = (self.board_offset_x, self.board_offset_y,
            self.map_cols*self.tile_size, self.map_rows*self.tile_size)
        self.menu_rect = (self.board_offset_x+50, self.board_offset_y+50,
            self.map_cols*self.tile_size-100, self.map_rows*self.tile_size-100)
        self.center_x  = round(self.window_w / 2)
        self.center_y  = round((self.window_h) / 2)

        # colors
        self.black = (0,0,0)
        self.white = (255,255,255)
        self.red = (250,50,50)
        self.blue = (50,50,250)
        self.green = (50, 200, 100)
        self.yellow = (200,200,50)

        self.init_board_blocks = 2

        # star 
        self.if_star = True
        self.star_pos = (2,2)

        self.win_condition_block = self.__calculate_win_block()
        self.milestone_mode = True
        self.milestone = [2**i for i in range(16)]

        #self.__self_check():

    def __self_check():
        raise NotImplementedError
        #raise Exception("Bad set up logic")

    def __calculate_win_block(self):
        ret = 2 ** (int(math.sqrt(self.map_rows * self.map_cols))*3 - 1)
        
        if self.debug_mod:
            if self.map_rows == 3:
                ret = 32
            if self.map_rows == 4:
                ret = 256

        return ret

    def __calculate_board_offset(self):
        offset_x = round(self.window_w / 2 - self.map_cols * self.tile_size / 2)
        offset_y = round((self.window_h - self.status_bar_size) / 2 - 
            self.map_rows * self.tile_size / 2)
        return offset_x, offset_y

F = Flags()

