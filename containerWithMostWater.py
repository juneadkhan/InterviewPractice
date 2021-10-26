"""
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0).
Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.

Notice that you may not slant the container.

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

"""


# Sliding Window Solution
# Time: O(n), Space: O(1)
def maxArea(height: List[int]) -> int:
    maxArea = 0
    left, right = 0, len(height) - 1
    # Work From the outsides in
    while left < right:
        # The area can only be as tall as the smallest height. Thus min.
        area = (right-left) * min(height[left], height[right])
        if area > maxArea:
            maxArea = area
        # You want to look for the biggest heights the furthest out.
        # So if the height on the right is bigger, look at the next closest left height.
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return maxArea



# BRUTE FORCE
# Time: O(n^2), Space: O(1)
def maxArea(height: List[int]) -> int:
    maxArea = 0
    for i in range(len(height)):
        for j in range(i+1, len(height)):
            area = (j-i) * min(height[i], height[j])
            if area > maxArea:
                maxArea = area
    return maxArea
