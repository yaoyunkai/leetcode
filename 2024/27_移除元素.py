"""


Created at 2024/7/17
"""
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        max_n = len(nums)

        idx = 0

        while idx < max_n:
            if nums[idx] == val:
                max_n -= 1
                for j in range(idx, max_n):
                    nums[j] = nums[j + 1]
            else:
                idx += 1

        return max_n

    def removeElement2(self, nums: List[int], val: int) -> int:
        k = 0
        for x in nums:
            if x != val:
                nums[k] = x
                k += 1

        return k


if __name__ == '__main__':
    Solution().removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2)
