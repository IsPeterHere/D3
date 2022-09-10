import D3_Eng as d3
import D3_Dynamics as d3d
import random
from math import cos,radians,degrees
import time
class Tools:

    def player_load(self,x,y,z):
        self.player_shell = d3.Cuboid_group([0,0,0])
        self.Move_group = d3d.Dynamic(self.player_shell,self.solids)

        self.body = d3.Cuboid([x,y,y],[10,10,10])
        self.body.colour = "red"
        self.leg  = d3.Cuboid([x,y,y-10],[5,5,10])
        self.leg.colour = "red"

        self.player_shell.add(self.body)
        self.player_shell.add(self.leg)

        self.Move_group.cuboid_group = self.player_shell

    def move(self,window):
        self.Move_group.call(z = -2)

        if "A" in window.inputs:
            self.vr += -4
        
        elif "W" in window.inputs:
            self.vr += 4
            
        if "A" in window.inputs:
            self.hr += 4
            
        elif "D" in window.inputs:
            self.hr += -4

        if "q" in window.inputs:
            print(window.true_time)
                
        if "s" in window.inputs:
            self.Move_group.y_speed = 4
            self.direction = 120
        
        elif "w" in window.inputs:
            self.Move_group.y_speed = -4
            self.direction = 160
            
        if "a" in window.inputs:
            self.Move_group.x_speed = 4
            self.direction = 135
            
        elif "d" in window.inputs:
            self.Move_group.x_speed = -4
            self.direction = 230

        if self.jump == False:
            self.player_shell.move(z=-1)
            if self.player_shell.touching(self.solids):
                self.jump = True
                self.player_shell.move(z=1)
            else:
                self.jump = False
                self.player_shell.move(z=1)
                
         
        if self.jump ==  True:
            if " " in window.inputs: 
                self.Move_group.z_speed = 25
                self.jump = False

    def tunnel(self,window):
        self.mapsize = 5
        self.blocks = []
        for x in range(self.mapsize):
            self.blocks.append([])
            for y in range(self.mapsize):
                c = d3.Cuboid([x*40,y*40,0],[40,40,40])
                c.colour = "green"
                self.solids.add(c)
                window.add(c)
                self.blocks[x].append(c)

        for x in range(self.mapsize):
            self.blocks.append([])
            for y in range(self.mapsize):
                c = d3.Cuboid([x*40,y*40,200],[40,40,40])
                c.colour = "green"
                self.solids.add(c)
                window.add(c)
                self.blocks[x].append(c)
                
        for x in range(self.mapsize):
            self.blocks.append([])
            for y in range(self.mapsize-1):
                c = d3.Cuboid([x*40,0,40+y*40],[40,40,40])
                c.colour = "red"
                self.solids.add(c)
                window.add(c)
                self.blocks[x].append(c)

        for x in range(self.mapsize):
            self.blocks.append([])
            for y in range(self.mapsize-1):
                c = d3.Cuboid([x*40,160,40+y*40],[40,40,40])
                c.colour = "red"
                self.solids.add(c)
                window.add(c)
                self.blocks[x].append(c)

class Game(Tools):

    def __init__(self):

        self.hr = 160
        self.vr = 210

        self.jump = False
        
    def start(self):
        window = d3.Window(400,400)
        window.log_inputs = ['w','s','a','d']

        self.Set(window)

        window.start(self.main)

    def Set(self,window):

        window.clear()
    
        self.count = 0
        
        self.hr = 160
        self.vr = 210

        self.solids = d3.Cuboid_group([0,0,0])
        
        self.player_load(0,0,0)

        window.add(self.player_shell)

        self.tunnel(window)
        
        

    def main(self,window):
        window.horizontal_rotation = self.hr
        window.vertical_rotation = self.vr
        window.centre(self.player_shell.centre)
        self.move(window)

game = Game()
game.start()
