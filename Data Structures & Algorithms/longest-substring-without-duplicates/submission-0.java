class Solution {
    public int lengthOfLongestSubstring(String s) {
        int max_count = 0;
        int l = 0;
        HashSet<Character> set = new HashSet<>();
        for (int r = 0; r < s.length() ; r++) {
            while (set.contains(s.charAt(r))) {
                set.remove(s.charAt(l));
                l++;
            } 
            set.add(s.charAt(r));
            max_count = Math.max(max_count, r - l + 1);
        }

        return max_count;
    }
}
