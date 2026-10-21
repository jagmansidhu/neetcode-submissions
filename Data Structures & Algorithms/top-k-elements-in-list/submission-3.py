class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m = {}
        freq = [[] for i in range(len(nums) + 1)]

        # storing each val into buckets?
        for i in nums:
            m[i] = m.get(i, 0) + 1

        for n, c in m.items():
            freq[c].append(n)

        # The biggest quesiton is, I find x and y how do i find the top k

        res=[]

        for i in range(len(freq)-1, 0 , -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res


        return res




        

            

        