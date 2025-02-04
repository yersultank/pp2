class str:
    def getstring(self):
        self.text=input("Type something-")
    def printstring(self):
        print("Text with upper case "+ self.text.upper())
mystring=str()
mystring.getstring()
mystring.printstring()

