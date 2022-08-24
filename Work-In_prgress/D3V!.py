import graphics as G
import Tools as tools

class Cuboid:

    def __init__(self,centre,extent,colour = None):
        
        '''
        EXTENT; FROM 0,0,0

        CENTRE; POINT OF CENTRES POSITION
        '''

        self.__centre = centre
        self.__extent = extent
        self.colour = colour

        self.Faces = tools.GetFaces(self.__extent,self.__centre)

    def centre(self,new = None):
        if new == None:
            return self.__centre
        else:
            __centre = new
            self.Faces = tools.GetFaces(self.__extent,self.__centre)

class Window:

    def __init__(self,Width,Height):
        self.window = G.GraphWin('D3V', Width, Height, autoflush=False)
        self.window.setBackground("white")
        
        self.horizontal_rotation = 0
        self.vertical_rotation = 0

        self.distance = 100

        self.cuboids = []

    def add(self,cuboid):
        self.cuboids.append(cuboid)

    def remove(self,cuboid):
        self.cuboids.remove(cuboid)

    def start(self,frame_function = None):
        if frame_function == None:
            G.update()
        else:
            self.frame_function = frame_function
            self.__next()

    def __next(self):
        self.frame_function()
        self.__render()
        
        G.update(30)
        self.__next()

    def __render(self):
        print("___")
        for c in self.cuboids:
            c.z = tools.Cart(c.centre(),self.horizontal_rotation,self.vertical_rotation,self.distance)[2]
            print(c.z)
        
        

def Frame():
    pass
    
w = Window(400,400)
w.add(Cuboid([0,0,0],[5,5,5]))
w.add(Cuboid([-5,0,0],[5,5,5]))
w.add(Cuboid([-7,0,0],[5,5,5]))
w.start(Frame)
