class Solution {
    public boolean checkInclusion(String s1, String s2) {
        HashMap<Character, Integer> check = new HashMap<>();

        for (char s :  s1.toCharArray()) {
            check.put(s, check.getOrDefault(s, 0) + 1);
        }
        
        for (int i = 0; i < s2.length(); i++) {
            Map<Character, Integer> check1 = new HashMap<>();
            int cur = 0;
            for (int j = i; j < s2.length(); j++) {
                char c = s2.charAt(j);
                check1.put(c, check1.getOrDefault(c, 0) + 1);

                if (check.getOrDefault(c, 0) < check1.get(c)){
                    break;
                }

                if (check.getOrDefault(c, 0) == check1.get(c)) {
                    cur++;
                } 

                if (cur == check.size()) return true;
            }
        }

        return false;
    }
}
