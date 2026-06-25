class Solution:
    def isValid(self, s: str) -> bool:
        if not len(s)%2 == 0:
            return False

        stack = []

        # stack.append(s[0])

        for i in s:
            if i =='}' and '{' in stack and stack[-1] == '{':
                stack.pop()
                continue
            elif i ==')' and '(' in stack and stack[-1] == '(':
                stack.pop()
                continue
            elif  i ==']' and '[' in stack and stack[-1] == '[':
                stack.pop()
                continue
            else:
                stack.append(i)

        
        return not stack
