from math import *

def GetFaces(extent,centre):

    origin = [centre[0]-extent[0]/2,centre[1]-extent[1]/2,centre[2]-extent[2]/2,]
    extent = [extent[0]-extent[0]/2,extent[1]-extent[1]/2,extent[2]-extent[2]/2,]
    
    faces = []
        
    Pos = [0,1,2]
    for Constant in range(3):
        for flip in range(2):
            faces.append([[origin[0],origin[1],origin[2]],
                            [origin[0],origin[1],origin[2]],
                            [origin[0],origin[1],origin[2]],
                            [origin[0],origin[1],origin[2]]])
            half = True
            for Count in range(3):
                
                if Count == Constant:

                    if flip == 1:

                        for x in range(4):
                            faces[-1][x][Constant] +=  extent[Constant]
                        
                else:
                    if half:
                        for x in range(2):
                            faces[-1][x][Count] += extent[Count]

                        half = False

                    else:
                        faces[-1][0][Count] += extent[Count]
                        faces[-1][3][Count] += extent[Count]
                            
    return faces



def Z(o,r,h,a1,a2):
    return (cos(radians(a2))*r*sin(radians(a1)+o))-(sin(radians(a2))*h)

def Circle(o,r,h,a1,a2,d):

    z = Z(o,r,h,a1,a2)

    if d-z <= 0:
        return ["Q","Q"]

    x = (d/(d-z))*r*cos(radians(a1)+o)

    y = (d/(d-z))*((r*sin(radians(a2))*sin(radians(a1)+o))+h*cos(radians(a2)))


    return [x,y,((r*sin(radians(a2))*sin(radians(a1)+o))+h*cos(radians(a2)))]

def Cart(cord,a1,a2,d):
    x = cord[0]
    y = cord[1]
    z = cord[2]
    return Circle(atan2(radians(y),radians(x)),sqrt(x**2+y**2),z,a1,a2,d)
