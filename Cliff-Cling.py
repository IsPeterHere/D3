import Engine as d3
import Dynamics as d3d
import random

class The_Wall:
    def __init__(self,window):
        self.wall = d3.Entity([0,0])
        window.add(self.wall)

    def load(self,level):
        for x in range(10):
            for y in range(10):
                cuboid = d3.Cuboid([x*40,y*40,0],[40,40,40])
                cuboid.colour = "grey"
                self.wall.add(cuboid)
class Player:
    def __init__(self,window):
        center = [0,0,80]
        self.player = d3.Entity(center)
        window.add(self.player)

        self.body = d3.Cuboid(center,[30,10,60])
        self.body.colour = "red"
        self.player.add(self.body)


        
class Game:

    def __init__(self):
        self.window = d3.Window(400,400,"Cliff-cling")
        self.window.log_inputs = ['w','s','a','d']

    def start(self):
        self.restart = True
        self.window.start(self.frame_function)

    def set_up(self):
        self.wall = The_Wall(self.window)
        self.wall.load(1)

        self.player = Player(self.window)
        
        self.restart = False
        
    def frame_function(self,window):
        if self.restart is True:
            self.set_up()
        else:
            window.centre(self.player.player.centre)
            d3.mouse_direction(window)

Game().start()
