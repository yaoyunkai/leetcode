"""
给你一个整数 x ，如果 x 是一个回文整数，返回 true ；否则，返回 false 。
回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。


"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x == 0:
            return True

        return str(x) == str(x)[::-1]


if __name__ == '__main__':
    d = '1234'

    ret = Solution().isPalindrome(12321)
    print(ret)
