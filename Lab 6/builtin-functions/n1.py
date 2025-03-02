from math import prod

def multiply_list_numbers(numbers):
    return prod(numbers)

numbers = [1, 2, 3, 4, 5]
result = multiply_list_numbers(numbers)
print(f"The product of the numbers in the list is: {result}")