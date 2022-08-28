import D3_Eng as d3



def Main(window):
    global last_mark
    d3.mouse_direction(window)

    if "w" in window.inputs:
        player.move(y= 3) 
    elif "s" in window.inputs:
        player.move(y= -3) 
    if "a" in window.inputs:
        player.move(x= -3) 
    elif "d" in window.inputs:
        player.move(x= 3)
        
    if player.y >= last_mark:
        for i in range(100):
            c = d3.Cuboid([0,60*i,-30],[40,40,40])
            c.colour = "green"
            objects.append(c)
            window.add(c)

        for i in range(100):
            window.remove(objects[i])

        last_mark+=100
        
            
    
w = d3.Window(400,400)
w.log_inputs = ['w','s','a','d']

player = d3.Cuboid([0,0,0],[20,20,20])
player.colour = "red"
w.add(player)

objects = []
for i in range(100):
    c = d3.Cuboid([0,0,60*i],[40,40,40])
    c.colour = "green"
    objects.append(c)
    w.add(c)
            
last_mark = 0
    
w.start(Main)
