import Engine as d3

def movment(window):
    if "a" in window.inputs:
        window.horizontal_rotation +=5
    elif "d" in window.inputs:
        window.horizontal_rotation -=5

    if "w" in window.inputs:
        window.vertical_rotation +=5
    elif "s" in window.inputs:
        window.vertical_rotation -=5
        
def frame(window):
    global last_data
    movment(window)
    file = open("test.txt","r")
    data = file.read()
    file.close()
    
    if last_data != data or last_data is None:
        cuboid_data = []
        for cuboid in data.split("\n"):
            cuboid_data.append(cuboid)
            
        file.close()
        entity.cuboids = []
        
        for line in range(len(cuboid_data)):
            if len(cuboid_data[line])>12:
                try:
                    cuboid =''.join([split for split in cuboid_data[line].split(" ") if split != ' '])
                    cuboid = cuboid.split(".")
                    centre = [int(num) for num in cuboid[0].split(",")]
                    extent = [int(num) for num in cuboid[1].split(",")]

                    if len(centre) == 3 and len(centre) == 3:
                        colour = cuboid[2]
                        entity.add(d3.Cuboid(centre,extent,colour))
                    else:
                        print("error on line",line+1)
                except:
                    print("error on line",line+1)

    last_data = data

window = d3.Window(400,400)

cuboid = d3.Cuboid([0,0,0],[40,40,40])
cuboid.colour = 'green'

entity = d3.Entity([0,0,0],cuboid)

window.add(entity)

last_data = None
window.log_inputs = ["a","d","w","s"]
window.start(frame)
