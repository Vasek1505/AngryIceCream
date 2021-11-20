import pygame
from enum import Enum

TILE_SIZE = 40
GRID_SIZE_X = 27
GRID_SIZE_Y = 27

class tile_type(Enum):
    ICE = 0
    FREE = 1
    OBSTACLE = 2


class Player:
    
    def __init__(self, number, x, y, img):
        self.x = x
        self.y = y
        self.adj_x = 0
        self.adj_y = 0
        self.number = number
        self.img = img
        self.next_x = 0
        self.next_y = 0
        self.movement_step = 1
        self.moving = False
        self.dir = (1,0)
        self.move_dir = (0,0)
        self.movement_speed = 20
        self.icing = False
        self.frames = 0
        self.melting = False

    def move(self, keys, tiles):
        if not self.moving:
            if self.number == 1:
                if keys[pygame.K_w]:
                    self.move_dir = (0,-1)
                elif keys[pygame.K_s]:
                    self.move_dir = (0,1)
                elif keys[pygame.K_a]:
                    self.move_dir = (-1,0)
                elif keys[pygame.K_d]:
                    self.move_dir = (1,0)
            
                if self.x + self.move_dir[0] > GRID_SIZE_X or self.x + self.move_dir[0] < 0 or self.y + self.move_dir[1] > GRID_SIZE_Y or self.y + self.move_dir[1] < 0:
                    self.move_dir = (0,0) 
                if tiles[self.y + self.move_dir[1]][self.x + self.move_dir[0]].type != tile_type.ICE and (self.move_dir[0] != 0 or self.move_dir[1] != 0):
                    self.moving = True

                if keys[pygame.K_x] and not self.moving and not self.icing:
                    self.icing = True
                    self.frames = 2
            
            else:
                if keys[pygame.K_UP]:
                    self.move_dir = (0,-1)
                elif keys[pygame.K_DOWN]:
                    self.move_dir = (0,1)
                elif keys[pygame.K_LEFT]:
                    self.move_dir = (-1,0)
                elif keys[pygame.K_RIGHT]:
                    self.move_dir = (1,0)

                if self.x + self.move_dir[0] > GRID_SIZE_X or self.x + self.move_dir[0] < 0 or self.y + self.move_dir[1] > GRID_SIZE_Y or self.y + self.move_dir[1] < 0:
                    self.move_dir = (0,0) 
                if tiles[self.y + self.move_dir[1]][self.x + self.move_dir[0]].type != tile_type.ICE and (self.move_dir[0] != 0 or self.move_dir[1] != 0):
                    self.moving = True

                if keys[pygame.K_RCTRL] and not self.moving and not self.icing:
                    self.icing = True
                    self.frames = 2
        else:
            self.icing = False
            if self.move_dir[0] == 1:
                self.adj_x = TILE_SIZE/self.movement_speed * self.movement_step
            elif self.move_dir[0] == -1:
                self.adj_x = -TILE_SIZE/self.movement_speed * self.movement_step
            elif self.move_dir[1] == 1:
                self.adj_y = TILE_SIZE/self.movement_speed * self.movement_step
            else:
                self.adj_y = -TILE_SIZE/self.movement_speed * self.movement_step
            self.movement_step += 1
            if self.movement_step == self.movement_speed:
                self.moving = False
                self.adj_x = 0
                self.adj_y = 0
                self.x += self.move_dir[0]
                self.y += self.move_dir[1]
                self.movement_step = 1
                self.dir = self.move_dir
                self.move_dir = (0,0)

    def ice(self, tiles, step):
        if self.x + self.dir[0] * step > GRID_SIZE_X-1 or self.y + self.dir[1] * step > GRID_SIZE_Y-1 or self.x + self.dir[0] * step < 0 or self.y + self.dir[1] * step < 0:
            self.icing = False
            return
        tile = tiles[self.y + self.dir[1] * step][self.x + self.dir[0] * step]
        
        if tile.type == tile_type.FREE:
            if self.melting:
                self.melting = False
                self.icing = False
                return
            tile.set_type(tile_type.ICE)
        elif self.melting and tile.type == tile_type.ICE:
            tile.set_type(tile_type.FREE)
        elif tile.type == tile_type.ICE and step == 1:
            tile.set_type(tile_type.FREE)
            self.melting = True
        else:
            self.icing = False
            self.melting = False
    
    def update(self, tiles):
        if self.icing:
            self.frames += 1
            if self.frames % 3 == 0:
                self.ice(tiles, int(self.frames / 3))



    def draw(self, window):
        window.blit(self.img, (self.x*TILE_SIZE+420+self.adj_x, self.y* TILE_SIZE+self.adj_y))