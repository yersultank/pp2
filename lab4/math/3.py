import math
sides=int(input("number of sides: "))
lenght=int(input("lenght of one side: "))
apothem=(lenght)/(2*math.tan(math.pi/sides))
area=sides*lenght*apothem/2
print(int(area))