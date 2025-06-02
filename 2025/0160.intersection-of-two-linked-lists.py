"""
给你两个单链表的头节点 headA 和 headB ，请你找出并返回两个单链表相交的起始节点。如果两个链表不存在相交节点，返回 null 。

created at 2025/6/2
"""
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class SolutionOld:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        list_a = []

        while headA:
            list_a.append(headA)
            headA = headA.next

        while headB:
            if headB in list_a:
                return headB
            headB = headB.next
        return None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        A, B = headA, headB
        while A != B:
            A = A.next if A else headB
            B = B.next if B else headA
        return A
