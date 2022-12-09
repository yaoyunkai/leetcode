"""
20. 括号匹配



"""


class Solution:
    def isValid2(self, s: str) -> bool:
        _d = {'}': '{', ')': '(', ']': '['}

        arr = []

        if len(s) < 2:
            return False

        for ch in s:
            if ch in ['(', '{', '[']:
                arr.append(ch)
            elif ch in [')', '}', ']']:
                if not arr:
                    arr.append(ch)
                    continue

                if _d[ch] == arr[-1]:
                    arr.pop()
                else:
                    # 提前返回false 当栈顶左右不匹配时
                    return False
        return len(arr) == 0

    def isValid(self, s: str) -> bool:
        dic = {'{': '}', '[': ']', '(': ')', '?': '?'}

        # 边界情况，当列表为空 第一个字符为右括号的情况
        stack = ['?']
        for c in s:
            if c in dic:
                stack.append(c)
            elif dic[stack.pop()] != c:
                return False
        return len(stack) == 1


if __name__ == '__main__':
    d1 = ')[]{}'
    ret = Solution().isValid(d1)
    print(ret)
