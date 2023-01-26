import arcade

class Torpedo:
    def __init__(self, x_init, y_init):
        self.center_x = x_init
        self.center_y = y_init
        self.size = 20
    def update(self):
        self.center_y += 15
    def display(self):
        arcade.draw_ellipse_filled(self.center_x, self.center_y, self.size, self.size,
        arcade.color.WHITE)