# 反转一个单链表。
#
# 示例:
#
# 输入: 1->2->3->4->5->NULL
# 输出: 5->4->3->2->1->NULL

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

    return getNext(l)


def showList(l: ListNode):
    while l:
        print(l.val)
        l = l.next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # def getNext(l):
        #     if l and l.next:
        #         theNext, theHead = getNext(l.next)
        #         theNext.next = l
        #         l.next = None
        #         return l, theHead
        #     else:
        #         return l, l
        #
        # theNext, theHead = getNext(head)
        # return theHead
        node = head
        head2 = None
        while (node != None):
            nextNode = node.next
            node.next = head2
            head2 = node
            node = nextNode

        return head2



s = Solution()
l = getList([1, 2, 3, 4, 5])
r = s.reverseList(l)
showList(r)
r = s.reverseList(None)
