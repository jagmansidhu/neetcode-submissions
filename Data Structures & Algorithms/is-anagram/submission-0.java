class Solution {
    public boolean isAnagram(String s, String t) {
        HashMap<Character, Integer> counts = new HashMap<>();
        HashMap<Character, Integer> countt = new HashMap<>();

        if (s.length() != t.length()) return false;

        for (int i = 0 ; i < s.length() ; i++) {
            counts.put(s.charAt(i), counts.getOrDefault(s.charAt(i), 0)+1);
            countt.put(t.charAt(i), countt.getOrDefault(t.charAt(i), 0)+1);
        }

        return counts.equals(countt);

    }
}
