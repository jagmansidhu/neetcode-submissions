class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #Lookin at this we need to determin all subsets
        # this means for 1, 2
            # [] [1] [2] [1,2]

        # list of lists 


        res = []
        cur = []
        def dfs(i):
            if i >= len(nums):
                res.append(cur[:])
                return
            cur.append(nums[i])
            dfs(i+1)
            cur.pop()
            dfs(i+1)

        dfs(0)
        return res

