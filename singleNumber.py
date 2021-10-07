"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

Input: nums = [4,1,2,1,2]
Output: 4

"""

def singleNumber(nums):
    
    counts = Counter(nums) # Counts all occurences of values in nums
    
    for value, count in counts.items(): # For all the values and their counts
        if count == 1: # if the count is 1
            return value # Return that value as that is the one that has only 1 element.