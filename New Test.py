import D3_Eng as d3
import random
from math import cos,radians,degrees
import time


class Game:

    def __init__(self):

        self.hr = 160
        self.vr = 210


    def move(self,window):
                
        if "s" in window.inputs:
            self.vr += -4
        
        elif "w" in window.inputs:
            self.vr += 4
            
        if "a" in window.inputs:
            self.hr += 4
            
        elif "d" in window.inputs:
            self.hr += -4

        if "q" in window.inputs:
            print(window.true_time)

            

        
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
        

        self.mapsize = 25
        self.blocks = []
        for x in range(self.mapsize):
            self.blocks.append([])
            for y in range(self.mapsize):
                c = d3.Cuboid([x*80,y*80,0],[40,40,40])
                c.colour = "green"
                window.add(c)

                self.blocks[x].append(c)
        

    def main(self,window):
        window.horizontal_rotation = self.hr
        window.vertical_rotation = self.vr
        self.move(window)

        for e in self.blocks:
            self.count += 0.01
            for i in e:
                self.count += -0.01
                i.move(z = 50*cos(self.count))

game = Game()
game.start()
