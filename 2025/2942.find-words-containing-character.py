"""
给你一个下标从 0 开始的字符串数组 words 和一个字符 x 。

请你返回一个 下标数组 ，表示下标在数组中对应的单词包含字符 x 。

注意 ，返回的数组可以是 任意 顺序。

created at 2025/5/24
"""
from typing import List


class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        arr = []

        for idx, word in enumerate(words):
            if x in word:
                arr.append(idx)

        return arr
