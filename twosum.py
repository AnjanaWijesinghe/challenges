'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
'''

def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(len(nums)-i-1):
            if (nums[i] + nums[j+i+1]) == target:
                return [i, j+i+1]
        

def twoSum2(nums, target):
    seen = {}
    for i, value in enumerate(nums):
        # deduct the current number to get the required value
        remaining = target - nums[i]
        
        if remaining in seen:
            # check if the required value is in the seen dict
            # if yes, get the number and return with it
            return [i, seen[remaining]]
        
        # if not in the seen dict, add it
        seen[value] = i 
            

print(twoSum2([3, 4, 5, 6], 9))
