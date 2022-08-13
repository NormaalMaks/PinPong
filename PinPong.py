from pygame import *
from math import *

#____________________________________________________________________________________________________________________________________________

class GameSprite():
    def __init__(self, player_img, pl_x, pl_y, p_speed, width, height):
        super().__init__()
        self.image = transform.scale(image.load(player.img), (width, height))
        self.speed = p_speed
        self.rect = self.image.get_rect()
        self.rect.x = pl_x
        self.rect.y = pl_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    pass

win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
blue = (200, 255, 255)
window.fill(blue)
display.set_caption("Pin Pong")

clock = time.Clock()
fps = 60
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    display.update()
    clock.tick(60)