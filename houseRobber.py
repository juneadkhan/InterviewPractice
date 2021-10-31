"""
You are a professional robber planning to rob houses along a street.
Each house has a certain amount of money stashed, the only constraint stopping you from robbing
each of them is that adjacent houses have security systems connected and it will automatically
contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house,
return the maximum amount of money you can rob tonight without alerting the police.

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

"""

# Time: O(n), Space: O(1)
def rob(nums: List[int]) -> int:
    # Will keep a running count of max robbable
    rob2ago, rob1ago = 0, 0
    
    for i in nums:
        # Comparing total through last house with current house + total from 2 houses ago.
        # rob2ago represents 2 houses ago
        # rob1ago represents 1 house ago.
        # max(i+rob2ago [current + 2 houses ago], rob1ago [last house])

        rob2ago, rob1ago = rob1ago, max(i+rob2ago, rob1ago)

        # rob2ago becomes the last house. 
        # rob1ago becomes the max of potential vals.
    
    return rob1ago # return the last value which will be the max money possible