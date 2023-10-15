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
        self.applyGravity()
        frame_movement = (movement[0] + self.velocity[0], movement[1] + self.velocity[1])

        self.pos[0] += frame_movement[0]
        entity_rect = self.getRect()
        for rect in self.game.tilemap.getClosePhysicsRect(self.pos):
            if entity_rect.colliderect(rect):
                if frame_movement[0] > 0:
                    self.collisions['right'] = True
                    entity_rect.right = rect.left
                if frame_movement[0] < 0:
                    self.collisions['left'] = True
                    entity_rect.left = rect.right
                self.pos[0] = entity_rect.x


        self.pos[1] += frame_movement[1]
        entity_rect = self.getRect()
        for rect in self.game.tilemap.getClosePhysicsRect(self.pos):
            if entity_rect.colliderect(rect):
                if frame_movement[1] > 0:
                    self.collisions['down'] = True
                    entity_rect.bottom = rect.top
                if frame_movement[1] < 0:
                    self.collisions['up'] = True
                    entity_rect.top = rect.bottom
                self.pos[1] = entity_rect.y


    def applyGravity(self):
        self.velocity[1] = min(5, self.velocity[1] + 0.1)

        if(self.collisions['down'] or self.collisions['up']):
            self.velocity[1] = 0

