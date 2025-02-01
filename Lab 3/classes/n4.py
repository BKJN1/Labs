import math

class coord:
    def __init__(s, x, y):
        s.x = x
        s.y = y
    
    def move(s, x, y):
        direction = input("Enter direction (up, down, left, right): ").lower()
        units = int(input("Enter number of units to move: "))

        if direction == "up":
            s.y += units
        elif direction == "down":
            s.y -= units
        elif direction == "left":
            s.x -= units
        elif direction == "right":
            s.x += units
    
    def dist(s, other):
        return math.sqrt(((s.x - other.x) **2) + ((s.y - other.y)**2))
    
    def show(s):
        print("x:", s.x, ", y:", s.y)


point = coord(int(input("Enter x value: ")), int(input("Enter y value: ")))

while True:
    a = str(input("\nPrint 'q' if you want to quit \nWhat do you want? \nshow \nmove \ndist \n\n"))
    
    if a == 'q':
        break
    elif a == "show":
        point.show()
    elif a == "move":
        point.move()
    elif a == "dist":
        x2 = int(input("Enter x value of second point: "))
        y2 = int(input("Enter y value of second point: "))
        other = coord(x2,y2)
        print(f"dist: {point.dist(other):.2f}")