#booleans represent one of two values: True or False
print(10>9)

print(10==9)

print(10<9)

x=100
y=50
if x>y:
    print("x is greater than y")
else:
    print("y is greater than x")

print(bool("Hello"))

print(bool(15))

print(bool(x))

a="abcd"
print(bool(a))

print(bool(["pen", "pencil", "note"]))

#below are examples of False values:
print(bool(False))

print(bool(None))

print(bool(0))

print(bool(""))

print(bool(()))

print(bool([]))

print(bool({}))


def func():
    return True
print(func())
if func():
   print("yes")
else:
   print("no")
 
t=1045
print(isinstance(t,int))