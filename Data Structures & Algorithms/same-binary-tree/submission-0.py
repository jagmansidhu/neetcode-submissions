# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def check (l, r) -> bool:
            if not l and not r:
                return True

            if not l or not r:
                return False
            
            if l.val != r.val:
                return False

            return check(l.right, r.right) and check(l.left, r.left)

        return check(p, q)