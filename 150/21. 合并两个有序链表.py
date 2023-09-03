"""

将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。

TODO 206. 反转链表.py


Created at 2023/9/1
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next_=None):
        self.val = val
        self.next = next_


class Solution:
    def mergeTwoLists1(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        root = cur = ListNode()

        while list1 or list2:

            if list1 and list2:
                if list1.val > list2.val:
                    cur.next = list2
                    list2 = list2.next
                else:
                    cur.next = list1
                    list1 = list1.next

            elif list1:
                cur.next = list1
                list1 = list1.next

            else:
                cur.next = list2
                list2 = list2.next

            cur = cur.next

        return root.next

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1

        if list1.val > list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2
