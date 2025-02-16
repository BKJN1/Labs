def ff(x):
    y = 1
    while y <= x:
        yield y ** 2
        y += 1

a = int(input("enter a number: "))
for i in ff(a):
    print(i)

