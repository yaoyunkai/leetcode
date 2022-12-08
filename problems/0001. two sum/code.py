from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        target = num1 + num2
        num2 = target - num1


        :param nums:
        :param target:
        :return:
        """

        hashtable = dict()
        for i, num in enumerate(nums):

            # 如果匹配 就返回当前数和dict中的index
            if target - num in hashtable:
                return [hashtable[target - num], i]

            # 先用dict保存一个数与index的关系
            hashtable[nums[i]] = i
        return []


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    ret = Solution().twoSum(nums, target)
    print(ret)
