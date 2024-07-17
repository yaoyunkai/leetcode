"""


Created at 2024/7/17
"""
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        [0,0,1,1,1,2,2,3,3,4]

        :param nums:
        :return:
        """
        left = 0

        for num in nums:
            if nums[left] == num:
                continue

            left += 1
            nums[left] = num

        return left + 1


if __name__ == '__main__':
    Solution().removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4])
