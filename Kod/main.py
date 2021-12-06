import pygame, sys
from pygame.locals import *
from tile import *
from random import randint
from player import *
from pygame.time import *

sys.dont_write_bytecode = True

BLUE = (0,0,255)
WHITE =  (255,255,255)



pygame.init()

WINDOW = pygame.display.set_mode((1920,1080))


def terminate():
    pygame.quit()
    sys.exit()

level = ["UU             ",
         "             U ",
         "    UU       U ",
         "             U ",
         "UU      UUUU   ",
         "               ",
         " UUUUU        U",
         "        UU     ",
         "               ",
         "U        UU UUU",
         "    UU         ",
         "         UU   U",
         " UUU           ",
         "      UUU      ",
         "             UU"
        ]

tiles = []

for i in range(GRID_SIZE_X):
    new = []
    for j in range(GRID_SIZE_Y):
        if level[j][i] == "X":
            new.append(Tile(tile_type.ICE, ICE_IMG, j, i))
        elif level[j][i] == "U":
            new.append(Tile(tile_type.OBSTACLE, OBSTACLE_IMG, j, i))
        else:
            new.append(Tile(tile_type.FREE, None, j , i))
    tiles.append(new)

ice = 0
while ice < 60:
    x = randint(0, GRID_SIZE_X-1)
    y = randint(0, GRID_SIZE_Y-1)

    if tiles[x][y].type == tile_type.FREE:
        tiles[x][y].set_type(tile_type.ICE)
        ice += 1


fruits = []

while len(fruits) < 4:
    x = randint(0, GRID_SIZE_X-1)
    y = randint(0, GRID_SIZE_Y-1)

    for fruit in fruits:
        if fruit.x == x and fruit.y == y:
            continue
    if tiles[x][y].type == tile_type.FREE:
        rand = randint(0,6)
        if rand == 0 or rand == 1 or rand == 3:
            fruits.append(Fruit(x,y,1, LEMON_IMG))
        elif rand == 4 or rand == 5:
            fruits.append(Fruit(x,y,2, APPLE_IMG))
        else:
            fruits.append(Fruit(x,y, 3, STRAWBERRY_IMG))
                       

player_one = Player(1, 10, 0)
player_two = Player(2, 11, GRID_SIZE_Y-1)

tiles[10][0].set_type(tile_type.PLAYER)
tiles[11][GRID_SIZE_Y-1].set_type(tile_type.PLAYER)

clock = pygame.time.Clock()

font = pygame.font.Font("freesansbold.ttf", 32)

spawn_fruits = pygame.USEREVENT + 0

pygame.time.set_timer(spawn_fruits, 4000)



while True:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == QUIT:
            terminate()
        
        if event.type == spawn_fruits and len(fruits) < 10:
            while True:
                x = randint(0, GRID_SIZE_X-1)
                y = randint(0, GRID_SIZE_Y-1)

                if tiles[x][y].type == tile_type.FREE:
                    rand = randint(0,6)
                    if rand == 0 or rand == 1 or rand == 3:
                        fruits.append(Fruit(x,y,1, LEMON_IMG))
                    elif rand == 4 or rand == 5:
                        fruits.append(Fruit(x,y,2, APPLE_IMG))
                    else:
                        fruits.append(Fruit(x,y, 3, STRAWBERRY_IMG))
                    break  

    
    WINDOW.fill((0,0,0))

    pygame.draw.rect(WINDOW, (2,21,59), (0 ,0, 1920, 1080))
    pygame.draw.rect(WINDOW, (65,181,217), (420, 0, 1080, 1080))

    for i in range(GRID_SIZE_X):
        for j in range(GRID_SIZE_Y):
            tiles[i][j].draw(WINDOW)
    
    keys = pygame.key.get_pressed()

    for fruit in fruits:
        fruit.draw(WINDOW)

    tiles[player_one.x][player_one.y].set_type(tile_type.FREE)
    tiles[player_two.x][player_two.y].set_type(tile_type.FREE)

    player_one.move(keys, tiles, fruits)
    player_two.move(keys, tiles, fruits)

    tiles[player_one.x][player_one.y].set_type(tile_type.PLAYER, player_one)
    tiles[player_two.x][player_two.y].set_type(tile_type.ENEMY, player_two)

    player_one.update(tiles)
    player_two.update(tiles)

    player_one.draw(WINDOW)
    player_two.draw(WINDOW)


    text3 = font.render("Lemon = 1 points", True, WHITE)
    text4 = font.render("Apple = 2 points", True, WHITE)
    text5 = font.render("Strawberry = 3 points", True, WHITE)

    text3_r = text3.get_rect()
    text3_r.topleft = (25, 500)
    text4_r = text4.get_rect()
    text4_r.topleft = (25, 600)
    text5_r = text5.get_rect()
    text5_r.topleft = (25, 700)

    WINDOW.blit(text3, text3_r)
    WINDOW.blit(text4, text4_r)
    WINDOW.blit(text5, text5_r)

    text1 = font.render(f"Player black score: {str(player_one.score)}", True, WHITE)
    text1_rect = text1.get_rect()
    text1_rect.topleft = (25,50)
    text2 = font.render(f"Player white score: {str(player_two.score)}", True, WHITE)
    text2_rect = text2.get_rect()
    text2_rect.topleft = (1920-400,50)

    WINDOW.blit(text1, text1_rect)
    WINDOW.blit(text2, text2_rect)

    pygame.display.update()
    

