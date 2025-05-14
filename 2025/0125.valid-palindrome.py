"""
如果在将所有大写字符转换为小写字符、并移除所有非字母数字字符之后，短语正着读和反着读都一样。
则可以认为该短语是一个 回文串 。

字母和数字都属于字母数字字符。

给你一个字符串 s，如果它是 回文串 ，返回 true ；否则，返回 false 。


"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s == ' ':
            return True
        arr = []

        for ch in s:
            if ch.isalpha() or ch.isdigit():
                arr.append(ch)

        if len(arr) == 0:
            return True
        if len(arr) == 1:
            return True

        n = len(arr)

        for idx in range(n // 2):
            if arr[idx].lower() == arr[n - 1 - idx].lower():
                continue
            return False
        return True
