import pygame, sys
from pygame.locals import *
from tile import *
from player import *

TILE_SIZE = 40
BLUE = (0,0,255)
WHITE =  (255,255,255)


PLAYER_ONE_IMG = pygame.image.load("player_one.png")
PLAYER_TWO_IMG = pygame.image.load("player_two.png") 


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

    player_one.move(keys, tiles)
    print(player_one.adj_x)
    player_two.move(keys, tiles)

    player_one.draw(WINDOW)
    player_two.draw(WINDOW)

    pygame.display.update()
    clock.tick(60)
    



