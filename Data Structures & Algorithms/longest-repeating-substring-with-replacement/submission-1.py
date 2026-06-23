class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l = 0
        maxf = 0
        res = 0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count.get(s[r]))

            # maxf is the char that has the max freq
            # (r - l + 1) is the size of the current window
            # while the size - maxf > k, we keep moving left over by 1
            # if not than we know that we have a potential candidate for result
            # And we go ahead and break out of loop and res = max(res, r-l+1)
            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1
            
            res = max(res, r-l +1)

        return res