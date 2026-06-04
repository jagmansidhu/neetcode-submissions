class Solution {
    public int[] productExceptSelf(int[] nums) {
        int cur = 1;
        int[] res = new int[nums.length];
        int[] pre = new int[nums.length];
        int[] suf = new int[nums.length];

        for (int i = 0 ; i < nums.length ; i++){
            pre[i] = cur;
            cur *= nums[i];
        }

        cur = 1;
        for (int i = nums.length - 1 ; i >= 0 ; i--) {
            suf[i] = cur;
            cur *= nums[i];
        }

        for (int i = 0 ; i < nums.length ; i++) res[i] = suf[i] * pre[i];
        
        return res;
    }
}  
