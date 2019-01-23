import math


class Flags(object):
    """docstring for Flags"""

    def __init__(self):
        self.debug_mod = True

        self.tile_size = 100
        self.map_rows = 3
        self.map_cols = 3
        self.proj_path = '/home/whoji/Desktop/ILC_2019/2048/'

        self.black = (0,0,0)
        self.white = (255,255,255)
        self.red = (255,0,0)

        self.option_bg_img_path = self.proj_path + 'asset/water.png'

        self.init_board_blocks = 2

        self.if_star = False
        self.star_pos = (2,2)

        self.win_condition_block = self.__calculate_win_block()

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

F = Flags()

