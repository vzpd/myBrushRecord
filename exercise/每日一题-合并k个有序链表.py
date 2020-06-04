# 合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。
#
# 示例:
#
# 输入:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# 输出: 1->1->2->3->4->4->5->6


# Definition for singly-linked list.
from typing import List

from exercise.myUtils import list2ListNode, listNode2List, timer


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    @timer
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # 顺序合并
        # if not lists:
        #     return None
        # root = ListNode(-1)
        # root.next = lists[0]
        # for i in range(1, len(lists)):
        #     currNode = root
        #     while lists[i]:
        #         nextNode = currNode.next
        #         if nextNode:
        #             if nextNode.val > lists[i].val:
        #                 tempNode = lists[i]
        #                 tempNextNode = tempNode.next
        #                 tempNode.next = nextNode
        #                 currNode.next = tempNode
        #                 currNode = tempNode
        #                 lists[i] = tempNextNode
        #             else:
        #                 currNode = currNode.next
        #                 if not currNode.next:
        #                     currNode.next = lists[i]
        #                     break
        #         else:
        #             currNode.next = lists[i]
        #             break
        #
        # return root.next

        # 分治合并
        # length = len(lists)
        # l1, l2 = None, None
        # if length == 0:
        #     return None
        # elif length == 1:
        #     return lists[0]
        # elif length == 2:
        #     l1, l2 = lists[0], lists[1]
        # else:
        #     l1 = self.mergeKLists(lists[:length // 2])
        #     l2 = self.mergeKLists(lists[length // 2:])
        #
        # root = ListNode(-1)
        # currNode = root
        # while l1 or l2:
        #     if l1 and l2:
        #         if l1.val <= l2.val:
        #             currNode.next = l1
        #             l1 = l1.next
        #         else:
        #             currNode.next = l2
        #             l2 = l2.next
        #         currNode = currNode.next
        #     elif l1:
        #         currNode.next = l1
        #         break
        #     elif l2:
        #         currNode.next = l2
        #         break
        # return root.next
        if not lists:
            return
        root = ListNode(-1)
        root.next = lists[0]
        for i in range(1, len(lists)):
            l1 = root.next
            l2 = lists[i]
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
                elif l2:
                    curr.next = l2
                    break

        return root.next


s = Solution()

assert listNode2List(s.mergeKLists([])) == []

l1 = list2ListNode([1, 4, 5])
l2 = list2ListNode([1, 3, 4])
l3 = list2ListNode([2, 6])
assert listNode2List(s.mergeKLists([l1, l2, l3])) == [1, 1, 2, 3, 4, 4, 5, 6]

l1 = list2ListNode([])
l2 = list2ListNode([1, 3, 4])
l3 = list2ListNode([2, 6])
assert listNode2List(s.mergeKLists([l1, l2, l3])) == [1, 2, 3, 4, 6]

l1 = list2ListNode([10])
l2 = list2ListNode([1, 3, 4])
l3 = list2ListNode([2, 6])
assert listNode2List(s.mergeKLists([l1, l2, l3])) == [1, 2, 3, 4, 6, 10]

l1 = list2ListNode([10])
l2 = list2ListNode([8])
l3 = list2ListNode([7, 9, 11])
assert listNode2List(s.mergeKLists([l1, l2, l3])) == [7, 8, 9, 10, 11]

l1 = list2ListNode([10])
l2 = list2ListNode([])
l3 = list2ListNode([7, 9, 11])
assert listNode2List(s.mergeKLists([l1, l2, l3])) == [7, 9, 10, 11]
