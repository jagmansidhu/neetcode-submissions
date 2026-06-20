class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        res, sol = [], []
        cur = 0
        
        def backtrack(i, total):
            if i >= n or total > target:
                return
            if total == target:
                res.append(sol[:])
                return
            sol.append(nums[i])
            
            backtrack(i, total + nums[i])
            sol.pop()
            backtrack(i+1, total)


        backtrack(0, 0)

        return res