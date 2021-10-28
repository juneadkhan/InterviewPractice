"""
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Input: root = [3,9,20,null,null,15,7]
Output: 3

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Added optinal paramter depth. (default = 0)
    def maxDepth(self, root: Optional[TreeNode], depth = 0) -> int:
        if root == None:
            return depth
        # At each call, depth increases by 1. Will stop calling once it reaches bottom of tree. 
        # Returns max of left/right sub-trees.
        return max(self.maxDepth(root.left, depth + 1), self.maxDepth(root.right, depth + 1))
        