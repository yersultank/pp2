#global variables
x="Yersultan"
def myfunc():
    print("my name is", x)
myfunc()

x="Yersultan"
def myfunc():
    x="Anton"
    print("my name is", x)
myfunc()

#To create a global variable inside a function, you can use the global keyword.
def myfunc():
    global x
    x="dosymzhan"
myfunc()
print("my name is", x) #now global variable x changed from Yersultan to dosymzhan.