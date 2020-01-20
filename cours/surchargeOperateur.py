class Point:
    def __init__(self,x,y,z=None):
        self.x = x
        self.y = y
        self.z = z
    def ToString(self):
        if self.z != None:
            print('P(',"%.2f" % self.x,',',"%.2f" % self.y,',',"%.2f" % self.z,')')
        else:
            print('P(',"%.2f" % self.x,',',"%.2f" % self.y,')')
            
P1=Point(2,3)
P1.ToString()
P2=Point(1,-5,6)
P2.ToString()
