import arcade
import random


class Fruit(arcade.Sprite):
    def __init__(self,image_file, game):
        super().__init__(image_file)
        self.width = 30
        self.height = 30
        self.change_x = 0
        self.change_y = 0
        self.center_x = random.randint(10, game.width -10)
        self.center_y = random. randint(10, game.width -10)


class Apple(Fruit):
    def __init__(self, game):
        super().__init__("apple.png", game)
        self.width = 30
        self.height = 30


class Pear(Fruit):
    def __init__(self, game):
        super().__init__("pear.png", game)
        self.width = 30
        self.height = 30


class Feces(Fruit):
    def __init__(self, game):
        super().__init__("poop.png", game)
        self.width = 30
        self.height = 30
