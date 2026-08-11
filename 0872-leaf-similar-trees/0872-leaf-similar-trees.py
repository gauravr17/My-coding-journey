# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: Optional[TreeNode]
        :type root2: Optional[TreeNode]
        :rtype: bool
        """
        def get_leaves(node):
            if node is None:
                return []
            if node.left is None and node.right is None:
                return [node.val]
            return get_leaves(node.left) + get_leaves(node.right)

        return get_leaves(root1) == get_leaves(root2)