"""
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。

Created at 2023/8/31
"""


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for ch in s:
            if ch == '(':
                stack.append(ch)
            elif ch == '{':
                stack.append(ch)
            elif ch == '[':
                stack.append(ch)
            elif ch == ')':
                if not stack or stack.pop() != '(':
                    return False
            elif ch == '}':
                if not stack or stack.pop() != '{':
                    return False
            elif ch == ']':
                if not stack or stack.pop() != '[':
                    return False

        return len(stack) == 0
