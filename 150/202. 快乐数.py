"""

对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和。
然后重复这个过程直到这个数变为 1，也可能是 无限循环 但始终变不到 1。
如果这个过程 结果为 1，那么这个数就是快乐数。


Created at 2023/11/13
"""


class Solution:
    def isHappy(self, n: int) -> bool:
        res = {}

        while True:

            if n in res:
                return False

            num = self.get_res(n)
            print('n: {}, result: {}'.format(n, num))

            if num == 1:
                return True

            res[n] = num
            n = num

    def get_res(self, num: int) -> int:
        count = 0

        while num != 0:
            num, r = divmod(num, 10)
            count = count + (r ** 2)

        return count


if __name__ == '__main__':
    # Solution().isHappy(12)
    # print(get_res(234))
    pass
    Solution().isHappy(2)
