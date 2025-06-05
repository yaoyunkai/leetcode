"""
给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的 字母异位词。

字母异位词是通过重新排列不同单词或短语的字母而形成的单词或短语，并使用所有原字母一次。
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cnt = dict()
        for ch in s:
            if ch not in cnt:
                cnt[ch] = 0
            cnt[ch] += 1

        for ch in t:
            if ch not in cnt or cnt[ch] == 0:
                return False
            cnt[ch] -= 1

        return all([val == 0 for val in cnt.values()])


if __name__ == '__main__':
    Solution().isAnagram(s="anagram", t="nagaram")
