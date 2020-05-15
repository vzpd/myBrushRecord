# 将两个升序链表合并为一个新的升序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 
#
# 示例：
#
# 输入：1->2->4, 1->3->4
# 输出：1->1->2->3->4->4


# Definition for singly-linked list.
from exercise.myUtils import list2ListNode, listNode2List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        root = ListNode(0)
        curr = root
        while l1 or l2:
            if l1 and l2:
                if l1.val < l2.val:
                    curr.next = l1
                    l1 = l1.next
                else:
                    curr.next = l2
                    l2 = l2.next
                curr = curr.next
            elif l1:
                curr.next = l1
                break
            else:
                curr.next = l2
                break

        return root.next


s = Solution()
l1 = list2ListNode([1, 2, 4])
l2 = list2ListNode([1, 3, 4])
assert listNode2List(s.mergeTwoLists(l1, l2)) == [1, 1, 2, 3, 4, 4]
l1 = list2ListNode([1, 2, 4])
assert listNode2List(s.mergeTwoLists(l1, None)) == [1, 2, 4]
assert listNode2List(s.mergeTwoLists(None, None)) == []
