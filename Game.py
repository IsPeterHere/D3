import D3_Eng as d3
"""
def door(x,y,z,colour,rot):
    rim = 5
    height = 150
    width = 70

    xl = 0
    yl = 0
    if rot == 0:
        xl = width
    else:
        yl = width


    c = d3.Cuboid([x,y,height/2-rim/2+z],[rim,rim,height-rim/4])
    c.colour = colour
    w.add(c)
    
    c = d3.Cuboid([x+xl,y+yl,height/2-rim/2+z],[rim,rim,height-rim/4])
    c.colour = colour
    w.add(c)

    c = d3.Cuboid([x+(xl/2),y+(yl/2),height+z],[xl+rim,yl+rim,rim])
    c.colour = colour
    w.add(c)

    draw_diagonal([x+xl/2,y+yl/2,height/2-2],[width-7-(width-10)*rot,3+(width-10)*rot,height-4])
"""
class Door:
    def __init__(self,x,y,z,colour,rot):
        self.x = x
        self.y = y
        self.z = z
        self.colour = colour
        self.rot = rot

        self.rim = 5
        self.height = 150
        self.width = 70

        self.xl = 0
        self.yl = 0
        if rot == 0:
            self.xl = self.width
        else:
            self.yl = self.width

    def make(self):
        c = d3.Cuboid([self.x,self.y,self.height/2-self.rim/2+self.z],[self.rim,self.rim,self.height-self.rim/4])
        c.colour = self.colour
        w.add(c)
        
        c = d3.Cuboid([self.x+self.xl,self.y+self.yl,self.height/2-self.rim/2+self.z],[self.rim,self.rim,self.height-self.rim/4])
        c.colour = self.colour
        w.add(c)

        c = d3.Cuboid([self.x+(self.xl/2),self.y+(self.yl/2),self.height+self.z],[self.xl+self.rim,self.yl+self.rim,self.rim])
        c.colour = self.colour
        w.add(c)

        c = d3.Cuboid([self.x+self.xl/2,self.y+self.yl/2,self.height/2-2],[self.width-7-(self.width-10)*self.rot,3+(self.width-10)*self.rot,self.height-4])
        c.colour = self.colour
        w.add(c)
    
    def open(self):
        draw_diagonal([self.x+self.xl/2,self.y+self.yl/2,self.height/2-2],[self.width-7-(self.width-10)*self.rot,3+(self.width-10)*self.rot,self.height-4])


def desk(x,y,z,colour,rot):
    depth = 5
    width = 100
    length = 70
    xl = 0
    yl = 0
    if rot == 0:
        xl = width
        yl = length
    else:
        xl = length
        yl = width
    c = d3.Cuboid([x,y,z],[xl,yl,depth])
    c.colour = colour
    w.add(c)


def draw_diagonal(start,end):
    grad = (end[1]-start[1])/(end[0]-start[0])
    
    x = start[0]
    y = start[1]

    while x < end[0]:
        x += 1
        y += grad

        print(grad)

        c = d3.Cuboid([x,round(y,0),end[2]/2],[1,1,end[2]])
        c.colour = "blue"
        w.add(c)

def Main(window):
    d3.mouse_direction(window)
    if "w" in window.inputs:
        player.move(y= 3) 
    elif "s" in window.inputs:
        player.move(y= -3) 
    if "a" in window.inputs:
        player.move(x= -3) 
    elif "d" in window.inputs:
        player.move(x= 3)
    if "e" in window.inputs:
        player.move(z= 3) 
    elif "q" in window.inputs:
        player.move(z= -3)
    if 'y' in window.inputs:
        w.x += 3
    elif 'h' in window.inputs:
        w.x -= 3
    if 'g' in window.inputs:
        w.y += 3
    elif 'j' in window.inputs:
        w.y -= 3
    if 't' in window.inputs:
        w.z += 3
    elif 'u' in window.inputs:
        w.z -= 3
    
w = d3.Window(400,400)
w.log_inputs = ['w','s','a','d','e','q','y','g','h','j','u','t']

player = d3.Cuboid([0,0,0],[5,5,5])
player.colour = "red"
w.add(player)

door1 = Door(0,0,0,"brown",1)
door1.make()

door2 = Door(0,100,0,"green",0)
door2.make()

door1.open()
desk(150,150,50,"blue",0)

w.start(Main)
