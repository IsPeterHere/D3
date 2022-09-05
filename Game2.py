import D3_Eng as d3
import D3_Dynamics as d3d
import random
from math import cos,radians,degrees

class Tools:
    def player_load(self,x,y,z):
        self.body = d3.Cuboid([x+0,y+0,z+44],[20,10,34])
        self.body.colour = "red"
        self.solids.add(self.body)
        self.leg  = d3.Cuboid([x+10,y+0,z+0],[5,5,44])
        self.leg.colour = "red"
        self.solids.add(self.leg)
        self.leg2  = d3.Cuboid([x+-10,y+0,z+0],[5,5,44])
        self.leg2.colour = "red"
        self.solids.add(self.leg2)
        self.arm  = d3.Cuboid([x+15,y+0,z+40],[5,5,44])
        self.arm.colour = "red"
        self.solids.add(self.arm)
        self.arm2  = d3.Cuboid([x+-15,y+0,z+40],[5,5,44])
        self.arm2.colour = "red"
        self.solids.add(self.arm2)
        self.head = d3.Cuboid([x+0,y+0,z+70],[15,15,15])
        self.head.colour = "red"
        self.solids.add(self.head)

        self.Move_group.cuboid_group = self.player_shell
        
        self.limbs = [self.body,self.arm,self.arm2,self.leg,self.leg2,self.head]
        
    def player_forward(self,x,y,z):
        
        self.leg.centre([10,0,44])
        
        self.leg2.centre([-10,0,44])
        
        self.arm.centre([15,0,44])
        
        self.arm2.centre([-15,0,44])

    def player_side(self,x,y,z):
        self.leg.centre([0,10,44])
        
        self.leg2.centre([0,-10,44])
        
        self.arm.centre([0,15,44])
        
        self.arm2.centre([0,-15,44])

    def less_limb(self,window):
        if len(self.limbs) > 0:
            less = random.choice(self.limbs)
            while True:

                if less == self.head and len(self.limbs) > 1:
                    less = random.choice(self.limbs)
                else:
                    if less == self.body and len(self.limbs) > 2:
                        less = random.choice(self.limbs)
                    else:
                        break
    
            group = d3.Cuboid_group([0,0,0])
            group.add(less)
            group.id = self.limbs.index(less)
            window.add(group)
            self.limbs.remove(less)
            self.player_shell.remove(less)
            self.solids.add(less)
            self.lost_limbs.append(d3d.Dynamic(group,self.solids))

    def load(self,window):
        window.remove(self.player_shell)
        self.player_shell.cuboids = []
        
        for i in self.limbs:
            self.player_shell.add(i)

        window.add(self.player_shell)
        
    def move(self,window):
        self.Move_group.call(z = -2)
                
        if "w" in window.inputs:
            self.player_forward(self.player_shell.centre[0],self.player_shell.centre[1],self.player_shell.centre[2])
            self.Move_group.y_speed = 4
        
        elif "s" in window.inputs:
            self.player_forward(self.player_shell.centre[0],self.player_shell.centre[1],self.player_shell.centre[2])
            self.Move_group.y_speed = -4
            
        if "a" in window.inputs:
            self.player_side(self.player_shell.centre[0],self.player_shell.centre[1],self.player_shell.centre[2])
            self.Move_group.x_speed = 4
            
        elif "d" in window.inputs:
            self.player_side(self.player_shell.centre[0],self.player_shell.centre[1],self.player_shell.centre[2])
            self.Move_group.x_speed = -4

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
                self.less_limb(window)
                self.Move_group.z_speed = 20
                self.jump = False

        if self.player_shell.centre[2] < -700 :
            self.Move_group.z_speed = -5
            self.less_limb(window)
            if self.player_shell.centre[2] < -730:
                self.state_change = True
                self.lost_limbs = []
                self.sate = 0
                
        self.load(window)
        for i in self.lost_limbs:
            i.call(z = -random.randint(1,3))
        
class Game(Tools):

    def __init__(self):
        self.state = 0
        self.state_change = True
        self.jump = False
        self.lost_limbs = []

    

        
    def start(self):
        w = d3.Window(400,400)
        w.log_inputs = ['w','s','a','d']

        w.start(self.main)


    
    def main(self,window):
        if self.state_change == True:
            if self.state == 0:
                window.clear()
                self.save_cords = [0,0,0]
                self.solids = d3.Cuboid_group([0,0,0])
                self.player_shell = d3.Cuboid_group([0,0,0])
                self.Move_group = d3d.Dynamic(self.player_shell,self.solids)

                self.player_load(0,0,0)
                self.player_shell.centre = [0,0,0]

                self.player_forward(0,0,0)
                window.add(self.player_shell)

                c = d3.Cuboid([0,0,-50],[40,40,40])
                c.colour = "green"
                window.add(c)
                self.solids.add(c)
                
                c = d3.Cuboid([0,88,-50],[40,40,40])
                c.colour = "green"
                window.add(c)
                self.solids.add(c)
                
                self.win = d3.Cuboid([-98,88,-50],[40,40,40])
                self.win.colour = "red"
                window.add(self.win)
                self.solids.add(self.win)
                
                window.vertical_rotation = 195
                window.horizontal_rotation = 250

                self.state_change = False

            elif self.state == 1:
                window.clear()
                window.add(self.player_shell)

                self.solids = d3.Cuboid_group([0,0,0]) 

                c = d3.Cuboid([-98,88,-50],[40,40,40])
                c.colour = "gold"
                window.add(c)
                self.solids.add(c)
                
                c = d3.Cuboid([-180,88,-90],[40,40,40])
                c.colour = "green"
                window.add(c)
                self.solids.add(c)

                c = d3.Cuboid([-180,200,-90],[40,40,40])
                c.colour = "green"
                window.add(c)
                self.solids.add(c)
                
                self.win = d3.Cuboid([-240,300,-90],[40,40,40])
                self.win.colour = "red"
                window.add(self.win)
                self.solids.add(self.win)
                
                window.vertical_rotation = 195
                window.horizontal_rotation = 250

                self.state_change = False
                
        else:

            if self.state == 0:
                
                window.horizontal_rotation = 160-degrees(cos(radians(self.player_shell.centre[1]/2)))/6
                window.vertical_rotation = 175+degrees(cos(radians(self.player_shell.centre[2]/4)))/2
                window.centre(self.player_shell.centre)

                self.move(window)

                if len(self.player_shell.cuboids) == 0:
                    self.state_change = True
                    self.lost_limbs = []

                self.player_shell.move(z=-1)
                if self.player_shell.touching(self.win):
                    self.state_change = True
                    self.state = 1
                    self.lost_limbs = []
                    self.player_shell.move(z=1)
                    self.save_cords = self.player_shell.centre
                else:
                    self.jump = False
                    self.player_shell.move(z=1)

            elif self.state == 1:
                
                window.horizontal_rotation = 160-degrees(cos(radians(self.player_shell.centre[1]/2)))/6
                window.vertical_rotation = 175+degrees(cos(radians(self.player_shell.centre[2]/4)))/2
                window.centre(self.player_shell.centre)

                self.move(window)

                if len(self.player_shell.cuboids) == 0:
                    self.state_change = True
                    self.lost_limbs = []

                self.player_shell.move(z=-1)
                if self.player_shell.touching(self.win):
                    self.state_change = True
                    self.state = 1
                    self.lost_limbs = []
                    self.player_shell.move(z=1)
                    self.save_cords = self.player_shell.centre
                else:
                    self.jump = False
                    self.player_shell.move(z=1)



            
            
                

game = Game()
game.start()
