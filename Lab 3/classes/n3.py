class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(length):
        print("Area is: ", length**2)

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(length, width):
        print("Area is: ", length * width)

x = int(input("Enter length of Rectangle: "))
y = int(input("Enter width of Rectangle: "))
Rectangle.area(x, y)