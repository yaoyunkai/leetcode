"""
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

Created at 2023/8/30
"""
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """

        :param strs:
        :return:
        """
        max_len = 0
        result = ""

        for string in strs:
            max_len = max(max_len, len(string))

        for idx in max_len:
            pass
