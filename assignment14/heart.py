
import arcade

class Heart(arcade.Sprite):
    def __init__(self, x):
        super().__init__("ImageHeart.png")
        self.center_x = 30 * x
        self.center_y = 30
        self.width = 40
        self.height = 40

    def lose_heart(self):
        self.hearts -= 1
        if self.hearts ==0:
            print("game over")
            arcade.close_window()
        else:
            self.center_x= self.game_width//2
            self.center_y = 80
            

    