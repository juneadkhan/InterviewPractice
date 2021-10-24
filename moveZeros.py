"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

"""

# Time: O(n), Space: O(1)
def moveZeroes(nums: List[int]) -> None:
    count = 0
    for i in nums:
        # If number is not zero
        if i != 0:
            nums[count] = i # Update list from start to have non 0 vals
            count += 1 # Count the number of non 0 values
    # Update rest of the list to be 0s
    for i in range(count, len(nums)):
        nums[i] = 0
            