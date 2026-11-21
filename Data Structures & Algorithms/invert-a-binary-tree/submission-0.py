# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        dfs = deque([root])

        while dfs:
            cur = dfs.popleft()

            temp = cur.right
            cur.right = cur.left
            cur.left = temp
            
            if cur.right:
                dfs.append(cur.right)

            if cur.left:
                dfs.append(cur.left)


        return root



        