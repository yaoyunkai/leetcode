"""
Created at 2023/8/31

给你两个字符串：ransomNote 和 magazine ，判断 ransomNote 能不能由 magazine 里面的字符构成。

输入：ransomNote = "aa", magazine = "aab"
输出：true

"""
from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        set1 = Counter(ransomNote)
        set2 = Counter(magazine)

        for k, v in set1.items():
            if set2.get(k, 0) < v:
                return False
        return True


if __name__ == '__main__':
    Solution().canConstruct(ransomNote="aa", magazine="aab")
