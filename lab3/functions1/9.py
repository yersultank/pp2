import math
def volume(radius):
    sphere_volume=4/3 * math.pi * radius**3
    return sphere_volume

r=float(input("write radius: "))
print(volume(r))