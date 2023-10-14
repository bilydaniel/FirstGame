import pygame

class Tilemap:
    def __init__(self, game, tile_size = 16):
        self.game = game
        self.tile_size = tile_size
        self.tiles = {}
        self.createSimpleMap()

    def createSimpleMap(self):
        for i in  range (10):
            self.tiles[str(i) + ";" + str(6)] = {"type" : "grass", "variant": 1 , "pos": (i,6)}
            self.tiles[str(7) + ";" + str(i)] = {"type": "stone", "variant": 1, "pos": (7, i)}


    def render(self, surface):
        for tile in self.tiles:
            color = (0,0,0)
            if(self.tiles[tile]['type'] == 'grass'):
                color = (124, 252, 0)
            if(self.tiles[tile]['type'] == 'stone'):
                color = (183, 176, 156)
            pygame.draw.rect(surface, color, (self.tiles[tile]['pos'][0] * self.tile_size, self.tiles[tile]['pos'][1] * self.tile_size, self.tile_size, self.tile_size))


