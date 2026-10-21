class Solution:
    def frequencySort(self, s: str) -> str:
        m = {}

        freq = [[] for i in range(len(s) + 1)]

        for cha in s:
            m[cha] = m.get(cha, 0) + 1


        for cha, count in m.items():
            freq[count].append(cha)

        
        res = ""
        for i in range(len(freq)-1, 0 , -1):
            for x in freq[i]:
                temp = i
                while temp > 0:
                    temp -= 1
                    res += x

            
        return res


            
