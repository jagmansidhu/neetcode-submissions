class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Start from O's we check its sorroundings until,
        we either get another O, and X or a out of bounds
        If the O reaches X's on all sides, we update that value
        Else go to next O
        """

        ROW = len(board)
        COL = len(board[0])
        

        def dfs(r, c, visited) -> bool:
            if r > ROW - 1 or r < 0 or c > COL - 1 or c < 0:
                return False

            if board[r][c] == 'X' or (r,c) in visited:
                return True

            visited.add((r,c))

            return dfs(r + 1, c, visited) and dfs(r - 1, c, visited) and dfs(r, c + 1, visited) and dfs(r, c - 1, visited)

        for r in range(ROW):
            for c in range(COL):
                if board[r][c] == 'O':
                    res = dfs(r, c, set())
                    if res:
                        board[r][c] = 'X'
