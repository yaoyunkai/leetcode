"""
Created at 2023/8/30

给定字符串 s 和 t ，判断 s 是否为 t 的子序列。

字符串的一个子序列是原始字符串删除一些（也可以不删除）
字符而不改变剩余字符相对位置形成的新字符串。（例如，"ace"是"abcde"的一个子序列，而"aec"不是）。

"""


class Solution:
    def isSubsequence1(self, s: str, t: str) -> bool:
        if not s:
            return True

        # 不用回退
        s_idx = 0
        t_idx = 0

        len_s = len(s)
        len_t = len(t)

        while t_idx < len_t:
            if t[t_idx] == s[s_idx]:
                s_idx += 1
            if s_idx == len_s - 1:
                return True
            t_idx += 1
        return False

    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True

        # 不用回退
        s_idx = 0
        t_idx = 0

        len_s = len(s)
        len_t = len(t)

        while t_idx < len_t:
            if t[t_idx] == s[s_idx]:
                s_idx += 1
            if s_idx == len_s:
                return True
            t_idx += 1
        return False
