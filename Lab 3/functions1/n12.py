def histogram(nums):
    for i in range(len(nums)):
        print("*" * (nums[i]))  
nums = list(map(int, input("Enter numbers separated by spaces: ").split()))

histogram(nums)