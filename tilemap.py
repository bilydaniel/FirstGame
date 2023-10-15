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
            self.tiles[str(i) + ";" + str(6)] = {"type" : "grass", "variant": 1 , "pos": (i,6)}
            self.tiles[str(7) + ";" + str(i + 3)] = {"type": "stone", "variant": 1, "pos": (7, i + 3)}

        for a in  range (10,20):
            self.redTiles[str(a) + ";" + str(6)] = {"type" : "grass", "variant": 1 , "pos": (a,6)}
            self.redTiles[str(7) + ";" + str(a + 3)] = {"type": "stone", "variant": 1, "pos": (7, a + 3)}


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


    def getCloseTiles(self, tile_pos):
        closeTiles = []
        self.redTiles = {}
        for offset in CLOSE_TILES_OFFSETS:
            offsetLocation = str(tile_pos[0] + offset[0]) + ";" + str(tile_pos[1] + offset[1])
            if(offsetLocation in self.tiles):

                self.redTiles[offsetLocation] = (self.tiles[offsetLocation])
                closeTiles.append(self.tiles[offsetLocation]["pos"])


        return closeTiles


    def getClosePhysicsRect(self, pos):
        tile_pos = pixelToTile(pos)
        closeTiles = self.getCloseTiles(tile_pos)
        print(closeTiles)
        drawRedRects(self.game.display, closeTiles)
        #print(closeTiles)
        #location = str(pos[0]) + ";" + str(pos[1])

        #if location in self.tiles:

        return []
