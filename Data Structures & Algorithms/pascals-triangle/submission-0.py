class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []

        for i in range(numRows):
            cur = [1] * (i + 1)

            # leave cur[0] = 1 and cur[len(cur)-1] = 1
            # And now we add the rest
            # is the ones above -1 and i itself?
            for j in range(1, len(cur) - 1):
                cur[j] = res[i-1][j-1] + res[i-1][j]

            res.append(cur)

        

        return res
        
    