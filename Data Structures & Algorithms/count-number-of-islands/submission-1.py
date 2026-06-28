class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0

        COL = len(grid)
        ROW = len(grid[0])

        def dfs(i, j):
            if i < 0 or j < 0 or i >= COL or j >= ROW or grid[i][j] == "0":
                return

            # As we go through the "1"'s in the islands we convert them to "0"
            # This is how we track what cells have been reached and which have not been reached.
            grid[i][j] = "0"
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        # Go through every item in graph
        for i in range(COL):
            for j in range(ROW):
                # If item in graph == 1 lets start search for island
                if grid[i][j] == "1":
                    dfs(i, j)
                    res += 1

        return res
