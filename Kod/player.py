import pygame
from enum import Enum

TILE_SIZE = 72
GRID_SIZE_X = int(1080/TILE_SIZE)
GRID_SIZE_Y = int(1080/TILE_SIZE)

class tile_type(Enum):
    ICE = 0
    FREE = 1
    OBSTACLE = 2
    ENEMY = 3
    PLAYER = 4

def scale(image):
    size = (TILE_SIZE, TILE_SIZE)
    return pygame.transform.scale(image , size)





class Player:
    
    def __init__(self, number, x, y):
        self.x = x
        self.y = y
        self.adj_x = 0
        self.adj_y = 0
        self.number = number
        self.next_x = 0
        self.next_y = 0
        self.movement_step = 1
        self.moving = False
        self.dir = (1,0)
        self.move_dir = (0,0)
        self.movement_speed = 24
        self.icing = False
        self.frames = 0
        self.melting = False
        self.images = {}
        self.load_textures()
        self.move_timer = 0
        self.last_dir = (0,0)
        self.time_until_icing = 30
        self.score = 0
        

    def load_textures(self):
        self.images["(-1, 0)"] = scale(pygame.image.load(f"Grafika/player{self.number}_left.png"))
        self.images["(1, 0)"] = scale(pygame.image.load(f"Grafika/player{self.number}_right.png"))
        self.images["(0, -1)"] = scale(pygame.image.load(f"Grafika/player{self.number}_up.png"))
        self.images["(0, 1)"] = scale(pygame.image.load(f"Grafika/player{self.number}_down.png"))
    def move(self, keys, tiles, fruits):
        if not self.moving and not self.icing:
            self.current_move_dir = (0,0)
            if self.number == 1:

            
                
                if keys[pygame.K_w]:
                    self.current_move_dir = (0,-1)
                elif keys[pygame.K_s]:
                    self.current_move_dir = (0,1)
                elif keys[pygame.K_a]:
                    self.current_move_dir = (-1,0)
                elif keys[pygame.K_d]:
                    self.current_move_dir = (1,0)

                if not self.moving and not self.icing:        
                    if self.last_dir == self.current_move_dir:
                        self.move_timer += 1
                        if self.move_timer > 8:
                            self.move_dir = self.last_dir
                    else:
                        self.last_dir = self.current_move_dir
                        if self.last_dir != (0,0): 
                            self.dir = self.last_dir
                        self.move_timer = 0



                if self.x + self.move_dir[0] > GRID_SIZE_X-1 or self.x + self.move_dir[0] < 0 or self.y + self.move_dir[1] > GRID_SIZE_Y-1 or self.y + self.move_dir[1] < 0:
                    self.move_dir = (0,0) 
                if tiles[self.x + self.move_dir[0]][self.y + self.move_dir[1]].type == tile_type.FREE and (self.move_dir[0] != 0 or self.move_dir[1] != 0):
                    self.moving = True

                if keys[pygame.K_x] and not self.moving and not self.icing and self.time_until_icing == 0:
                    self.icing = True
                    self.move_timer = 0
                    self.frames = 2
                    self.time_until_icing = 30
            
            else:
                if keys[pygame.K_UP]:
                    self.current_move_dir = (0,-1)
                elif keys[pygame.K_DOWN]:
                    self.current_move_dir = (0,1)
                elif keys[pygame.K_LEFT]:
                    self.current_move_dir = (-1,0)
                elif keys[pygame.K_RIGHT]:
                    self.current_move_dir = (1,0)


                if not self.moving and not self.icing:        
                    if self.last_dir == self.current_move_dir:
                        self.move_timer += 1
                        if self.move_timer > 8:
                            self.move_dir = self.last_dir
                    else:
                        self.last_dir = self.current_move_dir
                        if self.last_dir != (0,0): 
                            self.dir = self.last_dir
                        self.move_timer = 0


                if self.x + self.move_dir[0] > GRID_SIZE_X-1 or self.x + self.move_dir[0] < 0 or self.y + self.move_dir[1] > GRID_SIZE_Y-1 or self.y + self.move_dir[1] < 0:
                    self.move_dir = (0,0) 
                if tiles[self.x + self.move_dir[0]][self.y + self.move_dir[1]].type == tile_type.FREE and (self.move_dir[0] != 0 or self.move_dir[1] != 0):
                    self.moving = True

                if keys[pygame.K_RCTRL] and not self.moving and not self.icing and self.time_until_icing == 0:
                    self.icing = True
                    self.move_timer = 0
                    self.frames = 2
                    self.time_until_icing = 30
        
        elif not self.icing:
            self.icing = False
            if self.move_dir[0] == 1:
                self.adj_x = 3 * self.movement_step
            elif self.move_dir[0] == -1:
                self.adj_x = -3 * self.movement_step
            elif self.move_dir[1] == 1:
                self.adj_y = 3 * self.movement_step
            else:
                self.adj_y = -3 * self.movement_step
            self.movement_step += 1
            self.dir = self.move_dir

            if self.movement_step == self.movement_speed/2:
                for i in range(len(fruits)):
                    if fruits[i].x == self.x + self.move_dir[0] and fruits[i].y == self.y + self.move_dir[1]:
                        self.score += fruits[i].score
                        del fruits[i]
                        break
                            

            if self.movement_step == self.movement_speed:
                self.moving = False
                self.adj_x = 0
                self.adj_y = 0
                self.x += self.move_dir[0]
                self.y += self.move_dir[1]
                self.movement_step = 1
                self.move_dir = (0,0)


    def ice(self, tiles, step):
        if self.x + self.dir[0] * step > GRID_SIZE_X-1 or self.y + self.dir[1] * step > GRID_SIZE_Y-1 or self.x + self.dir[0] * step < 0 or self.y + self.dir[1] * step < 0:
            self.icing = False
            self.melting = False
            return
        tile = tiles[self.x + self.dir[0] * step][self.y + self.dir[1] * step]
        
        if tile.type == tile_type.PLAYER or tile.type == tile_type.ENEMY:
            self.icing = False
            self.melting = False
            return

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
        elif self.time_until_icing > 0:
            self.time_until_icing -= 1


    def draw(self, window):
        window.blit(self.images[str(self.dir)], (self.x*TILE_SIZE+420+int(self.adj_x), self.y* TILE_SIZE+int(self.adj_y)))