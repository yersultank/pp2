#operators
# there are several types of operators
#Arithmetic Operators:
print(10+2) # + Addition
print(10-2) # - Subtraction
print(10*2) # * Multiplication
print(10/2) # / Divison
print(10%2) # % Modulus
print(10**2) # ** Exponentiation
print(10//2) # // Floor division
#Assignment Operators:
x=5
print(x)
x=5
x+=3
print(x)
x=5
x-=3
print(x)
x=5
x*=3
print(x)
x=5
x/=3
print(x)
x=5
x%=3
print(x)
x=5
x**=3
print(x)
x=5
x//=3
print(x)
x=5
x&=3
print(x)
x=5
x|=3
print(x)
x=5
x^=3
print(x)
x=5
x>>=3
print(x)
x=5
x<<=3
print(x)
x=5
print(x:=3)

#Comparison Operators:
x=3
y=2
print(x==y)
print(x!=y)
print(x>y)
print(x<y)
print(x>=y)
print(x<=y)

#Logical Operators:
x=3
print(x>0 and x<5)
print(x>10 or x<6)
print(not(x>0 and x<5))

#Identity Operators:
x=["wow", "that's crazy"]
y=["wow", "that's crazy"]
z=x
print(x is z)
print(x is y)
print(x==y)

#Membership Operators:
x=["wow", "that's crazy"]
print("wow" in x)
print("hello" not in x)

#Bitwise Operators:
print(6&3)
print(6|3)
print(6^3)
print(~3)
print(3<<2)
print(8>>2)

#Operator Precedence
print((6+3)-(6+3)) # Parentheses
print(100+ 5*3) # Multiplication, division, floor division, and modulus
print(100- 3**3) # Exponentiation
print(100+ ~3) # Unary plus, unary minus, and bitwise NOT
print(100 - 5*3) # Addition and subtraction
print(8 >> 4-2) # Bitwise left and right shifts
print(6 & 2+1) # Bitwise AND
print(6 ^ 2+1) # Bitwise XOR
print(6 | 2+1) # Bitwise OR
print(5 == 4+1) # Comparisons, identity, and membership operators
print(not 5 == 5) # Logical NOT
print(2 or 3 and 4) #AND
print(4 or 5+10 or 8) #OR
