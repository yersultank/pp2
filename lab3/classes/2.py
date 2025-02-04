class Shape:
    def area(self):
        return 0
class Square(Shape):
    def __init__(self, length):
        self.lenght=length
    def area(self):
        return self.lenght**2
size=int(input())
kvadrat=Square(size)
print("area of square: ", kvadrat.area())
shape=Shape()
print("default value:",shape.area())

