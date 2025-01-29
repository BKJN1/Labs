
import random

def game(num, n):
    x=""
    while x!=num:
        x = int(input("Take a guess. "))
        if x<num:
            print("Your guess is too low.")
        elif x>num:
            print("Your guess is too high.")
        n+=1
    return n

name = str(input("Hello! What is your name? "))
num = random.randint(1, 20)
n=0
print("Well, "+ name +", I am thinking of a number between 1 and 20.")

n=game(num, n)
print("Good job, " +name+"! You guessed my number in "+str(n)+" guesses!")