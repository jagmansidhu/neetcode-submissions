# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        l_q = deque([p])
        r_q = deque([q])

        while l_q and r_q:
            l = l_q.popleft()
            r = r_q.popleft()


            if not l and not r:
                continue

            if r is None or l is None or l.val != r.val:
                return False

            l_q.append(l.right)
            l_q.append(l.left)
            r_q.append(r.right)
            r_q.append(r.left)

        return True