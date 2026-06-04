class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, List<String>> ana = new HashMap<>();

        for (String str : strs) {
            char[] chr = str.toCharArray();
            Arrays.sort(chr);
            String strOrdered = new String(chr);

            List<String> list = ana.getOrDefault(strOrdered, new ArrayList());

            list.add(str);
            
            ana.put(strOrdered, list);
        }

        return new ArrayList<>(ana.values());
    }
}
