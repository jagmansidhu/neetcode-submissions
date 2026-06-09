class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # The math is (Target - Position)/Speed

        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)

        count = 0
        prev = 0
        for p, s in pair:
            time = (target-p)/s

            if time > prev:
                count += 1
                prev = time

            

        return count

