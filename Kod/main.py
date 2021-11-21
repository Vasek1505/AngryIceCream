import pygame, sys
from pygame.locals import *
from tile import *
from player import *

sys.dont_write_bytecode = True

BLUE = (0,0,255)
WHITE =  (255,255,255)

#vasek smrdi
PLAYER_ONE_IMG = pygame.image.load("Grafika/player_one.png")
PLAYER_TWO_IMG = pygame.image.load("Grafika/player_two.png") 


pygame.init()

WINDOW = pygame.display.set_mode((1920,1080))


def terminate():
    pygame.quit()
    sys.exit()

level = ["               ",
         "               ",
         "               ",
         "               ",
         "               ",
         "               ",
         "               ",
         "          XXXXX",
         "  XXXX         ",
         "               ",
         "   XXXXXXXXXXX ",
         "               ",
         "               ",
         "               ",
         "               "
        ]

tiles = []

for i in range(GRID_SIZE_X):
    new = []
    for j in range(GRID_SIZE_Y):
        if level[j][i] == "X":
            new.append(Tile(tile_type.ICE, ICE_IMG, j, i))
        else:
            new.append(Tile(tile_type.FREE, None, j , i))
    tiles.append(new)


player_one = Player(1, 10, 10, PLAYER_ONE_IMG)
player_two = Player(2, 11, 10, PLAYER_TWO_IMG)

tiles[10][10].set_type(tile_type.PLAYER)
tiles[10][11].set_type(tile_type.ENEMY)

clock = pygame.time.Clock()

font = pygame.font.Font("freesansbold.ttf", 32)


while True:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == QUIT:
            terminate()

    
    WINDOW.fill((0,0,0))

    pygame.draw.rect(WINDOW, (0,0,0), (420, 0, 1080, 1080))

    for i in range(GRID_SIZE_X):
        for j in range(GRID_SIZE_Y):
            tiles[i][j].draw(WINDOW)
    
    keys = pygame.key.get_pressed()

    tiles[player_one.x][player_one.y].set_type(tile_type.FREE)
    tiles[player_two.x][player_two.y].set_type(tile_type.FREE)

    player_one.move(keys, tiles)
    player_two.move(keys, tiles)

    tiles[player_one.x][player_one.y].set_type(tile_type.PLAYER, player_one)
    tiles[player_two.x][player_two.y].set_type(tile_type.ENEMY, player_two)

    player_one.update(tiles)
    player_two.update(tiles)

    player_one.draw(WINDOW)
    player_two.draw(WINDOW)
    
    fps_text = font.render(str(int(1000/clock.get_time())), True, (255,255,255))
    WINDOW.blit(fps_text, (0,0))



    pygame.display.update()
    



