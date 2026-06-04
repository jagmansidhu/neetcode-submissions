class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> ret = new ArrayList<>();
        Arrays.sort(nums);
        
        for (int i = 0 ; i < nums.length; i++) {
            if (nums[i] > 0) break;
            if (i > 0 && nums[i] == nums[i-1]) continue;

            int l = i + 1;
            int r = nums.length -1 ;

            // Two pointer loop for the next two items
            while (l < r) {
                int threesume = nums[i] + nums[l] + nums[r];
                if (threesume > 0) r--;
                if (threesume < 0) l++;
                if (threesume == 0){
                    ret.add(Arrays.asList(nums[i], nums[l], nums[r]));
                    r--;
                    l++;
                    while (l < r && nums[l] == nums[l - 1]) {
                        l++;
                    }
                }
            }

        }


        

        return ret;
    }
}
