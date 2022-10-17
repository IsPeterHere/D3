import tkinter as tk
import Engine_Tools as tools
import time
import cProfile
import pstats

class Face:
    '''

    Face class is a disposable class used in rendering.

    Stores points that make up a cuboids face,draws the  points onto the tkinter canvas and
    provides the 'depth' of the face to be used in rendering order.
    
    '''

    def __init__(self,points,colour,depth):
        '''
        Data:
            points - translated 3d cordinates that make up a 2d polygon  

            colour - parent cuboids colour

            depth - a new 'z' value for the face, Used in rendering, to layer all 2d faces correctly.
        '''
        self.__points = points
        self.__colour = colour
        self.depth = depth
        
    def draw(self,canvas):
        '''
        draws self on to the tkinter canvas
        '''
        canvas.create_polygon(self.__points, outline='black',fill=self.__colour, width=1)


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

    def __get_translated_faces(self,conversion_maths):
        origin = [self.__centre[0]-self.__extent[0]/2,self.__centre[1]-self.__extent[1]/2,self.__centre[2]-self.__extent[2]/2]
        extent = self.__extent
        
        bt1 = conversion_maths.get_2D_cord(origin)
        bt2 = conversion_maths.get_2D_cord([origin[0]+ extent[0],origin[1],origin[2]])
        bt3 = conversion_maths.get_2D_cord([origin[0]+ extent[0],origin[1]+extent[1],origin[2]])
        bt4 = conversion_maths.get_2D_cord([origin[0],origin[1]+ extent[1],origin[2]])

        tp1 = conversion_maths.get_2D_cord([origin[0],origin[1],origin[2] + extent[2]])
        tp2 = conversion_maths.get_2D_cord([origin[0]+ extent[0],origin[1],origin[2] + extent[2]])
        tp3 = conversion_maths.get_2D_cord([origin[0]+ extent[0],origin[1]+extent[1],origin[2] + extent[2]])
        tp4 = conversion_maths.get_2D_cord([origin[0],origin[1]+ extent[1],origin[2] + extent[2]])
        
        polygons=[
            [bt1,bt2,bt3,bt4],
            [tp1,tp2,tp3,tp4],
            [bt2,bt1,tp1,tp2],
            [bt4,bt3,tp3,tp4],
            [bt4,bt1,tp1,tp4],
            [bt3,bt2,tp2,tp3]]
        
        return polygons
    
    def get_faces(self,conversion_maths):
        
        self.faces = []
        
        translated_faces = self.__get_translated_faces(conversion_maths)
        
        for count in range(len(translated_faces)):

            if not any([False if i is not None else True for i in translated_faces[count]]):
                face = Face([cord[:-1] for cord in translated_faces[count]],
                            self.colour,
                            (sum([cord[2] for cord in translated_faces[count]])/4))
                self.faces.append(face)
            else:
                return None
        
        return self.faces

    def get_centre(self):
        return self.__centre

    def set_pos(self,cord):
        self.__centre = cord
    
    def centre(self,new = None):
        if new is None:
            return self.get_centre()
        else:
            self.set_pos(new)
            
    def extent(self,new = None):
        if new is None:
            return self.__extent
        else:
            self.__extent = new
            
    def move(self,x=0,y=0,z=0):
        self.__centre[0]+= x
        self.__centre[1]+= y
        self.__centre[2]+= z
           
    def touching(self,other_cuboid):
        if self == other_cuboid:
            return False
        
        if abs(self.__centre[0] -other_cuboid.centre()[0]) < abs(self.__extent[0]/2+other_cuboid.extent()[0]/2):
            if abs(self.__centre[1] -other_cuboid.centre()[1]) < abs(self.__extent[1]/2+other_cuboid.extent()[1]/2):
                if abs(self.__centre[2] -other_cuboid.centre()[2]) < abs(self.__extent[2]/2+other_cuboid.extent()[2]/2):
                    return True
        
        return False
    
class Entity:

    def __init__(self,centre,*cuboids):
        self.centre = centre
        self.cuboids = []

        for c in cuboids:
            self.cuboids.append(c)

    def add(self,cuboids):
        if cuboids is list:
            for c in cuboid_s:
                self.cuboids.append(c)
        else:
            self.cuboids.append(cuboids)

    def remove(self,cuboids):
        if cuboids is list:
            for c in cuboid_s:
                self.cuboids.remove(c)
        else:
            self.cuboids.remove(cuboids)     

    def touching(self,other):


        if isinstance(other,Entity):
            for self_c in self.cuboids:
                for other_c in other.cuboids:
                    if self_c.touching(other_c):
                        return True
        else:
            for self_c in self.cuboids:
                if self_c.touching(other):
                    return True

    
        return False

    def move(self,x=0,y=0,z=0):
        for c in self.cuboids:
            c.move(x,y,z)
        self.centre[0] += x
        self.centre[1] += y
        self.centre[2] += z

    def set_pos(self,cord):
        change_x = -self.centre[0] + cord[0]
        chnage_y = -self.centre[1] + cord[1]
        chnage_z = -self.centre[2] + cord[2]
        for c in self.cuboids:
            c.move(change_x,chnage_y,chnage_z)
        self.centre[0] = cord[0]
        self.centre[1] = cord[1]
        self.centre[2] = cord[2]
        
class Window(tools.Bindings):

    def __init__(self,width,height,title = "D3"):
        self.window = tk.Tk()
        self.canvas = tk.Canvas(self.window, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.window.bind("<Key>", self.handle_keypress)
        self.window.bind("<KeyRelease>", self.handle_up)
        self.window.bind('<Motion>',self.MousePosition)
        self.window.bind('<Button-1>',self.Left_pressed)
        
        self.window.title(title)
        self.window.geometry(str(width)+'x'+str(height))
        self.width = width
        self.height = height

        self.frames_per_second = 25

        self.cartesian_maths = tools.Conversion_maths()
        self.horizontal_rotation = 0
        self.vertical_rotation = 180
        self.distance = 600
        self.render_depth = 5000
        self.true_time = 0
        self.x = 0
        self.y = 0
        self.z = 0

        self.entities = []
        
        self.monitored_current = []
        self.inputs = []
        self.log_inputs = []
        self.mouse_current_position = [0,0]
        self.l_is_pressed = False


    def add(self,entity):
        if entity not in self.entities:
            self.entities.append(entity)

    def remove(self,entity):
        self.entities.remove(entity)


    def start(self,frame_function = None):
        if frame_function is None:
            print("start needs Frame function")
        else:
            self.frame_function = frame_function
            self.window.after(50,self.__next)
            self.window.mainloop()

    def __next(self):
        start = time.time()
        #-----
        with cProfile.Profile() as pr:
            self.__process()
        stats = pstats.Stats(pr)
        stats.sort_stats(pstats.SortKey.TIME)

        self.pr = stats
        #-----
        end = time.time()
        
        self.true_time = str(int((end-start)*1000))+"/"+str(int(1000/self.frames_per_second))
        self.pause = max(1,int(1000/self.frames_per_second-((end-start)*1000)))

        self.window.after(self.pause,self.__next)

    def __process(self):
        
        for input_ in self.monitored_current:
            self.inputs.append(input_)
            
        self.frame_function(self)

        self.cartesian_maths.update(self)

        self.__render()

        self.width = self.window.winfo_width()
        self.height = self.window.winfo_height()
        
        self.inputs = []
        
    def __render(self):

        #Find suitable 2d equivlent z value and change render order acordingly
        self.faces_to_render = []

        cuboids = []
        for entity in self.entities:
            for cuboid in entity.cuboids:
                cuboids.append(cuboid)


        for cuboid in cuboids:

            cuboid_faces = cuboid.get_faces(self.cartesian_maths)
            
            if cuboid_faces is not None:
                sub_face_block = cuboid_faces

                sub_face_block.remove(min(sub_face_block,key = tools.Return_depth))
        
                self.faces_to_render += sub_face_block
            
        '''
        for i in range(0,len(self.faces_to_render)):
            Value = self.faces_to_render[i]
            Pos = i
            while Pos > 0 and Value.depth < self.faces_to_render[Pos-1].depth:

                self.faces_to_render[Pos] =self.faces_to_render[Pos-1]
                Pos -= 1
                self.faces_to_render[Pos] = Value
        '''
        self.faces_to_render.sort(key = tools.Return_depth)
        #clar screen and draw all objects
        self.__clear()
        
    
        for face in self.faces_to_render:
            face.draw(self.canvas)

        
    def __clear(self):
        self.canvas.delete("all")

    def clear(self):
        self.entities = []

    def centre(self,cord = None):

        if cord is None:
            return [self.x,self.y,self.z]
        else:
            self.x = cord[0]
            self.y = cord[1]
            self.z = cord[2]
        
        
def mouse_direction(window):

    if window.mouse_current_position[0]-40 > window.width/2:
        window.horizontal_rotation += (window.width/2-window.mouse_current_position[0])/100
    elif window.mouse_current_position[0]+40 < window.width/2:
        window.horizontal_rotation += (window.width/2-window.mouse_current_position[0])/100
    
    if window.mouse_current_position[1]-40 > window.height/2:
        window.vertical_rotation +=(window.height/2-window.mouse_current_position[1])/100
    elif window.mouse_current_position[1]+40 < window.height/2:
        window.vertical_rotation +=(window.height/2-window.mouse_current_position[1])/100
    


class TEST_Unit():
    def __init__(self):
        
        self.window = Window(400,400)
        self.window.log_inputs = ['w','s','a','d']

        self.w = Entity([0,0,0])
        '''
        for i in range(90):
            c = Cuboid([0,60*i,20],[40,40,40])
            c.colour = "blue"
            self.w.add(c)

            c = Cuboid([0,1200,80+60*i],[40,40,40])
            c.colour = "dark green"
            self.w.add(c)

            c = Cuboid([0,70+60*i,80],[40,40,40])
            c.colour = "yellow"
            self.w.add(c)

            c = Cuboid([200,70+60*i,40],[40,40,40])
            c.colour = "red"
            self.w.add(c)

            c = Cuboid([0,0,80+60*i],[40,40,40])
            c.colour = "green"
            self.w.add(c)

            c = Cuboid([80+60*i,0,20],[40,40,40])
            c.colour = "purple"
            self.w.add(c)

            c = Cuboid([80+60*i,400,-20],[40,40,40])
            c.colour = "dark blue"
            self.w.add(c)
        '''
        cube = 3
        for x in range(cube):
            for y in range(cube):
                for z in range(cube):
                    c = Cuboid([x*80,y*80,z*80],[40,40,40])
                    c.colour = "green"
                    self.w.add(c)
                    
    def TEST_frame(self,window):
        mouse_direction(window)
        if 'q' in window.inputs:
            window.pr.print_stats()
            print(window.true_time)

        

    def TEST_run(self):
        self.window.add(self.w)
        self.window.start(self.TEST_frame)

if __name__ == "__main__":
    u = TEST_Unit()
    u.TEST_run()

