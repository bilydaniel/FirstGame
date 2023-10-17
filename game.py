import pygame
import os
import sys
from tilemap import *
from player import *
from helpers import *
from Clouds import *

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.tilemap = Tilemap(self)
        self.display = pygame.Surface((DISPLAY_WIDTH, DISPLAY_HEIGHT))
        self.clock = pygame.time.Clock()
        self.player = Player(self, (50,50))
        self.movement = [False, False]


        self.assets = {
            "player": load_image('player.png'),
            "background": load_image("background.png"),
            "clouds": load_image("cloud.png")
        }
        self.clouds = Clouds(self.assets['clouds'])

    def run(self):
        while True:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        self.movement[LEFT] = True
                    if event.key == pygame.K_d:
                        self.movement[RIGHT] = True

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_a:
                        self.movement[LEFT] = False
                    if event.key == pygame.K_d:
                        self.movement[RIGHT] = False

            self.update()
            self.render()



    def update(self):
        self.player.update((self.movement[RIGHT] - self.movement[LEFT],0))
        self.clouds.update()

    def render(self):
        self.display.blit(self.assets['background'], (0,0))
        self.tilemap.render(self.display)
        self.player.render(self.display)
        self.clouds.render(self.display)
        self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0,0))

        pygame.display.update()
        self.clock.tick(DESIRED_FPS)



