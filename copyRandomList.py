# @Author ltj
# @Time   2021/7/23 15:34
# @File   copyRandomList.py


# Definition for a Node.
import collections


class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """

        # h1 = head
        # if not h1:
        #     return
        #
        # res = Node(h1.val, None, None)
        # h2 = res
        # h1 = h1.next
        #
        # while h1:
        #     h2.next = Node(h1.val, None, None)
        #     h2 = h2.next
        #     h1 = h1.next
        #
        # h1 = head
        # h2 = res
        #
        # while h1:
        #     if h1.random is None:
        #         h2.random = None
        #     else:
        #         h3 = h1.random
        #         h4 = head
        #         h5 = res
        #         while h3 != h4:
        #             h4 = h4.next
        #             h5 = h5.next
        #         h2.random = h5
        #
        #     h1 = h1.next
        #     h2 = h2.next
        #
        # return res

        if not head:
            return None
        
        h1 = head
        while h1:
            h2 = Node(h1.val, None, None)
            h2.next = h1.next
            h1.next = h2
            h1 = h1.next.next

        h1 = head
        while h1:
            if h1.random:
                h1.next.random = h1.random.next
            h1 = h1.next.next

        res = head.next
        h1 = head
        h2 = res
        while h2.next:
            h1.next = h2.next
            h1 = h1.next
            h2.next = h1.next
            h2 = h2.next

        h1.next = None

        return res
