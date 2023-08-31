"""


Created at 2023/8/31
"""


class Solution:
    def fib(self, n: int) -> int:
        a, b = 0, 1
        for i in range(n):
            a, b = a + b, a
        return a
