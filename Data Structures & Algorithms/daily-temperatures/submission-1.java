class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        Stack<Integer> temp = new Stack<>();
        int[] days = new int[temperatures.length];
        
        for (int t = 0 ; t < temperatures.length ; t++) {
            int j = 1;
            int k = t+1;


            while (k < temperatures.length && temperatures[k] <= temperatures[t]) {
                j++;

                if (temperatures[k] > temperatures[t]) break;

                k++;
            }

            days[t] = j;

            if (k+1 > temperatures.length) days[t] = 0;
        }


        return days;
    }
}
