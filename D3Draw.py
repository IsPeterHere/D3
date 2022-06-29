from graphics import *


win = GraphWin('Drawing', 500, 400)

while True:
    P = []
    while True:
        
        i = win.checkMouse()
    
        if i != None:
            P.append(i)
            if len(P) == 2:
                break
        
            

    Rectangle(  P[0], P[1]).draw(win)
