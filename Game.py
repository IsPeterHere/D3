import D3_Eng as d3

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


    c = d3.Cuboid([x,y,height/2-rim/2],[rim,rim,height-rim/4])
    c.colour = colour
    w.add(c)
    
    c = d3.Cuboid([x+xl,y+yl,height/2-rim/2],[rim,rim,height-rim/4])
    c.colour = colour
    w.add(c)

    c = d3.Cuboid([x+(xl/2),y+(yl/2),height],[xl+rim,yl+rim,rim])
    c.colour = colour
    w.add(c)

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

door(0,0,0,"brown",1)
door(0,100,0,"green",0)
desk(150,150,50,"blue",0)
w.start(Main)
