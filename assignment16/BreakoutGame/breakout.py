import arcade
from rocket import Rocket
from ball import Ball
from brick import Brick
from heart import Heart


class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=500, height=600, title= "Breakout")
        arcade.set_background_color(arcade.color.NAVY_BLUE)
        self.rocket = Rocket(self)
        self.ball = Ball(self)
        self.brick_list = []
        self.color_list = [arcade.color.GREEN, arcade.color.YELLOW, arcade.color.ORANGE, arcade.color.RED]
        self.heart_list = []

        for row in range(4):
            for col in range(14):
                brick = Brick (row, col, self.color_list[row])
                brick.center_x = 20 + col * 35
                brick.center_y = 500 - row * 20
                self.brick_list.append(brick)

        for h in range(1, 4):
            self.heart = Heart(h+1)
            self.heart_list.append(self.heart)


    def on_draw(self):
        arcade.start_render()
        
        for brick in self.brick_list:
            brick.draw()

        self.rocket.draw()
        self.ball.draw()
         
        for heart in self.heart_list:
            heart.draw()

        arcade.draw_text(f"score: {self.rocket.score}", self.width//10, 570,\
                          arcade.color.WHITE, bold= True)
        
        if len(self.heart_list) == 0:
             arcade.draw_lrtb_rectangle_filled(0, 500, 600, 0, arcade.color.BLACK)
             arcade.draw_text("GAME OVER!", 100,300, arcade.color.RED, 30)   
             del self.ball
             del self.rocket 
             
        if len(self.brick_list)==0:
          arcade.draw_text(" Congrate!",100, 300, arcade.color.YELLOW, 30) 
          del self.ball
          del self.rocket      

        arcade.finish_render()


    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        if self.rocket.height < y < self.height-self.rocket.height:
           self.rocket.center_x = x
       # self.rocket.center_y = y

    def on_key_release(self, symbol: int, modifiers: int):
        if symbol == arcade.key.RIGHT:
            self.rocket.chenge_x = 1

        if symbol == arcade.key.LEFT:
            self.rocket.change_x = -1


    def on_update(self, delta_time):
        self.ball.move()
        
        for brick in self.brick_list:
            if arcade.check_for_collision(self.ball, brick):
                self.brick_list.remove(brick)
                self.ball.change_y *=-1
                self.rocket.score +=1
                

        if self.ball.center_x < 0 or self.ball.center_x > self.width:
            self.ball.change_x *=-1

        if self.ball.center_y > self.height:
            self.ball.change_y= -1

        if arcade.check_for_collision(self.ball, self.rocket):
            self.ball.change_y = 1

        if self.ball.center_y <0:
            if len(self.heart_list) >0:
                self.heart_list.pop(-1)
                del self.ball
                self.ball = Ball(self)

game = Game()
arcade.run()