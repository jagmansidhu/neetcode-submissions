class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 1

        if len(s) == 0 :
            return 0

        longest = 0
        while r < len(s):
            longest = max(longest, r - l)
            while s[r] in s[l:r] and l < len(s) - 1:
                l += 1
            r+=1
        
        return max(longest, r - l)



            

                

            