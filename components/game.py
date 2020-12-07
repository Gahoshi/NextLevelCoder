import pygame

from components.ball import Ball
from components.player import Player
from utils.text_utils import draw_text
from components.powerup import Powerup
from components.heald import Heald
from components.info import Info
from utils.constants import (
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    TITLE,
    BLACK,
    IMG_DIR,
    FPS

)
from os import path

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.background_img = pygame.image.load(path.join(IMG_DIR, "spacefield.png")).convert()
        self.background_img = pygame.transform.scale(self.background_img, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.running = True
        self.power = False
        self.vida = 3
        pygame.mixer.init()
        pygame.mixer.music.load(path.join(IMG_DIR, 'town4.mp3'))
        pygame.mixer.music.play(-1)
        self.bala = 5

    def run(self):
        self.create_components()
        #Game loop:
        self.power = False
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def create_components(self):
        self.all_sprites = pygame.sprite.Group()
        self.balls = pygame.sprite.Group()
        self.powerups = pygame.sprite.Group()
        self.player = Player(self)

        self.all_sprites.add(self.player)
        ball = Ball(1)
        self.all_sprites.add(ball)
        self.balls.add(ball)

        self.powerup = pygame.sprite.Group()
        powerup = Powerup(1)
        self.all_sprites.add(powerup)
        self.powerups.add(powerup)

        self.heald = pygame.sprite.Group()
        heald = Heald(1)
        self.all_sprites.add(heald)
        self.heald.add(heald)

        self.info = pygame.sprite.Group()
        info = Info(1)
        self.info.add(info)
        self.all_sprites.add(info)




    def update(self):
        self.all_sprites.update()
        hits = pygame.sprite.spritecollide(self.player, self.balls, False)
        if hits:
            self.vida -= 1
            if self.vida <= 0:
                self.playing = False
        hits = pygame.sprite.groupcollide(self.balls, self.player.bullets, True, True)
        if hits:
            self.bala -= 1
        for hit in hits:
            if hit.size < 4:
                for i in range (0, 2):
                    ball = Ball(hit.size + 1)
                    self.all_sprites.add(ball)
                    self.balls.add(ball)

        hits = pygame.sprite.spritecollide(self.player, self.powerups, True)
        if hits:
            self.power = True
        if self.bala == 0:
            self.power = False

        hits = pygame.sprite.spritecollide(self.player, self.heald , True)
        if hits:
            self.vida += 1


    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.player.shoot(self.power)





    def draw(self):
        background_rect = self.background_img.get_rect()
        self.screen.blit(self.background_img, background_rect)
        self.all_sprites.draw(self.screen)
        pygame.display.flip()

    def show_start_screen(self):
        self.screen.blit(self.background_img, self.background_img.get_rect())
        draw_text(self.screen, "Game working!!", 64, SCREEN_WIDTH/2, SCREEN_HEIGHT/4)
        draw_text(self.screen, "Teclas Izq/Der para moverse y SPACIO para disparar", 25, SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
        draw_text(self.screen, "presione ENTER para comenzar", 25, SCREEN_WIDTH/2, SCREEN_HEIGHT*3/5)
        pygame.display.flip()
        waiting = True
        while waiting:
            self.clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit(0)
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_RETURN:
                        waiting = False