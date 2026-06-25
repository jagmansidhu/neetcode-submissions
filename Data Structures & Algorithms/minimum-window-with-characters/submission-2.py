class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        count = {}
        res = ""

        count_cur = 0
        min_len = float("inf")

        for i in t:
            count[i] = count.get(i, 0) + 1

        l = 0
        for r, char in enumerate(s):
            # here if the item is in char and == 0 we increment our count 
            if char in count:
                count[char] = count.get(char) - 1
                # for our count_cur we only count when that distinct key's value is == 0
                # which is why we use len(count) == count_cur when comparing in our while loop
                if count[char] == 0:
                    count_cur += 1

            # once our count is at the length of our t
            # we will first check to see if our window string is smaller than current string
            # if smaller res = window
            # We will also update l positions place in the count and increment +1
            while count_cur == len(count):

                if (r - l + 1) < min_len:
                    min_len = r - l + 1
                    res = s[l:r+1] 

                if s[l] in count:
                    if count[s[l]] == 0:
                        count_cur -= 1
                    count[s[l]] += 1
                
                l += 1

        return res