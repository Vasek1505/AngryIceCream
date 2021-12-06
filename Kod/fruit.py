from player import *



LEMON_IMG = scale(pygame.image.load("Grafika/lemon.png"))
APPLE_IMG = scale(pygame.image.load("Grafika/apple.png"))
STRAWBERRY_IMG = scale(pygame.image.load("Grafika/strawberry.png"))


class Fruit:

    def __init__(self, x, y, score, img):
        self.x = x
        self.y = y
        self.score = score
        self.image = img


    def draw(self, window):
        window.blit(self.image, (self.x*TILE_SIZE+420, self.y* TILE_SIZE))