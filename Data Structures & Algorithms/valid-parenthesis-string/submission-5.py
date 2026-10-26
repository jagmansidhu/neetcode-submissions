class Solution:
    def checkValidString(self, s: str) -> bool:
        paran = []
        star = []

        for i, p in enumerate(s):

            if p == '(':
                paran.append(i)
            
            elif p == '*':
                star.append(i)

            else:
                if not star and not paran:
                    return False

                if paran:
                    paran.pop()
                else:
                    star.pop()

        while star and paran:
           if paran.pop() > star.pop():
            return False

        return not paran