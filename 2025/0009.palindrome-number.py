"""
9. 回文数

给你一个整数 x ，如果 x 是一个回文整数，返回 true ；否则，返回 false 。
回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        arr = []

        while x > 0:
            left, right = divmod(x, 10)
            arr.append(right)
            x = left

        n = len(arr)

        for idx in range(n // 2):
            if arr[idx] == arr[n - idx - 1]:
                continue
            return False
        return True


if __name__ == '__main__':
    Solution().isPalindrome(1213)
