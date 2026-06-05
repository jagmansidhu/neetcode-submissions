class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        m = {}

        for i, n in enumerate(nums):
            t = target - n
            if t in m:
                return [m[t], i]
            m[n] = i
            