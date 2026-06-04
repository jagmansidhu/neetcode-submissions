class Solution {
    public boolean isValidSudoku(char[][] board) {

        HashSet<Character> temp;

        // Row check
        for (int i = 0 ; i < 9 ; i ++) {
            temp = new HashSet<>();
            for (int j = 0 ; j < 9; j ++) {
                if (board[i][j] == '.') continue;

                if (temp.contains(board[i][j])) {
                    return false;
                }

                temp.add(board[i][j]);
            }
        }

        // Column check
        for (int i = 0 ; i < 9 ; i ++) {
            temp = new HashSet<>();
            for (int j = 0 ; j < 9 ; j ++) {
                if (board[j][i] == '.') continue;

                if (temp.contains(board[j][i])) {
                    return false;
                }

                temp.add(board[j][i]);
            }
        }

        for (int sq = 0; sq < 9; sq++) {
            temp = new HashSet<>();
            for (int i = 0; i < 3; i++) {
                for (int j = 0; j < 3; j++) {
                    int row = (sq / 3) * 3 + i;
                    int col = (sq % 3) * 3 + j;
                    if (board[row][col] == '.') {
                        continue;
                    }
                    if (temp.contains(board[row][col])) {
                        return false;
                    }
                    temp.add(board[row][col]);
                }
            }
        }

        return true;
    }
}
