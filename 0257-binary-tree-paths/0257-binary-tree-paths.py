# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[str]
        """
        result = []
        
        def dfs(node, path):
            if node is None:
                return
            
            path.append(str(node.val))
            
            if node.left is None and node.right is None:
                # leaf node — finalize this path
                result.append("->".join(path))
            else:
                dfs(node.left, path)
                dfs(node.right, path)
            
            path.pop()  # backtrack
        
        dfs(root, [])
        return result