def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

nums = list(map(int, input("Enter numbers separated by spaces: ").split()))

prime_numbers = list(filter(lambda x: is_prime(x), nums))

print("Prime numbers:", prime_numbers)