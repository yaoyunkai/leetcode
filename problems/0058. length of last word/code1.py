import re


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if not s:
            return 0

        result = re.split(r'\s+', s)
        return len(result[-1]) if len(result[-1]) != 0 else len(result[-2])


if __name__ == '__main__':
    demo = "   fly me   to   the moon  "
    print(Solution().lengthOfLastWord(demo))
