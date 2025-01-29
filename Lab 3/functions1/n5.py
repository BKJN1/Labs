from itertools import permutations

def generate_permutations(x):
    return ["".join(perm) for perm in permutations(x)]
x = input("Enter a string: ")
perm_list = generate_permutations(x)
print(perm_list)