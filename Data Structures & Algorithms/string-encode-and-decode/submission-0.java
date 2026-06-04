class Solution {
    char seperator = ';';

    public String encode(List<String> strs) {
        StringBuilder s = new StringBuilder();
        for (String str : strs) {
            s.append(str + seperator);
        }

        return (s.toString());
    }

    public List<String> decode(String str) {
        List<String> strs = new ArrayList<>();

        int cur_start = 0;
        for (int i = 0 ; i < str.length(); i++){
            if (str.charAt(i) == seperator) {
                strs.add(str.substring(cur_start, i));
                cur_start = i + 1;
            }

        }
        return strs;
        
    }
}
