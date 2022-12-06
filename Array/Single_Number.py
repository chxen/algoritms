"""Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.

Input: nums = [2,2,1]
Output: 1"""

def singleNum(arr: list[int]) -> int:
    ans = list[0]
    for i in range(1, len(arr)):
        if arr[i-1] == arr[i]:
