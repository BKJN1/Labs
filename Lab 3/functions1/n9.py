import math

def volume(r):
    return (4/3) * math.pi * (r ** 3)

r = float(input("Enter the radius of the sphere: "))
v = volume(r)
print("Volume of the sphere:", v)