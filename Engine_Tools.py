from math import radians,sqrt,cos,sin,atan2

def Return_depth(c):
        return c.depth


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


class Conversion_maths:

    def __init__(self):
        pass


    def update(self,window):
        self.height = window.height
        self.width = window.width
        
        self.vr = radians(window.vertical_rotation)
        self.hr = radians(window.horizontal_rotation)

        self.cos_vr = cos(self.vr)
        self.sin_vr = sin(self.vr)

        self.d = window.distance
        self.render_depth = window.render_depth

        self.window_x = window.x
        self.window_y = window.y
        self.window_z = window.z

    def get_2D_cord(self,cord):

        cords = self.cartesian_translate(cord)

        if cords is None:
            return None

        x = int(cords[0]+self.width/2)
        y = int(cords[1]+self.height/2)
        
        return [x,y,cords[2]]
        
        
    def Depth(s,o,r,h):
        s.sin_hr = sin(s.hr+o)
        
        return (s.cos_vr*r*s.sin_hr)-(s.sin_vr*h)

    def Circle(s,o,r,h):
        
        depth = s.Depth(o,r,h)
        
        s.cos_hr = cos(s.hr+o)

        lens_distance = s.d-depth
        
        if lens_distance <= 0 or abs(depth) > s.render_depth:
            return None

        distortion = (s.d/lens_distance)

        x = distortion*r*s.cos_hr

        y = distortion*(r*s.sin_vr*s.sin_hr+h*s.cos_vr)

        return [x,y,depth]

    def cartesian_translate(self,cord):
        x = cord[0] - self.window_x
        y = cord[1] - self.window_y
        z = cord[2] - self.window_z
        
        return self.Circle(atan2(x,y),sqrt(x**2+y**2),z)

                         
