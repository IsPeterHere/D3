import graphics as G
from math import *

#[0,1]

#[0,0,1]

Width = 500
Height = 400


class Tools:

    def GetFaces(extent,origion):
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

class Cuboid(Tools):

    def __init__(self,A,B):
        '''Enter two points to generate cubiod between

            --- A is origion
            --- B is extent'''
        
        self.origion = A
        self.extent = [B[0]-A[0],B[1]-A[1],B[2]-A[2]]

        #collecion of 3d vectors making all faces
        self.polygons = Tools.GetFaces(self.extent,self.origion)

        self.Current = None
            
    def change(self,x = 0,y = 0,z = 0):
        self.extent = [self.extent[0]+x,self.extent[1]+y,self.extent[2]+z]
        self.polygons = Tools.GetFaces(self.extent,self.origion)
            
            

    def draw(self,win):
        
        self.undraw()
        self.Current = []
        Order = []

        
        for Face in reversed(self.polygons):
            #print("m",midpointD(Face))
            
            Set = [E(Face[0]),E(Face[1]),E(Face[2]),E(Face[3])]
            
            if "Q" in Set:
                print("Qpasssss")
            else:
                self.Current.append(G.Polygon(Set[0][0],Set[1][0],Set[2][0],Set[3][0]))
                self.Current[-1].draw(win)
                Order.append(min(Set[0][1],Set[1][1],Set[2][1],Set[3][1]))
                
            
        try:
            
            #self.Current[1].setFill("green")
            #self.Current[0].setFill("red")
            #self.Current[4].setFill("blue")
            #self.Current[5].setFill("purple")
            #self.Current[2].setFill("yellow")
            #self.Current[3].setFill("brown")
            
            Raise = self.Current.copy()
            N = min(Order)

        
            NumR = []
            RR = []
            for i in range(len((Order))):
                if Order[i] != N:
                    NumR.append(Order[i])
                    RR.append(Raise[i])

            for i in range(len(NumR)): 
                Order.remove(NumR[i])
                Raise.remove(RR[i])
                        

            #print(Order)

            Raise[2].setFill("green")
            Raise[1].setFill("red")
            Raise[0].setFill("blue")

            
            win.tag_raise(Raise[2].id)

            win.tag_raise(Raise[1].id)

            win.tag_raise(Raise[0].id)
            

        except:
            print("passs")

            
    def undraw(self):
        if self.Current != None:
            for item in self.Current:
                item.undraw()
                self.Current = None

    def setpos(self,A):
        self.origion = A
        self.polygons = Tools.GetFaces(self.extent,self.origion)

#Capital X AND Y are 2D Equivelents
#cord Equivelent = point
d = 100



    
def Z(o,r,h,a1,a2):
    return (cos(radians(a2))*r*sin(radians(a1)+o))-(sin(radians(a2))*h)

def Circle(o,r,h,a1,a2):

    z = Z(0,r,h,a1,a2)

    if d-z <= 0:
        return ["Q","Q"]

    x = (d/(d-z))*r*cos(radians(a1)+o)

    y = (d/(d-z))*((r*sin(radians(a2))*sin(radians(a1)+o))+h*cos(radians(a2)))


    #FIX THIS!!!!
    return [x,y,(cos(radians(a1+(d-z))*sin(radians(a2-(d-z)))))]

def Cart(x,y,z,a1,a2):
    return Circle(atan2(radians(y),radians(x)),sqrt(x**2+y**2),z,a1,a2)
    
def E(cord):

    a1 = Hr
    a2 = Vr

    XY = Cart(cord[0],cord[1],cord[2],a1,a2)

    if XY[0] == "Q":
        return "Q"
    return G.Point(int(XY[0]),int(XY[1])),XY[2]


class Screen:

    def __init__(self):
        self.objects = []

        self.win = G.GraphWin('Drawing', Width, Height, autoflush=False)
        self.win.setCoords(-1*int(Width/2), -1*int(Height/2),int(Width/2),int(Height/2)) 

    def add(self,item):
        self.objects.append(item)
    
    def update(self):

        Order = []

        for obj in self.objects:
            Order.append(E(obj.origion)[1])

        for i in range(0,len(Order)):

            Value = Order[i]
            Value2 = self.objects[i]
    
            Pos = i

            while Pos > 0 and Value < Order[Pos-1]:

                Order[Pos] =Order[Pos-1]
                self.objects[Pos] =self.objects[Pos-1]
                    
                Pos -= 1

            Order[Pos] = Value
            self.objects[Pos] = Value2

        for i in reversed(self.objects):
            i.draw(self.win)

        G.update()
        

        
screen= Screen()
for x in range(1):
    for z in range(1):
    
        Cube = Cuboid([0,0,0],[30,30,30])
        Cube.setpos([30*x,0,30*z])
        screen.add(Cube)

Hr = 0
Vr = 20

for x in range(2000):
    print(Vr,Hr)
    screen.update()


    #Vr += 1

    Hr += 1
    #Hr += int(input())
    print(Hr)
    #Vr += int(input())
