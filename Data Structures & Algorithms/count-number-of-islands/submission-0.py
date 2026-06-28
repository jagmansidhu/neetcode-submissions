class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0

        COL = len(grid)
        ROW = len(grid[0])

        def dfs(i, j):
            if i < 0 or j < 0 or i >= COL or j >= ROW or grid[i][j] == "0":
                return

            grid[i][j] = "0"
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        for i in range(COL):
            for j in range(ROW):
                if grid[i][j] == "1":
                    dfs(i, j)
                    res += 1

        return res
