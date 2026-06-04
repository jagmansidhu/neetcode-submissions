class Solution {
    public int[] productExceptSelf(int[] nums) {
        int prev = 1;
        int[] res = new int[nums.length];

        for (int i = 0; i < nums.length ; i++) {
            int cur = prev;
            for (int j = i + 1 ; j < nums.length ; j++) {
                cur *= nums[j];
            }

            res[i] = cur;
            prev *= nums[i];
            cur = 0;
        }
        
        return res;
    }
}  
