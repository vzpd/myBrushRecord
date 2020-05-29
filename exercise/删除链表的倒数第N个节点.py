# Definition for singly-linked list.
from exercise.myUtils import list2ListNode, listNode2List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        temp = ListNode(-1)
        temp.next = head
        slow = temp
        fast = temp
        i = 0
        while fast:
            if i > n:
                slow = slow.next
            fast = fast.next
            i += 1
        slow.next = slow.next.next

        return temp.next


s = Solution()
head = list2ListNode([1, 2, 3, 4, 5])
assert listNode2List(s.removeNthFromEnd(head, 2)) == [1, 2, 3, 5]
head = list2ListNode([1])
assert listNode2List(s.removeNthFromEnd(head, 1)) == []
