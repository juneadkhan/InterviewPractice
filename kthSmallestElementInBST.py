"""
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

Input: root = [3,1,4,null,2], k = 1
Output: 1

"""


# Time: O(n) - Recursive In-Order Traversal
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        return self.traversal(root)[k-1]
        
    def traversal(self, root):
        result = []
        if root:
            result.extend(self.traversal(root.left))
            result.append(root.val)
            result.extend(self.traversal(root.right))
        return result


# Time: O(H + k) - Iterative In-Order Traversal, stopping early
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        INPUT: root of a TreeNode.
        OUTPUT: the value int of the kth smallest element.
        """
        stack = []
        
        while True:
            while root:
                # Go all the way down to the left until None and add all to stack.
                stack.append(root)
                root = root.left
            # 
            root = stack.pop()
            k -= 1
            if not k:
                return root.val
            root = root.right
            
        