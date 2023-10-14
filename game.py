import pygame
import os
import sys
from tilemap import *

class Game:
    def __init__(self):
        pygame.init()
        SCREEN_WIDTH = 640
        SCREEN_HEIGHT = 480
        self.DESIRED_FPS = 60
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.tilemap = Tilemap(self)
        self.display = pygame.Surface((320, 240))
        self.clock = pygame.time.Clock()


    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.render()



    def render(self):
        self.display.fill((14, 219, 248))
        self.tilemap.render(self.display)
        self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0,0))
        pygame.display.update()
        self.clock.tick(self.DESIRED_FPS)



