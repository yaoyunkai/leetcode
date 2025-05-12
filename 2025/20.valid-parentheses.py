"""
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
每个右括号都有一个对应的相同类型的左括号。

"""


class Solution:
    """
    stack

    append
    pop


    """

    def isValid(self, s: str) -> bool:
        _map = {
            '}': '{',
            ')': '(',
            ']': '[',
        }

        arr = []

        for ch in s:
            if ch in ['(', '{', '[']:
                arr.append(ch)
            else:
                if len(arr) == 0 or arr.pop() != _map[ch]:
                    return False

        return len(arr) == 0
