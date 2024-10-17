import D3_Eng as d3
import D3_Dynamics as d3d
import random
from math import cos,radians,degrees

import cProfile
import pstats
class Game:

    def __init__(self):
        self.body = d3.Cuboid([2,-60,40],[10,10,10])
        self.body.colour = "red"
        self.leg  = d3.Cuboid([2,-60,30],[5,5,10])
        self.leg.colour = "red"

        self.last_mark = -1
        self.solids = d3.Cuboid_group([0,0,0])
        self.old_solids = d3.Cuboid_group([0,0,0])
        self.colour = "green"
        self.g_y = 0
        self.jump = True
        self.b_jump = True
        self.last_pos = [0,0,0]
        self.min = 5
        self.max = 60


        self.player_shell = d3.Cuboid_group([0,0,40])
        self.player_shell.add(self.body)
        self.player_shell.add(self.leg)
        
    def start(self):
        w = d3.Window(400,400)
        w.log_inputs = ['w','s','a','d']

        w.add(self.player_shell)

        self.Move_group = d3d.Dynamic(self.player_shell,self.solids)

        w.vertical_rotation = 195
        w.horizontal_rotation = 250

        c = d3.Cuboid([0,0,-30],[40,40,40])
        c.colour = "gold"
        self.old_solids.add(c)
        
        w.start(self.main)

    def load_new(self,window):
        new_solids = d3.Cuboid_group([0,0,0])
    
        for i in range(20):
            size = random.randint(self.min,self.max)
            c = d3.Cuboid([0,self.last_mark*60+60*i+(random.randint(-22,10)),-30+self.g_y*42],[size,size,size])
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
            
            for i in old_solids.cuboids[-8:]:
                self.solids.cuboids.insert(0,i)
                
            self.Move_group.solid_group = self.solids
            window.add(self.solids)
            window.add(self.player_shell)
            window.add(old_solids)
            self.last_mark += 20

            i = random.randint(1,2)
            if i == 1:
                self.g_y += 0.5
                self.min = random.randint(3,11)
                self.max = random.randint(4,53)
                while self.max < self.min:
                    self.max = random.randint(4,60)
                self.colour = random.choice(['green','yellow','pink','brown'])
            elif i == 2:
                self.min = random.randint(3,44)
                self.max = random.randint(4,53)
                while self.max < self.min:
                    self.max = random.randint(4,60)
                self.g_y += -0.5
                self.colour = random.choice(['green','yellow','pink','brown'])

            self.g_y = min(8,max(-8,self.g_y))
            
        self.Move_group.call(z = -2)

        window.centre(self.player_shell.centre)

        if self.jump == False:
            self.player_shell.move(z=-1)
            if self.player_shell.touching(self.solids):
                self.body.colour = "red"
                self.leg.colour = "red"
                self.jump = True
                self.last_pos = self.player_shell.centre.copy()
                self.player_shell.move(z=1)
            else:
                self.jump = False
                self.player_shell.move(z=1)

        self.b_jump = False
        self.body.move(z=-1)
        if self.solids.touching(self.body):
            self.b_jump = True
            self.body.move(z=1)
        else:
            self.b_jump = False
            self.body.move(z=1)
    
        if "w" in window.inputs:
            self.Move_group.y_speed = 4
        elif "s" in window.inputs:
            self.Move_group.y_speed = -4
            
        if self.b_jump == True:
            if " " in window.inputs:
                self.body.colour = "gold"
                self.Move_group.z_speed = 30
                self.b_jump = False
                self.jump = False
        else:
            if self.jump == True:
                if " " in window.inputs:
                    self.leg.colour = "gold"
                    self.Move_group.z_speed = 20
                    self.jump = False

        if self.player_shell.centre[2] < -600 :
            self.Move_group.z_speed = -5
            if self.player_shell.centre[2] < -730:
                self.player_shell.set_pos(self.last_pos)

game = Game()
with cProfile.Profile() as pr:
    game.start()

stats = pstats.Stats(pr)
stats.sort_stats(pstats.SortKey.TIME)
stats.print_stats()

