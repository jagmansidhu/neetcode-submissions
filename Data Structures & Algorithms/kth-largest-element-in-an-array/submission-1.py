class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        l = [-x for x in nums]

        heapq.heapify(l)

        res = 0
        while k != 0:
            res = -heapq.heappop(l)
            k -= 1

        return res