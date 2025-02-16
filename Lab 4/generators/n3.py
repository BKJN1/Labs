def ff(x):
    y = 1
    while y <= x:
        if y%3==0 and y%4==0:
            yield y
        y += 1

a = int(input("enter a number: "))
for i in ff(a):
    print(i)