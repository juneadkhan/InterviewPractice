"""
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

Input: p = [1,2,3], q = [1,2,3]
Output: true

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # Time: O(n), Space: O(n)
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        INPUT: 2 Tree Nodes p and q.
        OUTPUT: Boolean. True if they are identical. False if not.
        
        Condition: left and right children must be the same for every node.
        """

        # When it gets to the bottom of the tree, the left and right nodes will both be None. Thus return True
        if p == None and q == None:
            return True
        
        # If one is None and the other is not, return False
        if (p == None) ^ (q == None): 
            return False
                
        # If the values are the same, make sure their left and right trees are the same.
        if p.val == q.val:        
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        
        return False
        
        