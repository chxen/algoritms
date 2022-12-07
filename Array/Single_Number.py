"""Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.

Input: nums = [2,2,1]
Output: 1"""

def singleNum(num: list[int]) -> int:
    ans = 0
    for n in num:
        ans = n ^ ans
    return ans

print(singleNum([2,2,1,1,5]))