class Dynamic:

    def __init__(self,cuboid_group,solid_group):
        self.cuboid_group = cuboid_group
        self.solid_group = solid_group

        self.x_speed = 0 
        self.y_speed = 0
        self.z_speed = 0
    

    def call(self,x= 0, y = 0, z = 0):
        self.__x_res(x)
        self.__y_res(y)
        self.__z_res(z)

    def __x_res(self,pull):
        
        if self.x_speed > 0 :
            self.x_speed = int(self.x_speed )-1
            
        elif self.x_speed < 0 :
            self.x_speed = int(self.x_speed )+1
        else:
            return None

        if self.x_speed > 0 :
            for num in reversed(range(0,self.x_speed)):
                if not self.solid_group.touching(self.cuboid_group):
                    self.cuboid_group.move(x = self.x_speed)
            
        elif self.x_speed < 0 :
            for num in range(self.x_speed,0):
                if not self.solid_group.touching(self.cuboid_group):
                    self.cuboid_group.move(x = self.x_speed)
        else:
            return None

    def __y_res(self,pull):
        if self.y_speed > 0 :
            self.y_speed = int(self.y_speed )-1
            
        elif self.y_speed < 0 :
            self.y_speed = int(self.y_speed )+1
        else:
            return None

        if self.y_speed > 0 :
            for num in reversed(range(0,self.y_speed)):
                if not self.solid_group.touching(self.cuboid_group):
                    self.cuboid_group.move(y = self.y_speed)
            
        elif self.y_speed < 0 :
            for num in range(self.y_speed,0):
                if not self.solid_group.touching(self.cuboid_group):
                    self.cuboid_group.move(y = self.y_speed)
        else:
            return None
        
    def __z_res(self,pull):
        if self.z_speed > 0 :
            self.z_speed = int(self.z_speed )-1
            
        elif self.z_speed < 0 :
            self.z_speed = int(self.z_speed )+1
        else:
            return None

        if self.z_speed > 0 :
            for num in reversed(range(0,self.z_speed)):
                if not self.solid_group.touching(self.cuboid_group):
                    self.cuboid_group.move(z = self.z_speed)
            
        elif self.z_speed < 0 :
            for num in range(self.z_speed,0):
                if not self.solid_group.touching(self.cuboid_group):
                    self.cuboid_group.move(z = self.z_speed)
        else:
            return None
