# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def setNextNode(l1, l2, carry, lr):
            v1 = l1.val if l1 is not None else 0
            v2 = l2.val if l2 is not None else 0
            if (v1 + v2 + carry > 9):
                lr.val = v1 + v2 + carry - 10
                carry = 1
            else:
                lr.val = v1 + v2 + carry
                carry = 0

            if ((l1 is not None and l1.next is not None) or (l2 is not None and l2.next is not None) or carry):
                lr.next = ListNode(0)
                setNextNode(l1.next if l1 is not None else None, l2.next if l2 is not None else None, carry,
                            lr.next)

        lr = ListNode(0)
        setNextNode(l1, l2, False, lr)
        return lr


def initNodeList(l: [int]):
    def setNextNode(lr, l: [int]):
        if len(l) > 0:
            lr = ListNode(l[0])
            l.pop(0)
            if len(l) > 0:
                lr.next = setNextNode(lr.next, l)
            return lr

    lr = None
    return setNextNode(lr, l)


def pringList(l: ListNode):
    while l:
        print(l.val)
        l = l.next


def equalList(l1: ListNode, l2: ListNode):
    while l1 or l2:
        try:
            if l1.val != l2.val:
                return False
            l1 = l1.next
            l2 = l2.next
        except:
            return False
    return True


s = Solution()

l1 = initNodeList([2, 4, 3])
l2 = initNodeList([5, 6, 4])
assert equalList(s.addTwoNumbers(l1, l2), initNodeList([7, 0, 8]))

l1 = initNodeList([2, 4, 5])
l2 = initNodeList([5, 6, 4, 9])
assert equalList(s.addTwoNumbers(l1, l2), initNodeList([7, 0, 0, 0, 1]))
