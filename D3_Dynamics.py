class Dynamic:

    def __init__(self,cuboid_group,solid_group):
        self.cuboid_group = cuboid_group
        self.solid_group = solid_group

        self.x_speed = 0 
        self.y_speed = 0
        self.z_speed = 0
    

    def call(self,x= 0, y = 0, z = 0):
        if self.solid_group.touching(self.cuboid_group):
            self.cuboid_group.move(z = 5)
        self.__x_res(x)
        self.__y_res(y)
        self.__z_res(z)

    def __x_res(self,pull):
        self.x_speed+= pull
        
        if self.x_speed > 0 :
            self.x_speed = int(self.x_speed )-1
            
        elif self.x_speed < 0 :
            self.x_speed = int(self.x_speed )+1
        else:
            return None

        if self.x_speed > 0 :
            for num in range(0,self.x_speed):
                self.cuboid_group.move(x = 1)
                if self.solid_group.touching(self.cuboid_group):
                    self.cuboid_group.move(x = -1)
                    self.x_speed = 0
                    break

                    
            
        elif self.x_speed < 0 :
            for num in range(self.x_speed,0):
                self.cuboid_group.move(x = -1)
                if self.solid_group.touching(self.cuboid_group):
                    self.cuboid_group.move(x = 1)
                    self.x_speed = 0
                    break
        else:
            return None

    def __y_res(self,pull):
        self.y_speed+= pull
        
        if self.y_speed > 0 :
            self.y_speed = int(self.y_speed )-1
            
        elif self.y_speed < 0 :
            self.y_speed = int(self.y_speed )+1
        else:
            return None

        if self.y_speed > 0 :
            for num in range(0,self.y_speed):
                self.cuboid_group.move(y = 1)
                if self.solid_group.touching(self.cuboid_group):
                    self.cuboid_group.move(y = -1)
                    self.y_speed = 0 
                    break

                    
            
        elif self.y_speed < 0 :
            for num in range(self.y_speed,0):
                self.cuboid_group.move(y = -1)
                if self.solid_group.touching(self.cuboid_group):
                    self.cuboid_group.move(y = 1)
                    self.y_speed = 0
                    break
        else:
            return None
        
    def __z_res(self,pull):
        self.z_speed+= pull
        
        if self.z_speed > 0 :
            self.z_speed = int(self.z_speed )-1
            
        elif self.z_speed < 0 :
            self.z_speed = int(self.z_speed )+1
        else:
            return None

        if self.z_speed > 0 :
            for num in range(0,self.z_speed):
                self.cuboid_group.move(z = 1)
                if self.solid_group.touching(self.cuboid_group):
                    self.cuboid_group.move(z = -1)
                    self.z_speed = 0
                    break

                    
            
        elif self.z_speed < 0 :
            for num in range(self.z_speed,0):
                self.cuboid_group.move(z = -1)
                if self.solid_group.touching(self.cuboid_group):
                    self.cuboid_group.move(z = 1)
                    self.z_speed = 0
                    break
        else:
            return None
