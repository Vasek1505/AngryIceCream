import pygame, sys
from enum import Enum

from pygame.constants import QUIT
from player import *

ICE_IMG = pygame.image.load("E:\Python\BADICECREAMRIPOFF\ice.png")

class Tile:

    def __init__(self, type, img, x ,y):
        self.type = type
        self.img = img
        self.x = x
        self.y = y 

    def set_type(self, type):
        self.type = type
        if self.type == tile_type.ICE:
            self.img = ICE_IMG
        elif self.type == tile_type.FREE:
            self.img = None 

    def draw(self, window):
        if self.img != None:
            window.blit(self.img, (self.x * TILE_SIZE + 420, self.y * TILE_SIZE))

