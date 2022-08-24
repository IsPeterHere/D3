import graphics as G
import Tools as tools
import time
import random

class Cuboid:

    def __init__(self,centre,extent,colour = None):
        
        '''
        EXTENT; FROM 0,0,0

        CENTRE; POINT OF CENTRES POSITION
        '''

        self.__centre = centre
        self.__extent = extent
        self.colour = colour

        self.faces = tools.GetFaces(self.__extent,self.__centre)

    def centre(self,new = None, key = None):
        if new == None:
            if key == None:
                return self.__centre
            elif key == "y":
                return [0,self.__centre[1],0]
        else:
            __centre = new
            self.faces = tools.GetFaces(self.__extent,self.__centre)

class Window:

    def __init__(self,Width,Height):
        self.window = G.GraphWin('D3V', Width, Height, autoflush=False)
        self.window.setCoords(-1*int(Width/2), -1*int(Height/2),int(Width/2),int(Height/2)) 
        self.window.setBackground("white")
        
        self.horizontal_rotation = 0
        self.vertical_rotation = 180

        self.distance = 300

        self.cuboids = []

        self.__polygons = []

    def add(self,cuboid):
        self.cuboids.append(cuboid)

    def remove(self,cuboid):
        self.cuboids.remove(cuboid)

    def start(self,frame_function = None):
        if frame_function == None:
            G.update()
        else:
            self.frame_function = frame_function
            while True:
                self.__next()

    def __next(self):
        self.frame_function(self)
        self.__render()
        
        G.update(30)

    def __render(self):

        #Find suitable 2d equivlent z value and change render order acordingly
        
        for c in self.cuboids:
            c.z = tools.Cart(c.centre(key = 'y'),self.horizontal_rotation,self.vertical_rotation,self.distance)[2]


        for i in range(0,len(self.cuboids)):

            Value = self.cuboids[i].z

            Pos = i

            while Pos > 0 and Value < self.cuboids[Pos-1].z:

                self.cuboids[Pos].z =self.cuboids[Pos-1].z

                Pos -= 1

                self.cuboids[Pos].z = Value

        self.__clear()
        
        for cuboid in self.cuboids:
            self.__cube_draw(cuboid)
        

    def __clear(self):
        for poly in self.__polygons:
            poly.undraw()
        self.__polygons = []
                
    def __cube_draw(self,cuboid):

        for face in cuboid.faces:
            
            translated_cords = []
            for cord in face:
                
                translated_cords.append(self.__d2_cord(cord))

            try:
                new_poly = G.Polygon(translated_cords[0],
                                     translated_cords[1],
                                     translated_cords[2],
                                     translated_cords[3])
            except:
                continue

            self.__polygons.append(new_poly)
            
            new_poly.draw(self.window)

            new_poly.setFill(cuboid.colour)
            #new_poly.setOutline(cuboid.colour)

        

        #print([c.z for c in self.cuboids])

    def __d2_cord(self,cord):

        d2_cord = tools.Cart(cord,self.horizontal_rotation,self.vertical_rotation,self.distance)

        if d2_cord[0] == "Q":
            return None
        
        return G.Point(int(d2_cord[0]),int(d2_cord[1]))
        
        

def frame(window):
    window.horizontal_rotation += 1
    #window.vertical_rotation +=1
    
w = Window(400,400)

c = Cuboid([0,0,0],[40,40,40])
c.colour = "green"
w.add(c)

for i in range(10):
    
    c = Cuboid([i*100,0,0],[40,40,40])
    c.colour = random.choice(["green",'blue','red'])
    w.add(c)

w.start(frame)
