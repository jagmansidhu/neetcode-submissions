class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # kth 
        # do i do the euclidean distance first put into the list and then heapify?
        # map ? that take all keys and hepify them
        # once we find the one we want we do map[x] 

        r = []
        for l in points:
            x1 = l[0]
            y1 = l[1]
            m = math.sqrt(x1**2 + y1**2)
            r.append((m, l))

        res = []
        heapq.heapify(r)

        while k != 0 and r:
            size, points = heapq.heappop(r)
            res.append(points)
            k -= 1

        return res
