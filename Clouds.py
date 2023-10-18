import random


class Cloud:
    def __init__(self, pos, speed, depth, img):
        self.pos = list(pos)
        self.speed = speed
        self.depth = depth
        self.img = img

    def update(self):
        self.pos[0] += self.speed

    def render(self, surf, offset=(0, 0)):
        render_pos = (self.pos[0] - offset[0] * self.depth, self.pos[1] - offset[1] * self.depth)
        surf.blit(self.img, (render_pos[0] % (surf.get_width() + self.img.get_width()) - self.img.get_width(),
                             render_pos[1] % (surf.get_height() + self.img.get_height()) - self.img.get_height()))

class Clouds:
    def __init__(self, images, number_of_clouds=16):
        self.clouds = []
        for i in range(number_of_clouds):
            position = (random.random() * 99999, random.random() * 99999)
            img = random.choice(images) #TODO poslat vic obrazku, vybrat jeden
            speed = random.random() * 0.05 + 0.05
            depth = random.random() * 0.6 + 0.2
            self.clouds.append(Cloud(position, speed, depth, img))

        self.clouds.sort(key=lambda x: x.depth)

    def update(self):
        for cloud in self.clouds:
            cloud.update()

    def render(self, surf, offset=(0, 0)):
        for cloud in self.clouds:
            cloud.render(surf, offset=offset)