import D3_Eng as d3
import D3_Dynamics as d3d


def Main(window):
    global last_mark
    d3.mouse_direction(window)
    Move_group.call(z = -2)
    if "w" in window.inputs:
        Move_group.y_speed = 4
    elif "s" in window.inputs:
        Move_group.y_speed = -4
    if "a" in window.inputs:
        Move_group.x_speed = 4
    elif "d" in window.inputs:
        Move_group.x_speed = -4
        

    

        
            
    
w = d3.Window(400,400)
w.log_inputs = ['w','s','a','d']

player = d3.Cuboid([0,0,45],[20,20,20])
player.colour = "red"


player_shell = d3.Cuboid_group([0,0,0])
player_shell.add(player)

solids = d3.Cuboid_group([0,0,0])

w.add(player_shell)

Move_group = d3d.Dynamic(player_shell,solids)

for i in range(100):
    c = d3.Cuboid([0,60*i,-30],[40,40,40])
    c.colour = "green"
    solids.add(c)
    w.add(solids)
    
w.start(Main)
