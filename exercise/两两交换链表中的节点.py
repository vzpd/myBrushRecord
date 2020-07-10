# Definition for singly-linked list.
from exercise.myUtils import list2ListNode


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # root = ListNode(-1)
        # root.next=head
        # pre = None
        # last = root
        # while head:
        #     if not pre:
        #         pre = head
        #         head = head.next
        #     else:
        #         next = head.next
        #         last.next=head
        #         head.next=pre
        #         pre.next=next
        #         last = pre
        #         pre = None
        #         head = next
        #
        # return root.next
        if head and head.next:
            node1 = head
            node2 = head.next
            node1.next = self.swapPairs(node2.next)
            node2.next = node1
            return node2
        else:
            return head


s=Solution()
head = list2ListNode([1,2,3,4])
s.swapPairs(head)