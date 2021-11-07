"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Because nums[0] + nums[1] == 9, we return [0, 1].

Input: nums = [3,2,4], target = 6
Output: [1,2]

"""

class Solution:
    # Time: O(n), Space: O(n)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        store = {} # Store remainders and associated indexes
        
        for i in range(len(nums)):        
            # If you find a number that is a remainder, return the current index and the index of the number that when subtracted by target gives you the remainder.
            if nums[i] in store:
                return [store[nums[i]],i]
            # Otherwise, add the remainder to store as the key, with the index as the value
            else:
                store[target - nums[i]] = i