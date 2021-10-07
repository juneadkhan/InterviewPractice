"""
Given an array, rotate the array to the right by k steps, where k is non-negative.

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

"""

def rotate(self, nums: List[int], k: int) -> None:
    nums[:] = nums[-k:] + nums[:-k]


# O(n) Time, O(1) Space as does it In-Place

# nums[:] used to change all values of nums to new Array

# nums[-k:] would be all values from kth from last index to the end. 
# e.g. for [1,2,3,4,5,6,7], nums[-k:] -> [5, 6, 7]

# nums[:-k] would be all values from start to kth from last index. 
# e.g. for [1,2,3,4,5,6,7], nums[:-k] -> [1,2,3,4]

# Thus nums[-k:] + nums[:-k] -> [5,6,7,1,2,3,4]