class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # 1 == land
        # 0 == water
        # horizontal or vertical is connection of island
        # ["0","0","0","0","0"],
        # ["0","0","0","0","0"],
        # ["0","0","0","0","1"],
        # ["0","0","0","0","0"]

        # edge cases - Columns - -1 & Col.length(Assuming .size is 0 based) + 1
        # Rows - -1 & row.length + 1

        # count tracking as well


        ROW = len(grid)
        COL = len(grid[0])

        island_count = 0
        def search(r, c):
            if r < 0 or c < 0 or r >= ROW or c >= COL or grid[r][c] == "0":
                return


            grid[r][c] = "0"

            search(r + 1, c)
            search(r - 1, c)
            search(r, c + 1)
            search(r, c - 1)
            

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == "1":
                    # This search will looks at right left down up and see
                    # Where there are 1's
                    island_count += 1
                    search(r,c)


        return island_count

