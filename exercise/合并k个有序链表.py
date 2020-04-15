# 合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。
#
# 示例:
#
# 输入:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# 输出: 1->1->2->3->4->4->5->6
from typing import List


class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next


def generateList(lLeft):
    if lLeft:
        return ListNode(lLeft[0], generateList(lLeft[1:]))


def showList(l: ListNode):
    while l:
        print(l.val)
        l = l.next


def listNode2list(head: ListNode):
    dp = []
    while head:
        dp.append(head.val)
        head = head.next
    return dp


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if len(lists) == 0:
            return None
        while len(lists) > 1:
            for i in range(len(lists)):
                head = ListNode(0)
                currentNode = head
                if i + 1 < len(lists):
                    head.next = lists[i]
                    while lists[i] and lists[i + 1]:
                        if lists[i].val < lists[i + 1].val:
                            currentNode.next = lists[i]
                            lists[i] = lists[i].next

                        else:
                            currentNode.next = lists[i + 1]
                            lists[i + 1] = lists[i + 1].next
                        currentNode = currentNode.next
                    currentNode.next = lists[i] if lists[i] else lists[i + 1]
                    lists[i] = head.next
                    lists.pop(i + 1)
        return lists[0]


s = Solution()

l1 = generateList([-10, -9, -9, -9, -7, - 2, -1, 2, 4])
l2 = generateList([-9, -7, -6, -6, -3, 0, 1, 3])
l3 = generateList([-10, -9, -2, -1, 1, 3])
assert listNode2list(s.mergeKLists([l1, l2, l3])) == [-10, -10, -9, -9, -9, -9, -9, -7, -7, -6, -6, -3, -2, -2, -1, -1,
                                                      0, 1, 1, 2, 3, 3, 4]

l1 = generateList([1, 2, 3])
l2 = generateList([1, 3])
l3 = generateList([2, 3])
assert listNode2list(s.mergeKLists([l1, l2, l3])) == [1, 1, 2, 2, 3, 3, 3]

l1 = generateList([1, 2, 3])
l2 = generateList([1])
l3 = generateList([])
assert listNode2list(s.mergeKLists([l1, l2, l3])) == [1, 1, 2, 3]

assert listNode2list(s.mergeKLists([])) == []

l1 = generateList([1])
assert listNode2list(s.mergeKLists([l1])) == [1]

l1 = generateList([])
l2 = generateList([1])
l3 = generateList([])
assert listNode2list(s.mergeKLists([l1, l2, l3])) == [1]

l1 = generateList([])
l2 = generateList([])
l3 = generateList([])
assert listNode2list(s.mergeKLists([l1, l2, l3])) == []

l1 = generateList([1, 1, 1, 2, 2, 2, 3, 3, 3])
l2 = generateList([1, 2, 2])
l3 = generateList([2, 3, 3])
assert listNode2list(s.mergeKLists([l1, l2, l3])) == [1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3]
