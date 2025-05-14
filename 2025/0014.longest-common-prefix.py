"""
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

"""
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        min_len = min(len(strs[0]), len(strs[-1]))

        cnt = 0
        for idx in range(min_len):
            if strs[0][idx] == strs[-1][idx]:
                cnt += 1
            else:
                break
        return strs[0][0:cnt]


if __name__ == '__main__':
    s1 = ["flower", "flow", "flight"]
    Solution().longestCommonPrefix(s1)
