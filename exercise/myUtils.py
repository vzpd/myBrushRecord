import time
from functools import wraps
from typing import List


def timer(func):
    @wraps(func)
    def int_time(*args, **kwargs):
        param = ''
        if len(args):
            if hasattr(args[0], func.__name__):
                argsstr = [str(x) for x in args[1:]]
                param += ', '.join(argsstr)
        for key in kwargs.keys():
            if param:
                param += ', ' + str(key) + '=' + str(kwargs[key])
            else:
                param += str(key) + '=' + str(kwargs[key])
        param = '(' + param + ')'
        start_time = time.time()  # 程序开始时间
        res = func(*args, **kwargs)
        over_time = time.time()  # 程序结束时间
        total_time = (over_time - start_time) * 1000

        print('{:^10.5f}毫秒,\t{}{:<30} \t=> {}'.format(round(total_time, 3), func.__name__, param, res, chr(12288)))
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
