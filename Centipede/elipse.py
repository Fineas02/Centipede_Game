import arcade

class Elipse:
    def __init__(self, center_x, center_y, size):
        self.center_x = center_x
        self.center_y = center_y
        self.size = size
    def display(self):
        arcade.draw_ellipse_filled(self.center_x, self.center_y, self.size, self.size, arcade.color.BLUE_SAPPHIRE)
    