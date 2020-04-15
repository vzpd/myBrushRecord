# 将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
#
# 示例：
#
# 输入：1->2->4, 1->3->4
# 输出：1->1->2->3->4->4

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def getList(l):
    def getNext(lLeft):
        if lLeft:
            currentNode = ListNode(lLeft[0])
            currentNode.next = getNext(lLeft[1:])
            return currentNode

    headNode = getNext(l)
    return headNode


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # if l1 is None:
        #     return l2
        # elif l2 is None:
        #     return l1
        # else:
        #     if l2.val < l1.val:
        #         l1, l2 = l2, l1
        #     currentNode = l1
        #     while currentNode and l2:
        #         while currentNode.next and currentNode.next.val < l2.val:
        #             currentNode = currentNode.next
        #         currentNode.next, l2 = l2, currentNode.next
        #         if currentNode.next:
        #             currentNode = currentNode.next
        #     return l1
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2

    pass


s = Solution()
l1 = getList([1, 2, 3])
l2 = getList([1, 3, 4])
nodeMerged = s.mergeTwoLists(l1, l2)
while nodeMerged:
    print(nodeMerged.val)
    nodeMerged = nodeMerged.next
l1 = getList([-9, 3])
l2 = getList([5, 7])
nodeMerged = s.mergeTwoLists(l1, l2)
while nodeMerged:
    print(nodeMerged.val)
    nodeMerged = nodeMerged.next
