def ch(x):
    if len(x) % 2 != 0:
        x = x[:len(x)//2] + x[(len(x)//2) + 1:]  
    
    n = len(x) // 2
    y1 = x[:n]  
    y2 = x[-n:][::-1] 
    
    if y1 == y2:
        return True
    return False

x = str(input("give string: ").lower().replace(" ", ""))
print("Yes") if ch(x) else print("no")