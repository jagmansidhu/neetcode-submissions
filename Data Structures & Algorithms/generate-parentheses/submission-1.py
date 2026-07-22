class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # My thinking
        # Lets say n = 3
        # 1: (()())
        stack = []
        res = []

        def backtrack(cur: str, l: int, r: int):
            if l == r == n:
                res.append(cur)
                return

            if l < n:
                backtrack(cur + "(", l + 1, r)
            if r < l:
                backtrack(cur + ")", l, r + 1)     

        backtrack("", 0,0)    

        return res