# @Author ltj
# @Time   2021/7/21 15:59
# @File   getIntersectionNode.py

# Definition for singly-linked list.
from _winapi import NULL


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type headA, headB: ListNode
        :rtype: ListNode
        """

        # TODO 双指针
        pA = headA
        pB = headB

        flagA = flagB = 0

        while True:
            if pA == pB:
                return pA

            if pA:
                pA = pA.next
            else:
                if flagA == 0:
                    pA = headB
                    flagA = 1
                else:
                    return

            if pB:
                pB = pB.next
            else:
                if flagB == 0:
                    pB = headA
                    flagB = 1
                else:
                    return
