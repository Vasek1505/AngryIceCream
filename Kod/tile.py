import pygame, sys
from enum import Enum

from pygame.constants import QUIT
from player import *

ice = True





def scale(image, x_scale, y_scale):
    size = (72, 72)
    return pygame.transform.scale(image , size)


ICE_IMG = scale(pygame.image.load("Grafika/ice1texture.png"), 0.257, 0.257)

class Tile:

    def __init__(self, type, img, y ,x, entity = None):
        self.type = type
        self.entity = None
        if type == tile_type.ENEMY or type == tile_type.PLAYER:
            self.entity = entity
        self.img = img
        self.x = x
        self.y = y

    def set_type(self, type, entity = None):
        self.type = type
        if self.type == tile_type.ICE:
            self.img = ICE_IMG
        elif self.type == tile_type.FREE:
            self.img = None 
        elif self.type == tile_type.PLAYER or self.type == tile_type.ENEMY:
            self.entity = entity

    def draw(self, window):
        if self.img != None:
            window.blit(self.img, (self.x * TILE_SIZE + 420, self.y * TILE_SIZE))
        


