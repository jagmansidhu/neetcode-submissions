# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True


        # First 2 levels
        # Root; Doesnt matter - inf and + inf
        # Level 1 lef; -inf and root.val = As long as less than root it good
        # Level 1 right; root.val and + inf = As long as greater than root it good
        # Level 2 as we go only left or only right there is no outer bound
        #   But if we go lef then right our values update and we get in the ranges we need to be
        # Example Cur vale, Left = 1 and Right = 2
                # As long as cur cal is greater than left and less than righ we chill
        q = deque([(root, float("-inf"), float("inf"))])

        while q:
            node, left, right = q.popleft()
            if not (left < node.val < right):
                return False
            if node.left:
                q.append((node.left, left, node.val))
            if node.right:
                q.append((node.right, node.val, right))

        return True