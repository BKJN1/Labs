class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(length):
        print("Area is: ", length**2)

x = int(input("Enter length of square: "))
a = Square
a.area(x)