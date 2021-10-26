"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

"""

# Time: O(n), Space: O(1)
def maxSubArray(nums: List[int]) -> int:
    maxSum = nums[0] # Is the first value.
    curSum = 0
    
    # Iterate through the array
    for i in nums:
        print(maxSum, curSum)
        if curSum < 0: # If the current sum is negative, reset it to 0.
            curSum = 0
        curSum += i 
        maxSum = max(maxSum, curSum) 
    return maxSum
