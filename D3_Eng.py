import tkinter as tk
import D3_Eng_Tools as tools
import time

class Face:

    def __init__(self,points,cuboid,cart_maths):
        self.points = points
        self.colour = cuboid.colour
        self.cuboid = cuboid
        
        self.cart_maths = cart_maths

    def draw(self,canvas):
            
        translated_cords = []
        for cord in self.points:
            x,y = self.cart_maths.d2_cord(cord)

            if x == "Q":
                continue
            
            translated_cords.append(x)
            translated_cords.append(y)
            
        if len(translated_cords)>0:
            canvas.create_polygon(translated_cords, outline='black',fill=self.colour, width=1)

    def centre(self):
        x = sum([i[0] for i in self.points])/4
        y = sum([i[1] for i in self.points])/4
        z = sum([i[2] for i in self.points])/4
        return [x,y,z]

class Cuboid:

    def __init__(self,centre,extent,colour = None):
        
        '''
        EXTENT; FROM 0,0,0

        CENTRE; POINT OF CENTRES POSITION
        '''

        self.__centre = centre
        self.__extent = extent
        self.colour = colour

        self.x = self.__centre[0]
        self.y = self.__centre[1]
        self.z = self.__centre[2]

        self.faces = tools.GetFaces(self.__extent,self.__centre)

    def centre(self,new = None):
        if new == None:
            if key == None:
                return self.__centre
        else:
            __centre = new
            self.faces = tools.GetFaces(self.__extent,self.__centre)

    def touching(self,cuboid):
        if self.__centre[0]+self.__extent[0]/2-cuboid.__centre[0]+cuboid.__extent[0]/2 > 0:
            return True
            if self.__centre[1]+self.__extent[1]/2-cuboid.__centre[1]+cuboid.__extent[1]/2 > 0:
                return True
                if self.__centre[2]+self.__extent[2]/2-cuboid.__centre[2]+cuboid.__extent[2]/2 > 0:
                    return True
        return False

    def move(self,x=0,y=0,z=0):
        print(self.__centre)
        self.__centre[0]+= x
        self.__centre[1]+= y
        self.__centre[2]+= z
        self.faces = tools.GetFaces(self.__extent,self.__centre)

class Window(tools.Bindings):

    def __init__(self,width,height):
        self.window = tk.Tk()
        self.canvas = tk.Canvas(self.window, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.window.bind("<Key>", self.handle_keypress)
        self.window.bind("<KeyRelease>", self.handle_up)
        self.window.bind('<Motion>',self.MousePosition)
        self.window.bind('<Button-1>',self.Left_pressed)
        
        self.window.title('D3')
        self.window.geometry(str(width)+'x'+str(height))
        self.width = width
        self.height = height

        self.cart_maths = tools.Cart_maths()
        self.horizontal_rotation = 0
        self.vertical_rotation = 180
        self.distance = 600
        self.render_depth = 3000
        self.x = 0
        self.y = 0
        self.z = 0

        self.cuboids = []

        self.monitored_current = []
        self.inputs = []
        self.log_inputs = []
        self.mouse_current_position = [0,0]
        self.l_is_pressed = False


    def add(self,cuboid):
        self.cuboids.append(cuboid)

    def remove(self,cuboid):
        self.cuboids.remove(cuboid)

    def start(self,frame_function = None):
        if frame_function == None:
            print("start needs Frame function")
        else:
            self.frame_function = frame_function
            self.window.after(50,self.__next)
            self.window.mainloop()

    def __next(self):
        start = time.time()
        #-----
        for input_ in self.monitored_current:
            self.inputs.append(input_)
            
        self.frame_function(self)

        self.cart_maths.update(self)
        self.__render()

        self.width = self.window.winfo_width()
        self.height = self.window.winfo_height()
        
        self.inputs = []
        #-----
        end = time.time()
        self.pause = max(1,int(50-((end-start)*1000)))
        self.window.after(self.pause,self.__next)

    def __render(self):

        #Find suitable 2d equivlent z value and change render order acordingly
        self.faces_to_render = []
        
        for c in self.cuboids:
            sub_face_block = []
            
            for face_cords in c.faces:
                face = Face(face_cords,c,self.cart_maths)
                face.z = self.cart_maths.cart(face.centre())[2]
                if face.z == "Q":
                    pass
                else:
                    sub_face_block.append(face)

            if len(sub_face_block) > 0 :
                sub_face_block.sort(key = tools.Return_z)
                sub_face_block.remove(min(sub_face_block, key = tools.Return_z))
                    
                self.faces_to_render += sub_face_block
        '''
        for i in range(0,len(self.faces_to_render)):
            Value = self.faces_to_render[i]
            Pos = i
            while Pos > 0 and Value.z < self.faces_to_render[Pos-1].z:

                self.faces_to_render[Pos] =self.faces_to_render[Pos-1]
                Pos -= 1
                self.faces_to_render[Pos] = Value
        '''
        self.faces_to_render.sort(key = tools.Return_z)


        #clar screen and draw all objects
        self.clear()
        
    
        for face in self.faces_to_render:
            face.draw(self.canvas)

        
    def clear(self):
        self.canvas.delete("all")
        
        
def mouse_direction(window):
    

    if window.mouse_current_position[0]-40 > window.width/2:
        window.horizontal_rotation += (window.width/2-window.mouse_current_position[0])/100
    elif window.mouse_current_position[0]+40 < window.width/2:
        window.horizontal_rotation += (window.width/2-window.mouse_current_position[0])/100
    if window.mouse_current_position[1]-40 > window.height/2:
        window.vertical_rotation +=(window.height/2-window.mouse_current_position[1])/100
    elif window.mouse_current_position[1]+40 < window.height/2:
        window.vertical_rotation +=(window.height/2-window.mouse_current_position[1])/100




if __name__ == "__main__":
         
    w = Window(400,400)
    w.log_inputs = ['w','s','a','d']



    for i in range(90):
        c = Cuboid([0,60*i,20],[40,40,40])
        c.colour = "blue"
        w.add(c)

        c = Cuboid([0,70+60*i,80],[40,40,40])
        c.colour = "yellow"
        w.add(c)

        c = Cuboid([200,70+60*i,40],[40,40,40])
        c.colour = "red"
        w.add(c)

        c = Cuboid([0,0,80+60*i],[40,40,40])
        c.colour = "green"
        w.add(c)

        c = Cuboid([80+60*i,0,20],[40,40,40])
        c.colour = "purple"
        w.add(c)



    w.start(mouse_direction)
