class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int[] res = new int[2];
        
        int l = 0;
        int r = numbers.length - 1;
        while (l < r) {
            int nr = numbers[r];
            int nl = numbers[l];
            if (nr + nl == target) {
                res[1] = r + 1;
                res[0] = l + 1;
                break;
            } else if (nr + nl > target) {
                r--;
            } else {
                l++;
            }
            
        }

        return res;
    }
}
