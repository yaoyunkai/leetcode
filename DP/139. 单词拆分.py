"""
Created at 2023/9/6

给你一个字符串 s 和一个字符串列表 wordDict 作为字典。
请你判断是否可以利用字典中出现的单词拼接出 s 。

注意：不要求字典中出现的单词全部都使用，并且字典中的单词可以重复使用。

s = "applepenapple", wordDict = ["apple", "pen"]


"""
import pprint
from typing import List


class Solution:
    def wordBreak1(self, s: str, wordDict: List[str]) -> bool:
        word_dic = {}
        for idx, word in enumerate(wordDict):
            word_dic[word] = idx

        n = len(s)
        dp = [[-1 for _ in range(n)] for _ in range(n)]

        for word, idx in word_dic.items():

            for i in range(n):
                if s[i: i + len(word)] == word:
                    dp[i][i + len(word)] = idx

        pprint.pprint(dp)

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)

        dp = [False for _ in range(n + 1)]
        dp[0] = True

        # 每个下标开始的子串和dict去匹配，匹配到的dp[j] 置为True
        # 前提条件是 [0-i] 的位置也被匹配了
        for i in range(n):

            # n + 1 是因为 s[i:j) 右边是开区间
            for j in range(i + 1, n + 1):
                if dp[i] and s[i:j] in wordDict:
                    dp[j] = True

        return dp[-1]


if __name__ == '__main__':
    Solution().wordBreak(s="applepenapple", wordDict=["apple", "pen"])
