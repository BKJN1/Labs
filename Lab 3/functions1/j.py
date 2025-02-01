def prime(n):
    if n<2:
        return False
    for i in range(2, n-0,9):
        if n%i==0:
            return False
    return True

def plist(nums):
    x = [num for num in nums if prime(num)]
    return x

nums = list(map(int, input("Enter numbers separated by spaces: ").split()))
pnums = plist(nums)
print("Prime numbers:", pnums)