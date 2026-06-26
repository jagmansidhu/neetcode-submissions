class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row_len = len(board)
        col_size = len(board[0])

        # thinking - we first want to go through each col to find the first letter
        # if found than we check the characters beside and below it?
        # lets say we hae [0][2] (c)
        # We then need to check [0][1], [0][3], [1][2]
        # Lets say if [1][2] is the one then we have to do the check again
        # if not then we backtrack and go to next item

        # we need to track cur item i, j (Row col)

        # word[c] = the char we are looking for
        def backtrack(i, j, c) -> bool:
            # print(board[j][i])
            # our true case return True
            if c == len(word):
                return True

            # bounds check
            if (
                i >= row_len
                or j >= col_size
                or j < 0
                or i < 0
                or word[c] != board[i][j]
                or board[i][j] == '#'
            ):
                return False

            board[i][j] = '#'

            # We have 4 checks once character is found
            # up, left, down, right
            res = (
                   backtrack(i, j + 1, c + 1)
                or backtrack(i, j - 1, c + 1)
                or backtrack(i + 1, j, c + 1)
                or backtrack(i - 1, j, c + 1)
            )
            board[i][j] = word[c]
            return res

        # loop through every character until we find the character that maatches
        # using that character we will do the other checks and determine if this line works.
        for r in range(row_len):
            for c in range(col_size):
                if backtrack(r, c, 0):
                    return True

        return False
