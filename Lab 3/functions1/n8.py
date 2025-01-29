def check(nums):
    for i in range(0, len(nums)):
        if nums[i]==7 and nums[i-1]==0 and nums[i-2]==0:
            return True
    return False

nums = list(map(int, input("Enter numbers separated by spaces: ").split()))
print("true") if check(nums) else print("false")