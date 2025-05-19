"""
给你一个字符串 text，你需要使用 text 中的字母来拼凑尽可能多的单词 "balloon"（气球）。

字符串 text 中的每个字母最多只能被使用一次。请你返回最多可以拼凑出多少个单词 "balloon"。

"""


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        _tmp = {
            'a': 0,
            'b': 0,
            'n': 0,
            'l': 0,
            'o': 0,
        }

        for ch in text:
            if ch in ['b', 'a', 'n']:
                _tmp[ch] += 2
            if ch in ['l', 'o']:
                _tmp[ch] += 1

        return min(_tmp.values()) // 2
