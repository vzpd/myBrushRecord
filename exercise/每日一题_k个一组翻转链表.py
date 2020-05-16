from exercise.myUtils import ListNode, list2ListNode, listNode2List


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if k == 1:
            return head
        lastTail = None
        root = None
        slow, fast = head, head
        while fast:
            for i in range(k - 1):
                fast = fast.next
                if fast is None:
                    break
            else:
                fast = fast.next
                end = slow
                before = slow
                curr = before.next
                while curr != fast:
                    next = curr.next
                    curr.next = before
                    before, curr = curr, next
                if lastTail is None:
                    root = before
                else:
                    lastTail.next = before
                lastTail = end
                end.next = fast
                slow = fast
        return root


s = Solution()
head = list2ListNode([1, 2, 3, 4, 5])
assert listNode2List(s.reverseKGroup(head, 2)) == [2, 1, 4, 3, 5]
head = list2ListNode([1, 2, 3, 4, 5])
assert listNode2List(s.reverseKGroup(head, 3)) == [3, 2, 1, 4, 5]
