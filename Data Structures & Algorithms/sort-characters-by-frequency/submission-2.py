class Solution:
    def frequencySort(self, s: str) -> str:
        m = {}

        freq = defaultdict(list)

        for cha in s:
            m[cha] = m.get(cha, 0) + 1


        for cha, count in m.items():
            freq[count].append(cha)

        
        res = ""
        for i in range(len(s), 0 , -1):
            for x in freq[i]:
                temp = i
                res += (x*i)

            
        return res


            
