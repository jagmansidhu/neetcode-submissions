class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])

        m = 0

        def dfs(i, j):
            if i < 0 or j < 0 or i >= ROW or j >= COL or grid[i][j] == 0:
                return 0

            grid[i][j] = 0

            return 1 + dfs(i - 1, j) + dfs(i + 1, j) + dfs(i, j - 1) + dfs(i, j + 1)

        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == 1:
                    m = max(dfs(i, j), m)

        return m
