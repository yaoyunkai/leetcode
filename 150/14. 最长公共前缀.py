"""
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

Created at 2023/8/30
"""
from typing import List


class Solution:
    def longestCommonPrefix1(self, strs: List[str]) -> str:
        """

        :param strs:
        :return:
        """
        max_len = 0
        result = ""

        for string in strs:
            max_len = max(max_len, len(string))

        for idx in range(0, max_len):

            tmp = []

            for string in strs:
                if idx > len(string) - 1:
                    break
                else:
                    ch = string[idx]
                    tmp.append(ch)

            if len(tmp) != len(strs):
                break
            else:
                if len(set(tmp)) == 1:
                    result += tmp[0]
                else:
                    break

        print(result)

    def longestCommonPrefix(self, strs: List[str]) -> str:

        # 不会比任意元素长
        length = len(strs[0])
        count = len(strs)

        for i in range(length):
            # 取第一个元素的第i列
            ch = strs[0][i]

            for j in range(1, count):

                # 比第j个元素长的时候
                if i == len(strs[j]):
                    return strs[0][:i]  # 返回前一个

                # 比较每个元素的第i列
                if strs[j][i] != ch:
                    return strs[0][:i]  # 返回前一个

        return strs[0]


if __name__ == '__main__':
    Solution().longestCommonPrefix(["flower", "flow", "flight"])
    Solution().longestCommonPrefix(["flower", "flow", "flowxr"])
