"""
给你单链表的头结点 head ，请你找出并返回链表的中间结点。

如果有两个中间结点，则返回第二个中间结点。

"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next_=None):
        self.val = val
        self.next = next_


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = cur = head

        while cur and cur.next:
            cur = cur.next.next
            prev = prev.next

        return prev
