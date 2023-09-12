"""


Created at 2023/9/12
"""


class Solution:

    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x < 10:
            return True

        new = 0
        cx = x

        while True:
            left, right = divmod(cx, 10)

            new = new * 10 + right
            if left == 0:
                break
            cx = left

        return x == new


if __name__ == '__main__':
    Solution().isPalindrome(210)
