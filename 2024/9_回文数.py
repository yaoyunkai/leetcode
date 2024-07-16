"""


Created at 2024/7/16
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
