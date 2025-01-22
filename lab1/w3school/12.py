#strings
print("hello")

#is the same as:
print('hello')

#You can use quotes inside a string, as long as they don't match the quotes surrounding the string:
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

#this is how you announce a string:
x="Hello"
print(x)

#for assigning multyline strings:
y=""" multyline
string
writing
"""
print(y)

#access each character from string by index:
x="Hello world"
print(x[1])

#loopint through strings:
for i in "Yersultan":
    print(i)

#To get the length of a string, use the len() function.
print(len(x))

#To check if a certain phrase or character is present in a string, we can use the keyword in.
b="programming principles II"
print("program" in b)
if "II" in b:
    print("yes")
print("computer" not in b)
if "computer" not in b:
    print("yes")
