class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, List<String>> ana = new HashMap<>();

        for (String str : strs) {
            char[] chr = str.toCharArray();
            Arrays.sort(chr);
            String strOrdered = String.valueOf(chr);

            ana.putIfAbsent(strOrdered, new ArrayList<>());

            ana.get(strOrdered).add(str);
        }

        return new ArrayList<>(ana.values());
    }
}
