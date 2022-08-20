from pygame import *
from math import *
import os

#____________________________________________________________________________________________________________________________________________

class GameSprite():
    def __init__(self, player_img, pl_x, pl_y, p_speed, width, height):
        super().__init__()
        self.image = transform.scale(image.load(player_img), (width, height))
        self.speed = p_speed
        self.rect = self.image.get_rect()
        self.rect.x = pl_x
        self.rect.y = pl_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 145:
            self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 145:
            self.rect.y += self.speed

speed_x = 3
speed_y = 3

racket1 = Player("racket.png", 30, 200, 4, 50, 150)
racket2 = Player("racket.png", 520, 200, 4, 50, 150)
ball = GameSprite("tenis_ball.png", 200, 200, 4, 50, 50)

font.init()
font = font.Font(None, 35)
lose1 = font.render("Player 1 lost!", True, (0,0,0))
lose2 = font.render("Player 2 lost!", True, (0,0,0))
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
blue = (200, 255, 255)
window.fill(blue)
display.set_caption("Pin Pong")

clock = time.Clock()
fps = 60
game = True
finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.fill(blue)
        racket1.update_l()
        racket2.update_r()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            speed_x *= -1
        if ball.rect.y > win_height-50 or ball.rect.y < 0:
            speed_y *= -1
        if ball.rect.x > win_width:
            finish = True
            window.blit(lose2,(200, 200))
        if ball.rect.x < 0:
            finish = True
            window.blit(lose1,(200, 200))
        racket1.reset()
        racket2.reset()
        ball.reset()
    display.update()
    clock.tick(60)