""" Удаляет дубликаты из отсортированного массива
Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores)."""

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        l = 1
        for r in range(1, len(nums)):
            if nums[r-1] != nums[r]:
                nums[l] = nums[r]
                l += 1
        return nums[:l]

A = Solution()
print(A.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))

print(list(set([0,0,1,1,1,2,2,3,3,4])))