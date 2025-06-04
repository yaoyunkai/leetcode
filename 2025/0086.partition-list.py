"""
给你一个链表的头节点 head 和一个特定值 x ，请你对链表进行分隔，使得所有 小于 x 的节点都出现在 大于或等于 x 的节点之前。

你应当 保留 两个分区中每个节点的初始相对位置。

"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next_=None):
        self.val = val
        self.next = next_


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        list1 = ListNode()
        list2 = ListNode()

        l1_cur = list1
        l2_cur = list2

        # cur = head

        while head:
            if head.val < x:
                l1_cur.next = head
                l1_cur = l1_cur.next
            else:
                l2_cur.next = head
                l2_cur = l2_cur.next
            head = head.next

        l1_cur.next = list2.next
        l2_cur.next = None  # 防止成环

        return list1.next


if __name__ == '__main__':
    l1 = ListNode(1)
    l2 = ListNode(2)
    l3 = ListNode(2)
    l4 = ListNode(4)
    l5 = ListNode(3)
    l6 = ListNode(5)

    l1.next = l2
    l2.next = l3
    l3.next = l4
    l4.next = l5
    l5.next = l6

    Solution().partition(l1, 3)
