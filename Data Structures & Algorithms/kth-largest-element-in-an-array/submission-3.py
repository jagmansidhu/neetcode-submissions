class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        heapq.heapify_max(nums)
        # print(nums)

        while k > 1 and len(nums) > 0:
            heapq.heappop_max(nums)
            # print(nums)
            k -= 1



        return nums[0] if len(nums) > 0 else -1

        