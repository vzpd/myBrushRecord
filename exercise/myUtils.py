import inspect
import time
from functools import wraps
from typing import List


def timer(func):
    @wraps(func)
    def int_time(*args, **kwargs):
        sig = inspect.signature(func)
        bound_sig = sig.bind(*args, **kwargs)
        if 'self' in bound_sig.arguments:
            bound_sig.arguments.pop('self')
        argsstr = ''
        for k, v in bound_sig.arguments.items():
            argsstr += ',' + str(k) + '=' + str(v)
        start_time = time.time()  # 程序开始时间
        res = func(*args, **kwargs)
        over_time = time.time()  # 程序结束时间
        total_time = (over_time - start_time) * 1000
        args = argsstr[1:36] if len(argsstr) <= 36 else argsstr[1:36] + '...'
        print('{:^10.5f}毫秒,\t{}({:<40}) \t=> {}'.format(round(total_time, 3), func.__name__, args, res))
        return res

    return int_time


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def list2ListNode(nums: List) -> ListNode:
    if nums:
        currNode = ListNode(nums[0])
        currNode.next = list2ListNode(nums[1:])
        return currNode


def listNode2List(root: ListNode) -> List:
    res = []
    while root:
        res.append(root.val)
        root = root.next
    return res


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def list2TreeNode(list: List, n: int = 0) -> TreeNode:
    if n >= len(list) or (list[n] is None and n * 2 + 1 >= len(list)):
        return
    root = TreeNode(list[n])
    root.left = list2TreeNode(list, 2 * n + 1)
    root.right = list2TreeNode(list, 2 * n + 2)
    return root


def comparelist(a, b):
    if len(a) != len(b):
        return False

    s = set(map(tuple, a))
    for i in range(len(b)):
        if tuple(b[i]) not in s:
            return False

    return True
