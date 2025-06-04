"""
给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。

"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        prev = None

        while cur:
            tmp = cur.next
            cur.next = prev

            prev = cur
            cur = tmp

        return prev
