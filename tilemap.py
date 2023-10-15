import pygame
from helpers import *

class Tilemap:
    def __init__(self, game, tile_size = 16):
        self.game = game
        self.tile_size = tile_size
        self.tiles = {}
        self.redTiles = {}
        self.createSimpleMap()


    def createSimpleMap(self):
        for i in  range (10):
            self.tiles[str(i) + ";" + str(6)] = {"type" : "stone", "variant": 1 , "pos": (i,6)}
            self.tiles[str(7) + ";" + str(i + 3)] = {"type": "stone", "variant": 1, "pos": (7, i + 3)}


    def render(self, surface):
        for tile in self.tiles:
            color = (0,0,0)
            if(self.tiles[tile]['type'] == 'grass'):
                color = (124, 252, 0)
            if(self.tiles[tile]['type'] == 'stone'):
                color = (183, 176, 156)
            pygame.draw.rect(surface, color, (self.tiles[tile]['pos'][0] * self.tile_size, self.tiles[tile]['pos'][1] * self.tile_size, self.tile_size, self.tile_size))

        for tile in self.redTiles:
            color = (255,0,0)
            pygame.draw.rect(surface, color, (self.redTiles[tile]['pos'][0] * self.tile_size, self.redTiles[tile]['pos'][1] * self.tile_size, self.tile_size, self.tile_size))



    def makeRectFromTile(self, pos, tile_size=16):
        pixelPos = tileToPixel(pos)
        return pygame.Rect(pixelPos[0], pixelPos[1], tile_size, tile_size)

    def getClosePhysicsRect(self, pos):
        tile_pos = pixelToTile(pos)
        closeRects = []
        for offset in CLOSE_TILES_OFFSETS:
            offsetLocation = str(tile_pos[0] + offset[0]) + ";" + str(tile_pos[1] + offset[1])
            if (str(offsetLocation) in self.tiles):
                if (self.tiles[offsetLocation]['type'] in PHYSICS_TILES):
                    closeRects.append(self.makeRectFromTile(self.tiles[offsetLocation]["pos"]))

        return closeRects

