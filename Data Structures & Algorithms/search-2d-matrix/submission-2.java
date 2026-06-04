class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        // array[0] = row 0
        // get size/columns of that row with array[0].size
        // array.size will give how many rows in the arra

        // This is n^2

        for (int i = 0; i < matrix.length ; i ++) {
            int l = 0;
            int r = matrix[i].length;

            if (matrix[i][0] <= target && matrix[i][r - 1] >= target) {
                while (l < r) {
                    int mid = l + (r - l) / 2;

                    if (matrix[i][mid] == target) {
                        return true;
                    } else if (matrix[i][mid] > target) {
                        r = mid;
                    } else {
                        l = mid + 1;
                    }
                }                
            }
        }
        return false;    
    }
}
