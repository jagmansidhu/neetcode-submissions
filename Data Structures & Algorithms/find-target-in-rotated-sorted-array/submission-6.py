class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (r + l) // 2

            if nums[mid] == target:
                return mid

            # first check : is is this range from mid to l sorted
            if nums[l] <= nums[mid]:
                # is it out of this range ; if so l = mid + 1
                # if it is in this range we bring ; r = mid - 1
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            # else we check the rest of array to find a sorted range
            else:
                # if the target is not in this range
                # Bring r = mid - 1
                # If in this range = bring left in
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        
        return -1

