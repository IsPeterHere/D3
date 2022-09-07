import D3_Eng as d3
import D3_Dynamics as d3d
import random
from math import cos,radians,degrees

class Tools:
    def player_load(self,x,y,z):

        self.body = d3.Cuboid([x,y,y],[10,10,10])
        self.body.colour = "red"
        self.leg  = d3.Cuboid([x,y,y-10],[5,5,10])
        self.leg.colour = "red"

        self.player_shell.add(self.body)
        self.player_shell.add(self.leg)

        self.Move_group.cuboid_group = self.player_shell

        
    def move(self,window):
        self.Move_group.call(z = -2)
                
        if "s" in window.inputs:
            self.Move_group.y_speed = 4
            self.direction = False
        
        elif "w" in window.inputs:
            self.Move_group.y_speed = -4
            self.direction = False
            
        if "a" in window.inputs:
            self.Move_group.x_speed = 4
            self.direction = True
            
        elif "d" in window.inputs:
            self.Move_group.x_speed = -4
            self.direction = True

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
            
class Game(Tools):

    def __init__(self):

        self.hr = 160
        self.vr = 210

        self.direction = False
        self.jump = False

    

        
    def start(self):
        window = d3.Window(400,400)
        window.log_inputs = ['w','s','a','d']

        self.Set(window)

        window.start(self.main)

    def Set(self,window):

        window.clear()
        
        self.solids = d3.Cuboid_group([0,0,0])
        self.player_shell = d3.Cuboid_group([0,0,0])
        self.Move_group = d3d.Dynamic(self.player_shell,self.solids)

        self.player_load(0,0,0)
        self.player_shell.centre = [0,0,0]

        window.add(self.player_shell)

        self.mapsize = 10
        self.blocks = []
        for x in range(self.mapsize):
            self.blocks.append([])
            for y in range(self.mapsize):
                c = d3.Cuboid([x*80,y*80,-x*y],[40,40,40])
                c.colour = "green"
                window.add(c)
                self.solids.add(c)

                self.blocks[x].append(c)
        

    def main(self,window):
        if self.direction == False:
            if self.hr != 160:
                if self.hr > 160:
                    self.hr += -1
                else:
                    self.hr += 1
        else:
            if self.hr != 130:
                if self.hr > 130:
                    self.hr += -1
                else:
                    self.hr += 1

        
        window.horizontal_rotation = self.hr-degrees(cos(radians(self.player_shell.centre[1]/2)))/6
        window.vertical_rotation = self.vr
        window.centre(self.player_shell.centre)

        
        for x in range(10):
            block = self.blocks[random.randint(0,self.mapsize-1)][random.randint(0,self.mapsize-1)]

            block.move(z=1)
            if self.player_shell.touching(block):
                block.colour = "yellow"
                block.move(z=-1)
            else:
                if block.colour == "yellow":
                    block.colour = "green"
                else:
                    block.move(z = random.randint(1,15))
                    block.move(z=-1)
        
        avg = 0
        leng = 0
        for i in self.blocks:
            for e in i:
                avg += e.centre()[2]
                leng +=1
        avg = (avg/leng) - 35

        for i in self.blocks:
            for e in i:
                if e.centre()[2] > avg:
                    if e.colour != "yellow":
                        e.colour = "green"
                else:
                    e.colour = "red"
                    
        if self.player_shell.centre[2] < -700 :
            self.Set(window)
                
        self.move(window)


            
                
game = Game()
game.start()
