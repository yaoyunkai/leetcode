"""
给你两个整数数组 nums1 和 nums2 ，请你以数组形式返回两数组的交集。
返回结果中每个元素出现的次数，应与元素在两个数组中都出现的次数一致（如果出现次数不一致，则考虑取较小值）。可以不考虑输出结果的顺序。

"""
from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        arr = []
        used_idx1 = []
        used_idx2 = []

        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        for idx1, num1 in enumerate(nums1):
            for idx2, num2 in enumerate(nums2):
                if num1 == num2 and idx1 not in used_idx1 and idx2 not in used_idx2:
                    used_idx1.append(idx1)
                    used_idx2.append(idx2)
                    arr.append(num1)

        return arr


if __name__ == '__main__':
    Solution().intersect(nums1=[4, 9, 5], nums2=[9, 4, 9, 8, 4])
