"""
给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。

请你将两个数相加，并以相同形式返回一个表示和的链表。

你可以假设除了数字 0 之外，这两个数都不会以 0 开头。


Created at 2023/9/1
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next_=None):
        self.val = val
        self.next = next_


class Solution:

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        return self._inner(l1, l2, 0)

    def _inner(self, l1: Optional[ListNode], l2: Optional[ListNode], carry=0) -> Optional[ListNode]:
        if not l1 and not l2:
            return ListNode(carry) if carry else None

        # 交换 l1, l2
        if l1 is None:
            l1, l2 = l2, l1

        carry = carry + l1.val + (l2.val if l2 else 0)
        l1.val = carry % 10
        l1.next = self._inner(l1.next, l2.next if l2 else None, carry // 10)
        return l1

    def addTwoNumbers2(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        # 尾插法
        root = cur = ListNode()

        carry = 0
        while l1 or l2 or carry:
            v1 = 0 if not l1 else l1.val
            v2 = 0 if not l2 else l2.val

            # 当前位置结果
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

    def addTwoNumbers1(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        # 指向链表的指针
        root = cur = ListNode()

        left = l1
        right = l2

        up = 0
        while left or right:
            v1 = 0 if not left else left.val
            v2 = 0 if not right else right.val

            # 当前位置结果
            cnt = v1 + v2 + up
            if cnt < 10:
                cur.next = ListNode(cnt)
                up = 0
            else:
                cur.next = ListNode(cnt % 10)
                up = 1
            cur = cur.next

            if left:
                left = left.next
            if right:
                right = right.next

        if up == 1:
            cur.next = ListNode(1)

        return root.next


if __name__ == '__main__':
    a3 = ListNode(2)
    a2 = ListNode(4)
    a1 = ListNode(3)

    a3.next = a2
    a2.next = a1

    a4 = ListNode(5)
    a5 = ListNode(6)
    a6 = ListNode(4)

    a4.next = a5
    a5.next = a6

    Solution().addTwoNumbers(a3, a4)
