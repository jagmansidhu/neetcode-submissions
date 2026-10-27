class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        def dfs(i, cur):
            if i > len(nums) - 1:
                res.append(cur[:])
                return

            cur.append(nums[i])

            dfs(i+1, cur)
            cur.pop()
            dfs(i+1, cur)


        '''
            i = 0 
            cur.append[nums[0]]
        '''
            



        dfs(0, [])
        return res