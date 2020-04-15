# 给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
#
# 如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
#
# 您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
#
# 示例：
#
# 输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
# 输出：7 -> 0 -> 8
# 原因：342 + 465 = 807

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
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # l3 = l1
        # carry = 0
        # while l1 or l2:
        #     x1 = l1.val if l1 else 0
        #     x2 = l2.val if l2 else 0
        #     sum = x1 + x2 + carry
        #     carry = sum // 10
        #     l1.val = sum - carry * 10
        #     if not l1.next and l2 and l2.next:
        #         l1.next = l2.next
        #         l2.next = None
        #     if l1:
        #         if l1.next is None and carry:
        #             l1.next = ListNode(carry)
        #             break
        #         l1 = l1.next
        #     if l2:
        #         l2 = l2.next
        # return l3
        def getNext(l1, l2, carry):
            x1 = l1.val if l1 else 0
            x2 = l2.val if l2 else 0
            sum = x1 + x2 + carry
            if sum == 0 and not l1 and not l2:
                return
            carry = sum // 10
            tempNode = ListNode(sum - carry * 10)
            if l1 or l2 or carry:
                tempNode.next = getNext(l1.next if l1 else None, l2.next if l2 else None, carry)
            return tempNode

        return getNext(l1, l2, 0)


s = Solution()
l1 = getList([2, 4, 3])
l2 = getList([5, 6, 4])
l3 = s.addTwoNumbers(l1, l2)
showList(l3)

l1 = getList([2, 4, 5, 9])
l2 = getList([5, 6, 4])
l3 = s.addTwoNumbers(l1, l2)
showList(l3)

l1 = getList([5, 6, 4])
l2 = getList([2, 4, 5, 9])
l3 = s.addTwoNumbers(l1, l2)
showList(l3)

l1 = getList([5, 6, 4])
l2 = getList([])
l3 = s.addTwoNumbers(l1, l2)
showList(l3)

l1 = getList([])
l2 = getList([5, 6, 4])
l3 = s.addTwoNumbers(l1, l2)
showList(l3)

l1 = getList([0])
l2 = getList([0])
l3 = s.addTwoNumbers(l1, l2)
showList(l3)

l1 = getList([0])
l2 = getList([])
l3 = s.addTwoNumbers(l1, l2)
showList(l3)
