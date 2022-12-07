"""Given a sorted array of distinct integers and a target value, 
return the index if the target is found. If not, return the index 
where it would be if it were inserted in order.
You must write an algorithm with O(log n) runtime complexity."""

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            avg = (right + left) // 2
            if target == nums[avg]:
                return avg
            elif target > nums[avg]:
                left = avg + 1
            elif target < nums[avg]:
                right = avg - 1
        return left

A = Solution()
print(A.search([1,3,5,6], 2))