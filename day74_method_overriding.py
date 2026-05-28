

class shape:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def area(self):
        return self.x*self.y

class circle(shape):
    def __init__(self, radius):
        self.radius=radius
        super().__init__(radius,radius)
        
    def area(self):
        return 3.41*super().area()  #self.radius*self.radius
    
    #rec=shape(3,5)
    #print(rec.area())

c=circle(5)
print(c.area())




                                                                                         















