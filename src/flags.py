# 


class Flags(object):
    """docstring for Flags"""

    def __init__(self):
        self.tile_size = 100
        self.map_rows = 5
        self.map_cols = 5
        self.proj_path = '/home/whoji/Desktop/ILC_2019/2048/'

        self.black = (0,0,0)
        self.white = (255,255,255)
        self.red = (255,0,0)

        self.init_board_blocks = 2

        self.if_star = False
        self.star_pos = (2,2)

        #self.__self_check():

    def __self_check():
        raise NotImplementedError
        #raise Exception("Bad set up logic")

F = Flags()

