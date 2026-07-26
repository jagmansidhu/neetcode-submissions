class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Start from O's we check its sorroundings until,
        we either get another O, and X or a out of bounds
        If the O reaches X's on all sides, we update that value
        Else go to next O


        Start from 'O's on edges and work in...
        """

        ROW = len(board)
        COL = len(board[0])
        dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def capture():
            q = deque()

            for r in range(ROW):
                for c in range(COL):
                    if (r == ROW - 1 or r == 0 or c == COL - 1 or c == 0) and board[r][c] == "O":
                        q.append((r, c))

                    
            while q:
                r,c = q.popleft()

                if board[r][c] == 'O':
                    board[r][c] = 'T'
                    for dr, dc in dir:
                        if 0 < r + dr < ROW -1 and 0 < c + dc < COL - 1:
                            q.append((r + dr,c + dc))


        capture()

        for r in range(ROW):
            for c in range(COL):
                if board[r][c] == 'T':
                    board[r][c] = 'O'
                elif board[r][c] == 'O':
                    board[r][c] = 'X'