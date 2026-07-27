class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }
        if len(digits) <= 0:
            return res

        def dfs(d, s):
            if len(s) == len(digits):
                res.append(s)
                return

            for c in digitToChar[digits[d]]:
                dfs(d + 1, s + c)

        dfs(0, "")

        return res