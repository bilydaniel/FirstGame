import pygame

LEFT = 0
RIGHT = 1

SCREEN_SCALE = 1
SCREEN_WIDTH = 640 * SCREEN_SCALE
SCREEN_HEIGHT = 480 * SCREEN_SCALE

DISPLAY_SCALE = 1
DISPLAY_WIDTH = 320 * DISPLAY_SCALE
DISPLAY_HEIGHT = 240 * DISPLAY_SCALE


DESIRED_FPS = 60
BASE_DIR = "images/"

PHYSICS_TILES = {"grass", "stone"}
CLOSE_TILES_OFFSETS = [(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1)]

def load_image(path):
    image = pygame.image.load(BASE_DIR + path).convert()
    image.set_colorkey((0,0,0))
    return image


def pixelToTile(pos, tile_size=16):
    return (pos[0] // tile_size, pos[1] //tile_size)

def tileToPixel(pos, tile_size=16):
    return (pos[0] * tile_size, pos[1] * tile_size)


def drawRedRects(surface, positions, tile_size=16):
    for position in positions:
        drawRedRect(surface, position)

def drawRedRect(surface, position, tile_size=16):
    red = (255,0,0)
    print(position)
    x, y = position[0] * tile_size, position[1] * tile_size
    rect = pygame.Rect(x, y, tile_size, tile_size)
    pygame.draw.rect(surface, red, rect)
    #pygame.draw.rect(surface, red, position[0] * tile_size, position[1] * tile_size, tile_size, tile_size)