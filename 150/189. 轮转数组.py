"""
给定一个整数数组 nums，将数组中的元素向右轮转 k 个位置，其中 k 是非负数。

nums = "----->-->"; k =3
result = "-->----->";

reverse "----->-->" we can get "<--<-----"
reverse "<--" we can get "--><-----"
reverse "<-----" we can get "-->----->"
this visualization help me figure it out :)

Created at 2023/8/31
"""
from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.

        k的大小比n还大的时候

        """

        n = len(nums)
        # k的大小比n还大的时候
        k %= n

        for i in range(0, n):
            if i == n // 2:
                break
            self.swap(nums, i, n - 1 - i)

        for i in range(0, k):
            if i == k // 2:
                break
            self.swap(nums, i, k - 1 - i)

        for i in range(k, n):
            if i == k + (n - k) // 2:
                break
            self.swap(nums, i, n - 1 - i + k)
        print(nums)

    def swap(self, nums, i, j):
        tmp = nums[j]
        nums[j] = nums[i]
        nums[i] = tmp


if __name__ == '__main__':
    Solution().rotate([1, 2, 3, 4, 5, 6, 7], 3)
