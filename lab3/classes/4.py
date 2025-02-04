import math
class Point():
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def show(self):
        print(f"Coordinates: ({self.x}), ({self.y})")

    def move(self,xx,yy):
        self.x=xx
        self.y=yy

    def dist(self):
        #if you draw you can get right triangle
        #use Pythagorean theorem
        dx=self.x - secpoint.x
        dy=self.y - secpoint.y
        distance=math.sqrt(dx**2 + dy**2)
        return distance
a=float(input("x - "))
b=float(input("y - "))
firstpoint=Point(a,b)
secpoint=Point(a,b)

firstpoint.show()
c=float(input("xx - "))
d=float(input("yy - "))

firstpoint.move(c,d)
firstpoint.show()

distance=firstpoint.dist()
print("Distance between first and second points: ", distance)


    