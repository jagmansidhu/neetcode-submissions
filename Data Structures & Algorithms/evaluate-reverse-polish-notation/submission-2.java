class Solution {
    public int evalRPN(String[] tokens) {
        Stack<Integer> countTokens = new Stack<>();

        if (tokens.length == 0) return 0;

        for (String token : tokens) {
            if (token.equals("+")) {
                int num1 = countTokens.pop();
                int num2 = countTokens.pop();

                countTokens.push(num1 + num2);

            } else if (token.equals("-")) {
                int num1 = countTokens.pop();
                int num2 = countTokens.pop();

                countTokens.push(num2-num1);

            } else if (token.equals("/")) {
                int num1 = countTokens.pop();
                int num2 = countTokens.pop();

                countTokens.push(num2/num1);
                
            } else if (token.equals("*")) {
                int num1 = countTokens.pop();
                int num2 = countTokens.pop();

                countTokens.push(num1*num2);
            } else {
                countTokens.push(Integer.parseInt(token));
            }
            
        }

        return countTokens.pop();
        
    }
}
