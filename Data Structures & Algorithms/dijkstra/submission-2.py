class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        # n = number of verticies
        # Edges (u,v,w)
        # src - start node
        # Step 1 -- Adjacency list

        e = collections.defaultdict(list)

        for u,v,w in edges:
            e[u].append((v,w))

        # queue = (dist/path, node)
        # since this question is asking for smallest value we will use min heap here
        q = [(0, src)]

        # visited keeps track of already visited
        # If we already visited than we have used the min way to get there so others will be forgotton essentially

        # here is where go through graph and find min path
        res = {}
        while q:
            dist, n1 = heapq.heappop(q)

            if n1 in res:
                continue
            res[n1] = dist

            for v, w in e[n1]:
                if v not in res:
                    cur_dist = dist + w
                    heapq.heappush(q, (cur_dist, v))

        for i in range(n):
            if i not in res:
                res[i] = -1

        return res