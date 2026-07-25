class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])
        fresh = 0
        queue = deque()
        routes = ((1,0),(0,1),(-1,0),(0,-1))

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 2:
                    queue.append([r,c])
                if grid[r][c] == 1:
                    fresh += 1

        # only rotten if horizontal or veritical fruit is rotten:
        # Diagonal does not count

        count = 0
        while fresh > 0 and queue:
            for q in range(len(queue)):
                r,c = queue.popleft()

                for dr, dc in routes:
                    row = r + dr
                    col = c + dc

                    if (row in range(ROW)) and (col in range(COL)) and (grid[row][col] == 1):
                        fresh -= 1
                        grid[row][col] = 2
                        queue.append([row,col])

            count += 1

        print(fresh)

        return count if fresh == 0 else -1





