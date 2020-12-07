import pygame

from os import path
from utils.constants import (BLACK,IMG_DIR,)

class Info(pygame.sprite.Sprite):
    def __init__(self,size):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(path.join(IMG_DIR,"vida.png"))
        self.image = pygame.transform.scale(self.image, (40//size,40//size))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = 0 - self.rect.width
        self.rect.y = 0
        self.size = size

    def update(self):
        self.rect.x = 10
        self.rect.y = 10

