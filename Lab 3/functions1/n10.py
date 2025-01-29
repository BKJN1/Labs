def uni(nums):
    x = []
    for i in nums:
        if i not in x:
            x.append(i)
    return x

nums = list(map(int, input("Enter numbers separated by spaces: ").split()))
print(uni(nums))