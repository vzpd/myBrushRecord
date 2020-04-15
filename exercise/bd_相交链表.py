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
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        # l1Length = 0
        # l2Length = 0
        # headAFirst, headBFirst = headA, headB
        # while (headA and headA.next) or (headB and headB.next):
        #     if headA and headA.next:
        #         headA = headA.next
        #         l1Length += 1
        #     if headB and headB.next:
        #         headB = headB.next
        #         l2Length += 1
        #     if l1Length == l2Length and headA == headB:
        #         return headA
        #
        # if headA == headB:
        #     if l1Length > l2Length:
        #         headAFirst, headBFirst = headBFirst, headAFirst
        #     step = l1Length - l2Length if l1Length > l2Length else l2Length - l1Length
        #     for i in range(step):
        #         headBFirst = headBFirst.next
        #     while headAFirst != headBFirst:
        #         headAFirst = headAFirst.next
        #         headBFirst = headBFirst.next
        #     return headAFirst
        # else:
        #     return None
        p1, p2 = headA, headB
        while p1 != p2:
            p1 = p1.next if p1 else headB
            p2 = p2.next if p2 else headA
        return p1


s = Solution()
l1 = generateList([1, 2, 3, 4, 5])
l2 = generateList([1, 2])
l2.next.next = l1.next.next
assert s.getIntersectionNode(l1, l2) == l1.next.next

l1 = generateList([1, 2, 3, 4, 5])
l2 = generateList([1, 2])
assert s.getIntersectionNode(l1, l2) == None

l1 = generateList([1, 2, 3])
l2 = generateList([1, 2])
l2.next.next = l1.next.next
assert s.getIntersectionNode(l1, l2) == l1.next.next

l1 = generateList([1, 2, 3])
l2 = generateList([])
assert s.getIntersectionNode(l1, l2) == None

l1 = generateList([4, 1])
l2 = generateList([5, 0, 1, 8, 4, 5])
l1.next.next = l2.next.next.next
assert s.getIntersectionNode(l1, l2) == l1.next.next

l1 = generateList([0, 9, 1, 2, 4])
l2 = generateList([3, 2])
l2.next.next = l1.next.next.next.next
assert s.getIntersectionNode(l1, l2) == l2.next.next
