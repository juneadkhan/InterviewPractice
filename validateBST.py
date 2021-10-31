"""
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

Input: root = [2,1,3]
Output: true

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        INPUT: root node of type TreeNode
        OUTPUT: Boolean as to whether it is a BST or not
        
        Con1: All nodes of Left Subtree < current node
        Con2: All nodes of Right Subtree > current node
        Con3: Both left and right subtrees should be BSTs
        
        - Do a DFS on left and right subtrees.
        - Compare each value in the left and right subtrees with the root.val to see if its < >
        - Recurse on left and right subtrees to see if they are also valid BSTs
        """
        
        # When you reach the bottom you return True as if it wasn't true by now it would have already returned False.
        if root == None:
            return True
        
        # Find all nodes on left and right
        leftVals = self.dfs(root.left)
        rightVals = self.dfs(root.right)
        
        # If any of the nodes are incorrectly > or < root.val then return False
        for i in leftVals:
            if i >= root.val:
                return False
            
        for i in rightVals:
            if i <= root.val:
                return False
            
        # Check if left and right subtrees are BSTs.
        return self.isValidBST(root.left) and self.isValidBST(root.right)
            
        
    # Depth First Search Implemntation
    def dfs(self, root):
        visited = []
        stack = [root]
        while stack:
            vertex = stack.pop()
            if vertex == None:
                continue
            if vertex.val in visited:
                continue
            else:
                visited.append(vertex.val)
                stack.extend([vertex.left, vertex.right])
        return visited
            
        