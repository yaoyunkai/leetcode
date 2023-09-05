"""

给你两个只包含 1 到 9 之间数字的数组 nums1 和 nums2 ，每个数组中的元素 互不相同 ，
请你返回 最小 的数字，两个数组都 至少 包含这个数字的某个数位。

Created at 2023/9/5
"""
from typing import List


class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        if len(nums1) < len(nums2):
            nums1, nums2 = nums2, nums1

        min1 = nums1[0]
        min2 = nums2[0]

        comm = set(nums1) & set(nums2)
        if comm:
            return min(comm)

        for idx, num in enumerate(nums1):
            if idx < len(nums2):
                num2 = nums2[idx]

                if num2 < min2:
                    min2 = num2

            if num < min1:
                min1 = num

        # print(min1, min2)
        return min(min1 * 10 + min2, min2 * 10 + min1, *comm)


if __name__ == '__main__':
    ret = Solution().minNumber(nums1=[6, 4, 3, 7, 2, 1, 8, 5], nums2=[6, 8, 5, 3, 1, 7, 4, 2])
    print(ret)
