def ff(x):
    y = 2
    while y <= x:
        yield y
        y += 2

a = int(input("enter a number: "))
b = []
for i in ff(a):
    b.append(str(i))
print (", ".join(b))


