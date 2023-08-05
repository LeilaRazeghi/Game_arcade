import arcade
import random

class Ball(arcade.Sprite):
    def __init__(self, game):
        super().__init__()
        self.center_x = game.width//2
        self.center_y = game.height//2
        self.color =arcade.color.YELLOW
        self.radious = 15
        self.change_x = random.choice([-1, 1])
        self.change_y = random.choice([-1, 1])
        self.speed = 2
        self.width = self.radious * 2
        self.height = self.radious * 2

    def move(self):
        self.center_x +=self.change_x * self.speed
        self.center_y +=self.change_y * self.speed

    def draw(self):
        arcade.draw_circle_filled(self.center_x, self.center_y, self.radious, self.color)