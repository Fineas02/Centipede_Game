from Obstacle import Obstacle

class Centipede(Obstacle):
    def __init__(self, x_init, y_init, color, x_dir, y_dir):
        super().__init__(x_init, y_init, color)
        self.x_dir = x_dir
        self.y_dir = y_dir
    def update(self):
        self.center_x += self.x_dir


    