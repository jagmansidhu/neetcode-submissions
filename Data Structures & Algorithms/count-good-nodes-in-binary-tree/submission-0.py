# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# good node if node is greater than prior node 
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0

        def loop(prevmax:int, root: TreeNode):
            nonlocal res
            if prevmax <= root.val:
                res += 1


            if root.left:
                loop(max(prevmax, root.val), root.left)
            if root.right:
                loop(max(prevmax, root.val), root.right)
            
        loop(root.val, root)
        
        return res
        
            
