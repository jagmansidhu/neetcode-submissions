class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROW = len(heights)
        COL = len(heights[0])
        p, a = set(), set()
        res = []


        def dfs(r, c, visited, prevHeight):
            if ((r, c) in visited or
                r < 0 or c < 0 or
                r == ROW or c == COL or
                heights[r][c] < prevHeight
            ):
                return

            visited.add((r,c))
            dfs(r + 1, c, visited, heights[r][c])
            dfs(r, c + 1, visited, heights[r][c])
            dfs(r - 1, c, visited, heights[r][c])
            dfs(r, c - 1, visited, heights[r][c])

        for r in range(ROW):
            dfs(r, 0, p, heights[r][0])
            dfs(r, COL - 1, a, heights[r][COL - 1])

        for c in range(COL):
            dfs(0, c, p, heights[0][c])
            dfs(ROW - 1, c, a, heights[ROW - 1][c])

        for r, c in p:
            if (r,c) in p and (r,c) in a:
                res.append([r,c])


        return res



        

