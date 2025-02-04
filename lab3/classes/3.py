class Shape:
    def area(self):
        return 0
class Rectangle(Shape):
    def __init__(self, length,width):
        self.lenght=length
        self.width=width
    def area(self):
        return self.lenght*self.width
lenght=int(input())
width=int(input())
myrec=Rectangle(lenght,width)
print("area of square: ", myrec.area())


