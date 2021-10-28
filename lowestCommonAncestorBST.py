"""
Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

According to the definition of LCA on Wikipedia: 
“The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # Time: O(log(n))
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Since it is a BST, We know we can compare with the root to determine what side a node will be on.
        # If 2 nodes are on different sides, we know their common ancestor is the node at which this first occured.
        if p.val < root.val < q.val or q.val < root.val < p.val:
            return root
        # The 2nd Option is if the root is one of the nodes. This means one of it's subnodes will be the other value, making this the LCA.
        elif p.val == root.val or q.val == root.val:
            return root
        # If neither, we must continue to traverse.
        # Traverse left if both q and p are less than the root and right if otherwise.
        if q.val < root.val and p.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return self.lowestCommonAncestor(root.right, p, q)

        