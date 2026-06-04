class Solution {
    public int findMin(int[] nums) {
        int min = Integer.MAX_VALUE;

        int l = 0;
        int r = nums.length - 1;

        if (r == 0) return nums[0];

        while (l <= r) {

            min = Math.min(min, Math.min(nums[l], nums[r]));


            l++;
            r--;
        }

        return min;
        
    }
}
