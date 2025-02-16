def squares(a, b):
    for num in range(a, b + 1):
        yield num ** 2

a = int(input("enter 1st number: "))
b = int(input("enter 2nd number: "))
for square in squares(a, b):
    print(square)