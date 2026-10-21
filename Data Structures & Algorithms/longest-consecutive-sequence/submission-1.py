class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        m = set(nums)
        l = 0

        for i in nums:
            if (i-1) not in m:
                cur_l = 1
                while (i + cur_l) in m:
                    cur_l+=1
                l = max(cur_l, l)
        
        return l