import math

a = float(input("Enter the number of sides: "))
b = float(input("Enter the length of a side: "))

d = (a * b ** 2) / (4 * math.tan(math.pi / a))
print(f"Area of the regular polygon is {d:.2f}")    