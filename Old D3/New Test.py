import D3_Eng as d3
import random
from math import cos,radians,degrees
import time


class Game:

    def __init__(self):

        self.hr = 160
        self.vr = 210
        self.past = 3000
        self.wave_toggle = False

        col_file = open("hex_colours.txt","r")
        self.col_arr = col_file.read().split("\n")
        col_file.close()
    
    def get_hex(self,x,y):
        r = int(255-((x-self.mapsize[0]/2)*255/self.mapsize[0])-((y-self.mapsize[1]/2)*255/self.mapsize[1]))
        g = 255
        b = 255
        
        if x > (self.mapsize[0]/2) and y < (self.mapsize[1]/2):
            b = 255
            r = int(255-((x-self.mapsize[0]/2)*255/self.mapsize[0])*2)
        elif x < (self.mapsize[0]/2):
            r = 255
            b = int(x*255/self.mapsize[0])*2

        if y > (self.mapsize[1]/2) and x < (self.mapsize[0]/2):
            g = 255
            r = int(255-((y-self.mapsize[1]/2)*255/self.mapsize[1])*2)
        elif y < (self.mapsize[1]/2):
            if x < (self.mapsize[0]/2):
                r = 255
            g = int(y*255/self.mapsize[1])*2

        r = min(255,max(0,r))
        g = min(255,max(0,g))
        b = min(255,max(0,b))
        
        return f"#{r:02x}{g:02x}{b:02x}"

    def move(self,window):
        window.render_depth = 300000
                
        if "s" in window.inputs:
            self.vr += -4
        
        elif "w" in window.inputs:
            self.vr += 4
            
        if "a" in window.inputs:
            self.hr += 4
            
        elif "d" in window.inputs:
            self.hr += -4
        elif " " in window.inputs:
            window.z += 40

        if "q" in window.inputs:
            print(window.true_time)
        if "e" in window.inputs:
            print(window.render_depth)
        
        if "t" in window.inputs:
            if self.wave_toggle == True:
                self.wave_toggle = False
            else:
                self.wave_toggle = True
        
        """
        if window.true_time > 0:
            window.render_depth -= (window.true_time**2)-window.true_time/1.5
        else:
            window.render_depth += (window.true_time**2)-window.true_time/1.5
        if window.render_depth > 3000:
            window.render_depth = 3000
        elif window.render_depth < 20:
            window.render_depth = self.past
        self.past = window.render_depth
        """
        
        
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
        

        self.mapsize = [25,25]
        self.blocks = []
        for x in range(self.mapsize[0]):
            self.blocks.append([])
            for y in range(self.mapsize[1]):
                c = d3.Cuboid([x*80,y*80,0],[40,40,40])
                c.colour = self.get_hex(x,y)
                window.add(c)

                self.blocks[x].append(c)
        

    def main(self,window):
        window.horizontal_rotation = self.hr
        window.vertical_rotation = self.vr
        self.move(window)

        if self.wave_toggle == True:
            for e in self.blocks:
             self.count += 0.01
             for i in e:
                self.count += -0.01
                i.move(z = 50*cos(self.count))
        

game = Game()
game.start()
