"""
Created at 2023/9/6

给你一个字符串 s 和一个字符串列表 wordDict 作为字典。
请你判断是否可以利用字典中出现的单词拼接出 s 。

注意：不要求字典中出现的单词全部都使用，并且字典中的单词可以重复使用。

s = "applepenapple", wordDict = ["apple", "pen"]


"""
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        pass


if __name__ == '__main__':
    Solution().wordBreak(s="applepenapple", wordDict=["apple", "pen"])
