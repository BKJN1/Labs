def check(nums):
    for i in range(0, len(nums)):
        if nums[i]==3 and nums[i-1]==3:
            return True
    return False

nums = list(map(int, input("Enter numbers separated by spaces: ").split()))
print("true") if check(nums) else print("false")