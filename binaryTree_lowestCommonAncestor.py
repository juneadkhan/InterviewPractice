"""
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia:
“The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # Time: O(n), Space: O(n)
    """
    Works by going to very bottom of tree and backtracking.
    If the root is null, return null
    Keep going until you find matches of q and p.
    Then backtrack, until leftTree and rightTree are not null.

    LCA of p = 6, q = 4

                    5 (This is the LCA, since  leftTree and rightTree are both not null)
                   / \
              (6) 6   2 (4)
                     / \
                (n) 7   4 (4)
                   / \
                  n   n
    """
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Check if Root is null, if it is return null
        if root == None:
            return None
        
        # Check if the root is one of P or Q. if it is, return it.
        if root == p or root == q:
            return root
        
		# Look for p/q in the left subtree
        leftTree = self.lowestCommonAncestor(root.left, p, q)
		
		# Look for p/q in the right subtree
        rightTree = self.lowestCommonAncestor(root.right, p, q)
        
		# If neither of the left/right subtrees are null. This means one of P and Q was found in each, which means this is LCA.
        if leftTree != None and rightTree != None:
            return root
        
		# If not, this means one of the subtrees is empty, so the LCA will be the one that is not empty.
        # If both are null, it will just return null
        if leftTree:
            return leftTree
        else:
            return rightTree
        
        