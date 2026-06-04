class TimeMap {
    HashMap<String, TreeMap<Integer, String>> pass;

    public TimeMap() {
        pass = new HashMap<>();
        
    }
    
    public void set(String key, String value, int timestamp) {
        pass.computeIfAbsent(key, k -> new TreeMap<>()).put(timestamp, value);
        
    }
    
    public String get(String key, int timestamp) {
        TreeMap<Integer, String> cur = pass.get(key);

        if (cur == null) {
            return "";
        }

        Integer floorKey = cur.floorKey(timestamp);
        
        if (floorKey == null) {
            return "";
        }
        
        return cur.get(floorKey);
    }
}
