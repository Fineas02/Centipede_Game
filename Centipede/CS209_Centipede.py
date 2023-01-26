import arcade
from math import sqrt
from random import uniform
from Obstacle import Obstacle
from Torpedo import Torpedo
from centipede import Centipede
from elipse import Elipse



def dist_circle(d, c):
    return sqrt((c.center_x-d.center_x)**2 + (c.center_y-d.center_y)**2)                

class Main(arcade.Window):
# constructor
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        self.elipse = Elipse(100, 50, 30)
        self.moving_left = False
        self.moving_right = False 
        self.hit = False
        self.score = 0
        self.torpedo_list = []
        self.obstacle_list = []
        self.centipede_list = []
        
        while len(self.obstacle_list) < 25:
            self.obstacle_list.append(Obstacle(uniform(100, 950), uniform(150, 430), arcade.color.YELLOW))

        while len(self.centipede_list) < 8:
            self.centipede_list.append(Centipede(100 + (len(self.centipede_list) * 20), height-30, arcade.color.BABY_BLUE, 4, 4))

   #delete torpedo from list after it exits the screen 
    def delete_torpedo(self):
        for r in range(len(self.torpedo_list)-1, -1, -1):
            h = self.torpedo_list[r]
            if h.center_y > arcade.window.height + (h.size/2):
                del self.torpedo_list[r]

    def check_hit(self):
        i = 0
        while i < len(self.torpedo_list):
            j = 0
            hit = False
            while j < len(self.obstacle_list) and not hit:
                torp = self.torpedo_list[i]
                obst = self.obstacle_list[j]
                dist = dist_circle(torp, obst)
                if dist < (torp.size/2) + (obst.size/2):
                    hit = True
                    del self.torpedo_list[i]
                    del self.obstacle_list[j]
                    self.score+=1
                else:
                    j += 1
            if not hit:
                i += 1

    # hit btn elipse and centipede
    def check_hit_elipse_and_centipede(self):
        j = 0
        hit = False
        while j < len(self.centipede_list) and not hit:
            torp = self.centipede_list[j]
            obst = self.elipse
            dist = dist_circle(torp, obst)
            if dist < (torp.size/2) + (obst.size/2):
                hit = True
                self.hit = True
                break
            else:
                j += 1
        if self.hit == True: 
            arcade.draw_text('You Lose!', 400, 200, arcade.color.BABY_BLUE_EYES, 40, 80)
            self.moving_left = False
            self.moving_right = False
            self.torpedo_list = []
            self.centipede_list = []

    # hit between centipede and obstacle
    def check_hit_centipede(self):
        i = 0
        while i < len(self.torpedo_list):
            j = 0
            hit = False
            while j < len(self.centipede_list) and not hit:
                torp = self.torpedo_list[i]
                obst = self.centipede_list[j]
                dist = dist_circle(torp, obst)
                if dist < (torp.size/2) + (obst.size/2):
                    hit = True
                    del self.torpedo_list[i]
                    del self.centipede_list[j]
                    self.obstacle_list.append(Obstacle(obst.center_x, obst.center_y, arcade.color.AFRICAN_VIOLET))
                    self.score+=1
                else:
                    j += 1
            if not hit: 
                i += 1

    #centipede bounce off obstacle
    def bounce(self):
        i = 0
        while i < len(self.centipede_list):
            j = 0
            hit = False
            while j < len(self.obstacle_list) and not hit:
                torp = self.centipede_list[i]
                obst = self.obstacle_list[j]
                dist = dist_circle(torp, obst)
                if dist < (torp.size/2) + (obst.size/2):
                    hit = True
                    torp.x_dir *= -1
                    torp.center_y -= 25
                else:
                    j += 1
            if not hit:
                i += 1

    def on_draw(self):
        self.clear()

        #display centipede
        for centipede in self.centipede_list:
            centipede.display()
            centipede.update()
            if centipede.center_x > 1000:
                centipede.x_dir *= -1
                centipede.center_y -= 25
            if centipede.center_x < 0:
                centipede.x_dir *= -1
                centipede.center_y -= 25
                
        self.elipse.display()
        self.check_hit_elipse_and_centipede()
        self.delete_torpedo()
        self.check_hit()
        self.bounce()
        self.check_hit_centipede()
        self.win_game()

        arcade.draw_text('Your Score:' + str(self.score), 100, 450, arcade.color.RED,20,40)
        
        if self.moving_left:
            self.elipse.center_x -= 4
        elif self.moving_right:
            self.elipse.center_x += 4
        for torpedo in self.torpedo_list:
            torpedo.update()
            torpedo.display()
        for obstacle in self.obstacle_list:
            obstacle.display()
        
    

       # del self.torpedo_list[3]
    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.LEFT:
            self.moving_left = True
        elif symbol == arcade.key.RIGHT:
            self.moving_right = True
        elif symbol == arcade.key.SPACE:
            self.torpedo_list.append(Torpedo(self.elipse.center_x, self.elipse.center_y))
    def on_key_release(self, symbol: int, modifiers: int):
        if symbol == arcade.key.LEFT:
            self.moving_left = False
        elif symbol == arcade.key.RIGHT:
            self.moving_right = False
    

    def win_game(self):
        if len(self.centipede_list) == 0 and self.hit == False:
            arcade.draw_text('You Win!!', 400, 200, arcade.color.GREEN, 40, 80)
            self.moving_left = False
            self.moving_right = False
            self.torpedo_list = []
            self.centipede_list = []
        
# constructs an object of type Main
arcade.window = Main(1000, 500, 'Centipede')
arcade.run()