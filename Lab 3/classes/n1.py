class String:
    def __init__(self):
        self.txt = ""

    def getString(self):
        x = input("Enter a string: ")
        self.txt += x
    
    def printString(self):
        print(self.txt.upper())

a = String()
a.getString()
a.printString()