from math import *

def Return_z(c):
        return c.z

def GetFaces(extent,centre):

    origion = [centre[0]-extent[0]/2,centre[1]-extent[1]/2,centre[2]-extent[2]/2]
    polygons = []
        
    Pos = [0,1,2]
    for Constant in range(3):

        for flip in range(2):
                
            polygons.append([[origion[0],origion[1],origion[2]],
                            [origion[0],origion[1],origion[2]],
                            [origion[0],origion[1],origion[2]],
                            [origion[0],origion[1],origion[2]]])
            half = True
            for Count in range(3):
                
                if Count == Constant:

                        if flip == 1:

                            for x in range(4):
                                polygons[-1][x][Constant] +=  extent[Constant]
                        
                else:
                    if half:
                        for x in range(2):
                            polygons[-1][x][Count] += extent[Count]

                        half = False

                    else:
                        polygons[-1][0][Count] += extent[Count]
                        polygons[-1][3][Count] += extent[Count]
                            
    return polygons

class Bindings:

    def handle_keypress(self,event):
        if event.char in self.log_inputs and event.char not in self.monitored_current:
            self.monitored_current.append(event.char)
            
        self.inputs.append(event.char)

    def handle_up(self,event):
        if event.keysym in self.log_inputs:
            try:
                self.monitored_current.remove(event.keysym)
            except:
                print("KeyUp Error")

    def MousePosition(self,pos):
        x = max(0,min(self.window.winfo_width()-1,pos.x))
        y = max(0,min(self.height-1,pos.y))
        
        self.mouse_current_position = [int(x),int(y)]

    def Left_pressed(self,i):
        self.l_is_pressed = True    


class Cart_maths:

    def __init__(self):
        pass


    def update(self,window):
        self.height = window.height
        self.width = window.width
        
        self.a2 = radians(window.vertical_rotation)
        self.a1 = radians(window.horizontal_rotation)

        self.cos_a2 = cos(self.a2)
        self.sin_a2 = sin(self.a2)

        self.d = window.distance
        self.render_depth = window.render_depth

        self.window_x = window.x
        self.window_y = window.y
        self.window_z = window.z

    def d2_cord(self,cord):

        d2_cord = self.cart(cord)

        if d2_cord[0] == "Q":
            return "Q","Q"

        x = int(d2_cord[0]+self.width/2)
        y = int(d2_cord[1]+self.height/2)
        
        return x,y
        
        
    def Z(s,o,r,h,):
        return (s.cos_a2*r*sin(s.a1+o))-(s.sin_a2*h)

    def Circle(s,o,r,h):

        z = s.Z(o,r,h)

        if s.d-z <= 0 or z <-s.render_depth:
            return ["Q","Q","Q"]

        x = (s.d/(s.d-z))*r*cos(s.a1+o)

        y = (s.d/(s.d-z))*((r*s.sin_a2*sin(s.a1+o))+h*s.cos_a2)

        if x > s.width/1.5 or x< -s.width/1.5 or y > s.height/1.5 or y< -s.height/1.5:
            return ["Q","Q","Q"]
        
        return [x,y,z]

    def cart(self,cord):
        x = cord[0] + self.window_x
        y = cord[1] + self.window_y
        z = cord[2] + self.window_z
        return self.Circle(atan2(radians(y),radians(x)),sqrt(x**2+y**2),z)
