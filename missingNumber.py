"""
Given an array nums containing n distinct numbers in the range [0, n], 
return the only number in the range that is missing from the array.

Input: nums = [3,0,1]
Output: 2
Explanation: n = 3 since there are 3 numbers, 
so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.

"""

# O(n) Time, O(1) Space
def missingNumber(nums: List[int]) -> int:
    mini = min(nums) # O(n)
    maxi = max(nums) # O(n)
    
    for i in range(mini, maxi): # O(n)
        if i not in nums:
            return i
    if mini == 0:
        return maxi+1
    else:
        return mini-1