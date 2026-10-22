class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        top = 0
        bot = rows- 1

        while top <= bot:
            row = (top + bot) // 2
            if target > matrix[row][-1]:
                top += 1
            elif target < matrix[row][0]:
                bot -= 1
            else:
                break

        if not (top <= bot):
            return False

        row = (top + bot) // 2
        r = cols - 1
        l = 0

        while l <= r:
            mid = (r + l) // 2
            if target > matrix[row][mid]:
                l = mid + 1
            elif target < matrix[row][mid]:
                r = mid - 1

            if target == matrix[row][mid]:
                return True
        
        return False
