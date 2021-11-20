import pygame, sys
from pygame.locals import *
from tile import *
from player import *

sys.dont_write_bytecode = True

TILE_SIZE = 40
BLUE = (0,0,255)
WHITE =  (255,255,255)


PLAYER_ONE_IMG = pygame.image.load("Grafika/player_one.png")
PLAYER_TWO_IMG = pygame.image.load("Grafika/player_two.png") 


pygame.init()

WINDOW = pygame.display.set_mode((1920,1080))


def terminate():
    pygame.quit()
    sys.exit()

level = ["                           ",
         "                           ",
         "                           ",
         "                           ",
         "                           ",
         "                           ",
         "                           ",
         "                           ",
         "                           ",
         "                           ",
         "                    X      ",
         "                    X      ",
         "                    X      ",
         "                    X      ",
         " XXXXXXX            X      ",
         "                    X      ",
         "                           ",
         "XXXXXXXXXXXXXXXXXXXXXXXXXXX",
         "                           ",
         "                           ",
         "                           ",
         "                           ",
         "                           ",
         "                           ",
         "                           ",
         "                           ",
         "                           ",
         
        ]

tiles = []

for i in range(27):
    new = []
    for j in range(27):
        if level[i][j] == "X":
            new.append(Tile(tile_type.ICE, ICE_IMG, j, i))
        else:
            new.append(Tile(tile_type.FREE, None, j , i))
    tiles.append(new)


player_one = Player(1, 10, 10, PLAYER_ONE_IMG)
player_two = Player(2, 11, 10, PLAYER_TWO_IMG)

tiles[10][10].set_type(tile_type.PLAYER)
tiles[10][11].set_type(tile_type.ENEMY)

clock = pygame.time.Clock()

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            terminate()

    
    WINDOW.fill((0,0,0))

    pygame.draw.rect(WINDOW, (255,255,0), (420, 0, 1080, 1080))

    for i in range(27):
        for j in range(27):
            tiles[i][j].draw(WINDOW)
    
    keys = pygame.key.get_pressed()

    tiles[player_one.y][player_one.x].set_type(tile_type.FREE)
    tiles[player_two.y][player_two.x].set_type(tile_type.FREE)

    player_one.move(keys, tiles)
    player_two.move(keys, tiles)

    tiles[player_one.y][player_one.x].set_type(tile_type.PLAYER, player_one)
    tiles[player_two.y][player_two.x].set_type(tile_type.ENEMY, player_two)

    player_one.update(tiles)
    player_two.update(tiles)

    player_one.draw(WINDOW)
    player_two.draw(WINDOW)

    pygame.display.update()
    clock.tick(60)
    



