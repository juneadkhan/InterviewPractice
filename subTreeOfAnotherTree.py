"""
Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

Input: root = [3,4,5,1,2], subRoot = [4,1,2]
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
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        # If the subRoot is None, then its definetly a subtree
        if subRoot == None:
            return True
        
        # If root is None, but the subRoot is not, it cannot be a subtree.
        if root == None:
            return False
        
        # If we reach a node where the root and subRoot are equal in value
        if root.val == subRoot.val:
            # Check if the left trees and right trees are the same, if they are then return True since that means it has to be a subRoot.
            if self.isSame(root.left, subRoot.left) and self.isSame(root.right, subRoot.right):
                return True 
            
        # If the current root is not a subtree, check if the left or the right subTrees are.
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
    def isSame(self, root, subRoot):
                
        # If both are None, they are the same
        if root == None and subRoot == None:
            return True
        
        # If one of them is none and the other is not, they are definetly not the same
        if root == None or subRoot == None:
            return False
        
        # If the current node is equal in value, check if all the left and right nodes are also the same
        if root.val == subRoot.val:
            return self.isSame(root.left, subRoot.left) and self.isSame(root.right, subRoot.right)
        
     