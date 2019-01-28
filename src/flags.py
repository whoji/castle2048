import math


class Flags(object):
    """docstring for Flags"""

    def __init__(self):
        self.proj_path = '/home/whoji/Desktop/ILC_2019/2048/'
        self.option_bg_img_path = self.proj_path + 'asset/water.png'
        self.debug_mod = True

        # colors
        self.grey1 = (28,32,38)
        self.grey2 = (14,22,14)
        self.black = (0,0,0)
        self.white = (255,255,255)
        self.red = (250,50,50)
        self.blue = (50,50,250)
        self.green = (50, 200, 100)
        self.yellow = (200,200,50)
        self.orange = (255, 153, 58)

        # size and pos conf (general and menu)
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
        self.menu_rect = (self.board_offset_x+50, self.board_offset_y+50,
            self.map_cols*self.tile_size-100, self.map_rows*self.tile_size-100)
        self.center_x  = round(self.window_w / 2)
        self.center_y  = round((self.window_h) / 2)

        # size and pos conf (board)
        self.board_color = self.grey1
        self.board_frame_color = self.orange
        self.board_frame_px = 2
        self.board_rect = (self.board_offset_x, self.board_offset_y,
            self.map_cols*self.tile_size, self.map_rows*self.tile_size)
        self.board_outer_rect = (self.board_offset_x-self.board_frame_px,
            self.board_offset_y-self.board_frame_px, 
            self.map_cols*self.tile_size+2*self.board_frame_px, 
            self.map_rows*self.tile_size+2*self.board_frame_px)
        self.init_board_blocks = 2

        # star 
        self.if_star = True
        self.star_pos = (2,2)
        self.star_tile_color = self.red
        self.star_tile_frame_color = self.red

        # game flow control
        self.win_condition_block = self.__calculate_win_block()
        self.milestone_mode = True
        self.milestone = [2**i for i in range(16)]

        # block moving effect
        self.if_movable = True
        self.move_frame = 20 # frames to finish the move

        # run self check
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

