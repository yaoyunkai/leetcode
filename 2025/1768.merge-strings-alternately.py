"""
给你两个字符串 word1 和 word2 。请你从 word1 开始，通过交替添加字母来合并字符串。
如果一个字符串比另一个字符串长，就将多出来的字母追加到合并后字符串的末尾。

返回 合并后的字符串 。


created at 2025/5/15
"""


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        arr = []

        n1 = len(word1)
        n2 = len(word2)

        if n1 > n2:
            rem = word1[n2:]
            n1, n2 = n2, n1
        else:
            rem = word2[n1:]

        for idx in range(n1):
            arr.append(word1[idx])
            arr.append(word2[idx])

        return ''.join(arr) + rem
