class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROW = len(grid)
        COL = len(grid[0])
        visited = set()

        places = [(-1,0), (1,0), (0,-1), (0,1)]

        queue = deque()
        # We add all doors here
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 0:
                    queue.append([r, c])
                    visited.add((r, c))

        # This checks around the current block
        # If the blocks around are INF then we add then to visited, else we just return
        def bfs(r, c):
            if r < 0 or c < 0 or r >= ROW or c >= COL or grid[r][c] == -1 or (r,c) in visited:
                return
            visited.add((r, c))
            queue.append([r, c])

        distance = 0
        # BFS queue/loop
        # Distance increases by 1 for each time we go through queue
        while queue:
            for q in range(len(queue)):
                r,c = queue.popleft()
                grid[r][c] = distance

                for a, b  in places:
                    bfs(r + a, c + b)
            distance += 1


        return
