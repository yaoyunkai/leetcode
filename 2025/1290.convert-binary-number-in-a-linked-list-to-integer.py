"""

给你一个单链表的引用结点 head。链表中每个结点的值不是 0 就是 1。已知此链表是一个整数数字的二进制表示形式。

请你返回该链表所表示数字的 十进制值 。

1 0 1  -> 5

00000 1 -> 1



created at 2025/5/10
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next_=None):
        self.val = val
        self.next = next_


class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        rec = 0
        while head is not None:
            rec = rec * 2 + head.val
            head = head.next
        return rec


class Solution2:
    def getDecimalValue(self, head: ListNode) -> int:
        def helper(node, acc):
            if not node:
                return acc
            return helper(node.next, acc * 2 + node.val)

        return helper(head, 0)
