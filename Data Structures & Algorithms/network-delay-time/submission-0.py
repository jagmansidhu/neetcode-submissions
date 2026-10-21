class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # n nodes -- 1 -> n
        # ui = source nodes
        # vi = target node
        # ti = time ui -> vi

        # k the signal node
        # min time for all of the n nodes to receive signal
        # if not posible for a node return -1

        # times[i] = (ui,vi,ti)


        edges = collections.defaultdict(list)

        for u, v, t in times:
            edges[u].append((v,t))

        minheap = [(0, k)]
        visited = set()
        t = -1

        while minheap:
            dist, v = heapq.heappop(minheap)

            if v in visited:
                continue
            visited.add(v)

            t = max(dist, t)

            for node, w in edges[v]:
                if node not in visited:
                    new_dist = dist + w
                    heapq.heappush(minheap, (new_dist, node))

        return t if len(visited) == n else -1


                
                

            



