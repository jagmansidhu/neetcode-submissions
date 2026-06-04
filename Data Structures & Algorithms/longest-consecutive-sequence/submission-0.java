class Solution {
    public int longestConsecutive(int[] nums) {
        Set<Integer> numset = new HashSet<>();

        for (int n : nums) numset.add(n);

        int res = 0;

        for (int n : numset) {
            if (!numset.contains(n-1)) {
                int cur = 1;
                while (numset.contains(n + cur)) cur++;
                res = Math.max(cur, res);
            }

        }

        return res;
    }
}
