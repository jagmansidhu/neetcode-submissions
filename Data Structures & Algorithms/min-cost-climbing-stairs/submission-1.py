class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # you can step either (i + 1) floor or the (i + 2) floor   
        # start at index 0 or 1
        # Thinking start at last index and move backwards
        # Then return if cost[0] > cost [1]

        n = len(cost)
        
        step1 = 0 
        step2 = 0 
        
        for i in range(n - 1, -1, -1):
            current = cost[i]
            if step1 < step2:
                current += step1
            else:
                current += step2
            
            step2 = step1
            step1 = current
            
        return step1 if step1 < step2 else step2


