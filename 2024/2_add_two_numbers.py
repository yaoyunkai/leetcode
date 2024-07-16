"""

两数相加

两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。

输入：l1 = [2,4,3], l2 = [5,6,4]
输出：[7,0,8]
解释：342 + 465 = 807.



Created at 2024/7/16
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next_=None):
        self.val = val
        self.next = next_


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # point to the head of Node, so should return root.next
        root = cur = ListNode()

        carry = 0
        while l1 or l2 or carry:
            v1 = 0 if not l1 else l1.val
            v2 = 0 if not l2 else l2.val

            cnt = v1 + v2 + carry

            if cnt < 10:
                cur.next = ListNode(cnt)
                carry = 0
            else:
                cur.next = ListNode(cnt % 10)
                carry = 1

            cur = cur.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return root.next
