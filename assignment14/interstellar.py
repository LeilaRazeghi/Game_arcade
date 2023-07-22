import random
import arcade
from spaceship import Spaceship
from enemy import Enemy
from heart import Heart


class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=1000, height=600, title="Inetrstellar Game 2023")
        arcade.set_background_color(arcade.color.DARK_BLUE)
        self.background = arcade.load_texture(":resources:images/backgrounds/stars.png")
        self.me= Spaceship(self.width)
        self.enemy_list = []
        self.enemy_spwan_interval = 3
        arcade.schedule(self.spwan_enemy, self.enemy_spwan_interval)
        self.elapsed_time = 0
        self.heart_list =[]
        self.score = 0
        self.fire_sound = arcade.load_sound(":resources:sounds/laser3.wav")
        self.explosion_sound =arcade.load_sound(":resources:sounds/explosion2.wav")
        

        for x in range(1, 4):
            self.heart = Heart(x)
            self.heart_list.append(self.heart)

 
    def spwan_enemy(self, delta_time):
        new_enemy = Enemy (self.width, self.height)
        self.enemy_list.append(new_enemy)


    def on_key_press(self, symbol: int, modifiers: int):

       if symbol==arcade.key.LEFT or symbol==arcade.key.A:
           self.me.change_x = -1
       elif symbol==arcade.key.RIGHT or symbol==arcade.key.D:
           self.me.change_x = 1
       elif symbol ==arcade.key.DOWN:
           self.me.change_x = 0
        
       elif symbol ==arcade.key.SPACE:
           self.me.fire()

    def on_key_release(self, symbol: int, modifiers: int):
        self.me.change_x = 0

    #show
    def on_draw(self):
        arcade.start_render()

        self.me.draw()

        arcade.draw_lrwh_rectangle_textured(0, 0, 1000, 600, self.background)
        arcade.draw_text(f"score: {self.score}", 850, 50, arcade.color.WHITE, 20)

        for enemy in self.enemy_list:
           enemy.draw()
        
        for bullet in self.me.bullet_list:
            bullet.draw()

        for heart in self.heart_list:
            heart.draw()
        
        if len(self.heart_list) <= 0:
            arcade.draw_lrtb_rectangle_filled(0, 1000, 600, 0, arcade.color.BLACK)
            arcade.draw_text("GAME OVER!", 600,500, arcade.color.WHITE)
            arcade.draw_text(f"Score: {self.score}", 440,250,arcade.color.WHITE,20)
            self.me.center_x = -1
            self.me.center_y = -1


        arcade.finish_render()

    #منطق
    #function which automatically execute!
    def on_update(self, delta_time: float):
       self.elapsed_time +=1  #update elapsed time
       
       #increase enemy speed every 10 seconds
       if self.elapsed_time >= 10:
          for enemy in self.enemy_list:
              enemy.speed +=0.3 
          self.elapsed_time == 0  #reset elapsed time

       
       for enemy in self.enemy_list:
           if arcade.check_for_collision(self.me, enemy):
                 print("game over!")
                 exit(0)

        
       for enemy in self.enemy_list:
           for bullet in self.me.bullet_list:
               if arcade.check_for_collision(enemy, bullet):
                   self.explosion_sound.play()
                   self.enemy_list.remove(enemy)
                   self.score += 1
                   self.me.bullet_list.remove(bullet)

                
        
       self.me.move()

       for enemy in self.enemy_list:
          enemy.move()

       for bullet in self.me.bullet_list:
           bullet.move()

       for enemy in self.enemy_list:
           if enemy.center_y <0:
               self.enemy_list.remove(enemy)
               if len(self.heart_list) > 0:
                   self.heart_list.pop(-1)


       if random.randint(1, 100) == 6:
           self.new_enemy = Enemy(self.width, self.height)
           self.enemy_list.append(self.new_enemy)
    
    
window = Game()
arcade.run()