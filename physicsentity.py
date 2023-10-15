import pygame


class PhysicsEntity:
    def __init__(self, game, pos, e_type, size=(16,16)):
        self.game = game
        self.pos = list(pos)
        self.type = e_type
        self.velocity = [0, 0]
        self.collisions = {"up": False, "down": False, "left": False, "right": False}
        self.size = size

    def render (self, surf):
        surf.blit(self.game.assets[self.type], self.pos)

    def getRect(self):
        return pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])

    def update(self, movement):
        #self.applyGravity()
        frame_movement = (movement[0] + self.velocity[0], movement[1] + self.velocity[1])

        self.pos[0] += frame_movement[0]

        entity_rect = self.getRect()
        for rect in self.game.tilemap.getClosePhysicsRect(self.pos):
            pass



        self.pos[1] += frame_movement[1]


    def applyGravity(self):
        self.velocity[1] = min(5, self.velocity[1] + 0.1)

        #if(self.collisions['down'] or self.collisions['up']):
        #    self.velocity[1] = 0

