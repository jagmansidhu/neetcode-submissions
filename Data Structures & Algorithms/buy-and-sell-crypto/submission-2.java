class Solution {
    public int maxProfit(int[] prices) {
        // Two pointer?? 
        // left is alsways pointing lft and if left higher than right index rigt --
        // if right higher than left left++ ???
        int max = 0;
        int left = 0;
        int right = 1;

        while (right < prices.length) {
            int l = prices[left];
            int r = prices[right];
            if (l < r) {
                max = Math.max(max, r - l);
            } else {
                left = right;
            }

            right ++;
        }

        return max;
    }
}
