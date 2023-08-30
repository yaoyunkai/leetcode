"""
Created at 2023/8/30

如果在将所有大写字符转换为小写字符、并移除所有非字母数字字符之后，短语正着读和反着读都一样。
则可以认为该短语是一个 回文串 。
字母和数字都属于字母数字字符。

"""
import string


class Solution:
    def isPalindrome(self, s: str) -> bool:
        allow = string.ascii_lowercase + string.digits

        new = []

        for ch in s:
            ch = ch.lower()
            if ch in allow:
                new.append(ch)

        new = ''.join(new)

        n = len(new)

        for i in range(0, n // 2):
            if new[i] != new[n - 1 - i]:
                return False
        return True


if __name__ == '__main__':
    ret = Solution().isPalindrome("A man, a plan, a canal: Panama")
    print(ret)
