class MinStack {
    MinStack minstack;
    ArrayList<Integer> stack;
    int minVal;
    int count;

    public MinStack() {
        minVal = Integer.MAX_VALUE;
        stack = new ArrayList<>();
        count = -1;
    }
    
    public void push(int val) {
        stack.add(val);
        if(val < minVal) minVal = val;
        count++;
    }
    
    public void pop() {

        if (top() == minVal) {
            minVal = Integer.MAX_VALUE;
            for (int i = 0; i < count ; i++) {
                if (stack.get(i) < minVal) minVal = stack.get(i);
            }
        }
        stack.remove(count--);
    }
    
    public int top() {
        return stack.get(count);
    }
    
    public int getMin() {
        return minVal;
    }
}
