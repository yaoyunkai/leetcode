"""
给你一个字符串 paragraph 和一个表示禁用词的字符串数组 banned ，
返回出现频率最高的非禁用词。题目数据 保证 至少存在一个非禁用词，且答案 唯一 。

paragraph 中的单词 不区分大小写 ，答案应以 小写 形式返回。

注意 单词不包含标点符号。

created at 2025/5/15
"""
from collections import Counter
from typing import List


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        for ch in "!?',;.":
            paragraph = paragraph.replace(ch, ' ')
        paragraph_list = paragraph.split()
        cnt = Counter()
        arr = []

        for p in paragraph_list:
            p = p.lower()

            if p not in banned:
                arr.append(p)
        cnt.update(arr)

        return cnt.most_common(1)[0][0]
