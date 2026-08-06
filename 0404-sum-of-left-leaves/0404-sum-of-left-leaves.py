# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0
        
        total = 0
        
        if root.left:
            if not root.left.left and not root.left.right:
                # left child is a leaf
                total += root.left.val
            else:
                # left child has children, recurse into it
                total += self.sumOfLeftLeaves(root.left)
        
        # always recurse into the right side (it just can't contribute leaves directly here)
        total += self.sumOfLeftLeaves(root.right)
        
        return total