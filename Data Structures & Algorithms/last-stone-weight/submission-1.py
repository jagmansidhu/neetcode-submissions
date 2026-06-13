class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # We make every number negative so this is more like heap max
        # for example if we have [1,2,5,7 , -1]
        # we will now have [-1, -2, -5 ,-7, 1]
        # -7 will be on top of the list and when we pop then -5 will be there
        # as we continue to pop ...
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            node1 = heapq.heappop(stones)
            node2 = heapq.heappop(stones)
            
            if node2 > node1:
                heapq.heappush(stones, node1 - node2)

            
        stones.append(0)
        return abs(stones[0])



        