class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def ispalindrome(l, r) -> bool:
            while l <= r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1

            return True

        def backtack(j: int, i: int, b: list):
            if i >= len(s):
                if j == i:
                    res.append(b[::])
                return

            # we check if palindrome,
            # if yes we will append current substring from j -> i to our current list
            # else we will go to next values or substring
            # for example we just checked is palindrome [1, 2]
            # not a palindrom we go to backtrack [1,3]
            # if this is palindrom we will append to our res list
            if ispalindrome(j,i):
                b.append(s[j : i + 1])
                backtack(i+1,i + 1, b)
                b.pop()

            backtack(j,i + 1, b)

        backtack(0,0, [])

        return res