"""
编写一个函数来查找字符串数组中的最长公共前缀。
如果不存在公共前缀，返回空字符串 ""。

"""

from typing import List


class Solution:
    def longestCommonPrefix1(self, strs: List[str]) -> str:
        if not strs:
            return ''

        length, count = len(strs[0]), len(strs)

        # 遍历每一列
        for i in range(length):
            # 当前列的字符
            ch = strs[0][i]

            # 遍历每个字符
            for j in range(1, count):
                if i == len(strs[j]):
                    return strs[0][:i]
                if strs[j][i] != ch:
                    return strs[0][:i]

        return strs[0]

    def longestCommonPrefix(self, strs):
        if not strs: return ""
        s1 = min(strs)
        s2 = max(strs)
        for i, x in enumerate(s1):
            if x != s2[i]:
                return s2[:i]
        return s1


if __name__ == '__main__':
    demo1 = ["flower", "flow", "flight"]
    print(min(demo1))
    print(max(demo1))
