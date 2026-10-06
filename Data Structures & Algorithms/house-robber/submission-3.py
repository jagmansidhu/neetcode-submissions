class Solution:
    def rob(self, nums: List[int]) -> int:
        # [2,3,4,3,9,8,8,9]

        #Hash map? store value for each value in that house
        # For example for 2 the max value is value of house[4] + house[2]
        # But then for 4 Max value can be Max value of House[9] + house[4]
        # or house[8] + house[4]... 

        memo = [-1] * len(nums)

        def dfs(i) :
            if i >= len(nums):
                return 0
            if memo[i] != -1:
                return memo[i]
            
            memo[i] = max(nums[i] + dfs(i+2), dfs(i+1))            

            return memo[i];

        return dfs(0)

        