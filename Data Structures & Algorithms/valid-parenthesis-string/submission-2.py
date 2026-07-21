class Solution:
    def checkValidString(self, s: str) -> bool:
        para = []
        star = []

        cur = 0
        for i, p in enumerate(s):
            if p == '(':
                para.append(i)

            if p == '*':
                star.append(i)

            if p == ')':
                if para:
                    para.pop()
                elif star:
                    star.pop()
                else:
                    return False

        while star and para:
            if para.pop() > star.pop():
                return False

        return not para