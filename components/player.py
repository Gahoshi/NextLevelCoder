import pygame
from utils.constants import(
GREEN,
BLACK,
SCREEN_HEIGHT,
SCREEN_WIDTH,
IMG_DIR
)
from os import path
from components.bullet import Bullet

class Player(pygame.sprite.Sprite):
    def __init__(self, game):
        pygame.sprite.Sprite.__init__(self)
        self.game = game
        self.image = pygame.image.load(path.join(IMG_DIR, "alien.png"))
        self.image = pygame.transform.scale(self.image, (30,25))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH/2
        self.rect.bottom = SCREEN_HEIGHT -10
        self.bullets = pygame.sprite.Group()


    def update(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.rect = self.rect.move(0,0)
            self.rect.x -= 5
        if self.rect.left <= 0:
            self.rect.left = 0

        if key[pygame.K_RIGHT]:
            self.rect = self.rect.move(1,0)
            self.rect.x += 5
            if self.rect.right >= SCREEN_WIDTH:
                self.rect.right = SCREEN_WIDTH

    def shoot(self,power):
        sound_rifle = pygame.mixer.Sound(path.join(IMG_DIR, 'rifle.ogg'))
        pygame.mixer.Sound.play(sound_rifle)
        condicion = power
        if condicion == False:
            bullet = Bullet(self.rect.centerx, self.rect.top)
            self.game.all_sprites.add(bullet)
            self.bullets.add(bullet)
        elif condicion == True:
            bullet = Bullet(self.rect.centerx, self.rect.top)
            bullet1 = Bullet(self.rect.centerx - 10, self.rect.top)
            bullet2 = Bullet(self.rect.centerx - 20, self.rect.top)
            bullet3 = Bullet(self.rect.centerx - 30, self.rect.top)
            bullet4 = Bullet(self.rect.centerx + 10, self.rect.top)
            bullet5 = Bullet(self.rect.centerx + 20, self.rect.top)
            bullet6 = Bullet(self.rect.centerx + 30, self.rect.top)
            self.game.all_sprites.add(bullet)
            self.game.all_sprites.add(bullet1)
            self.game.all_sprites.add(bullet2)
            self.game.all_sprites.add(bullet3)
            self.game.all_sprites.add(bullet4)
            self.game.all_sprites.add(bullet5)
            self.game.all_sprites.add(bullet6)
            self.bullets.add(bullet)
            self.bullets.add(bullet1)
            self.bullets.add(bullet2)
            self.bullets.add(bullet3)
            self.bullets.add(bullet4)
            self.bullets.add(bullet5)
            self.bullets.add(bullet6)