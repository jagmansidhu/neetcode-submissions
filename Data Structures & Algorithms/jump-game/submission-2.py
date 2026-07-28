class Solution:
    '''
        Instead of thinking from left to right
        Think of left to right
        Start at the right and if a index to left + jump len >= this index 
        Then True else false

    '''
    def canJump(self, nums: List[int]) -> bool:
        i = 0

        reach = 0
        for n in range(len(nums) - 1, -1, -1):
            j_range = nums[n]
            if n + j_range >= reach:
                reach = n

        return True if reach == 0 else False
