import arcade

class Obstacle:
    def __init__(self, x_init, y_init, color):
        self.color = color
        self.center_x = x_init
        self.center_y = y_init
        self.size = 25
    def display(self):
        arcade.draw_ellipse_filled(self.center_x, self.center_y, self.size, self.size, self.color)
    