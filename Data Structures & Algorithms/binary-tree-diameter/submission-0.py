# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# longest length between any two roots
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
         
        m = 0
        def dfs(r):
            nonlocal m
            if not r:
                return 0

            left = dfs(r.left)
            right = dfs(r.right)

            m = max(m, left + right)

            return 1 + max(left, right)


        dfs(root)
        return m
    