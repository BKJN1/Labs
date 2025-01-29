def prime(n):
    if n<2:
        return False
    for i in range(2, int(n**(0.5)) + 1):
        if n%i==0:
            return False
    return True

def plist(nums):
    return [num for num in nums if prime(num)]

nums = list(map(int, input("Enter numbers separated by spaces: ").split()))
pnums = plist(nums)
print("Prime numbers:", pnums)