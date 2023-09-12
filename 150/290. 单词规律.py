"""
输入: pattern = "abba", s = "dog cat cat dog"
输出: true

Created at 2023/9/12
"""


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        word_dic = dict()

        new_s = []

        for idx, word in enumerate(s.split()):
            if word not in word_dic:
                word_dic[word] = str(idx)

            new_s.append(word_dic[word])

        new_s = ''.join(new_s)

        return self.isIsomorphic(pattern, new_s)

    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        res1 = dict()
        res2 = dict()

        n = len(s)

        for i in range(n):
            ch1 = s[i]
            ch2 = t[i]

            if (ch1 in res1 and res1[ch1] != ch2) or (ch2 in res2 and res2[ch2] != ch1):
                return False

            res1[ch1] = ch2
            res2[ch2] = ch1

        return True


if __name__ == '__main__':
    Solution().wordPattern('', 'dog cat cat dog')
