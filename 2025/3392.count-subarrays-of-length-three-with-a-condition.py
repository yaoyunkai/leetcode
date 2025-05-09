"""
给你一个整数数组 nums ，请你返回长度为 3 的 子数组 的数量，满足第一个数和第三个数的和恰好为第二个数的一半。

子数组 指的是一个数组中连续 非空 的元素序列。


"""
from typing import List


class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        cnt = 0

        for idx in range(len(nums) - 2):
            if nums[idx + 1] / 2 == (nums[idx] + nums[idx + 2]):
                cnt += 1

        return cnt


if __name__ == '__main__':
    Solution().countSubarrays([1, 2, 1, 4, 1])
