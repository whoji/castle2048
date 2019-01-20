import pygame
import random

from pygame.locals import *
from flags import F
# TODO
# from combine import Combiner
# from move import Mover

class Board(object):

    textures = {
        # WATER: pygame.image.load(F.proj_path + 'asset/water.png'),
        # BRICK: pygame.image.load(F.proj_path + 'asset/brick.png'),
        # DIAMOND: pygame.image.load(F.proj_path + 'asset/diamond.png'),
        # FIRE: pygame.image.load(F.proj_path + 'asset/fire.png'),
        #0 : pygame.image.load(F.proj_path + 'asset/water.png'),
        1 : pygame.image.load(F.proj_path + 'asset/brick.png'),
        2 : pygame.image.load(F.proj_path + 'asset/diamond.png'),
        4 : pygame.image.load(F.proj_path + 'asset/fire.png'),
        8 : pygame.image.load(F.proj_path + 'asset/grass.png'),
        16 : pygame.image.load(F.proj_path + 'asset/coal.png'),
        32 : pygame.image.load(F.proj_path + 'asset/glass.png'),
        64 : pygame.image.load(F.proj_path + 'asset/sand.png'),
        128 : pygame.image.load(F.proj_path + 'asset/stone.png'),
        256 : pygame.image.load(F.proj_path + 'asset/char.png'),
        512 : pygame.image.load(F.proj_path + 'asset/bird1.png'),
        1024 : pygame.image.load(F.proj_path + 'asset/bird2.png'),
        2048 : pygame.image.load(F.proj_path + 'asset/bird3.png'),
           
    }

    """docstring for World"""
    def __init__(self):
        self.textures = Board.textures
        self.resize_texture()

        self.board =[]
        self.prev_board = []
        self.prev_action = None
        self.total_moves = 0
        self.if_need_to_check_gg = False
        self.if_gg = False

        self.init_board()

    def __repr__(self):
        for r in self.board:
            print(r)
        return ""

    def resize_texture(self):
        for k,v in self.textures.items():
            self.textures[k] = pygame.transform.scale(
                self.textures[k], (F.tile_size, F.tile_size))

    def init_board(self):
        # initialize the map with all dirt
        self.board = [[0 for w in range(F.map_rows)] 
            for h in range (F.map_cols)]

        # spawn some random blocks
        for _ in range(F.init_board_blocks):
            self.spawn_block()

    def update_board(self, action = "up"):
        # 0. bak the old one
        new_board = [r[:] for r in self.board]

        # 1. move all the blocks
        self.move_all_to_direction(new_board, action)
        self.move_all_to_direction(new_board, action)
        self.move_all_to_direction(new_board, action)
        self.move_all_to_direction(new_board, action)
         # TODO three times? it should depends on the board size

        # 2. combine the blocks
        self.combine_blocks(new_board, action)
        self.move_all_to_direction(new_board, action)

        # 3. check if really updated. if yes update
        if self.check_if_same_board(new_board, self.board):
            return 0

        # 4. spawn another block
          #print("to spawn")
        self.total_moves += 1
        self.prev_action = action
        self.prev_board = self.board
        self.board = new_board
        #print("before spawn "+str(self))
        self.spawn_block()

        # 5. check GG condition
        if self.if_need_to_check_gg:
            if self.check_gg():
                self.if_gg = True
            else:
                self.if_need_to_check_gg = False

        return 1

    @staticmethod
    def check_if_same_board(b1, b2):
        for i in range(F.map_rows):
            for j in range(F.map_cols):
                if b1[i][j] != b2[i][j]:
                    return False
        return True

    @staticmethod
    def move_all_to_direction(b, action):
        m = F.map_rows
        n = F.map_cols
        if action == 'up':
            for i in range(1,m):
                for j in range(n):
                    Board.move_block_to_direction(b,i,j,action)
        elif action == 'down':
            for i in reversed(range(m-1)):
                for j in range(n):
                    Board.move_block_to_direction(b,i,j,action)
        elif action == 'right':
            for i in range(m):
                for j in reversed(range(n-1)):
                    Board.move_block_to_direction(b,i,j,action)
        elif action == 'left':
            for i in range(m):
                for j in range(1,n):
                    Board .move_block_to_direction(b,i,j,action)
        else:
            raise Exception("WTF is this action: %s" % str(action))

        return b

    @staticmethod
    def move_block_to_direction(b,i,j,direction):
        assert 0 <= i < F.map_rows
        assert 0 <= j < F.map_rows
        if b[i][j] == 0:
            return 0
        else:
            if direction == 'up' and b[i-1][j] == 0:
                b[i-1][j] = b[i][j]
                b[i][j] = 0
                return 1
            elif direction == 'down' and b[i+1][j] == 0:
                b[i+1][j] = b[i][j]
                b[i][j] = 0
                return 1
            elif direction == 'left' and b[i][j-1] == 0:
                b[i][j-1] = b[i][j]
                b[i][j] = 0
                return 1
            elif direction == 'right' and b[i][j+1] == 0:
                b[i][j+1] = b[i][j]
                b[i][j] = 0
                return 1
            else:
                return 0 

    @staticmethod
    def combine_blocks(b,action = 'up'):
        m = F.map_rows
        n = F.map_cols
        if action == 'up':
            for i in range(1,m):
                for j in range(n):
                    if Board.if_block_mergable(b[i][j],b[i-1][j]):
                        b[i-1][j] += b[i][j]
                        b[i][j] = 0
        elif action == 'down':
            for i in reversed(range(m-1)):
                for j in range(n):
                    if Board.if_block_mergable(b[i][j],b[i+1][j]):
                        b[i+1][j] += b[i][j]
                        b[i][j] = 0                    
        elif action == 'right':
            for i in range(m):
                for j in reversed(range(n-1)):
                    if Board.if_block_mergable(b[i][j],b[i][j+1]):
                        b[i][j+1] += b[i][j]
                        b[i][j] = 0                    
        elif action == 'left':
            for i in range(m):
                for j in range(1,n):
                    if Board.if_block_mergable(b[i][j],b[i][j-1]):
                        b[i][j-1] += b[i][j]
                        b[i][j] = 0
        else:
            raise Exception("WTF is this action: %s" % str(action))

        return b

    @staticmethod
    def if_block_mergable(a,b):
        if a == b:
            return True
        else:
            return False

    def add_to_board(self, pos, obj_type):
        self.board[pos[0]][pos[1]] = obj_type

    def remove_from_board(self, pos, obj_type):
        self.board[pos[0]][pos[1]] = None

    def spawn_block(self):
        valid_pos_candidates = self.get_valid_spawn_pos()
        #print(valid_pos_candidates)
        if len(valid_pos_candidates):
            self.if_need_to_check_gg = True
        spawn_pos = random.choice(valid_pos_candidates)
        spawn_type = random.choice([1,2])
        self.add_to_board(spawn_pos, spawn_type)
        return 1

    def get_valid_spawn_pos(self):
        m = F.map_rows
        n = F.map_cols
        return [(i,j) for i in range(m) for j in range(n) 
            if self.board[i][j] == 0 and (i == 0 or 
                j == 0 or i == m-1 or j == n-1)]

    def check_gg(self):
        temp_board = [row[:] for row in self.board]
        for action in ['up','down','left','right']:
            Board.move_all_to_direction(temp_board, action)
            Board.combine_blocks(temp_board, action)
            if not Board.check_if_same_board(self.board, temp_board):
                return False
        return True


