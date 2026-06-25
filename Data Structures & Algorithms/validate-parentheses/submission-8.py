class Solution:
    def isValid(self, s: str) -> bool:
        if not len(s)%2 == 0:
            return False   
        stack = []

        pairs = { ")" : "(", "]" : "[", "}" : "{" }
        # stack.append(s[0])

        for i in s:
            if i in pairs:
                if stack and stack[-1] == pairs[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)

        
        return not stack
