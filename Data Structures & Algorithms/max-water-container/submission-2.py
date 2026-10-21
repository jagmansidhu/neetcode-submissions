class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1

        res = 0
        while l < r:
            l_height = heights[l]
            r_height = heights[r]

            area = (r - l) * min(l_height, r_height)
            res = max(res, area)

            if l_height <= r_height:
                l += 1
            else:
                r -= 1


        return res
