class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # you can step either (i + 1) floor or the (i + 2) floor   
        # start at index 0 or 1
        # Thinking start at last index and move backwards
        # Then return if cost[0] > cost [1]
        memo = [-1] * len(cost)

        def dfs(i):
            if i >= len(cost):
                return 0

            if memo[i] != -1:
                return memo[i]
            
            memo[i] = cost[i] + min(dfs(i+1), dfs(i+2))
            return memo[i]



        return min(dfs(0), dfs(1))


