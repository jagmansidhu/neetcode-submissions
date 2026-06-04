class MedianFinder {
    List<Integer> nums;
    int size;

    public MedianFinder() {
        nums = new ArrayList<>();
        size = 0;
        
    }
    
    public void addNum(int num) {
        nums.add(num);
        size++;
    }
    

    public double findMedian() {
        Collections.sort(nums);
        
        int mid = size / 2; 

        if (size % 2 != 0) {
            return (double)nums.get(mid);
        } else {
            int notmid = mid - 1;  

            return (nums.get(mid) + nums.get(notmid)) / 2.0;
        }
        
    }
}
