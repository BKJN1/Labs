
def game(F, n):
    num = (5 / 9) * (F - 32)
    num = int(num)
    x=""
    while x!=num:
        x = int(input("Take a guess. "))
        if x<num:
            print("Your guess is too low.")
        elif x>num:
            print("Your guess is too high.")
        n+=1
    return n

F = int(input("Enter a tempreture in F and try to guess it in C! "))

n=0
n=game(F, n)
print("Good job! You guessed my C in "+str(n)+" guesses!")