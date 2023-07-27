import random
import arcade
from snake import Snake
from apple import Apple
from apple import Pear
from apple import Feces

class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=500, height=500, title="Super Snake V1")
        arcade.set_background_color(arcade.color.KHAKI)
        self.snake = Snake(self)
        self.apple = Apple(self)
        self.pear = Pear(self)
        self.feces = Feces(self)
        self.game_status = "ready"

    def on_draw(self):
        arcade.start_render()
        self.snake.draw()
        self.apple.draw()
        self.pear.draw()
        self.feces.draw()

        arcade.draw_text(f"score: {self.snake.score}", 30, 30, arcade.color.BLACK, 15, 20)
       
        if self.game_status == "game over":
            arcade.draw_lrtb_rectangle_filled(0, self.width, self.height, 0, arcade.color.BLACK)
            arcade.draw_text("Game Over!", 100, 250, arcade.color.YELLOW_ORANGE, 40, 40)

        arcade.finish_render()

    def on_update(self, delta_time: float):
        self.snake.move()
        if self.snake.center_x == 500 or self.snake.center_x ==0 or self.snake.center_y == 500 or self.snake.center_y ==0:
           self.game_status = "game over"

        for part in self.snake.body:
            if self.snake.center_x+30==part['x'] or self.snake.center_x+30==part['x'] or self.snake.center_y+30 ==part['y'] or self.snake.center_y+30==part['y']:
             self.game_status="game over"

        if arcade.check_for_collision(self.snake, self.apple):
            del self.apple
            self.snake.score += 1
            self.apple = Apple(self)

        elif arcade.check_for_collision(self.snake, self.pear):
            del self.pear
            self.snake.score += 2
            self.pear = Pear(self)

        elif arcade.check_for_collision(self.snake, self.feces):
            if self.snake.score > 0:
                self.snake.score -= 1
                self.feces = Feces(self)
            if self.snake.score <= 0:
                self.game_status = "game over"
                

    def on_key_release(self, symbol: int, modifiers: int):
       if symbol == arcade.key.UP:
           self.snake.change_x =0
           self.snake.change_y = 1
       elif symbol == arcade.key.DOWN:
           self.snake.change_x = 0
           self.snake.change_y = -1
       elif symbol == arcade.key.RIGHT:
           self.snake.change_x = 1
           self.snake.change_y = 0
       elif symbol == arcade.key.LEFT:
           self.snake.change_x = -1
           self.snake.change_y = 0

if __name__== "__main__":
    game = Game()
    arcade.run()
    
