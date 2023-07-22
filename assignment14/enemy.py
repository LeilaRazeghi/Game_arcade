import arcade 
import random

class Enemy(arcade.Sprite):
    def __init__(self, w, h):
        super().__init__(":resources:images/space_shooter/playerShip3_orange.png")
        self.center_x= random.randint(0, w)
        self.center_y= h + 24
        self.angle= 180
        self.width=48
        self.height=48
        self.speed = 0.5
    
    def move(self):
        self.center_y -= self.speed