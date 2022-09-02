import D3_Eng as d3
import D3_Dynamics as d3d
import random
from math import cos,radians,degrees

class Game:

    def __init__(self):
        body = d3.Cuboid([2,-60,40],[10,10,10])
        body.colour = "red"
        leg  = d3.Cuboid([2,-60,30],[5,5,10])
        leg.colour = "red"

        self.last_mark = -1
        self.solids = d3.Cuboid_group([0,0,0])
        self.old_solids = d3.Cuboid_group([0,0,0])
        self.colour = "green"
        self.g_y = 0
        self.jump = False
        self.last_pos = [0,0,0]


        self.player_shell = d3.Cuboid_group([0,0,40])
        self.player_shell.add(body)
        self.player_shell.add(leg)
        
    def start(self):
        w = d3.Window(400,400)
        w.log_inputs = ['w','s','a','d']

        w.add(self.player_shell)

        self.Move_group = d3d.Dynamic(self.player_shell,self.solids)

        w.vertical_rotation = 195
        w.horizontal_rotation = 250

        w.start(self.main)

    def load_new(self,window):
        new_solids = d3.Cuboid_group([0,0,0])
    
        for i in range(20):
            size = random.randint(5,60)
            c = d3.Cuboid([0,self.last_mark*60+60*i,-30+self.g_y*50],[size,size,size])
            c.colour = self.colour
            new_solids.add(c)

        return new_solids
    
    def main(self,window):
        #d3.mouse_direction(window)
        window.horizontal_rotation = 270-degrees(cos(radians(self.player_shell.centre[1]/4)))/2
        window.vertical_rotation = 155+degrees(cos(radians(self.player_shell.centre[2]/4)))
        
        if self.player_shell.centre[1] > (self.last_mark-5)*60:
            old_solids = self.solids
            self.solids = self.load_new(window)
            window.clear()
            
            for i in old_solids.cuboids[-6:]:
                self.solids.cuboids.insert(0,i)
                
            self.Move_group.solid_group = self.solids
            window.add(self.solids)
            window.add(self.player_shell)
            window.add(old_solids)
            self.last_mark += 20

            if random.randint(1,1) == 1:
                self.g_y += 1
                self.colour = random.choice(['green','yellow','pink','brown'])
        
        
        self.Move_group.call(z = -2)

        window.centre(self.player_shell.centre)

        if self.jump == False:
            self.player_shell.move(z=-1)
            if self.player_shell.touching(self.solids):
                self.jump = True
                self.last_pos = self.player_shell.centre.copy()
                self.player_shell.move(z=1)
            else:
                self.jump = False
                self.player_shell.move(z=1)
    
        if "w" in window.inputs:
            self.Move_group.y_speed = 4
        elif "s" in window.inputs:
            self.Move_group.y_speed = -4

        if self.jump == True:
            if " " in window.inputs:
                self.Move_group.z_speed = 20
                self.jump = False

        if self.player_shell.centre[2] < -600 :
            self.Move_group.z_speed = -5
            if self.player_shell.centre[2] < -730:
                self.player_shell.set_pos(self.last_pos)

game = Game()
game.start()
