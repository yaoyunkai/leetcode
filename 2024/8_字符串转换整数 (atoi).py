"""

"42"
"   -042"
"1337c0d3"
"0-1"
"words and 987"


Created at 2024/6/26
"""


class Solution:
    def myAtoi(self, s: str) -> int:
        if not s:
            return 0

        res = 0

        for c in s:
            if c in '0123456789':
                res = res * 10 + int(c)
