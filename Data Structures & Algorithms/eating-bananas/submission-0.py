class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # h = hours to eat
        # piles[i] = # of banaas in that pile
        # k = bananas per hour eating rate - We decide
        # If that pile less that k banas, we may finish this pile but wait until next
        # Find min k to eat banas within hours

        l = 1
        r = max(piles)

        res = r

        while l <= r:
            k = (l+r) // 2
            totalTime = 0
            for p in piles:
                totalTime += math.ceil(float(p) / k)

            print(totalTime)
            if totalTime <= h:
                res = k
                r = k - 1
            else:
                l = k + 1

        return res