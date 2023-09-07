"""
给你一个字符串数组 names ，和一个由 互不相同 的正整数组成的数组 heights 。两个数组的长度均为 n 。

对于每个下标 i，names[i] 和 heights[i] 表示第 i 个人的名字和身高。

请按身高 降序 顺序返回对应的名字数组 names 。

输入：names = ["Mary","John","Emma"], heights = [180,165,170]
输出：["Mary","Emma","John"]
解释：Mary 最高，接着是 Emma 和 John 。


Created at 2023/9/7
"""
from typing import List


class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        n = len(names)

        index = list(range(n))

        index.sort(key=lambda x: heights[x], reverse=True)

        res = []

        for i in index:
            res.append(names[i])

        return res
