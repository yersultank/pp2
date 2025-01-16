#numbers
x=1 #  a whole number, positive or negative, without decimals, of unlimited length.
y=1.1 # positive or negative number containing one or more decimals.
y1=35e2
z=1j # numbers that are written with a "j" as the imaginary part.
print(type(x))
print(type(y))
print(type(y1))
print(type(z))
#we can convert from one type to another:
a=float(x)
b=int(y)
c=complex(x)
print(a)
print(b)
print(c)
print(type(a))
print(type(b))
print(type(c))
# P.S. impossible to convert complex numbers into another number type.
#Python has a built-in module called random that can be used to make random numbers:
import random
print(random.randrange(1,10))
