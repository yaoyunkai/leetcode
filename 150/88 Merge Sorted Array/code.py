"""
Created at 2023/8/29


给你两个按 非递减顺序 排列的整数数组 nums1 和 nums2，另有两个整数 m 和 n ，分别表示 nums1 和 nums2 中的元素数目。

请你 合并 nums2 到 nums1 中，使合并后的数组同样按 非递减顺序 排列。


输入：nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
输出：[1,2,2,3,5,6]
解释：需要合并 [1,2,3] 和 [2,5,6] 。
合并结果是 [1,2,2,3,5,6] ，其中斜体加粗标注的为 nums1 中的元素。


"""
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        tail = m + n - 1

        left = m - 1
        right = n - 1

        while left >= 0 or right >= 0:
            if right == -1:
                nums1[tail] = nums1[left]
                left -= 1
            elif left == -1:
                nums1[tail] = nums2[right]
                right -= 1
            elif nums1[left] > nums2[right]:
                nums1[tail] = nums1[left]
                left -= 1
            else:
                nums1[tail] = nums2[right]
                right -= 1
            tail -= 1
