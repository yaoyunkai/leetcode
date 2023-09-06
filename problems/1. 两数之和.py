"""
Created at 2023/9/6

输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。

"""
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res_dict = {}

        for idx, num in enumerate(nums):
            if num in res_dict:
                return [idx, res_dict[num]]
            else:
                dif = target - num
                res_dict[dif] = idx


if __name__ == '__main__':
    Solution().twoSum(nums=[2, 7, 11, 15], target=9)
