class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        cur = []
        use = [False] * len(nums)

        def dfs():
            if len(cur) == len(nums):
                res.append(cur[:])
                return

            for i in range(len(nums)):
                if not use[i]:
                    cur.append(nums[i])
                    use[i] = True
                    dfs()
                    cur.pop()
                    use[i] = False

        dfs()
        return res