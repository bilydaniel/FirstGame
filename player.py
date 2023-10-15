from physicsentity import *

class Player(PhysicsEntity):
    def __init__(self, game, pos, size=(7,16)):
        super().__init__(game, pos, 'player', size)
        #TODO resize the player image

    def update(self, movement=(0,0)):
        super().update(movement)








    def render(self, surf):
        super().render(surf)
