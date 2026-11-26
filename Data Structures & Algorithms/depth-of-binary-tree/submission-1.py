# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q = deque([root])

        count = 0
        while q:
            cur = deque()


            count += 1

            while q:
                even_cur = q.pop()
                if even_cur:
                    if even_cur.right:
                        cur.append(even_cur.right)
                    if even_cur.left:
                        cur.append(even_cur.left)


            q = cur

        return count