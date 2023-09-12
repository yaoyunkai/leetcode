"""


Created at 2023/9/12
"""


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
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
    ret = Solution().isIsomorphic("badc", "baba")
    print(ret)
