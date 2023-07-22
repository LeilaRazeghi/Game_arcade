import arcade

COLUMN_SPACING = 20
ROW_SPACING = 20
LEFT_MARGIN = 100
BOTTOM_MARGIN = 100

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400
BLUE = arcade.color.BLUE
RED = arcade.color.RED


arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "complex_loops_box")

arcade.set_background_color(arcade.color.WHITE)

arcade.start_render()

for row in range(12):
    for column in range(12):
         x= column * COLUMN_SPACING + LEFT_MARGIN
         y= row * ROW_SPACING + BOTTOM_MARGIN

         if row % 2 ==0 and column % 2==0 or row % 2 !=0 and column % 2 !=0:
              arcade.draw_rectangle_filled(x, y, 10, 10, BLUE, 45)
         else:
              arcade.draw_rectangle_filled(x, y, 10, 10, RED, 45)

arcade.finish_render()

arcade.run()

