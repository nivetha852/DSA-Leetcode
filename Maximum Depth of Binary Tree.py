# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def maxdepth(root):
            if root is None:
                return 0
            leftdepth = maxdepth(root.right)
            rightdepth = maxdepth(root.left)
            return 1 + max(leftdepth,rightdepth)
        return maxdepth(root)