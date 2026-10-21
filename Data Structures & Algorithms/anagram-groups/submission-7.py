class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}

        for s in strs:
            count = [0] * 26    

            for c in s:
                count[ord(c) - ord('a')] += 1

            count = tuple(count)
            
            if count not in res:
                res[count] = []

            res[count].append(s)

        return list(res.values())