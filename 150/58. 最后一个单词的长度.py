"""
给你一个字符串 s，由若干单词组成，单词前后用一些空格字符隔开。返回字符串中 最后一个 单词的长度。


"   fly me   to   the moon  "
"Hello World"


Created at 2023/8/30
"""


class Solution:
    def lengthOfLastWord1(self, s: str) -> int:
        s = s.rstrip()

        idx = len(s) - 1
        count = 0

        while idx >= 0:
            if s[idx] != ' ':
                count += 1
            else:
                break

            idx -= 1
        return count

    def lengthOfLastWord(self, s: str) -> int:
        end = len(s) - 1

        while end >= 0 and s[end] == ' ':
            end -= 1

        if end < 0:
            return 0

        start = end
        while start >= 0 and s[start] != ' ':
            start -= 1

        return end - start


if __name__ == '__main__':
    Solution().lengthOfLastWord1('xxx')
