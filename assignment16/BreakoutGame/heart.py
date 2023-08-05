import arcade

class Heart(arcade.Sprite):
    def __init__(self, x):
        super().__init__("ImageHeart.png")
        self.center_x = 25*x
        self.center_y = 25
        self.width = 30
        self.height = 30