class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}

        for s in strs:
            count = [0] * 26
        
            for c in s:
                count[ord(c) - ord('a')] += 1
            
            count_tuple = tuple(count)

            if count_tuple not in res:
                res[count_tuple] = []
            
            res[count_tuple].append(s)

        return list(res.values())