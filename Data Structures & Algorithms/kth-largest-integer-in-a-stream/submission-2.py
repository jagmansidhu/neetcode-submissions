class KthLargest:

    # we only need k values in our heap since the kth value will be the largest one
    # so on intializing we heapify and then once heapify is done we pop() all values until we get kth size arr
    # Heap pop() removes the smalles element each time
    # So if k = 3 and nums = [1,2,3,4,5,5]
    # We will pop 1,2,3 and now we have [4, 5, 5]
    # So now we can just return nums[0] as this will always be the kth largest element
    def __init__(self, k: int, nums: List[int]):
        heapq.heapify(nums)
        self.kth = k
        self.arr = nums
        while len(self.arr) > k:
            heapq.heappop(self.arr)
        

    def add(self, val: int) -> int:
        heapq.heappush(self.arr, val)
        if len(self.arr) > self.kth:
            heapq.heappop(self.arr)
        return self.arr[0]

        
        
