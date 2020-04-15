# 给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。
#
# k 是一个正整数，它的值小于或等于链表的长度。
#
# 如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。
#
# 示例 :
#
# 给定这个链表：1->2->3->4->5
#
# 当 k = 2 时，应当返回: 2->1->4->3->5
#
# 当 k = 3 时，应当返回: 3->2->1->4->5
#
# 说明 :
#
# 你的算法只能使用常数的额外空间。
# 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

# Definition for singly-linked list.
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


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        # def reserse(head: ListNode, tail: ListNode):
        #     tail.next = None
        #     lastNode = None
        #     nextNode = head
        #     while nextNode:
        #         nextNode = nextNode.next
        #         currentNode = nextNode
        #         currentNode.next = lastNode
        #         lastNode = currentNode
        # 
        #     return tail, head
        # 
        # count = 0
        # firstNode = ListNode(0)
        # firstNode.next = head
        # subLinkHead = None
        # lastSubLinkTail = firstNode
        # tempNode = firstNode
        # while tempNode.next:
        #     tempNode = tempNode.next
        #     if count == 0:
        #         subLinkHead = tempNode
        #     count += 1
        #     if count == k:
        #         subLinkTail = tempNode
        #         nextNode = subLinkTail.next
        #         subLinkHead, subLinkTail = reserse(subLinkHead, subLinkTail)
        #         lastSubLinkTail.next = subLinkHead
        #         subLinkTail.next = nextNode
        #         lastSubLinkTail = subLinkTail
        #         tempNode = subLinkTail
        #         count = 0
        # 
        # return firstNode.next
        subLinkHead = None
        lastSubLinkTail = None
        count = 0
        tempNode = head
        while tempNode:
            count += 1
            if count == 1:
                subLinkHead = tempNode
                tempNode = tempNode.next
            elif count == k:
                nextNode = tempNode.next
                tempNode.next = lastSubLinkTail
                lastSubLinkTail = subLinkHead
                tempNode = nextNode
                subLinkHead = None
                count = 0
            else:
                tempNode = tempNode.next

        lastNode = subLinkHead
        tempNode = lastSubLinkTail
        while tempNode:
            nextNode = tempNode.next
            tempNode.next = lastNode
            lastNode = tempNode
            tempNode = nextNode

        return lastNode


s = Solution()
l = generateList([1, 2, 3, 4, 5])
showList(s.reverseKGroup(l, 2))
