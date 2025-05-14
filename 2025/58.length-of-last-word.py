"""
给你一个字符串 s，由若干单词组成，单词前后用一些空格字符隔开。返回字符串中 最后一个 单词的长度。

单词 是指仅由字母组成、不包含任何空格字符的最大子字符串。

"""


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])


class Solution2:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1
        while s[i] == ' ':
            i -= 1

        j = i - 1
        while j >= 0 and s[j] != ' ':
            j -= 1

        return i - j
