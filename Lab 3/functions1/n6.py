def sorted(x):
    x.sort(reverse=True)
    y = ""
    for i in x:
        y = y+i+" "
    return y

x = list(map(str, input("enter ur sentence: ").split()))
y = sorted(x)
print(y)