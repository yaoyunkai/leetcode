from typing import List


class Solution:
    def missingNumber1(self, nums: List[int]) -> int:
        h_set = set(nums)

        for i in range(len(nums) + 1):
            if i not in h_set:
                return i

    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        total = n * (n + 1) // 2
        arrSum = sum(nums)
        return total - arrSum
