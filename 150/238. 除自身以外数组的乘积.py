"""

输入: nums = [1,2,3,4]
输出: [24,12,8,6]

Created at 2023/9/21
"""
from typing import List


class Solution:
    def productExceptSelf1(self, nums: List[int]) -> List[int]:
        res = []
        n = len(nums)

        for i in range(n):

            cnt = None
            for j in range(n):
                if i != j:
                    if cnt is None:
                        cnt = nums[j]
                    else:
                        cnt *= nums[j]

            res.append(cnt)

        return res

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1 for _ in range(len(nums))]
        tmp = 1

        for i in range(1, len(nums)):
            res[i] = res[i - 1] * nums[i - 1]

        for i in range(len(nums) - 2, -1, -1):
            tmp *= nums[i + 1]
            res[i] *= tmp

        return res


if __name__ == '__main__':
    ret = Solution().productExceptSelf([1, 2, 3, 4])
    print(ret)
